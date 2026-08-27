---
title: 'LuneOS Cafe Cubano: An In-Depth Look'
date: '2015-08-06T00:16:31Z'
lastmod: '2015-12-10T17:20:20Z'
author: Chairman Honeycrisp
author_slug: chairmanhoneycrisp
categories:
- Reviews
slug: luneos-cafe-cubano-an-in-depth-look
summary: It’s pretty hard to believe that it’s only been three months since HP pulled the plug on official support on webOS and shut down its cloud services. Yet with the…
featured_image: /images/files/2015/08/LuneOSCafeCubano.png
source_url: https://pivotce.com/2015/08/06/luneos-cafe-cubano-an-in-depth-look/
wordpress_id: 3097
featured_image_source: https://pivotce.com/files/2015/08/LuneOSCafeCubano.png
archived: true
---

It’s pretty hard to believe that it’s only been three months since HP pulled the plug on official support on webOS and shut down its cloud services. Yet with the arrival of August, the loyal base of webOS developers and enthusiasts who have stuck around will likely be seeing the ninth stable release of LuneOS in the very near future.

Despite having been churning out stable builds for less than a year, the webOS Ports team’s LuneOS is already proving to be a very capable candidate to fill the void left behind by webOS. Read on past the jump, and we’ll examine how the latest LuneOS, Cafe Cubano, measures up to its predecessor.

Anyone familiar with webOS probably knows the story by now: After having been plagued by middling sales numbers, as well as subpar hardware compared to the competition, HP CEO Leo Apotheker pulled the plug on hardware development for webOS devices in 2011. After his sacking, replacement CEO, Meg Whitman open-sourced parts of the OS in 2012. It was this that the webOS Ports team took to build LuneOS. Since launching LuneOS, the team have stuck more or less to releasing a build every month, although there wasn’t a build last month, according to the team’s Twitter feed:

> Who works over the summer on coding projects? We do. Albeit a bit slower. No release this month. See you in August! [#LuneOS](https://twitter.com/hashtag/LuneOS?src=hash) is coming!
>
> — webOS Ports (@webosports) [July 12, 2015](https://twitter.com/webosports/status/620280049355345921)

And besides, it’s important to note that the LuneOS dev team, as they always stress, do not do timelines, although already-released builds available for download. The team have chosen to name their builds after kinds of coffee, in alphabetical order, using names such as Affogatto, and Cafe Cubano, the latest stable build which I’ll be looking at. I’m running this LuneOS build on my HP Touchpad (codename: Tenderloin). Builds are also available for the LG Nexus 4 (Mako), the 2012 Google Nexus 7 (Grouper), and for emulators such as VirtualBox (Qemux), although the team is currently focusing on the Touchpad and Nexus 4.

Installing LuneOS on the Touchpad can be a little tricky, but essentially it boils down to creating a partition for LuneOS, then installing the kernel and extracting the build to the partition using Novacom. Full instructions are listed here, but please do note that there are rules that you will have to agree to before using LuneOS. These are called “stable” builds, but it has to be stressed that this is alpha software that is still undergoing major developments, and therefore reserves the right to throw up its hands and brick your device anytime it chooses.

But I disgress. Let’s move on!

After booting into LuneOS, we’re greeted by a first-use app, which provides options to configure things such as wireless, as well as language and country. It’s essentially the basic settings that would normally be seen on any other first-use app. That being finished, the first-use app disappears in favor of the familiar face of the LuneOS homescreen.

![LuneOS Homescreen: Bet you haven't seen this before!](/images/files/2015/08/LuneOS_homescreen.png)
*The LuneOS Homescreen*

LuneOS keeps that familiar interface that we saw in the legacy webOS, and for those who haven’t used webOS before, it’s actually quite easy to pick up, with simple swipe gestures to bring up and minimize the app drawer, scroll through open apps, and close whatever you need.

It looks a lot like LunaSysMgr, which is what the legacy webOS interface was called, but it isn’t. The webOS Ports team made the decision to completely re-write LunaSysMgr using more modern web technologies such as WebKit 2 and Qt 5.2, dubbing the result Luna Next. According to the team, the rewrite will make things like porting and hardware acceleration easier in the long run.

And of course, LuneOS does keep the card multitasking metaphor that was perhaps webOS’s defining feature. It is interesting to note, however, that the LuneOS gang appear to be using the more rounded cards from the olden days of webOS 2.0, rather than the more rectangular cards used in the tablet-only webOS 3. It also has the good old gesture area, which webOS on the HP Touchpad didn’t have.

Users of legacy webOS, however, might be disappointed to discover that LunaCE, the community-developed modification to LunaSysMgr, is not included. That means that more advanced gestures such as bezel swiping to switch between cards and pinch-zooming to resize cards, have not been implemented yet, although the LuneOS team did state in their launch article that they are planning to implement LunaCE features in the future.

Almost a year into development as LuneOS, many core functionalities are already in place. Wi-Fi obviously works, and screen rotation was functional as of Cafe au Lait, the May stable build. Nexus 4 users will be also be happy to know that mobile data and SMS messaging do work, having been implemented in February with the Americano build. Telephony and Bluetooth aren’t working as of Cubano, but at least some backend is in place, and the dev team have listed it in their Cubano release article as a work in progress for future releases.

When it comes to bundled apps, LuneOS doesn’t disappoint. LuneOS has a web browser, which is nearly identical to its legacy counterpart. The web browsing experience on LuneOS is surprisingly good, with pages loading very well and, I dare say, rendering better than webOS (Case in point: Loading up pivotCE on my Touchpad won’t render some of the icons; LuneOS does so without skipping a beat). Even sites like YouTube work, although without hardware acceleration, the result is fairly choppy. But it’s great to know that the foundation is there.

![Above: The pivotCE website loaded on webOS. Below, the same site on LuneOS. Notice the missing icons.](/images/files/2015/08/browsercomparison.jpeg)
*Above: The pivotCE website loaded on webOS. Below, the same site on LuneOS. Notice the missing icons.*

The mail app also makes a return, working very similarly to its legacy counterpart. Of course, there are other basic apps such as Messages, Calendar, Notes, Settings and a File Manager. A re-designed Preware 2 (based on Enyo 2) is now the default app store. Being the alpha-level software that it is, LuneOS is also bundled with more developer-oriented apps such as Fingerterm, a terminal emulator, and an app called Testr, which has tools for testing things such as Notifications and HTML5 Audio.

However, that doesn’t translate into LuneOS’s third-party selection. That sector had always been a knock on the operating system, and so far LuneOS hasn’t changed that. Firing up Preware 2, webOS’s homebrew app catalog, reveals it contains a grand total of six apps in the catalog, all of them essentially repackaged websites. There are a couple more feeds that can be activated through the settings, and you can get more by side-loading or by adding feeds from the legacy Preware, but not all of them have been written for LuneOS and so may not work (Alan documented this in [a previous article](/2014/09/16/two-weeks-with-luneos-an-app-sideload-test/) on pivotCE).

Obviously, LuneOS is still under development, so technically there’s no point in counting how many apps it has right now. Interestingly, there are plans to include apps from other operating systems such as Sailfish, as Alan has [written here](/2015/06/18/where-will-luneos-get-its-apps/). This will allow LuneOS access to a list of apps that, although not as large as the likes of iOS and Android, are still more modern than legacy webOS’s.

![Not all hands can count how many apps Preware on LuneOS has. But some can.](/images/files/2015/08/only-six-apps.png)
*Not all hands can count how many apps Preware on LuneOS has. But some can.*

Overall, it’s a great start to a very promising new operating system. Let’s be honest here, LuneOS will probably never reach the heights of iOS and Android, but the progress the webOS Ports team have made so far is so encouraging, I wouldn’t be surprised if by next year it reaches a point where the features and stability are such that it LuneOS can become a daily driver OS.

Needless to say, I’ll certainly be following and rooting for LuneOS. After all, the idea of having all the features that made webOS so great, combined with an improved browsing experience and even a more modern app selection on my HP Touchpad makes my mouth water, and I look forward to the day when that becomes a reality.

So, ready to give LuneOS a go? Here are the links to the installation instructions:

[Tenderloin (HP Touchpad)](http://www.webos-ports.org/wiki/Install_LuneOS_for_Tenderloin)

[Mako (LG Nexus 4)](http://www.webos-ports.org/wiki/Install_LuneOS_for_Mako)

[Grouper (LG Nexus 7)](http://www.webos-ports.org/wiki/Install_LuneOS_for_Grouper)

[Emulator](http://www.webos-ports.org/wiki/Install_LuneOS_for_qemux86)

Download the latest builds, and happy installing!
