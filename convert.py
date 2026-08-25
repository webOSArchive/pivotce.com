#!/usr/bin/env python3
"""Convert the pivotCE WordPress REST API dump into sparse Markdown + YAML front matter."""
import json, re, glob, os, html, sys
from collections import OrderedDict
import yaml
from bs4 import BeautifulSoup, Comment, NavigableString
from markdownify import MarkdownConverter

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "articles")

# ---------- lookup tables ----------
def load(pattern):
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, pattern))):
        out.extend(json.load(open(f, encoding="utf-8")))
    return out

posts = load("raw/posts-p*.json")
cats  = {c["id"]: html.unescape(c["name"]) for c in load("raw/categories.json")}
tags  = {t["id"]: html.unescape(t["name"]) for t in load("raw/tags.json")}
media = {m["id"]: m for m in load("raw/media-*.json")}

authors = {}
for line in open(os.path.join(ROOT, "authors.tsv"), encoding="utf-8"):
    aid, slug, name = line.rstrip("\n").split("\t")
    authors[int(aid)] = {"name": name, "slug": slug}

IMG_EXT = re.compile(r"\.(jpe?g|png|gif|webp|bmp|svg)(\?.*)?$", re.I)

# ---------- HTML cleanup ----------
def clean(soup):
    # drop chrome that carries no article knowledge
    for sel in ("script", "style", "noscript", "meta", "svg", "button", "link"):
        for t in soup.find_all(sel):
            t.decompose()

    # drop HTML comments (incl. the WP <!--more--> read-more marker)
    for c in soup.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()

    # YouTube / Vimeo / other iframes -> a plain link line, so the reference survives
    for ifr in soup.find_all("iframe"):
        src = html.unescape(ifr.get("src") or "")
        if not src:
            ifr.decompose(); continue
        if src.startswith("//"):
            src = "https:" + src
        m = re.search(r"(?:youtube(?:-nocookie)?\.com/embed/|youtu\.be/)([\w-]+)", src)
        label = "Video"
        if m:
            src = "https://www.youtube.com/watch?v=" + m.group(1)
            label = "YouTube video"
        p = soup.new_tag("p")
        a = soup.new_tag("a", href=src); a.string = label
        p.append(a)
        ifr.replace_with(p)

    # WP lightbox / linked thumbnails: prefer the full-size target as the image src
    for a in soup.find_all("a"):
        img = a.find("img")
        href = a.get("href") or ""
        if img is not None and IMG_EXT.search(href) and len(a.find_all(True)) == 1:
            img["src"] = href
            a.replace_with(img)

    # <figure><img><figcaption>caption</figcaption></figure> -> image + italic caption
    for fig in soup.find_all("figure"):
        cap = fig.find("figcaption")
        cap_text = cap.get_text(" ", strip=True) if cap else ""
        if cap:
            cap.decompose()
        imgs = fig.find_all("img")
        fig.name = "p"
        for attr in list(fig.attrs):
            del fig[attr]
        if cap_text:
            if imgs and not (imgs[0].get("alt") or "").strip():
                imgs[0]["alt"] = cap_text
            em = soup.new_tag("em"); em.string = cap_text
            br = soup.new_tag("br")
            fig.append(br); fig.append(em)

    # normalise images: absolute src, strip srcset/sizes/classes noise
    for img in soup.find_all("img"):
        src = html.unescape(img.get("src") or "")
        if src.startswith("//"):
            src = "https:" + src
        img.attrs = {"src": src, "alt": (img.get("alt") or "").strip()}

    # absolute, de-entitied hrefs
    for a in soup.find_all("a"):
        href = html.unescape(a.get("href") or "")
        if href.startswith("//"):
            href = "https:" + href
        keep = {"href": href} if href else {}
        a.attrs = keep

    # unwrap layout-only containers
    for t in soup.find_all(["div", "span", "section", "figcaption"]):
        t.unwrap()

    # drop paragraphs that ended up empty
    for p in soup.find_all(["p", "li"]):
        if not p.get_text(strip=True) and not p.find("img"):
            p.decompose()
    return soup

class Conv(MarkdownConverter):
    def convert_img(self, el, text, parent_tags=None):
        src = el.get("src") or ""
        alt = (el.get("alt") or "").replace("[", "(").replace("]", ")")
        return f"![{alt}]({src})" if src else ""

def to_markdown(rendered):
    soup = BeautifulSoup(rendered or "", "html.parser")
    soup = clean(soup)
    md = Conv(heading_style="ATX", bullets="-", escape_underscores=False,
              escape_asterisks=False, escape_misc=False,
              strip=["form", "input"]).convert_soup(soup)
    md = html.unescape(md)
    md = md.replace(" ", " ").replace("​", "")
    md = re.sub(r"[ \t]+\n", "\n", md)          # trailing spaces
    md = re.sub(r"\n{3,}", "\n\n", md)          # collapse blank runs
    md = re.sub(r"^\s+|\s+$", "", md)
    return md

def plain(rendered):
    s = BeautifulSoup(rendered or "", "html.parser")
    for t in s.find_all(["script", "style", "a"]):
        if t.name != "a":
            t.decompose()
    txt = html.unescape(s.get_text(" ", strip=True))
    return re.sub(r"\s+", " ", txt).strip()

# ---------- YAML front matter ----------
def yscalar(v):
    return yaml.safe_dump(v, allow_unicode=True, default_flow_style=False,
                          width=10**6).rstrip("\n").removesuffix("...").strip()

def yflow(v):
    return yaml.safe_dump(v, allow_unicode=True, default_flow_style=True,
                          width=10**6).rstrip("\n")

def front_matter(fields):
    lines = ["---"]
    for k, v in fields.items():
        if v in (None, "", [], {}):
            continue                                   # sparse: omit empties
        lines.append(f"{k}: {yflow(v) if isinstance(v, list) else yscalar(v)}")
    lines.append("---")
    return "\n".join(lines)

# ---------- main ----------
def main():
    os.makedirs(OUT, exist_ok=True)
    index, seen = [], {}
    for p in posts:
        slug = p["slug"] or f"post-{p['id']}"
        date = p["date_gmt"] or p["date"]
        day = date[:10]
        body = to_markdown(p["content"]["rendered"])
        excerpt = plain(p["excerpt"]["rendered"])
        # WP auto-excerpts end with a "Continue reading <Post Title> →" link; drop it
        excerpt = re.sub(r"\s*Continue reading\b.*$", "", excerpt).strip()
        excerpt = re.sub(r"\s*(…|\.\.\.)$", "…", excerpt).strip()

        fm = OrderedDict()
        fm["title"] = html.unescape(p["title"]["rendered"]).strip()
        fm["date"] = date.replace("T", " ") + " UTC"
        if p.get("modified_gmt") and p["modified_gmt"][:19] != date[:19]:
            fm["modified"] = p["modified_gmt"].replace("T", " ") + " UTC"
        a = authors.get(p["author"])
        if a:
            fm["author"] = a["name"]
            fm["author_slug"] = a["slug"]
        fm["categories"] = [cats[c] for c in p.get("categories", []) if c in cats]
        fm["tags"] = sorted(tags[t] for t in p.get("tags", []) if t in tags)
        fm["slug"] = slug
        fm["source_url"] = p["link"]
        fm["wordpress_id"] = p["id"]
        if p.get("featured_media") and p["featured_media"] in media:
            fm["featured_image"] = media[p["featured_media"]].get("source_url")
        if excerpt:
            fm["excerpt"] = excerpt
        if p.get("status") and p["status"] != "publish":
            fm["status"] = p["status"]

        name = f"{day}-{slug}.md"
        if name in seen:                                   # defensive: never overwrite
            seen[name] += 1
            name = f"{day}-{slug}-{seen[name]}.md"
        else:
            seen[name] = 1

        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(front_matter(fm) + "\n\n# " + fm["title"] + "\n\n" + body + "\n")

        index.append({"file": name, "title": fm["title"], "date": day,
                      "author": fm.get("author", ""), "url": p["link"],
                      "words": len(body.split()), "chars": len(body)})

    json.dump(index, open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8"),
              indent=2, ensure_ascii=False)
    print(f"wrote {len(index)} files to {OUT}")
    empty = [i for i in index if i["words"] < 20]
    print(f"suspiciously short (<20 words): {len(empty)}")
    for e in empty[:15]:
        print("   ", e["words"], e["file"])


if __name__ == '__main__':
    main()
