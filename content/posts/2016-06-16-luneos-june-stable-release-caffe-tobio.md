---
title: 'LuneOS June Stable Release: Caffè Tobio'
date: '2016-06-16T12:34:57Z'
lastmod: '2016-08-10T01:51:24Z'
author: webosports
author_slug: webosports
categories:
- News
slug: luneos-june-stable-release-caffe-tobio
summary: Time flew, already another month passed since our previous release. We have been working hard on improving the stability of LuneOS and especially fixing a lot of minor QA issues…
featured_image: /images/files/2016/06/LuneOS_Caffe_Tobio.png
source_url: https://pivotce.com/2016/06/16/luneos-june-stable-release-caffe-tobio/
wordpress_id: 3669
featured_image_source: https://pivotce.com/files/2016/06/LuneOS_Caffe_Tobio.png
archived: true
---

Time flew, already another month passed since our previous release. We have been working hard on improving the stability of LuneOS and especially fixing a lot of minor QA issues in the Yocto build system we’re using. These were mainly QA warnings, but we didn’t have much chance to address these previously. These are all sorted now, so for new developers building from scratch it will mean they won’t run into errors or warnings.

We have been also looking into improving the stability and fixing some of the regression bugs that we had after we updated a large number of the system components in the previous release.

As a result LuneOS is now more stable (no more crashes of Luna-AppManager and MediaIndexer) and audio on the Nexus 4 (Mako) is working again. The Contacts app is the first app that has now been migrated to Enyo 2.7.

Furthermore we have done some initial work to get Instant Messaging (ICQ, AOL etc working in our system) using [Libpurple and Pidgin](https://developer.pidgin.im/wiki/WhatIsLibpurple). These are common components used on *nix for IM and were also used on legacy webOS. The advantage is that this can be extended with plugins for various protocols like [WhatsApp](https://github.com/davidgfnet/whatsapp-purple), [Telegram](https://github.com/majn/telegram-purple) and [SIPE](http://sipe.sourceforge.net/). This is far from finished yet and there’s still quite some ground to cover, but stay tuned for this!

We’ve also applied some minor updates to QtWebEngine & QtWebEngine-Chromium from upstream work done by the QT team.

**Main Changes:**

– Audio on Nexus 4 (Mako) is working again.
– Crashes and memory leaks for MediaIndexer and Luna-AppManager have been solved.
– Contacts migrated to Enyo 2.7 & on contact details pane, tapping on a phone number, email, IM, URL, address, birthday or anniversary attempts to open the appropriate app. Tapping on a relation searches for that name in Contacts.
– Initial work for IM support using libpurple/pidgin.
– Lots of minor QA fixes for components that are being built using our Yocto build system.
– Fixed data roaming toggle in Settings App.

**Known issues:**

– Splash screen disappears too quickly (though it has improved a lot since we fixed some high CPU usage problems).
– Ringtone & Audio Routing: Audio routing for calls needs fine tuning and there is no ringtone playback yet.
– Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now. We’re sanitizing our components that use [NodeJS](https://nodejs.org), so we’re better prepared going forward and will have an easier upgrade path to newer NodeJS versions. Most components are currently still on NodeJS 0.12.x and we’d like to move to 4.4.x and 6.x later on.

### **Changelog**

**Applications:**
– Tweaks: Cleanup of app code and drop no longer used Mojo version.
– org.webosports.app.phone: TelephonyManager: fix debug log.
– org.webosports.app.settings: Fix allow roaming toggle.
– org.webosports.app.settings: Fix the handling of launch params.
– core-apps: Add access for org.webosports.app.memos to com.palm.note.
– org.webosports.app.contacts: Switched to Enyo 2.7.
– org.webosports.app.contacts: On contact details pane, tapping on a phone number, email, IM, URL, address, birthday or anniversary attempts to open the appropriate app. Tapping on a relation searches for that name in Contacts.

**System Level:**
– luna-webappmanager: Fix initial scaling and viewport for apps.
– org.webosports.update: Drop unneeded systemd file. Same file was already provided by webos-system-update.
– qtwebengine-chromium: Update to latest Chromium 45 based from upstream (13 bugfixes/backports).
– qtwebengine: Update to latest 5.6.1 from upstream.
– nodejs-module-webos-pmlog: Switched to own repo instead of upstream.
– nodejs-module-webos-dynaload: Switched to own repo instead of upstream & fixed NodeJS 4.x/6.x compatibility.
– nodejs-module-webos-sysbus: Switched to own repo instead of upstream & fixed NodeJS 4.x/6.x compatibility.
– mojoloader: Switched to own repo instead of upstream.
– mojoservicelauncher: Switched to own repo instead of upstream.
– foundation-frameworks: Switched to own repo instead of upstream & fixed NodeJS 4.x/6.x compatibility.
– app-services: Add missing mediathumbnail filecache_type.
– imlibpurpleservice: Various fixes to make it work.
– utilities: Fix includes for bluetooth in build for Touchpad.
– luna-next-cardshell: Notifications, don’t resize client window too soon.
– luna-next-cardshell: Fix launchParams to be empty to maintain legacy compatibility.
– luna-service2: Update to latest from upstream.
– core-apps: Add access for org.webosports.app.memos to com.palm.note.
– webos-telephonyd: Make dial method compatible with legacy & improve errorCode reporting.
– org.webosports.app.tasks: Add initial db8 kind & permissions skeleton for Synergy for tasks.
– mediaindexer: Fix issue with image albums & memory leaks.
– luna-appmanager: Fix various warnings that lead to many crashes at boottime.
– org.webosports.app.contacts: Switched to Enyo 2.7.
– messaging-accounts: Added initial work for IM templates.
– luneos-default-wallpapers: Fix QA issues during build.
– connman-conf: install wired-setup to datadir.
– hunspell: move ispellaff2myspell to separate package.
– presage: add dependency on ncurses.
– android-property-service: Add DEPENDS on luna-prefs.
– org.webosports.service.update: Add RDEPENDS on bash.
– core-apps: Add RDEPENDS on bash.
– loadable-frameworks: Add RDEPENDS on bash.
– lxc: Add RDEPENDS on bash.
– packagegroup-luneos-development: Bring valgrind back.
– presage: Fix QA issues.
– luneos.inc: Add Ubuntu 15.10 and 16.04 to sanity tested distros.
– geoclue: Add avahi to DEPENDS.
– sensorfw: Add bash to RDEPENDS.
– ofono: Add patches to revert Python 3 changes.
– presage: Implement version independent approach to Python.
– https-everywhere: Add initial recipe for providing the https rulesets.
– pidgin: simplify bbappend.
– qtscenegraph-adaptations: Drop patches & follow upstream directly.
– lxc: Upgrade to 2.0.
– pulseaudio-modules-droid: Fix audio on Nexus 4 (Mako).-

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/tobio/images/) to get started. Tenderloin and Mako remain our focus for now, but the emulator, Maguro & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion](http://forums.webosnation.com/luneos/331239-pivotce-luneos-june-stable-release-caffe-tobio.html) on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
