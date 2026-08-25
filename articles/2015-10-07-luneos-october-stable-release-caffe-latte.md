---
title: 'LuneOS October Stable Release: Caffè Latte'
date: 2015-10-07 05:18:48 UTC
modified: 2015-12-10 17:21:10 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [Caffè Latte]
slug: luneos-october-stable-release-caffe-latte
source_url: https://pivotce.com/2015/10/07/luneos-october-stable-release-caffe-latte/
wordpress_id: 3246
featured_image: ../images/files/2015/10/Caffe-Latte-Prague.jpg
featured_image_source: https://pivotce.com/files/2015/10/Caffe-Latte-Prague.jpg
excerpt: We’re very pleased to present you our latest monthly stable release, Caffè Latte or “Latte” for short. For this month we have mainly been focusing on upgrading fundamentals of our…
---

# LuneOS October Stable Release: Caffè Latte

We’re very pleased to present you our latest monthly stable release, Caffè Latte or “Latte” for short.

For this month we have mainly been focusing on upgrading fundamentals of our OS. We have upgraded our Yocto release from Dizzy to [Fido (Yocto 1.8)](https://www.yoctoproject.org/downloads/core/fido18) which brings a great deal of improvements of various bits of the underlying software for LuneOS.

We also moved from Qt 5.4.2 to Qt 5.5 which brings us various performance improvements in the QML-side of things (noticable in the UI) and it brings us QtWebEngine instead of QtWebKit. [QtWebEngine is the replacement of QtWebKit and will allow Qt to keep up to date a lot more quickly with Google’s development of Blink/Chromium](https://blog.qt.io/blog/2013/09/12/introducing-the-qt-webengine/). In the short term this means that we will lack a number of minor features that QtWebKit used to offer, but the Qt development team is working hard to bridge the gaps. The move will for sure mean a lot better compatibility with modern websites and features as shown with the almost 100 point bump we got on <http://www.html5test.com> score while comparing our browser using QtWebKit and QtWebEngine.

For this release the browser has already been updated to make use of QtWebEngine. We are still working on updating the back-end rendering engine for Enyo 1/2 apps to make use of the new QtWebEngine as well, but as you can imagine this is not an easy task and requires a bit more time.

Seeing the number of significant changes in the underlying system bits we decided to still push out a release this month, so you can test it and provide us your feedback.

Grab your Nexus 4, HP TouchPad, Nexus 7 (2012 WiFi) or emulator and load up our latest builds!

Known issue: Audio on Nexus 4 currently doesn’t work due to an upgrade of PulseAudio. We’re investigating this and hope to have this solved the next release.

### Changelog

***Apps:***

- Settings: Cleaned up timezone handling
- Browser: Moved to QtWebEngine
- luneos-components: Added support for QtWebEngine
- C+DAV: Upgraded to version 0.3.34
- Testr: Added support for HTML5 banners/notification (not yet supported by our version of Qt though).

***UI:***

- Upgraded to Qt 5.5
- luna-next-cardshell: Allow removal of apps from launcher

***System:***

- luna-sysmgr: Fixed bug that allowed to bypass security PIN by connecting via USB.
- Upgraded from Qt 5.4.2 to Qt 5.5 bringing QtWebEngine.
- Upgraded various components to work with Qt 5.5 (webos-keyboard, qt5-qpa-hwcomposer-plugin, qtwayland, luna-next).
- Upgraded Yocto from Dizzy to Fido (Yocto 1.8).

*Current work in progress for next releases:*

- Complete migration to QtWebEngine for Enyo 1/2 apps
- Further sensor support (ambient light sensor etc)
- Implement LED-support so it’s visible to user.
- Further improvements/options for tabbed launcher
- Telephony support
- SMS & IM improvements & support
- Fix data connection on TP4G
- Support for custom APN’s for oFono
- Complete Bluetooth UI integration
- Further browser improvements and optimizations
- Further keyboard enhancements for different layouts & languages

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

Feel free to [download the updated builds](http://build.webos-ports.org/releases/latte/images/) to get started. Tenderloin and Mako remain our focus for now and the emulator & Grouper work too.

Installation instructions for [TouchPad (Tenderloin)](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](http://forums.webosnation.com/luneos/330629-pivotce-luneos-october-stable-release-caffe-latte.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!

*image: [Tamorlan](https://commons.wikimedia.org/wiki/File:Caffe-Latte-Prague.JPG).*
