---
title: 'LuneOS January Stable Release: Caffè Medici'
date: 2016-01-14 18:38:14 UTC
modified: 2016-02-07 17:20:21 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [Caffè Medici, Developer]
slug: luneos-january-stable-release-caffe-medici
source_url: https://pivotce.com/2016/01/14/luneos-january-stable-release-caffe-medici/
wordpress_id: 3443
featured_image: ../images/files/2016/01/Medici.jpg
featured_image_source: https://pivotce.com/files/2016/01/Medici.jpg
excerpt: We’re very pleased to present you our latest monthly stable release, Caffè Medici or “Medici” for short. We’ve had a bit of delay in getting this release out due to…
---

# LuneOS January Stable Release: Caffè Medici

We’re very pleased to present you our latest monthly stable release, Caffè Medici or “Medici” for short. We’ve had a bit of delay in getting this release out due to the holiday period and some bugs we wanted to sort first.

We have been working a lot on some of the issues that have been outstanding for a while in order to improve the general stability of the system and prepare for future features & releases.

**Main Changes:**

– Fixed the use of a hardware keyboard in the VirtualBox emulator.
– Added support for screen rotation with F6, F7, F8, F9 keys in VirtualBox emulator.
– Reworked banner, notification & dashboards to be compatible with legacy API.
– Fixed 2 bugs causing high CPU load & battery drain.
– Fixed relaunch handling for apps.
– Audio is working again for the browser and also MP3 playback is working again.
– Tap ripple works now properly on all resolutions and can be enabled/disabled in Tweaks.

**Known issues:**

– Splash screen disappears too quickly (though it has improved a lot since we fixed some high CPU usage problems).
– Device lockups: These seem to be due to some bugs in QT’s DBUS implementation which will be addressed in QT 5.6

**Applications:**

– Enyo 1.0: Fix high CPU load problem after QtWebEngine migration
– Testr: Fix test cases for DashBoards
– Clock: Fixed various bits so now it will actually work
– Messaging: Add relaunch handling to open incoming message/thread
– Messaging: Make sure the new SMS notification is compatible with API changes
– Browser: Bring back ContextMenu.
– FirstUse: Initial support for IEEE 802.1x (Enterprise Wifi)
– Update: Make sure the new update notification is compatible with API changes

**System level:**

– Luna-Next-Cardshell: Fixed high CPU issue for performance of DockMode Clocks
– QtWebEngine: Enabled Alsa & PulseAudio & codecs
– luna-webappmanager: Implement missing bits for notifications (banners/dashboards) to be compatible with legacy API
– luna-webappmanager: Launch Just Type at startup to reduce time when calling it and improve CPU usage
– luna-next: Implement missing bits for notifications (banners/dashboards) to be compatible with legacy API
– luna-next: Make Tap Ripple/Reticle behave better on various devices.
– luna-next: Add additional keys to emulator F6-F9 to rotate screen on emulator.
– luna-next: Add screen edge flick detection (up and down only for now)
– luneos-components: Add stub for DeviceKeyHandler
– luneos-components: Add support for newly added parameters for notifications to the tests
– luneos-components: Add a stub for GestureHandler
– luna-sysmgr: Changed the GridUnit value for emulator to 10 instead of 8 pixels. This because Tenderloin (aka Touchpad) uses uses 10 and they share the same resolution.
– webos-connman-adapter: Moved to our own fork instead of using upstream Open webOS.
– webos-connman-adapter: Migrated patches to commits
– webos-connman-adapter: Added initial support for IEEE 802.1x (Enterprise WifI)

This month was focused on getting some of the old bugs fixed and also making sure stability improved. The rework for the notifications was necessary in order to pave the road for further work on Messaging & Phone app in the future. We have also been preparing for the move to Yocto Project 2.0 (Jethro). We expect that this move will happen in the near future too, but no fixed time line yet. This will bring new versions of ConnMan & oFono which we can use to improve our network stack & capabilities in LuneOS. With Qt planning to release Qt 5.6 shortly we hope we’ll be finally able to kill the bug that locks up the devices. We have also been working on [improving the documentation for developers](http://webos-ports.org/wiki/Getting_Started), so it will be easier to get started for people who want to help out.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/medici/images/) to get started. Tenderloin and Mako remain our focus for now and the emulator & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin)[Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion](http://forums.webosnation.com/luneos/330875-pivotce-luneos-december-stable-release-caffe-marocchino.html) on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
