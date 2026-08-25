#!/usr/bin/env python3
"""Convert WordPress pages and reader comments to Markdown, reusing convert.py's helpers."""
import json, glob, os, re, html
from collections import OrderedDict, defaultdict
from convert import to_markdown, plain, front_matter, load, posts, ROOT

PAGES = os.path.join(ROOT, "pages")
COMMENTS = os.path.join(ROOT, "comments")

# ---------- pages ----------
os.makedirs(PAGES, exist_ok=True)
pages = load("raw/pages.json")
for p in sorted(pages, key=lambda x: x["slug"]):
    fm = OrderedDict()
    fm["title"] = html.unescape(p["title"]["rendered"]).strip()
    fm["type"] = "page"
    fm["date"] = (p["date_gmt"] or p["date"]).replace("T", " ") + " UTC"
    if p.get("modified_gmt") and p["modified_gmt"][:19] != (p["date_gmt"] or "")[:19]:
        fm["modified"] = p["modified_gmt"].replace("T", " ") + " UTC"
    fm["slug"] = p["slug"]
    fm["source_url"] = p["link"]
    fm["wordpress_id"] = p["id"]
    body = to_markdown(p["content"]["rendered"])
    with open(os.path.join(PAGES, f"{p['slug']}.md"), "w", encoding="utf-8") as f:
        f.write(front_matter(fm) + "\n\n# " + fm["title"] + "\n\n" + body + "\n")
print(f"pages written: {len(pages)}")

# ---------- comments ----------
os.makedirs(COMMENTS, exist_ok=True)
comments = load("raw/comments-p*.json")
bypost = defaultdict(list)
for c in comments:
    bypost[c["post"]].append(c)

post_by_id = {p["id"]: p for p in posts}
written = 0
for pid, cs in bypost.items():
    post = post_by_id.get(pid)
    if not post:
        continue
    day = (post["date_gmt"] or post["date"])[:10]
    stem = f"{day}-{post['slug']}"
    cs.sort(key=lambda c: c["date_gmt"] or c["date"])
    kids = defaultdict(list)
    for c in cs:
        kids[c.get("parent", 0)].append(c)

    lines = []
    def render(parent, depth):
        for c in kids.get(parent, []):
            ind = "> " * depth
            who = html.unescape(c.get("author_name") or "Anonymous").strip() or "Anonymous"
            when = (c["date_gmt"] or c["date"]).replace("T", " ") + " UTC"
            body = to_markdown(c["content"]["rendered"]) or "*(empty)*"
            lines.append(f"{ind}**{who}** — {when}")
            lines.append(ind.rstrip())
            for bl in body.split("\n"):
                lines.append((ind + bl).rstrip())
            lines.append("")
            render(c["id"], depth + 1)
    render(0, 0)

    fm = OrderedDict()
    fm["title"] = "Comments: " + html.unescape(post["title"]["rendered"]).strip()
    fm["type"] = "comments"
    fm["article"] = f"../articles/{stem}.md"
    fm["article_title"] = html.unescape(post["title"]["rendered"]).strip()
    fm["source_url"] = post["link"]
    fm["wordpress_id"] = pid
    fm["comment_count"] = len(cs)
    with open(os.path.join(COMMENTS, f"{stem}.md"), "w", encoding="utf-8") as f:
        f.write(front_matter(fm) + "\n\n# " + fm["title"] + "\n\n" + "\n".join(lines).rstrip() + "\n")
    written += 1
print(f"comment files written: {written} ({len(comments)} comments across {len(bypost)} posts)")
orphans = [p for p in bypost if p not in post_by_id]
if orphans:
    print("comments on non-post/unknown parents:", orphans)
