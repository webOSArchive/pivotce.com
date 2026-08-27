---
title: TIP – YouTube Search/Quality fix for webOS 1.x/2.x
date: '2013-10-03T21:12:47Z'
lastmod: '2013-11-01T19:50:24Z'
author: Alan Morford
author_slug: alanmorford
categories:
- Tips
slug: tip-youtube-searchquality-fix-for-webos-1-x2-x
summary: Has it been a while since you’ve used YouTube on your webOS phone? Say, before September of this year? If you answer yes, you’ll find that popping open the app…
source_url: https://pivotce.com/2013/10/03/tip-youtube-searchquality-fix-for-webos-1-x2-x/
wordpress_id: 191
archived: true
comment_page: 2013-10-03-tip-youtube-searchquality-fix-for-webos-1-x2-x
---

![brokenyoutube](/images/files/2013/10/brokenyoutube.png)Has it been a while since you’ve used YouTube on your webOS phone?  Say, before September of this year?  If you answer yes, you’ll find that popping open the app displays what you expect to see but search won’t return results and clicking on a video in the Popular Videos list will play, however, quality is terrible.  Even with your l337 hax0r skillz set to ENGAGE, you dig into and edit some YouTube javascript files on your phone and manage to reenable search, you’ll still notice video quality remains on “turd level”.  If you’re a Pre 3 user you’ll notice you don’t have the app but instead a launcher for the mobile YouTube site which means your search is unaffected yet your quality is reduced all the same.

Don’t worry!  Unsurprisingly, the webOS community responded in force and solved the issue practically overnight.  Who says all the devs left???

The solution came in two parts.  First, webOS Nation forum user Nafetz discovered the [solution to search](http://forums.webosnation.com/palm-pixi-pixi-plus/325994-palm-pixi-youtube-bug.html#post3401504) less than 24 hours after the first problem was reported.  But don’t change that dial just yet because Nafetz’s solution was quickly followed by webOS Nation user pcworld (known for such apps as Explorer for Dropbox, File Explorer, QuickChat for Facebook, Archive Manager, and FTPit!).  pcworld’s in-kind response corrected the quality issue and also incorporated the search fix from Nafetz with a [few patches](http://forums.webosnation.com/webos-patches/326010-patch-webos-2-fix-low-youtube-quality.html#post3401601) just 24 hours after that!  pcworld created 2 patches that work for different devices/webOS revisions.  Here’s the breakdown:

1. Phones with webOS 1.x/2.0.x/2.1.x or any “super script” meta-doctored version of webOS use – youtube-quality-fix_2.1.0-v1.patch
2. Phones with webOS 2.2.x (not “super” meta-doctored) use – youtube-quality-fix_2.2.4-v2.patch

Not sure what version to use?  Bottom line:  if you have the YouTube application use the first patch.  For everyone without the app but instead have a link to the mobile site, simply use the second patch.

So what happened?  It seems YouTube (ok, we’re really talking about Google) changed the API.  You can see their changelog for [v2](https://developers.google.com/youtube/2.0/developers_guide_protocol) and [v3](https://developers.google.com/youtube/v3/).

See the pictures below for before and after shots from a Palm Pre+ meta-doctored to 2.1.0.

I think it goes without saying but a HUGE thank you to Nafetz and pcworld!  If development continues, webOS continues.  Thanks!

#webosforever

This slideshow requires JavaScript.
