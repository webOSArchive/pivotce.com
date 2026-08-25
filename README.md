# pivotCE Archive

A rescue archive of **pivotCE.com** ("webOS News, Tips, and Tricks"), the webOS
community blog, whose domain was sold and is now monetised with injected
advertising by its new owner.

**279 articles · 8 pages · 4 events · 202 comments · 613 images · ~138,800 words · 2013-02-01 → 2024-12-05**

The archive is **self-contained**: every image is mirrored locally and the Markdown
points at the local copies, so nothing here depends on pivotce.com staying up.

## Layout

| Path             | Contents                                                       |
| ---------------- | -------------------------------------------------------------- |
| `articles/`      | 279 articles, one `YYYY-MM-DD-slug.md` each                      |
| `pages/`         | 8 site pages (About, Contributors, Donors, Intro to webOS, …)    |
| `comments/`      | 53 threaded comment files, named to match their article          |
| `events/`        | 4 calendar events (webOS user-group meetings, 2020)              |
| `images/`        | 613 mirrored images (254 MB), original directory structure       |
| `manifest.csv`   | Article index: date, title, author, file, URL, categories, counts |
| `media_manifest.csv` | Every media-library item: id, date, title, caption, alt, mime, local path, usage |
| `index.json`     | The same index as JSON                                           |
| `raw/`           | Unmodified WordPress REST API JSON — the source of truth         |
| `authors.tsv`    | WordPress author ID → slug → display name                        |
| `convert.py`     | Posts → Markdown                                                 |
| `convert_extras.py` | Pages and comments → Markdown                                 |
| `convert_events.py` | Calendar events → Markdown (via iCal export)                  |
| `mirror_images.py`  | Download every image referenced by an article or page         |
| `mirror_media_library.py` | Download the whole media library, used or not            |
| `find_missing_media.py`   | Locate media records the API silently drops              |
| `check_wayback.py`        | Cross-check the mirror against the Wayback Machine       |
| `rewrite_links.py`  | Repoint the Markdown at the local mirror                      |

## Article format

YAML front matter, then the article as clean Markdown. Empty fields are omitted
rather than left blank.

```yaml
---
title: 'Putting a Touchstone in My Car: A Walk Through My Process'
date: 2014-11-23 03:09:45 UTC
modified: 2014-12-02 21:50:59 UTC
author: Alan Morford
author_slug: alanmorford
categories: [Tutorial]
tags: [car]
slug: putting-a-touchstone-in-my-car-a-walk-through-my-process
source_url: https://pivotce.com/2014/11/23/putting-a-touchstone-in-my-car-...
wordpress_id: 2363
featured_image: ../images/files/2014/11/touchstonecar.jpg
featured_image_source: https://pivotce.com/files/2014/11/touchstonecar.jpg
excerpt: I finally put a touchstone in my car...
---
```

Field coverage across the 279 articles: `title`, `date`, `author`, `author_slug`,
`categories`, `slug`, `source_url`, `wordpress_id`, `excerpt` on all 279;
`modified` on 224; `featured_image` (+ `_source`) on 168; `tags` on 157.

Comment files carry an `article:` pointer back to the post they belong to, and
render replies as nested blockquotes with author and UTC timestamp.

## How it was extracted

The RSS feed at `/feed/` carries only the **10 most recent** posts — it would have
rescued 3.5% of the blog. The content instead came from the site's open WordPress
REST API (`/wp-json/wp/v2/posts`), which returns each post body straight from the
database.

That distinction matters: **the advertising is injected by the site's theme, not
stored in the post content.** A rendered article page is ~211 KB and carries a
Google AdSense *auto-ads* tag that generates the pop-overs and interstitials at
runtime. The REST API response contains none of it. Verified over the whole corpus:

| Ad-network signatures in… | Count |
| ------------------------- | ----- |
| API post content (our source) | **0** |
| Generated Markdown            | **0** |
| A live rendered page          | present (`googlesyndication`, `adsbygoogle`) |

The API also refused one thing: the author list is blocked by Wordfence, so the 14
author names in `authors.tsv` were recovered by scraping one representative post
page per author ID.

## Fidelity checks

Every article was diffed against its source HTML:

- **Text:** no file lost more than 10% of its source text (link text preserved).
- **Images:** 355 source `<img>` → 356 Markdown images. None lost.
- **Links:** 2,241 unique source links → 2,336 Markdown links. None lost.
- **Front matter:** all 340 Markdown files parse as valid YAML with required fields.
- **Image mirror:** all 521 local image references resolve on disk. 0 broken.
- No leftover HTML tags or undecoded HTML entities in any body.

Conversion notes: WordPress lightbox wrappers are unwrapped to the full-size image;
`<figure>`/`<figcaption>` becomes an image plus an italic caption; YouTube embeds
become `[YouTube video](https://www.youtube.com/watch?v=...)` links so the reference
survives; Twitter widget scripts, WP lightbox `<svg>`/`<button>` chrome, and
microdata `<meta>` are dropped. Jetpack CDN URLs (`i0.wp.com`) are collapsed onto
their origin path, so a file referenced both ways is stored once.

## Events

The 4 events are **not exposed by the WordPress REST API** — `/wp/v2/tribe_events`
reports a total of 0 — but the pages are live and The Events Calendar's per-event
iCal export still works. `convert_events.py` reads the sitemap, pulls each
`?ical=1` export for exact UTC start/end, creation and modification stamps, and
takes the description from the page.

The content is thin, and that is the original rather than a conversion loss: one
event body is Lorem ipsum, two are bare links to webOS Nation forum posts that died
with that site in 2023, and one has no description. The scheduling metadata is
intact and is the part worth having.

## The media library

Beyond the 521 images the articles actually embed, the whole WordPress media
library was mirrored — 559 items, including files uploaded but never published.
`media_manifest.csv` classifies each one:

| `used_in_archive` | Count | Meaning |
| ----------------- | ----- | ------- |
| `yes`     | 428 | embedded in an article or page |
| `variant` | 48  | same image at a different WordPress size — usually the **full-resolution original** of a picture the article shows shrunk |
| `no`      | 83  | never referenced anywhere |

The 83 unreferenced files are not junk. 34 carry real captions, which makes them
look like cut or never-published material — a complete "Before – Search is Broken /
After – Search Works" tutorial screenshot set from 2013-10, captioned LuneOS
"Affogato" release screenshots from 2014-08, and a Google Analytics PDF of the
site's own Oct–Nov 2013 traffic. Their captions are preserved in
`media_manifest.csv` even though no article ever used them.

## Known gaps

- **2 images could not be recovered**, from the origin, the Jetpack CDN, or the
  Wayback Machine. Both are non-content: a `forums.webosnation.com` emoticon and a
  TinyMCE 1×1 spacer GIF. These two references still point at their original URLs.
- Only **published** posts are visible to an unauthenticated API. Any drafts,
  private, or trashed posts are not included.
- Comment **email addresses and IPs** are not exposed by the public API, so
  comments carry display name and date only.
- **6 media records are unrecoverable.** The API reports 565 items but serves 559;
  the missing 6 are in 2013-01 (2), 2014-12, 2016-02, 2017-08 and 2018-03. They are
  counted by the database but fail to serialise, individually as well as in the
  listing — 550+ direct ID probes returned nothing. They are almost certainly
  orphaned rows whose files no longer exist on disk.
- **The Wayback cross-check never ran.** `web.archive.org` was unreachable
  throughout (`archive.org` itself responded fine, so this was a CDX-host outage).
  `check_wayback.py` is ready to run when it returns; it would catch any image that
  existed historically but has since been deleted from the live site.
- **The bbPress forum is gone from the live site.** Its sitemaps still advertise 8
  topics, 59 replies and 4 topic tags — including the editorial discussions
  `killing-pivotce`, `editorial-policy`, `new-comment-policy` and `buy-webos-nation`
  — but they are stale 2014 artifacts served by the SEO plugin. bbPress still
  renders and reports "Oh, bother! No forums were found here.": the database holds
  zero forums and zero topics. Every topic URL 404s, `/forums/feed/` is empty, and
  `?p=<id>` resolves to the bbPress permalink before 404ing. Nothing on the live
  site can reach that content. **The community holds a separate archive of the
  forum**, so it is deliberately out of scope here; the URL list is kept in
  `raw/forum/targets.json` for cross-referencing.
- `pages/contributors.md` is **Lorem ipsum in the original** — the page was never
  written. Attribution instead lives in each article's `author` field and in
  `authors.tsv` (14 authors). `pages/donors.md` is real and names the funders.

## Regenerating

```sh
python3 -m venv .venv
./.venv/bin/pip install html2text markdownify beautifulsoup4 pyyaml
./.venv/bin/python convert.py          # posts   -> articles/
./.venv/bin/python convert_extras.py   # pages   -> pages/, comments -> comments/
./.venv/bin/python convert_events.py   # events  -> events/
./.venv/bin/python mirror_images.py         # referenced images -> images/
./.venv/bin/python rewrite_links.py         # repoint Markdown at the local mirror
./.venv/bin/python mirror_media_library.py  # the rest of the media library
./.venv/bin/python check_wayback.py         # optional: cross-check vs Wayback
```

`raw/` holds the untouched API responses, so the whole archive can be rebuilt
offline without pivotce.com.
