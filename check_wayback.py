#!/usr/bin/env python3
"""Cross-check the local image mirror against everything the Wayback Machine ever
archived under pivotce.com/files/, and fetch anything we are missing.

web.archive.org was unreachable when the archive was built (archive.org itself was
fine, so this is a CDX-host outage). Re-run this when it comes back:

    ./.venv/bin/python check_wayback.py            # report only
    ./.venv/bin/python check_wayback.py --download # also fetch what's missing
"""
import json, os, re, sys, urllib.request, urllib.parse, concurrent.futures as cf
from mirror_images import local_path, enc, IMGDIR, UA, ROOT

CDX = ("https://web.archive.org/cdx/search/cdx?url=pivotce.com%2Ffiles%2F*"
       "&output=json&fl=original,timestamp,mimetype&collapse=urlkey&filter=statuscode:200")

def get(url, timeout=180):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=timeout).read()

try:
    rows = json.loads(get(CDX))
except Exception as e:
    sys.exit(f"CDX unreachable ({type(e).__name__}: {e}). web.archive.org may still be down; try again later.")

hdr, rows = rows[0], rows[1:]
orig_i = hdr.index("original"); ts_i = hdr.index("timestamp")
seen, missing = set(), []
for r in rows:
    url = r[orig_i]
    if not re.search(r"\.(jpe?g|png|gif|webp|pdf)$", url, re.I):
        continue
    if re.search(r"-\d{2,4}x\d{2,4}\.", url):     # skip WP generated sizes
        continue
    rel = local_path(url)
    if rel in seen:
        continue
    seen.add(rel)
    if not os.path.exists(os.path.join(IMGDIR, rel)):
        missing.append((url, r[ts_i], rel))

print(f"CDX rows: {len(rows)}   distinct original files: {len(seen)}   not in local mirror: {len(missing)}")
for u, t, rel in missing[:40]:
    print("   MISSING", t, u)
json.dump([{"url": u, "timestamp": t, "rel": rel} for u, t, rel in missing],
          open(os.path.join(ROOT, "raw", "wayback_missing.json"), "w"), indent=2)

if "--download" in sys.argv and missing:
    def grab(m):
        u, t, rel = m
        dest = os.path.join(IMGDIR, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        try:
            data = get(f"https://web.archive.org/web/{t}id_/{enc(u)}", timeout=90)
            if len(data) < 100:
                return (rel, False, "tiny")
            open(dest, "wb").write(data)
            return (rel, True, len(data))
        except Exception as e:
            return (rel, False, f"{type(e).__name__}")
    ok = 0
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        for rel, good, note in ex.map(grab, missing):
            if good: ok += 1
            else: print("   FAIL", rel, note)
    print(f"recovered from Wayback: {ok}/{len(missing)}")
