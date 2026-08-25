#!/usr/bin/env python3
"""Locate media records the listing endpoint silently drops, by narrowing date windows."""
import json, urllib.request, urllib.parse, calendar, sys, concurrent.futures as cf

UA = {"User-Agent": "Mozilla/5.0"}
BASE = "https://pivotce.com/wp-json/wp/v2/media"

def q(**kw):
    url = BASE + "?" + urllib.parse.urlencode(kw)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        total = int(r.headers.get("X-WP-Total", "0"))
        data = json.load(r)
    return total, (data if isinstance(data, list) else [])

def window(a, b, per=100):
    return q(per_page=per, after=a, before=b, orderby="date", order="asc")

months = []
for y, n in ((2013, 2), (2014, None), (2015, None), (2016, 1), (2017, 1), (2018, 1)):
    for m in range(1, 13):
        last = calendar.monthrange(y, m)[1]
        months.append((y, m, f"{y}-{m:02d}-01T00:00:00", f"{y}-{m:02d}-{last}T23:59:59"))

def check(mo):
    y, m, a, b = mo
    try:
        t, items = window(a, b)
        return (y, m, a, b, t, len(items), [i["id"] for i in items])
    except Exception as e:
        return (y, m, a, b, -1, -1, [])

bad = []
with cf.ThreadPoolExecutor(max_workers=10) as ex:
    for y, m, a, b, t, got, ids in ex.map(check, months):
        if t > 0 and t != got:
            bad.append((y, m, a, b, t, got, ids))
            print(f"{y}-{m:02d}: header={t} returned={got}  MISSING {t-got}")

# For each bad month, probe the ID range spanned by its neighbours
allids = set()
with cf.ThreadPoolExecutor(max_workers=10) as ex:
    for y, m, a, b, t, got, ids in ex.map(check, months):
        allids |= set(ids)
print(f"\nknown media ids in scanned months: {len(allids)}")

def probe(i):
    try:
        req = urllib.request.Request(f"{BASE}/{i}", headers=UA)
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
        return {"id": d["id"], "date": d.get("date"), "source_url": d.get("source_url"),
                "mime_type": d.get("mime_type"), "title": d.get("title", {}).get("rendered", ""),
                "post": d.get("post")}
    except Exception:
        return None

found = []
for y, m, a, b, t, got, ids in bad:
    if ids:
        lo, hi = min(ids) - 40, max(ids) + 40
    else:
        continue
    cand = [i for i in range(lo, hi + 1) if i not in allids]
    print(f"probing {len(cand)} ids around {y}-{m:02d} ({lo}-{hi})")
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for r in ex.map(probe, cand):
            if r and r["id"] not in allids:
                found.append(r)
seen, uniq = set(), []
for f in found:
    if f["id"] not in seen:
        seen.add(f["id"]); uniq.append(f)
print(f"\nrecovered media records not in the listing: {len(uniq)}")
for f in uniq: print("   ", f["id"], f["date"], f["mime_type"], f["source_url"])
json.dump(uniq, open("raw/media-hidden.json", "w"), indent=2)
