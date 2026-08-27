---
title: LuneOS Update for April
date: '2016-04-07T16:21:34Z'
lastmod: '2016-05-13T15:37:08Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- Developer
slug: luneos-update-for-april
summary: In the latter part of March, webOS Ports upgraded two major parts of the LuneOS system. The Yocto project is what we use to deploy an embedded Linux system to…
featured_image: /images/files/2016/04/Improvements.jpg
source_url: https://pivotce.com/2016/04/07/luneos-update-for-april/
wordpress_id: 3558
featured_image_source: https://pivotce.com/files/2016/04/Improvements.jpg
archived: true
---

In the latter part of March, webOS Ports upgraded two major parts of the LuneOS system. The [Yocto project](https://www.yoctoproject.org/about) is what we use to deploy an embedded Linux system to our target devices. Last month we moved to the latest version, named Jethro. In addition, the [Qt framework](http://www.qt.io/) we use for our GUI and system apps has just reached version 5.6 and we have upgraded our builds accordingly. The price of keeping LuneOS at the cutting edge is that major upgrades like these can break other parts of the system that rely on them. Fixing these glitches means it is difficult to produce a stable build of LuneOS, so in April we will focus on progressing the transition rather than making a stable build. We have been able to make great progress with regards to stability, however we still have a few important issues to iron out as well.

BUT we do have nightlies still coming. The latest of which are available for [Grouper](http://build.webos-ports.org/luneos-testing/images/grouper/luneos-dev-package-grouper.zip) (Nexus 7), [Maguro](http://build.webos-ports.org/luneos-testing/images/maguro/luneos-dev-package-maguro.zip) (Galaxy Nexus), [Mako](http://build.webos-ports.org/luneos-testing/images/mako/luneos-dev-package-mako.zip) (Nexus 4), [emulator](http://build.webos-ports.org/luneos-testing/images/qemux86/luneos-dev-emulator-qemux86.zip), and [Tenderloin](http://build.webos-ports.org/luneos-testing/images/tenderloin/luneos-dev-image-tenderloin.tar.gz) (HP TouchPad). Don’t forget the [latest uImage](http://build.webos-ports.org/luneos-testing/images/tenderloin/uImage) for TouchPad. We now also build nightly images for the [Raspberry Pi 2](http://build.webos-ports.org/luneos-testing/images/raspberrypi2/luneos-dev-image-raspberrypi2.rpi-sdimg). We’re ironing out a few final issues with the Raspberry Pi 3 build, so those images can be built in our build environment as well.

So what’s new? First off, we have a new supported device: Raspberry Pi 2! This was pending for a while, but we finally solved the obstacles on our build environment and images are now generated as part of our nightly build process. Also, the Raspberry Pi 3 port build is working on local machines, however we need to iron out a few issues before we can have builds on our server as well. More to come there.

**Changes:**

– Upgraded from QT 5.5.1 to QT 5.6.0, which solved a long outstanding issue of the device locking up after a while due to DBUS getting flooded.
– For this month we have mainly been focusing on upgrading fundamentals of our OS. We have upgraded our Yocto release from Fido to Jethro (Yocto 2.0) which brings a great deal of improvements of various bits of the underlying software for LuneOS.
– We can now do word prediction for the virtual keyboard (to be enabled in Settings).
– You can also connect a Bluetooth headset and listen to music (as soon as we get audio working again as per below known issue ;))
– Media Indexer is now populating more database kinds (Artist, Album, Genre), so when you sideload the legacy Music Player app, it will show information for Artist, Album & Genre.

**Known issues:**

– Email list doesn’t display in email app.
– Audio doesn’t seem to work in the browser/apps.
– Browser occasionally crashes (on [http://www.htmltest.com](http://www.html5test.com) for example).

**Device Specific Fixes:**

Raspberry Pi 2:
– Now available as nightly images 🙂

Applications:
– PDF: Initial work for migration to pdf.js’s internal viewer (not in nightlies yet).
– Settings: Rework of virtual keyboard settings handling, so it keeps working when updated in Settings app.
– Settings: Add further work for IEEE802.1x support.
– Settings: Cleanup Bluetooth code.
– Settings: Show WiFi MAC address in About.

System level:
– luna-sysmgr: Add .conf files for Raspberry Pi 2/3
– nyx-modules: Added config for Raspberry Pi 2/3
– qt5-qpa-hwcomposer-plugin: Updated to most recent upstream version
– jenkins-jobs: Add supports for Raspberry Pi 2/3
– android-property-service: Fix crash in getAllProperties method
– webos-keyboard: Make sure settings are saved when they are changed in the virtual keyboard.
– luna-webappmanager: Various fixes for bluetooth & wifi.
– luna-next-cardshell: Fix behavior of App Menu and it’s opening by gesture.
– pmcertificatemgr: Big rework & cleanup of Open webOS code (not yet in nightlies due to other components that need updating).
– qtwayland: Add a fix to make it work with Qt 5.6
– mediaindexer: Populate com.palm.media.audio.album, com.palm.media.audio.genre, com.palm.media.audio.artist & fix com.palm.media.audio.file.
– qtwebengine: Update to 5.6.0.
– qtwebengine-chromium: Update to Chromium 45-based for Qt 5.6.0.
– meta-rpi-luneos: Added layer for Raspberry Pi 2/3 to our repo.
– meta-raspberrypi: Added layer for Raspberry Pi 2/3 to our repo.
– wayland: Update to 1.9 from Yocto 2.1 in order to solve Qt 5.6.0 crashes.
– hunspell-dictionaries: Added dictionaries for various languages, to use with spellchecking & predictive text (Needs to be enabled in Settings and it’s still work in progress).
– hunspell: Update to 1.3.4.
– presage: Update to 0.9.1.
– maliit: Update to more recent upstream version.
– bluez4: Add dbus policy so that Bluetooth headset can connect and route audio.

Phew! That was a lot of work. As you can see, we’ve been very busy. Implement a lot of changes and closed a lot of bugs!

Help us test and [report your findings](http://issues.webos-ports.org/projects/ports/issues?set_filter=1), please! We’re always looking for energetic volunteers to [join the team](/2014/09/22/webos-ports-help-wanted/). See you next month.
