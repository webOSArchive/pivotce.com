#!/usr/bin/env python3
"""
One-time seed: turn the recovered archive into Hugo content.

`articles/`, `pages/`, `comments/` and `events/` are the immutable rescue
archive -- they stay exactly as extracted, with `raw/` as provenance.
This script projects them into `content/`, which is what Hugo builds and
what Sveltia CMS edits from here on.

Run it once. After that `content/` is canonical: re-running would discard
anything the community has edited or written since.
"""
import csv, datetime, pathlib, re, shutil, sys
from urllib.parse import urlparse

import yaml

ROOT = pathlib.Path(__file__).parent
CONTENT = ROOT / "content"


def split_front_matter(text):
    if not text.startswith("---"):
        raise ValueError("no front matter")
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm), body.lstrip("\n")


def to_rfc3339(value):
    """'2013-02-01 18:46:16 UTC' -> '2013-02-01T18:46:16Z' (Hugo parses this)."""
    if isinstance(value, datetime.datetime):
        return value.strftime("%Y-%m-%dT%H:%M:%SZ")
    if isinstance(value, datetime.date):
        return value.strftime("%Y-%m-%dT00:00:00Z")
    s = str(value).strip()
    m = re.match(r"^(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2}:\d{2})\s*(UTC|Z)?$", s)
    if m:
        return f"{m.group(1)}T{m.group(2)}Z"
    m = re.match(r"^(\d{4}-\d{2}-\d{2})$", s)
    if m:
        return f"{m.group(1)}T00:00:00Z"
    raise ValueError(f"unparseable date: {value!r}")


def strip_leading_h1(body):
    """Every recovered file repeats its title as an H1; the theme renders it."""
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith("# "):
            del lines[: i + 1]
            while lines and not lines[0].strip():
                lines.pop(0)
        break
    return "\n".join(lines)


def localise_media(text):
    """'../images/foo.jpg' -> '/images/foo.jpg' (images/ is mounted at /images)."""
    return text.replace("../images/", "/images/")


# <gasp>, <sigh>, <app name>, <webosnation.com> -- angle-bracket prose the
# original authors typed. Goldmark reads these as inline HTML and drops them
# (unsafe=false) or emits unknown tags the browser hides (unsafe=true); either
# way the words vanish. Escape anything that isn't a real autolink.
ANGLE = re.compile(r"<([^<>\s][^<>]*)>")
AUTOLINK = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.\-]*:|[^@\s]+@[^@\s]+\.[^@\s]+$)")


def escape_angle_prose(text):
    def repl(m):
        inner = m.group(1)
        if AUTOLINK.match(inner):
            return m.group(0)          # <https://...>, <mailto:...>, <a@b.com>
        return "\\<" + inner + "\\>"
    out = []
    for block in text.split("```"):
        out.append(block)
    # Only touch prose, never fenced code blocks (even indexes are outside).
    for i in range(0, len(out), 2):
        out[i] = ANGLE.sub(repl, out[i])
    return "```".join(out)



BOM = "\ufeff"


def strip_bom(value):
    """One 2014 post carries a literal U+FEFF in its title, which WordPress
    percent-encoded into the slug as %ef%bb%bf. Nothing downstream -- Hugo,
    nginx, git -- handles that well, so drop it and note the change."""
    if isinstance(value, str):
        return value.replace(BOM, "").replace("%ef%bb%bf", "")
    return value


# --------------------------------------------------------------------------
# Internal links
# --------------------------------------------------------------------------
# The rescued articles cross-reference each other by absolute pivotce.com URL.
# That domain was sold and now injects advertising, so every one of those links
# would push readers of the archive straight back at the thing the archive
# exists to escape. Repoint the ones we can serve ourselves; leave the rest
# alone rather than guess.
PIVOTCE = re.compile(r"https?://(?:www\.)?pivotce\.com(/[^\s)\"'\\>\]]*)?")
PIVOTCE_AUTOLINK = re.compile(r"<(https?://(?:www\.)?pivotce\.com[^>\s]*)>")


def build_link_map(root):
    """original pivotce.com path -> the path this site serves it at."""
    m = {}
    for src in (root / "articles").glob("*.md"):
        front, _ = split_front_matter(src.read_text(encoding="utf-8"))
        d = to_rfc3339(front["date"])[:10].replace("-", "/")
        m[urlparse(front["source_url"]).path.rstrip("/")] = f"/{d}/{strip_bom(front['slug'])}/"
    for src in (root / "pages").glob("*.md"):
        front, _ = split_front_matter(src.read_text(encoding="utf-8"))
        if front.get("source_url"):
            m[urlparse(front["source_url"]).path.rstrip("/")] = f"/{strip_bom(front['slug'])}/"
    return m


def resolve_pivotce(path, link_map, root, page_slugs=None):
    """Map one pivotce.com path onto ours, or None to leave it untouched."""
    bare = (path or "/").rstrip("/")
    if bare in link_map:
        return link_map[bare]
    # Some bodies link a page by a path that never matched its canonical
    # source_url (e.g. /the-webos-status-report vs /guide/the-webos-status-report).
    # Fall back to the final segment when it names a page we hold.
    tail = bare.rsplit("/", 1)[-1]
    if page_slugs and tail in page_slugs.get("pages", ()):
        return f"/{tail}/"
    if bare in link_map:
        return link_map[bare]
    if bare in ("", "/"):
        return "/"
    if bare.startswith("/files/"):                     # media library
        local = f"/images{bare}"
        return local if (root / "images" / bare.lstrip("/")).exists() else None
    # Only repoint a taxonomy URL if that term actually exists here. The old
    # site had tags no surviving post carries (/tag/luneos, /tag/release);
    # mapping those blindly would manufacture dead links.
    if bare.startswith("/tag/"):
        term = bare[len("/tag/"):]
        return f"/tags/{term}/" if term in (page_slugs or {}).get("tags", ()) else None
    if bare.startswith("/category/"):
        term = bare[len("/category/"):]
        return f"/categories/{term}/" if term in (page_slugs or {}).get("categories", ()) else None
    if bare == "/feed":
        return "/index.xml"
    return None


def relink(text, link_map, root, stats):
    # <http://pivotce.com/...> autolinks first: a bare relative path is not a
    # valid autolink, so these have to become proper Markdown links.
    def auto(m):
        target = resolve_pivotce(urlparse(m.group(1)).path, link_map, root,
                                 stats.get("page_slugs"))
        if not target:
            stats["left"] += 1
            return m.group(0)
        stats["fixed"] += 1
        return f"[{m.group(1)}]({target})"

    text = PIVOTCE_AUTOLINK.sub(auto, text)

    def plain(m):
        raw = m.group(1) or "/"
        path, sep, frag = raw.partition("#")
        target = resolve_pivotce(path, link_map, root, stats.get("page_slugs"))
        if target:
            target += sep + frag
        if not target:
            stats["left"] += 1
            return m.group(0)
        stats["fixed"] += 1
        return target

    return PIVOTCE.sub(plain, text)


def dump(front, body, dest):
    fm = yaml.safe_dump(
        front, sort_keys=False, allow_unicode=True, default_flow_style=False, width=10000
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"---\n{fm}---\n\n{body.rstrip()}\n", encoding="utf-8")


# --------------------------------------------------------------------------
# Articles -> content/posts/
# --------------------------------------------------------------------------
def seed_posts(link_map, stats):
    root_dir = ROOT
    have_comments = {p.name for p in (ROOT / "comments").glob("*.md")}
    n = 0
    for src in sorted((ROOT / "articles").glob("*.md")):
        front, body = split_front_matter(src.read_text(encoding="utf-8"))
        out = {
            "title": strip_bom(front["title"]),
            "date": to_rfc3339(front["date"]),
        }
        if "modified" in front:
            out["lastmod"] = to_rfc3339(front["modified"])
        for key in ("author", "author_slug", "categories", "tags", "slug"):
            if front.get(key):
                out[key] = strip_bom(front[key])
        if front.get("excerpt"):
            # Hugo markdown-renders a front-matter summary for RSS, so angle
            # brackets need escaping here exactly as they do in the body.
            out["summary"] = escape_angle_prose(relink(front["excerpt"], link_map, root_dir, stats))
        if front.get("featured_image"):
            out["featured_image"] = localise_media(front["featured_image"])
        # Provenance: where this was originally published, and its WP row id.
        # Recorded verbatim -- never BOM-stripped -- so the archive keeps an
        # honest record of the original URL even where we serve a cleaner one.
        for key in ("source_url", "wordpress_id", "featured_image_source"):
            if front.get(key):
                out[key] = front[key]
        out["archived"] = True          # distinguishes rescued posts from new ones
        if src.name in have_comments:
            out["comment_page"] = strip_bom(src.stem)

        dump(out, escape_angle_prose(relink(localise_media(strip_leading_h1(body)), link_map, root_dir, stats)), CONTENT / "posts" / strip_bom(src.name))
        n += 1
    return n


# --------------------------------------------------------------------------
# Pages -> content/pages/
# --------------------------------------------------------------------------
def seed_pages(link_map, stats):
    root_dir = ROOT
    n = 0
    for src in sorted((ROOT / "pages").glob("*.md")):
        front, body = split_front_matter(src.read_text(encoding="utf-8"))
        out = {"title": strip_bom(front["title"]), "date": to_rfc3339(front["date"])}
        if "modified" in front:
            out["lastmod"] = to_rfc3339(front["modified"])
        if front.get("slug"):
            out["slug"] = strip_bom(front["slug"])
        for key in ("source_url", "wordpress_id"):
            if front.get(key):
                out[key] = front[key]
        out["archived"] = True
        dump(out, escape_angle_prose(relink(localise_media(strip_leading_h1(body)), link_map, root_dir, stats)), CONTENT / "pages" / strip_bom(src.name))
        n += 1
    return n


# --------------------------------------------------------------------------
# Comments -> content/comments/  (headless: rendered into the post, never routed)
# --------------------------------------------------------------------------
def seed_comments(link_map, stats):
    root_dir = ROOT
    # Suppress the section itself: without this Hugo still routes /comments/
    # and /comments/index.xml even though every page in it is headless.
    dump(
        {"title": "Archived comments", "build": {"list": "never", "render": "never"}},
        "",
        CONTENT / "comments" / "_index.md",
    )
    n = 0
    for src in sorted((ROOT / "comments").glob("*.md")):
        front, body = split_front_matter(src.read_text(encoding="utf-8"))
        out = {
            "title": strip_bom(front["title"]),
            "comment_count": front.get("comment_count", 0),
            "article_title": front.get("article_title", ""),
            # Not a page of its own: no URL, no listing, no sitemap entry.
            "build": {"list": "never", "render": "never"},
        }
        dump(out, escape_angle_prose(relink(localise_media(strip_leading_h1(body)), link_map, root_dir, stats)), CONTENT / "comments" / strip_bom(src.name))
        n += 1
    return n


# --------------------------------------------------------------------------
# Events -> content/events/
# --------------------------------------------------------------------------
def seed_events(link_map, stats):
    root_dir = ROOT
    n = 0
    for src in sorted((ROOT / "events").glob("*.md")):
        front, body = split_front_matter(src.read_text(encoding="utf-8"))
        out = {
            "title": strip_bom(front["title"]),
            "date": to_rfc3339(front["start"]),
            "event_start": to_rfc3339(front["start"]),
            "event_end": to_rfc3339(front["end"]),
            "schedule": front.get("schedule", ""),
            "slug": front["slug"],
            "source_url": front.get("source_url", ""),
            "archived": True,
        }
        dump(out, escape_angle_prose(relink(localise_media(strip_leading_h1(body)), link_map, root_dir, stats)), CONTENT / "events" / src.name)
        n += 1
    return n


# --------------------------------------------------------------------------
# authors.tsv -> data/authors.yaml
# --------------------------------------------------------------------------
def seed_authors():
    authors = {}
    with (ROOT / "authors.tsv").open(encoding="utf-8") as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if len(row) < 3:
                continue
            wp_id, slug, name = row[0], row[1], row[2]
            authors[slug] = {"name": name, "wordpress_id": int(wp_id)}
    dest = ROOT / "data" / "authors.yaml"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(
        yaml.safe_dump(authors, sort_keys=True, allow_unicode=True), encoding="utf-8"
    )
    return len(authors)


if __name__ == "__main__":
    if CONTENT.exists() and "--force" not in sys.argv:
        sys.exit(
            "content/ already exists. This is a one-time seed -- re-running would\n"
            "discard community edits. Pass --force if you really mean it."
        )
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    link_map = build_link_map(ROOT)
    stats = {"fixed": 0, "left": 0}
    # Lookups used when repointing links: which pages and which taxonomy terms
    # this archive can actually serve.
    tags, cats = set(), set()
    for f in (ROOT / "articles").glob("*.md"):
        fm, _ = split_front_matter(f.read_text(encoding="utf-8"))
        for v in fm.get("tags") or []:
            tags.add(str(v).lower().replace(" ", "-"))
        for v in fm.get("categories") or []:
            cats.add(str(v).lower().replace(" ", "-"))
    stats["page_slugs"] = {
        "pages": {
            strip_bom(split_front_matter(f.read_text(encoding="utf-8"))[0]["slug"])
            for f in (ROOT / "pages").glob("*.md")
        },
        "tags": tags,
        "categories": cats,
    }
    print(f"posts:    {seed_posts(link_map, stats)}")
    print(f"pages:    {seed_pages(link_map, stats)}")
    print(f"comments: {seed_comments(link_map, stats)}")
    print(f"events:   {seed_events(link_map, stats)}")
    print(f"links:    {stats['fixed']} pivotce.com links repointed locally, "
          f"{stats['left']} left pointing at the old domain")
    print(f"authors:  {seed_authors()}")
