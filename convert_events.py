#!/usr/bin/env python3
"""Extract The Events Calendar entries (not exposed via the WP REST API) to Markdown."""
import re, os, html, json, urllib.request
from collections import OrderedDict
from bs4 import BeautifulSoup
from convert import to_markdown, front_matter, ROOT

OUT = os.path.join(ROOT, "events")
RAW = os.path.join(ROOT, "raw", "events")
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read().decode("utf-8", "replace")

def unfold(ics):
    out = []
    for line in ics.splitlines():
        if line[:1] in (" ", "\t") and out:
            out[-1] += line[1:]
        else:
            out.append(line)
    return out

def ics_fields(ics):
    """Parse only the VEVENT block — VTIMEZONE also carries a DTSTART."""
    f = {}
    inside = False
    for line in unfold(ics):
        u = line.strip().upper()
        if u == "BEGIN:VEVENT": inside = True; continue
        if u == "END:VEVENT": break
        if not inside or ":" not in line:
            continue
        k, v = line.split(":", 1)
        key = k.split(";")[0].upper()
        if key in ("DTSTART", "DTEND", "CREATED", "LAST-MODIFIED", "UID", "SUMMARY",
                   "DESCRIPTION", "URL", "LOCATION", "ORGANIZER", "CATEGORIES"):
            f.setdefault(key, v.replace("\\,", ",").replace("\\n", "\n").strip())
    return f

def fmt(ts):
    m = re.match(r"^(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})Z?$", ts or "")
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)} {m.group(4)}:{m.group(5)}:{m.group(6)} UTC" if m else ts

sm = get("https://pivotce.com/tribe_events-sitemap.xml")
urls = re.findall(r"<loc>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</loc>", sm)
print(f"events in sitemap: {len(urls)}")

os.makedirs(OUT, exist_ok=True); os.makedirs(RAW, exist_ok=True)
written = 0
for u in urls:
    slug = u.rstrip("/").split("/")[-1]
    ics = get(u + "?ical=1")
    open(os.path.join(RAW, slug + ".ics"), "w", encoding="utf-8").write(ics)
    f = ics_fields(ics)
    page = get(u)
    open(os.path.join(RAW, slug + ".html"), "w", encoding="utf-8").write(page)
    s = BeautifulSoup(page, "html.parser")

    node = s.find(class_="tribe-events-single-event-description") or s.find(class_="tribe-events-content")
    body = to_markdown(str(node)) if node else ""
    sched = s.find(class_="tribe-events-schedule")
    sched_txt = re.sub(r"\s+", " ", sched.get_text(" ", strip=True)) if sched else ""

    fm = OrderedDict()
    fm["title"] = html.unescape(f.get("SUMMARY") or slug)
    fm["type"] = "event"
    fm["start"] = fmt(f.get("DTSTART"))
    fm["end"] = fmt(f.get("DTEND"))
    if sched_txt: fm["schedule"] = sched_txt
    if f.get("LOCATION"): fm["location"] = f["LOCATION"]
    if f.get("ORGANIZER"): fm["organizer"] = f["ORGANIZER"]
    if f.get("CATEGORIES"): fm["categories"] = [c.strip() for c in f["CATEGORIES"].split(",") if c.strip()]
    fm["slug"] = slug
    fm["source_url"] = f.get("URL") or u
    if f.get("CREATED"): fm["created"] = fmt(f["CREATED"])
    if f.get("LAST-MODIFIED"): fm["modified"] = fmt(f["LAST-MODIFIED"])
    if f.get("UID"): fm["ical_uid"] = f["UID"]

    desc = html.unescape(f.get("DESCRIPTION") or "").strip()
    if not body and desc:
        body = desc if not desc.startswith("http") else f"[{desc}]({desc})"
    with open(os.path.join(OUT, f"{fm['start'][:10]}-{slug}.md"), "w", encoding="utf-8") as fh:
        fh.write(front_matter(fm) + "\n\n# " + fm["title"] + "\n\n" + (body or "*(no description)*") + "\n")
    written += 1
    print(f"  {fm['start'][:10]}  {fm['title']}")
print(f"events written: {written}")
