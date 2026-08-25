#!/usr/bin/env python3
"""Mirror the entire WordPress media library, including files never used in a post."""
import json, glob, os, re, html, csv, urllib.parse, urllib.request, concurrent.futures as cf
from mirror_images import local_path, enc, IMGDIR, UA, ROOT

def load(pat):
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, pat))): out.extend(json.load(open(f, encoding="utf-8")))
    return out

media = {m["id"]: m for m in load("raw/media-lib-p*.json")}
media.update({m["id"]: m for m in load("raw/media-*.json") if isinstance(m, dict) and "source_url" in m})
print(f"media library items: {len(media)}")

# what the articles/pages already reference
used = set()
for f in glob.glob(os.path.join(ROOT, "articles", "*.md")) + glob.glob(os.path.join(ROOT, "pages", "*.md")):
    t = open(f, encoding="utf-8").read()
    for m in re.findall(r'!\[[^\]]*\]\((\.\./images/[^)\s]+)\)', t): used.add(m.replace("../images/", "", 1))
    for m in re.findall(r'^featured_image:\s*\.\./images/(\S+)', t, re.M): used.add(m)

def fetch(item):
    url = item["source_url"]
    rel = local_path(url)
    dest = os.path.join(IMGDIR, rel)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return (item, rel, True, os.path.getsize(dest), "cached")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    last = ""
    for src in (enc(url), enc("https://i0.wp.com/pivotce.com/" + rel + "?ssl=1"),
                "https://web.archive.org/web/2020id_/" + enc(url)):
        try:
            req = urllib.request.Request(src, headers={"User-Agent": UA, "Referer": "https://pivotce.com/"})
            with urllib.request.urlopen(req, timeout=40) as r: data = r.read()
            if len(data) < 100: last = f"tiny ({len(data)}b)"; continue
            open(dest, "wb").write(data)
            return (item, rel, True, len(data), src)
        except Exception as e:
            last = f"{type(e).__name__}: {e}"[:70]
    return (item, rel, False, 0, last)

rows, newly, cached, failed, newbytes = [], 0, 0, [], 0
with cf.ThreadPoolExecutor(max_workers=8) as ex:
    for item, rel, good, size, note in ex.map(fetch, sorted(media.values(), key=lambda m: m["id"])):
        if good:
            if note == "cached": cached += 1
            else: newly += 1; newbytes += size
        else:
            failed.append((item["id"], item["source_url"], note))
        rows.append(dict(
            id=item["id"], date=(item.get("date_gmt") or item.get("date") or "")[:10],
            title=html.unescape(re.sub("<[^>]+>", "", item.get("title", {}).get("rendered", ""))).strip(),
            caption=html.unescape(re.sub("<[^>]+>", "", item.get("caption", {}).get("rendered", ""))).strip(),
            alt=html.unescape(item.get("alt_text") or "").strip(),
            mime=item.get("mime_type", ""), attached_to_post=item.get("post") or "",
            source_url=item["source_url"], local_path=("images/" + rel) if good else "",
            used_in_archive="yes" if rel in used else "no", downloaded="ok" if good else "FAILED"))

rows.sort(key=lambda r: (r["date"], r["id"]))
with open(os.path.join(ROOT, "media_manifest.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

orphans = [r for r in rows if r["used_in_archive"] == "no" and r["downloaded"] == "ok"]
print(f"already mirrored: {cached}   newly downloaded: {newly} ({newbytes/1048576:.1f} MB)   failed: {len(failed)}")
print(f"never referenced by any article/page (orphans): {len(orphans)}")
for i, u, n in failed[:20]: print(f"   FAIL {i} {u} | {n}")
