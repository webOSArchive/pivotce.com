#!/usr/bin/env python3
"""Mirror every image referenced by the archive and rewrite the Markdown to local paths."""
import re, os, glob, json, hashlib, urllib.parse, urllib.request, concurrent.futures as cf

ROOT = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(ROOT, "images")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

def local_path(url):
    """Map a URL to a stable local path, collapsing the Jetpack CDN onto the origin."""
    u = urllib.parse.urlsplit(url)
    host, path = u.netloc.lower(), u.path.lstrip("/")
    if host.startswith(("i0.wp.com", "i1.wp.com", "i2.wp.com")):
        # https://i0.wp.com/pivotce.com/files/... -> the origin path
        parts = path.split("/", 1)
        if parts[0].endswith("pivotce.com") and len(parts) > 1:
            host, path = "pivotce.com", parts[1]
        else:
            host, path = "cdn", path
    if host.endswith("pivotce.com"):
        rel = path
    else:
        rel = os.path.join("external", host, path)
    rel = re.sub(r"[^A-Za-z0-9._/\-]", "_", rel)
    if not os.path.splitext(rel)[1]:
        rel += ".img"
    return rel

def enc(url):
    """Percent-encode non-ASCII path characters so urllib can send the request."""
    u = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((u.scheme, u.netloc,
        urllib.parse.quote(u.path, safe="/%"), urllib.parse.quote(u.query, safe="=&%?"), ""))

def candidates(url):
    """Try the URL as given, then the origin, the CDN copy, and finally the Wayback Machine."""
    lp = local_path(url)
    out = [enc(url)]
    if not lp.startswith("external"):
        # only useful when sanitising did not alter the real path
        out.append(enc("https://pivotce.com/" + lp))
        out.append(enc("https://i0.wp.com/pivotce.com/" + lp + "?ssl=1"))
    out.append("https://web.archive.org/web/2020id_/" + enc(url))
    seen, uniq = set(), []
    for c in out:
        if c not in seen:
            seen.add(c); uniq.append(c)
    return uniq

# Known-dead and non-content assets: a forum emoticon and a TinyMCE 1x1 spacer.
# Neither exists at the origin, the CDN, or in the Wayback Machine.
SKIP = ("forums.webosnation.com/images/smilies/", "wp-includes/js/tinymce/")


# ---- download ----
def collect():
    # ---- collect every referenced image ----
    refs = {}   # original url -> local rel path
    files = sorted(glob.glob(os.path.join(ROOT, "articles", "*.md")) +
                   glob.glob(os.path.join(ROOT, "pages", "*.md")))
    for f in files:
        t = open(f, encoding="utf-8").read()
        for u in re.findall(r'!\[[^\]]*\]\((https?://[^)\s]+)\)', t): refs[u] = local_path(u)
        for u in re.findall(r'^featured_image:\s*(\S+)\s*$', t, re.M):
            u = u.strip("'\"")
            if u.startswith(("http://", "https://")):   # skip already-localised paths
                refs[u] = local_path(u)

    targets = {}
    for url, rel in refs.items():
        targets.setdefault(rel, []).append(url)
    print(f"{len(refs)} image references -> {len(targets)} unique files after CDN de-dup")
    return refs, targets

def fetch(rel_urls):
    rel, urls = rel_urls
    if any(k in rel for k in SKIP):
        return (rel, False, 0, "skipped: known-dead non-content asset")
    dest = os.path.join(IMGDIR, rel)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return (rel, True, os.path.getsize(dest), "cached")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    last = ""
    for src in candidates(urls[0]):
        try:
            req = urllib.request.Request(src, headers={"User-Agent": UA, "Referer": "https://pivotce.com/"})
            with urllib.request.urlopen(req, timeout=45) as r:
                data = r.read()
            if len(data) < 100:
                last = f"tiny ({len(data)}b)"; continue
            with open(dest, "wb") as fh:
                fh.write(data)
            return (rel, True, len(data), src)
        except Exception as e:
            last = f"{type(e).__name__}: {e}"[:70]
    return (rel, False, 0, last)

def main():
    refs, targets = collect()
    os.makedirs(IMGDIR, exist_ok=True)
    ok, fail, total = [], [], 0
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for rel, good, size, note in ex.map(fetch, sorted(targets.items())):
            if good: ok.append(rel); total += size
            else: fail.append((rel, note))
    print(f"downloaded/cached: {len(ok)}   failed: {len(fail)}   bytes: {total:,} ({total/1048576:.1f} MB)")
    for r, n in fail[:25]: print("   FAIL", r, "|", n)
    json.dump({"ok": ok, "failed": fail, "refs": refs}, open(os.path.join(ROOT, "images_report.json"), "w"), indent=2)


if __name__ == '__main__':
    main()
