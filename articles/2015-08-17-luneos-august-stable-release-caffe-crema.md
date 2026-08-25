---
title: 'LuneOS August Stable Release: Caffè Crema'
date: 2015-08-17 11:39:48 UTC
modified: 2015-09-08 03:09:31 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [crema, emulator]
slug: luneos-august-stable-release-caffe-crema
source_url: https://pivotce.com/2015/08/17/luneos-august-stable-release-caffe-crema/
wordpress_id: 3176
featured_image: ../images/files/2015/08/crema.jpg
featured_image_source: https://pivotce.com/files/2015/08/crema.jpg
excerpt: Over summer things always slow down a bit which is why we didn’t have a release last month. It’s about quality and because we basically had too many loose ends that needed…
---

# LuneOS August Stable Release: Caffè Crema

Over summer things always slow down a bit which is why we didn’t have a release last month. It’s about quality and because we basically had too many loose ends that needed fixing before we could push out a release we held off until this month. We’re very pleased to present you our latest monthly stable release, Caffè Crema or “Crema” for short.

We have been making significant progress in many areas:

Additional keyboard layouts have been added for further languages for both tablet and phone layouts like Arabic, Czech, Danish,  Finnish, Hebrew, Russian, Swedish,  Spanish and Russian thumb keyboard (proof of concept). Further work on additional languages is ongoing and should be available in future releases. We also found a bug in virtual keyboard input handling for Ajax calls on websites and in apps and this has now been resolved as well.

The browser has been improved. Multiple cards are now properly working, bookmarks and history are working again too. Support for various types of popup dialogs have been added (Alert Box, Prompt Box, Confirm Box, Certificate Dialog, Proxy Authentication Dialog etc) as well as support for various HTML input types like “file”. This has been added to the luna-webappmanager as well, so it can be used in apps as well.

Bluetooth back-end support for the TouchPad has been implemented. Work on the front-end in Settings has progressed significantly as well. We’re currently working on a plugin to glue the various bits together.

A new Google Maps app rewritten in Enyo 2 by [72ka](http://pivotce.com/2014/09/19/dev-highlight-72ka/) (the author of the legendary Google Maps app for legacy webOS (written in Mojo)) has been included in our images as well. It works fairly well already, considering this is an initial alpha release. It will need some polishing for sure but basic functionality is already there.

FirstUse has been reworked so it can be run standalone on the desktop with dummy luna-service calls to allow quicker development and bug fixes. Also added support to filter the long lists for countries, languages and timezones.

[C+Dav](http://pivotce.com/2014/11/11/use-caldav-to-maintain-google-calendar-sync/) has been updated to 0.3.33 which fixes various issues and improves stability.

Grab your Nexus 4, HP TouchPad, Nexus 7 (2012 WiFi) or emulator and load up our latest builds!

### Changelog

**Apps:**

- Browser: Various bugfixes and support for various dialogs, alerts and popups.
- Calculator: Various minor improvements.
- FirstUse: Reworked luna-service calls and added mock data for desktop & added filters in the lists.
- Preware: A number of minor bugfixes.
- Settings: Added proper handling of Audio settings.
- Luna-Next-Cardshell: Fixed various minor bugs.
- Photos & Videos: Initial app mock.
- PDF: Updated to pdf.js [1.1.215 pre-release.](https://github.com/webOS-ports/org.webosports.app.pdf/commit/8c5897ea44ffc327fd84b11ef5a929e4fd08c13b)
- [Testr: Fix bugs in luna-service calls.](https://github.com/webOS-ports/org.webosports.app.pdf/commit/8c5897ea44ffc327fd84b11ef5a929e4fd08c13b)
- Tweaks: Fix some cosmetics in banner messages.

**System:**

- utilities: Enable bluetooth on Touchpad.
- webos-keyboard: Added many additional languages and various bugfixes.
- Audio-service: Fix volume handling.
- luna-init: Enable all available keyboard languages.
- luna-webappmanager: Add support of new features like popups, dialogs and alerts.

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

Feel free to [download the updated builds](http://build.webos-ports.org/releases/crema/images/) to get started. Tenderloin and Mako remain our focus for now and the emulator & Grouper work too.

Installation instructions for [TouchPad (Tenderloin)](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to join the discussion on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
