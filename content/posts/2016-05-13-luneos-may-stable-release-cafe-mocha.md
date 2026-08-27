---
title: 'LuneOS May Stable Release: Café mocha'
date: '2016-05-13T15:32:29Z'
lastmod: '2016-06-16T22:16:19Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- Developer
slug: luneos-may-stable-release-cafe-mocha
summary: 'Welcome to May, LuneOS fans! It’s been over 2 months since our last stable release, but don’t worry: We have been working extremely hard in bringing a lot of updates…'
featured_image: /images/files/2016/05/LuneOS_Mocha.jpg
source_url: https://pivotce.com/2016/05/13/luneos-may-stable-release-cafe-mocha/
wordpress_id: 3611
featured_image_source: https://pivotce.com/files/2016/05/LuneOS_Mocha.jpg
archived: true
---

Welcome to May, LuneOS fans! It’s been over 2 months since our last stable release, but don’t worry: We have been working extremely hard in bringing a lot of updates to the underlying system.

These kinds of upgrades on the lower level of our OS have significant impact and usually lead to some [regressions](https://en.wikipedia.org/wiki/Software_regression) as well. This was one of the reasons why we didn’t have a release last month and the release this month is a bit later than usual. We wanted to iron out some critical bugs first.

Check out what we’ve been up to and get to the builds!

We have moved from Yocto 1.8 (Fido), through Yocto 2.0 (Jethro) to [Yocto 2.1 (Krogoth)](https://www.yoctoproject.org/docs/2.1/mega-manual/mega-manual.html) which was released a little under 2 weeks ago. Making this move means that we don’t need to maintain and test multiple versions of Yocto and we also don’t need to worry about upgrading for at least another 6 months until Yocto 2.2 is released.

This way we can focus on bringing more functionality to LuneOS in the coming months as well as fixing a number of outstanding bugs.

We have also upgraded from QT 5.5.1 to [QT 5.6](https://www.qt.io/qt5-6/) which includes a newer QtWebEngine which is based on Chromium 45. QT 5.6 is the first LTS (Long Term Support) version of QT since 4.8, so it’s the first LTS version based on QT 5. LTS means that it will receive 3 years of updates & maintenance releases, which is good for support & stability in the long term. The upgrade to QT 5.6 means that we were able to finally solve the bug that would cause devices to lock up after a while, since QT rewrote it’s buggy [DBUS](https://en.wikipedia.org/wiki/DBUS) handling 🙂

We mainly focused on getting the underlying system bits updated, so not too much new functionality has been added, but we were able to get some of the old bugs fixed and got stability improved significantly. We’re sure there will be a few new bugs as well, but we’ll solve those along the way.

We have also reworked the update mechanism a bit and expect it to be fully functional and implemented in the near future.

Support has been added to the virtual keyboard for word prediction & spell correction using Presage & Hunspell. We have included dictionaries for various languages as well. This is still work in progress and needs some polishing, but it works pretty well already. It can be enabled in Settings under “Language & Input”.

We have also been able to create our first [nightly images for the Raspberry Pi 2](http://build.webos-ports.org/luneos-testing/images/raspberrypi2/). They are not included in this release yet, but you can test the nightly images already. We expect to include them in our monthly release cycle from the next release.

**Main Changes:**

– Upgraded all low level OS components from Yocto 1.8 (Fido) to Yocto 2.1 (Krogoth).
– Upgraded to QT 5.6 LTS including Chromium 45 based QtWebEngine and support for Pepper Flash Plugin (plugin not included in our distribution due to copyright restrictions), but can be sideloaded.
– Nightly images for Raspberry Pi 2 are being built now.
– Initial support for spell checking & predictive text for the Virtual Keyboard (disabled by default, but can be enabled via Settings app under “Language & Input”.

**Known issues:**

– Splash screen disappears too quickly (though it has improved a lot since we fixed some high CPU usage problems).
– Ringtone & Audio Routing: Audio routing for calls needs fine tuning and there is no ringtone playback yet.
– Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now. We’re sanitizing our components that use [NodeJS](https://nodejs.org), so we’re better prepared going forward and will have an easier upgrade path to newer NodeJS versions. Most components are currently still on NodeJS 0.12.x and we’d like to move to 4.4.x and 6.x later on.

### **Changelog**

**Applications:**-Settings: Update to work with the new update service.
-FingerTerm: Worked together with people from Mer to have customizations for LuneOS build in. It now uses Prelude as font 🙂
-Calendar: Switch back to Enyo 1 app since it seems to be working fine now and Enyo 2 app was still missing a lot of functionality. Also the fact that there’s little known about Enyo past their 2.7 release made us decide to no longer actively develop the Enyo 2 Calendar App for now.

**System Level:**

-luna-sysmgr: Add .conf files for Raspberry Pi 2/3
-nyx-modules: Added config for Raspberry Pi 2/3
-qt5-qpa-hwcomposer-plugin: Updated to most recent upstream version
-jenkins-jobs: Add supports for Raspberry Pi 2/3
-android-property-service: Fix crash in getAllProperties method
-webos-keyboard: Make sure settings are saved when they are changed in the virtual keyboard.
-luna-webappmanager: Various fixes for bluetooth & wifi.
-luna-next-cardshell: Fix behavior of App Menu and it’s opening by gesture.
-pmcertificatemgr: Big rework & cleanup of Open webOS code (not yet in nightlies due to other components that need updating).
-qtwayland: Added a fix to make it work with Qt 5.6
-mediaindexer: Populate com.palm.media.audio.album, com.palm.media.audio.genre, com.palm.media.audio.artist & fix com.palm.media.audio.file. When you sideload the legacy Music Player app, it will work as expected now.
-qtwebengine: Update to 5.6.0.
-qtwebengine-chromium: Update to Chromium 45-based for Qt 5.6.0.
-meta-rpi-luneos: Added layer for Raspberry Pi 2/3 to our repo.
-meta-raspberrypi: Added layer for Raspberry Pi 2/3 to our repo.
-wayland: Update to 1.9 from Yocto 2.1 in order to solve Qt 5.6.0 crashes.
-hunspell-dictionaries: Added dictionaries for various languages, to use with spellchecking & predictive text (Needs to be enabled in Settings and it’s still work in progress).
-hunspell: Update to 1.3.4.
-presage: Update to 0.9.1.
-maliit: Update to more recent upstream.
-bluez4: Add dbus policy so that Bluetooth headset can connect and route audio.
-systemd: Disabled fdinfo stat to bypass Mako bootloop.
-pulseaudio-modules-droid: Make it work with PulseAudio 8
-mmsd: Update mssd.service with correct location
-pidgin: Update to 2.10.12
-qtwebengine: Update configuration so audio works correctly with QT 5.6
-keymanager: Disable node-sqlite3 database for now pending rework of various NodeJS bits.
-C+DAV: Update for compatibility with NodeJS 4.4.x
-Keymanager: Update for compatibility with NodeJS 4.4.x
-connman: Use recipe from openembedded core directly.
-qtwebengine: Fix crash on html5test.com and apps using HTML5 databases on ARM devices.
-org.webosports.update: Initial work for new update mechanism.
-org.webosports.service.downloadmgr: Initial work for downloadmanager that can be used by Update service & Browser.
-VirtualBox: Initial work to get audio working

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/mocha/images/) to get started. Tenderloin and Mako remain our focus for now, but the emulator, Maguro & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion](http://forums.webosnation.com/luneos/331186-pivotce-luneos-may-stable-release-cafe-mocha.html) on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
