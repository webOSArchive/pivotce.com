---
title: Bing Maps Patched for webOS
date: '2017-12-03T16:56:57Z'
author: Alan Morford
author_slug: alanmorford
categories:
- News
tags:
- bing
slug: bing-maps-patched-for-webos
summary: Bing Maps has been patched for their latest API change for webOS. webOS Nation forums user, Misj’, has developed two patches to cover both the Pre and TouchPad bases.
source_url: https://pivotce.com/2017/12/03/bing-maps-patched-for-webos/
wordpress_id: 4203
archived: true
---

![](/images/files/2017/12/Capture.png)

Bing Maps has been patched for their latest API change for webOS.  webOS Nation forums user, Misj’, has developed two patches to cover both the Pre and TouchPad bases.

Microsoft has switched over to v8 of the maps API and left our old v7 in the dust. Misj’ discovered the issue and wrote a simple patch to change the URL the app points to.

![Before and after on a Pre.](/images/files/2017/12/pre.jpg)
*Before and after on a Pre.*

It’s not 100% perfect since this change doesn’t fix a couple things:
– Birds-eye view does not work any more and results in a blank screen.
– Even though the locale is set to PalmSystem.locale, you may have to add your country to your search criteria to make sure you don’t get a random country result.

![Before and after on a TouchPad.](/images/files/2017/12/tp.jpg)
*Before and after on a TouchPad.*

There’s also a little bit of confusion about which patch to use since some have reported that the TouchPad version of the patch doesn’t work on all TouchPads.  For some reason, some TouchPads have the Pre version of Bing Maps or so it would seem. Basically, if you try to install the TouchPad patch and it fails, try the Pre3 version and you should be fine.

You can get the patches and talk about it [in the post of the forum](http://forums.webosnation.com/webos-patches/331888-bing-maps-v7-api-patch.html).

Personally I use Google Maps by 72ka [found in Preware](http://preware.pivotce.com/package/cz.72ka.googlemaps) which generally speaking works perfectly. But I’m always happy when a developer takes the time to restore functionality to webOS. Thanks Misj’!

#webOSforever
