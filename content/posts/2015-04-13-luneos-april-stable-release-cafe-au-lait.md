---
title: 'LuneOS April Stable Release: Café au lait'
date: '2015-04-13T13:45:24Z'
lastmod: '2015-06-24T16:46:59Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- au lait
slug: luneos-april-stable-release-cafe-au-lait
summary: No April Fools jokes here folks. Just a fresh cup of the April LuneOS stable build, Café au lait or “au lait” for short. Lots of changes this month. There…
featured_image: /images/files/2015/04/aulaitheader-1024x576.jpg
source_url: https://pivotce.com/2015/04/13/luneos-april-stable-release-cafe-au-lait/
wordpress_id: 2795
featured_image_source: https://pivotce.com/files/2015/04/aulaitheader-1024x576.jpg
archived: true
---

No April Fools jokes here folks. Just a fresh cup of the April LuneOS stable build, Café au lait or “au lait” for short. Lots of changes this month. *There better be since we didn’t produce a changelog for last month’s nightlies-only releases, amirite?* Hopefully we haven’t disappointed you.

Grab your Nexus 4 or HP TouchPad (or emulator) and load up our latest builds!

### Changelog

- Added contact-lib for common functionality when working with contacts in LuneOS
- Added initial support for sensor mananagement
- QML Apps: Switch to Lune.Service module for LunaService component
- Added initial support for LED
- Added initial support for Bluetooth on Nexus 4 (back-end only for now)
- Calculator app: Minor improvements
- File Manager: Update to Enyo 2.5.1.1
- Ported voicecall from Nemo to use in LuneOS
- Cleaned up webos-lib to remove duplication with enyo-webos
- Fix media indexer to store file name without extension
- Add alert service method to display manager
- Added telephony-lib for shared telephony functionality
- Update C+Dav to 0.3.25, Improved audio service
- Calendar app: Enyo 2 version has had some work, no back-end implementation yet
- Add support for phone app launching from first use (support for PIN window)
- Phone app: Work ongoing for making initial audio call support work
- luna-systemui: Fix restart options, charging status and battery notification handling
- FirstUse: Improved timezone layout and ability to show network passphrase
- Fixed orientation of keyboard window mask
- Add support for QT Quick Controls for QML applications
- Added luneos-components to support styling of QML components being used in apps
- Contacts app: Added support for contact editing & updating associated contacts
- Messaging app: Various minor fixes
- Testr: Added new icon
- webos-telephonyd: Fixed compiler warnings & cleaned up WAN enabling code
- Settings app: Fixed the toggle handling for Telephony
- Luna-Next: Added proper handling for orientation (no full orientation support available yet)
- Luna-Next Cardshell: Added support for PIN windows, ability to exit DockMode with gesture bar, layout improvement to system menu and status bar, fixed icon scaling

### General focus reminder

We get naysaying questions and comments via Twitter from time to time. They’re usually about “it’s a two horse race” or “you’ll never be able to saturate the market” or “it’s an old OS before you’ve even released it”.

**The main focus of LuneOS is to provide an operating system which is driven by the community and continues what we love(d) about webOS.** We’re not trying to reach feature comparison with Android or iOS but rather building a system to satisfy basic needs in the mobile environment. Building a good quality mobile operating system from scratch is a hard job and is built in just the spare free time everyone involved in the project has. To get the best ratio between what we want and what we can do, we’re analyzing architectural decisions from both existing solutions we can base our work on and whether we have to write things from scratch.

Our focus is not to add new devices as they appear on the market but instead to provide a stable, easy to use and easy to port software base. Porting OS pieces itself was never the real problem of our approach since we solved the most important bits by using [libhybris](https://github.com/libhybris/libhybris). The actual problem we’re facing is to get applications software implemented and to add all the back-end functionalities to the system we love and need.

We’re not in the cell phone or tablet business. We’re making a fun, user-centric mobile OS that can be ported to whatever device you can put it on in the future. The Nexus 4 is an easy canvas to use to make a stable OS. The TouchPad was added to increase dev involvement since most of us had them laying around anyway. Got it? 🙂

### Current work in progress for next releases:

- Sensor support (rotation etc)
- LED-support
- Tabbed launcher for Luna Next
- Additional security lock modes
- Telephony support
- SMS & IM improvements & support
- Fix data connection on TP4G
- Support for custom APN’s for oFono
- Bluetooth support

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

Feel free to [download the updated builds](http://build.webos-ports.org/releases/aulait/images/) to get started. Tenderloin and Mako remain our focus for now and the emulator works too.

Installation instructions for [TouchPad (Tenderloin)](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) and [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to join the discussion on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month! We’re getting closer and closer to being able to use LuneOS as a daily driver.

[Chat about it](http://forums.webosnation.com/luneos/329639-pivotce-luneos-april-stable-release-cafe-au-lait.html)
