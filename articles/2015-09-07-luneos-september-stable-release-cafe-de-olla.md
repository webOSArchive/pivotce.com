---
title: 'LuneOS September Stable Release: Café de Olla'
date: 2015-09-07 21:44:11 UTC
modified: 2015-10-07 11:15:27 UTC
author: webosports
author_slug: webosports
categories: [News]
slug: luneos-september-stable-release-cafe-de-olla
source_url: https://pivotce.com/2015/09/07/luneos-september-stable-release-cafe-de-olla/
wordpress_id: 3202
featured_image: ../images/files/2015/09/ollaheader.jpg
featured_image_source: https://pivotce.com/files/2015/09/ollaheader.jpg
excerpt: Only a few short weeks since our August release and we’re already providing you with another stable release. We’re very pleased to present you our latest monthly stable release, Café…
---

# LuneOS September Stable Release: Café de Olla

Only a few short weeks since our August release and we’re already providing you with another stable release. We’re very pleased to present you our latest monthly stable release, Café de Olla or “OIla” for short.

We have been making significant progress in many areas, most importantly in squeezing some long outstanding bugs, improving stability greatly and enhancing legacy webOS compatibility! Almost all Enyo 1 apps from legacy will now run on LuneOS as well. This has improved significantly compared to previous releases.

The most important changes for this month:

A lot of crashes have been solved, most importantly when closing multiple browser tabs & apps not launching properly. We still have a few cases where things break but it has been reduced by about 90-95%! We keep on stress testing our setup to iron out the last few bugs as well for the next releases!

The Browser has been tweaked to provide better compatibility on various websites.

The dashboards & banner messages have been completely reworked and are now working the way they should. We’ve also added variable height dashboard support like it was available in LunaCE! There’s still a few minor improvements to be made though (dashboards close when the apps closes while in legacy they remained active. We’re trying to solve this for a next release :))

We have removed quite some duplicated code from various components and moved this into luneos-components and luna-sysmgr-common so we only need to maintain code once.

Grab your Nexus 4, HP TouchPad, Nexus 7 (2012 WiFi) or emulator and load up our latest builds!

### Changelog

**Apps:**

- Browser: Various bugfixes to fix crashes, improve rendering of various pages and add a scroll indicator and use LunaWebView from luneos-components so we can share this with the Enyo webapps.
- Preware: Add the PivotCE feed (disabled by default).
- FirstUse: Move tests to luneos-components, so we can use the a single source for tests on desktop with QtCreator.

**UI:**

- Virtual Keyboard: Fix minor issues with URL layout for virtual keyboard.
- Luna-Next-Cardshell: Fix notification handling.
- Enyo 1.0: Fix faulty spinner, now using Enyo 2.0 variant instead.
- Accounts/Email: Removed the “Find More” option from HP since it’s no longer relevant.

**System:**

- luna-sysmgr: Make sure that banners are dealt with properly.
- luna-qml-launcher: Use the common application description from luna-sysmgr-common.
- luna-sysmgr-common: Rework the parsing of application description so it’s common across various components.
- luna-appmanager: Use the common application description from luna-sysmgr-common.
- luna-systemui: Fix charging banner behavior and make sure the sizes adopt properly to different screen sizes.
- qtwayland: Fixed bug causing incorrect window destruction.
- luna-next: Use window properties more consistently.
- luna-webappmanager: Use LunaWebView from luneos-components
- luneos-components: Fixed missing image for buttons, fixed ItemSelector for browser & apps, add LunaWebView for sharing the WebView between Browser and Enyo apps. Added test import stubs for use on desktop with QtCreator. Added more flexible approach for website/app database sizes.
- luna-init: Fixed issue with incorrect timezones & descriptions.

### Current work in progress for next releases:

- Further sensor support (ambient light sensor etc)
- Implement LED-support so it’s visible to user.
- Further improvements/options for tabbed launcher
- Telephony support
- SMS & IM improvements & support
- Fix data connection on TP4G
- Support for custom APN’s for oFono
- Bluetooth integration
- Further browser improvements and optimizations
- Further keyboard enhancements for different layouts & languages

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

Feel free to [download the updated builds](http://build.webos-ports.org/releases/olla/images/) to get started. Tenderloin and Mako remain our focus for now and the emulator & Grouper work too.

Installation instructions for [TouchPad (Tenderloin)](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](http://forums.webosnation.com/luneos/330523-pivotce-luneos-august-stable-release-cafe-de-olla.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
