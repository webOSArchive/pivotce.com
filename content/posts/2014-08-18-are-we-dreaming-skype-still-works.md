---
title: Are we dreaming? Skype still works!
date: '2014-08-18T16:05:09Z'
lastmod: '2014-08-19T16:48:44Z'
author: preemptive
author_slug: preemptive
categories:
- News
slug: are-we-dreaming-skype-still-works
summary: Microsoft recently announced the end of support for older versions of Skype including on it’s own Windows Phone 7 system. When reports started to be posted about Skype not working…
featured_image: /images/files/2014/08/Skype.jpg
source_url: https://pivotce.com/2014/08/18/are-we-dreaming-skype-still-works/
wordpress_id: 1922
featured_image_source: https://pivotce.com/files/2014/08/Skype.jpg
archived: true
---

Microsoft recently [announced the end of support for older versions of Skype](http://www.cnet.com/news/microsoft-to-kill-skype-for-windows-phone-7/) including on it’s own Windows Phone 7 system.

When reports started to be posted about Skype not working on webOS, they were greeted with an air of inevitability. Another bit was falling off the zombie!

So what are the options? Often the open nature of webOS means that when something stops working (usually due to an [API](http://en.wikipedia.org/wiki/API#Web_APIs) change) or needs some other improvement, it can be patched. It was possible that Skype was reading version numbers from apps and blocking the old version. Very early in webOS’s history, Palm were ‘spoofing’ Pre’s to appear to be iphones – enabling them to connect to itunes. This was a move swiftly blocked by Apple, but a similar trick was employed by a homebrew patch to ensure access to richer versions of mobile websites designed for the iOS products.

Unfortunately, Skype is a proprietary and closed-source product. Serious hacking skills would be required to convince the servers that Skype for webOS was an up to date version.

There are a number of options for running Android. On the Touchpad you can dual boot to Cyanogenmod, the open Android project or run [the ACL](/2014/02/14/acl-release-part-2/) under webOS. On the Pre3 you can try the [Android Chroot project](/2014/02/14/acl-release-part-2/). The developer Nikolay Nizov, has [tested Skype for Android](http://forums.webosnation.com/android-webos/327344-pre3-androidchroot-run-android-inside-webos-9.html#post3423412) and it appears to work, but it is still early days for this project. The limited memory of the Pre3 means it is slow and as sound support is yet to be implemented, only messaging is possible at this time.

Microsoft make a version of [Skype for desktop Linux](http://www.skype.com/en/download-skype/skype-for-linux/) and webOS is a Linux-based OS. It may be possible to run it on webOS devices, but as interfaces differ, usability may turn out to be impractical – it may not be possible to graft a card interface onto what is again, proprietary software.

Are there open-source options? Well, yes. For example, there is [Linphone](http://www.linphone.org), but here of course, we run up against the popularity problem. Who do you know who uses it or any system based on the open-source SIP protocol for Voice over Internet Protocol? Hmmm.

By now you are wondering about that headline. Doesn’t it say that Skype still works on webOS? In a suprisingly pleasant shock announcement today, the community manager of the [Skype forums](http://community.skype.com/t5/Other-devices/Skype-for-webOS-update/m-p/3559255#M18890) recommended re-logging in, claiming Skype on webOS was still supported. He’s right. So was it a coincidental temporay fault? Was webOS blocked in error then restored? There are no details. Let’s just be thankful and Skype our friends with the good news.

We should bear in mind that sooner or later, Skype will get an update that may break functionality with the webOS version. Given the current state of webOS, it’s unlikely that the Skype integration will be updated. So due consideration should still be given to the options above. One hope is that LG will want to offer video calling on those big screens and any future LGwebOS app may be portable to mobile devices…

[Update] In a roundabout way, I found there is an alpha version of [Linphone for webOS](http://forums.webosnation.com/webos-internals/274615-linphone-alpha-testing.html) which may have some use in the future.
