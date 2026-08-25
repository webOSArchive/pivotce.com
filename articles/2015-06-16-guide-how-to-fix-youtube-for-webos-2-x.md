---
title: 'Guide: How to Fix YouTube for webOS 2.x'
date: 2015-06-16 14:26:13 UTC
modified: 2015-12-10 18:03:44 UTC
author: Alan Morford
author_slug: alanmorford
categories: [Tips]
tags: [2.x, choorp]
slug: guide-how-to-fix-youtube-for-webos-2-x
source_url: https://pivotce.com/2015/06/16/guide-how-to-fix-youtube-for-webos-2-x/
wordpress_id: 3055
featured_image: ../images/files/2015/06/youtube.jpg
featured_image_source: https://pivotce.com/files/2015/06/youtube.jpg
excerpt: 'UPDATE: Stop what you’re doing and check out LuneTube. It doesn’t integrate into webOS for links yet but it’s developing very nicely as a YouTube client for webOS and LuneOS!…'
---

# Guide: How to Fix YouTube for webOS 2.x

**UPDATE:** Stop what you’re doing and [check out LuneTube](https://pivotce.com/2015/10/16/app-lunetube/#more-3262). It doesn’t integrate into webOS for links yet but it’s developing very nicely as a YouTube client for webOS and LuneOS!

As for the fix below, it still works but the suggested YouTube site links per device are now only showing RTSP feeds. Bad quality! The patched app and patch itself still work for better quality but only if you hit the 3 dot menu on the upper right of the mobile site and select Desktop. It’s a bit harder to see but the videos play with normal quality. Also, going to the desktop view immediately puts the cursor in the search bar so once the page loads, just start typing for what you want. If you scroll first or tap the search bar you’ll get the annoying bug where typing jumps up to the URL bar in the browser.

---

This fix for YouTube is for 2.x devices only. I have tried it on 1.x but it didn’t work. Logs show “Error: service request: “com.palm.app.youtube” was not found. *Smart people feel free to figure that one out!* I know I’ll be grateful since I do like to use my Pixi from time to time.

I have installed this fix onto a Pre3 with 2.2.4, a Pre 2 with 2.2.4, a Veer meta’d to 2.2.4, and a Pre+ meta’d to 2.1.0. Other 2.x versions should work fine but your results may vary. To clarify though, **if you’re on a stock 2.2.4 doctor for Pre3 or Pre2…just install the patch from TheOneill.**

**![brokenyoutube](../images/files/2013/10/brokenyoutube.png)What I did**

I installed the [new quality fix patch from TheOneill](http://forums.webosnation.com/webos-apps-games/329711-now-youtube.html#post3437650) on my Pre3. I then copied the com.palm.app.youtube folder from /usr/palm/applications to internal media and onto my PC and made a new installable package with [IPK packager](http://forums.webosnation.com/canuck-coding/237326-ipk-packager.html).

**Fix it – Read** ***everything*** **first!**

Download the [patched YouTube app](https://app.box.com/s/ka3pyp4eov11m4lud2p22s3exvdkxvb8).

You need to have [developer mode turned on](https://pivotce.com/2014/10/21/guide-coming-back-to-webos-in-2014-part-1/) (step 4) and have the system set to read/write. To do that install and open [Internalz Pro](http://preware.pivotce.com/package/ca.canucksoftware.internalz) on your phone and [enable Master Mode (video)](https://www.youtube.com/watch?v=6DalIh9Al98) in Preferences after you enable developer mode.

Plug your 2.x device into your computer and launch [WOSQI](http://forums.webosnation.com/canuck-coding/274461-webos-quick-install-v4-6-0-a.html). Click Tools > Linux Commandline. Issue the command ipkg remove com.palm.app.youtube. This removes the stock YouTube app. Open Internalz Pro on your phone and browse to /usr/palm/applications and delete the com.palm.app.youtube folder.

Add the downloaded ipk into WOSQI and install it. Open Internalz Pro again and browse to /media/cryptofs/apps/usr/palm/applications and **MOVE** the com.palm.app.youtube folder from there to /usr/palm/applications and then **REBOOT** your phone.

Open your browser and in preferences clear history, cache, and cookies.

The desktop view of youtube works on all devices but these sites look best on each device:

**Pre3** – m.youtube.com/?use_blazer=1&tsp=1
**Pre2** – m.youtube.com/?use_blazer=1&tsp=1
**Veer** – m.youtube.com/?app=m This one is finicky! Remember mine is on 2.2.4. You **MUST** clear history, cache, and cookies. The other youtube mobile site will force an rtsp stream which gets 3gp video and looks terrible. This website is pretty bland looking but is very readable and works well.
**Pre+** – m.youtube.com/?use_blazer=1&tsp=1

If the Veer gives you fits just use the desktop site which renders poorly. I tried the [Hulu patch](http://forums.webosnation.com/hp-pre-3/311733-hulu-patch-pre-3-a.html) and it didn’t help at all. I also tried Choorp’s [user agent](http://forums.webosnation.com/webos-patches/317911-patch-user-agent-override.html) override ([download](https://github.com/choorp/webos-patches/archive/master.zip)) which fixed the mobile view but I couldn’t get any videos to launch at all. None of my devices use the user agent override.

I recommend using [Shortcut Launcher](http://forums.webosnation.com/webos-apps-games/310073-awesome-update-shortcut-launcher.html) ([download](https://app.box.com/s/mr83ds9q5b9da0fycq48fnzkcxqzw6dp)) to make a nice looking YouTube icon in your launcher that brings up the links I gave you above. Good luck!

#webosforever
