---
title: 'Review: ACL™ for webOS Preview 0.6.0-4'
date: '2013-10-22T01:16:15Z'
lastmod: '2013-12-20T13:24:46Z'
author: Sören Müller
author_slug: pattyland
categories:
- Reviews
tags:
- ACL
slug: review-acl-for-webos-beta-0-6-0-4
summary: 'If you are an HP TouchPad owner, you might have heard of the Android Compatibility Layer (ACL) for webOS, a Kickstarter project from Phoenix International Communications (PIC). The project can be easily explained: run Android…'
source_url: https://pivotce.com/2013/10/22/review-acl-for-webos-beta-0-6-0-4/
wordpress_id: 320
archived: true
---

If you are an HP TouchPad owner, you might have heard of the **A**ndroid **C**ompatibility **L**ayer (ACL) for webOS, a [Kickstarter project](http://www.kickstarter.com/projects/1957339277/run-android-apps-in-webos-on-the-hp-touchpad) from Phoenix International Communications (PIC).  The project can be easily explained: run Android apps on the TouchPad without dual-booting to Android.

Two days ago, PIC tweeted that they [sent out the preview release to kickstarter backers](https://twitter.com/phxdevices/status/391411573702799360), giving us (me included) a chance to look at ACL before the general public.

## Installation

The installation was easy.  At first I restored my TouchPad to be sure that no previous Android/Ubuntu experiments interfered with ACL.  As with any other webOS .ipk it is simply installed via webOS Quick Install.

Tip: [Eric Blade](https://twitter.com/ekdikeo) told us on Twitter that he had [problems with WOSQI and ACL](https://twitter.com/ekdikeo/status/392039296518991872), and he had to reboot after 30 minutes to get ACL running.

After the reboot you have about 20 more icons in your Downloads tab of the webOS app launcher.  Besides the ACL App with information about ACL you’ve got a full palette of Andriod 2.x apps, including Browser, Email, Messaging, Music, Settings, etc.

![Bildschirmfoto 2013 10 20 um 23 23 53](/images/files/2013/10/Bildschirmfoto-2013-10-20-um-23.23.53.png)
WOSQI installing ACL preview; Took about 10 minutes

## Using

Using ACL was even easier than the installation.  Every Android App has an icon in the same place as the webOS ones while only the three [Android Navigation bar](http://developer.android.com/design/patterns/navigation.html) icons tell you that this is not a native app.

The first thing I wanted was a new browser, so I searched in the auto installed “OpenMobile AppMall”, a tiny version of the Google Play Store.  I couldn’t find either Opera or Firefox, so I sought out and installed the [Amazon](http://www.amazon.com/gp/mas/get/android) [Appstor](http://www.amazon.com/gp/mas/get/android)[e](http://www.amazon.com/gp/mas/get/android) [for Android](http://www.amazon.com/gp/mas/get/android).

Tip: At first I downloaded the Amazon app store .apk with the stock webOS browser but right now there is no *connection* between the two systems.  If you want to install the .apk you have to download it with the stock Android browser.

![Opera Mobile on the TouchPad via ACL, scoring 100/100 in the Acid3 Browser test; Much better than the webOS Stock browser!](/images/files/2013/10/SDL_2013-21-10_000855-1.png)
*Opera Mobile on the TouchPad via ACL, scoring 100/100 in the Acid3 Browser test; Much better than the webOS Stock browser!*

## Speed

For a pre-release the speed is really amazing.  An Android app takes only about 2 seconds longer than a native app to launch.

## Problems

As there are about 700,000 apps in the Play Store, there will be some that make problems.  In this short time I only tested the Amazon App Store and Opera Mobile, both work great.

The only big problem I got is when I try to mount my TouchPad in USB mode.  webOS says that there are open cards (though all are closed) and hangs in a state where you can’t open any app.

Tip: Don’t activate USB mode (in this version).

UPDATE:  It looks like PIC just [pushed the 0.6.0-5 update](https://www.facebook.com/photo.php?fbid=530122833746177&l=f30802493c) which fixes the USB mode bug.

## Conclusion

I’m really excited how good this will get.  Apps are very important for a mobile OS, and to be fair the HP App Catalog is not the one with the most or most relevant these days. Now we have hundreds of thousands apps more, which is really great!

Thank you so much PIC and OpenMobile for making this happen!  pivotCE will continue to bring updates about ACL for webOS as they are released.
