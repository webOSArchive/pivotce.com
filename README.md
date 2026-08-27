# pivotCE

**[www.webosarchive.org/pivot](https://www.webosarchive.org/pivot/)** — webOS
News, Tips, and Tricks.

pivotCE ran from 2013 to 2024. Its 279 articles were rescued from the dormant
domain, and the site is open again for new writing. If you have something to
say about webOS, it belongs here.

## Writing an article

Go to **[/pivot/admin/](https://www.webosarchive.org/pivot/admin/)** and sign in
with GitHub. That is the whole setup — you get an editor with image upload and
a preview, and you never need to touch Git.

What happens when you hit publish depends on your access:

- **On the webOSArchive team** — it goes live within about five minutes.
- **Everyone else** — it opens a pull request for a quick review first. Nothing
  is lost; you will get a comment if anything needs changing.

Ask in [Discord](https://docs.webosarchive.org/community/) if you would like
write access, or if anything looks wrong.

### A few conventions

- **Summary** is what appears on the front page and in the RSS feed. Worth
  writing properly.
- **Categories** are broad (News, Tutorial, Review, Editorial). **Tags** are
  specific (TouchPad, LuneOS, ACL).
- **Images** go in through the editor, not linked from elsewhere — the site is
  self-contained by design and should stay that way.
- Write in Markdown. Raw HTML is stripped when the site is built.

## Prefer Git?

Add a Markdown file to `content/posts/` named `YYYY-MM-DD-some-slug.md`, copy
the front matter from any neighbouring file, and open a pull request.

## Editing the rescued articles

Please don't. The 279 articles marked `archived: true` are a historical record
of what pivotCE published, typos and all. Corrections belong in a new article
that links to the old one. Fixing a genuinely broken link or image is welcome.

## The archive itself

[`SITE.md`](SITE.md) documents how the content was recovered, what is missing
and why, and how the site is built and deployed.
