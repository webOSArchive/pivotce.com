---
title: 'LuneOS December Stable Release: Caffè Marocchino'
date: '2015-12-10T17:14:03Z'
lastmod: '2016-02-05T20:30:33Z'
author: webosports
author_slug: webosports
categories:
- News
slug: luneos-december-stable-release-caffe-marocchino
summary: We’re very pleased to present you our latest monthly stable release, Caffè Marocchino or “Marocchino” for short. We’ve had a bit of delay in getting this release out due to…
featured_image: /images/files/2015/12/IMG_1753.jpg
source_url: https://pivotce.com/2015/12/10/luneos-december-stable-release-caffe-marocchino/
wordpress_id: 3358
featured_image_source: https://pivotce.com/files/2015/12/IMG_1753.jpg
archived: true
---

We’re very pleased to present you our latest monthly stable release, Caffè Marocchino or “Marocchino” for short. We’ve had a bit of delay in getting this release out due to some issues with our build server and issue tracker but those are now resolved. Yay!

We didn’t have a November stable release of LuneOS. We were still in the middle of the migration from QtWebKit to QtWebEngine for the rendering of Enyo 1 and Enyo 2 apps. There were a few critical bugs that we wanted to iron out first before pushing out a new release to the community.

The below information *includes* the changes from our November update because they’re all changes from the last **stable.**

The Galaxy Nexus is back. And the RaspBerry Pi 2 port will still most likely be an official target soon. We still need to work out logistics on our build server and a few other things first.

**Changes:**

– Updated from QT 5.5.0 to QT 5.5.1.
– Migrated rendering of Enyo 1/2 apps from QtWebKit to QtWebEngine. Seems to work quite well, but we’re happy to get any feedback of things not working as expected.
– QtLocation plugin support so we can use HTML 5 Geolocation in apps and browser.

**Known issues:**

– Splash screen disappears too quickly
– Audio doesn’t seem to work in the browser
– Device lockups: These seem to be due to some bugs in QT’s DBUS implementation which will be addressed in QT 5.6

**Device Specific Fixes:**

**Nexus 4:**
– Fixed not working PulseAudio after upgrade to PulseAudio 6

**Galaxy Nexus GSM:**
– Brought back support for Samsung Galaxy Nexus. In theory you CAN install LuneOS to your CDMA Galaxy Nexus but cell radio will likely not work and it might break your device. If you try and you brick it, don’t say you weren’t warned.

**Applications:**
– Testr: Added tests for responsive images
– Browser: Migrated BrowserUtils to QtWebEngine as well.
– FirstUse: Added support for enabling 3rd party Preware (LuneOS App Catalog) feeds to FirstUse.
– FirstUse: Switch to use luneos-components and use QtWebEngine instead of QtWebKit.
– Phone: Migrated to use luneos-components
– Tweaks: Fixed broken banner notifications
– Calculator: New rotatable layout, that makes full use of QtWebEngine features.
– Luna-next-cardshell: Made time display in correct format (12/24 hrs), added optional system menu items for devices without hardware power/volume buttons (RaspBerry Pi 2)
– Luna-next-cardshell: Hide notifications when pressing the gesture area.
– Luna-next-cardshell: Work on Bluetooth submenu of System Menu
– Clock: Fix sloppy bugs in code that caused problems with alarms.
– Accounts: Fix references to files that are not available.
– Contacts: Fix processLaunchParam for Enyo 2.5.1 and webOSjs 1.0.0

**System level:**
– luna-webappmanager: Migrated Enyo 1/2 apps to QtWebEngine. Still quite fresh, so looking for feedback on things that don’t work.
– luna-appmanager: Improved handling of a crash in luna-webappmanager so that Power menu and other apps will keep working.
– luna-init: Added a default keyboard size.
– luneos-components: Fix fonts on desktop.
– luneos-components: Add stub component for BT dbus module.
– luna-qml-launcher: Tweaked behavior for QML apps using QtWebEngine.
– webos-keyboard: Fixed erratic/non working extended keys on … keys.
– downloadmanager: Initial work on a download manager for browser and other system bits.
– luna-service2: Switched from QtWebProcess to QtWebEngineProcess
– luna-sysservice: Fixed error messages due to JSON versions.
– luna-sysmgr: Standardization of available fields in device specific .conf file.
– luna-sysmgr: Made sure to remove com.palm.app apps and replace them with org.webosports.app equivalents where available.
– qtwebengine-chromium: Migration webOS/LuneOS specifics from QtWebKit to qtwebengine-chromium
– qtwebengine: Migration webOS/LuneOS specifics from QtWebKit to qtwebengine-chromium
– luna-next: Fixed non-working back gesture in Enyo 1 apps.
– luna-next: Fixed Units and Settings singletons.
– webos-systemd-services: Correct the ls-hubd_public.service description
– webos-telephonyd: Spelling fixes
– luna-qml-launcher: Add qtpositioning plugin

We’re still working very hard on LuneOS. We implemented a lot of low level changes so the back-end of the system is now running with the latest technologies available and we solved a lot of bugs at the same time as well!

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/marocchino/images/) to get started. Tenderloin and Mako remain our focus for now and the emulator & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin)[Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion](http://forums.webosnation.com/luneos/330875-pivotce-luneos-december-stable-release-caffe-marocchino.html) on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
