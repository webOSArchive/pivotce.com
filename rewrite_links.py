#!/usr/bin/env python3
"""Point the Markdown at the local image mirror, keeping provenance in front matter."""
import re, os, glob, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mirror_images import local_path

ROOT = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(ROOT, "images")

def have(url):
    rel = local_path(url)
    return rel if os.path.exists(os.path.join(IMGDIR, rel)) else None

changed = rewritten = missing = 0
missing_urls = set()
for f in sorted(glob.glob(os.path.join(ROOT, "articles", "*.md")) +
                glob.glob(os.path.join(ROOT, "pages", "*.md"))):
    depth_prefix = "../images/"
    t = orig = open(f, encoding="utf-8").read()

    def img_sub(m):
        global rewritten, missing
        alt, url = m.group(1), m.group(2)
        rel = have(url)
        if rel:
            rewritten += 1
            return f"![{alt}]({depth_prefix}{rel})"
        missing += 1; missing_urls.add(url)
        return m.group(0)
    t = re.sub(r'!\[([^\]]*)\]\((https?://[^)\s]+)\)', img_sub, t)

    # featured_image -> local, with the original kept as featured_image_source
    def fi_sub(m):
        global rewritten, missing
        url = m.group(1).strip("'\"")
        rel = have(url)
        if not rel:
            missing += 1; missing_urls.add(url); return m.group(0)
        rewritten += 1
        return f"featured_image: {depth_prefix}{rel}\nfeatured_image_source: {url}"
    t = re.sub(r'^featured_image:\s*(\S+)\s*$', fi_sub, t, flags=re.M)

    if t != orig:
        open(f, "w", encoding="utf-8").write(t); changed += 1

print(f"files rewritten: {changed}")
print(f"image references now local: {rewritten}")
print(f"references left pointing remote: {missing}")
for u in sorted(missing_urls): print("   remote:", u)
