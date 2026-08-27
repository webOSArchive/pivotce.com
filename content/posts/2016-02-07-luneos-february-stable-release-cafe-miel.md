---
title: 'LuneOS February Stable Release: Café Miel'
date: '2016-02-07T15:39:58Z'
lastmod: '2016-03-08T15:35:40Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- calls
slug: luneos-february-stable-release-cafe-miel
summary: We’re very pleased to present you our latest monthly stable release, Café Miel or “Miel” for short.
featured_image: /images/files/2016/02/Cafe_Miel.jpg
source_url: https://pivotce.com/2016/02/07/luneos-february-stable-release-cafe-miel/
wordpress_id: 3477
featured_image_source: https://pivotce.com/files/2016/02/Cafe_Miel.jpg
archived: true
---

We’re very pleased to present you our latest monthly stable release, Café Miel or “Miel” for short.

We have been working hard to bring the most sought after feature: phone calls! In order to do so we have upgraded our whole connection stack (ConnMan, oFono, VoiceCall, libconnman-qt, libqofono, phonesim) to the latest version available from these projects. We have done a lot of work on our phone app, both layout and functionality wise. As a result you can now make and receive calls with LuneOS!

This month was focused on getting some of the old bugs fixed, making sure stability improved and getting basic phone calls working. We have also been preparing for the move to Yocto Project 2.0 (Jethro) as well, but we still have a few regression issues to fix before we can migrate. We expect that this move will happen in the near future too. With Qt planning to release Qt 5.6 shortly we hope we’ll be finally able to kill the bug that locks up the devices. We have also been working on [improving the documentation for developers](http://webos-ports.org/wiki/Getting_Started), so it will be easier to get started for people who want to help out.

There’s a lot of ground to cover in future releases, but the basics are there. We’re still lacking a ringtone and proper audio routing, but that’s scheduled for the near future. In order to provide proper support we’ll need to extend our audio service to add the required support.

We have also been hooking up Bluetooth in the Settings app for initial Bluetooth support. We still need to  fine tune it a bit and integrate it further in our audio stack as well.

The PDF app has been updated to the latest PDF.js library and now has rotate and next/previous page buttons as well.

The Maps app has been updated so pinch-to-zoom and panning works correctly.

The Testr app now has test cases for vibration which lays some of the ground work for haptic feedback and notification vibration.

And more! Read on…

**Main Changes:**

– Phone App can now make & receive calls.
– PDF App updated to latest PDF.js, added rotate and next/previous page buttons.
– Maps app fixed so pinch-to-zoom works correctly.
– Media Indexer: Various fixes to be compatible with legacy.
– Added org.webosports.* at various parts of the OS as privileged.
– Added initial Bluetooth support & category icons.
– Virtual Keyboard: Added _ and dismiss button for phone vkb layouts.

**Known issues:**

– Splash screen disappears too quickly (though it has improved a lot since we fixed some high CPU usage problems).
– Device lockups: These seem to be due to some bugs in QT’s DBUS implementation which will be addressed in QT 5.6.
– Ringtone & Audio Routing: Audio routing for calls needs fine tuning and there is no ringtone playback yet.

**Applications:**

– PDF (org.webosports.app.pdf): Update PDF.js to v1.3.90, add sample files, fix syntax errors, added document rotation and previous/next page buttons.
– Messaging (org.webosports.app.messaging): Handle Just Type launch params (you can now create a new message from Just Type).
– Testr (org.webosports.app.testr): Add tests for vibration API.
– Maps (org.webosports.app.maps): Fix pinch to zoom & panning during pinch-to-zoom (fixes bugs 957 & 1043).
– Update (org.webosports.update): Add new update icon.
– FileManager (org.webosports.app.filemanager): Update to Enyo 2.5.1.1 and latest libs, display filesize in kb, mb, gb etc where needed. Fixed app name from bootplate to it’s proper name.
– Preware: (org.webosinternals.preware): Cleanup of old bits (opkg replaced by ipkg) and preware.org replaced with preware.net.
– Phone: (org.webosports.app.phone): Major code cleanup, layout tuning & making the app actually work. Added call history, contact lookup & favorites.
– Settings: (org.webosports.app.settings): Add category icons (fixes bug 1053), added initial Bluetooth support, use default FilePicker for sounds, add initial support for hidden networks.

**System level:**

– activitymanager: Allow 1 minute intervals to solve some issues in logs with db8, enable modem reading again.
– sleepd: Add alarms.xml file.
– luna-universalsearchmanager: Fix various memory leaks, make org.webosports.* also privileged like com.palm.* so they can have Just Type actions.
– luna-next-carshell: Fix removal of notification.
– luna-appmanager: Add org.webosports.* apps as trusted apps.
– luna-init: Add handlers for various filetypes, cleanup no longer used types and fix syntax errors.
– Media Indexer: Setup permissions for legacy apps, so when they’re sideloaded they can work. Fixed com.palm.media.audio.file:1 to be compatible with legacy (still missing thumbnail images). Fixed com.palm.media.video.file:1, com.palm.media.image.file:1 and com.palm.media.misc.file:1 to be compatible with legacy.
– luna-webappmanager: Add support for hidden wifi networks, added resetDeviceList function for Bluetooth.
– webos-keyboard: Add dismiss & underscore key to phone vkb.
– C+DAV (org.webosports.service.contacts.carddav): Add access to org.webosports.app.contacts as well just like com.palm.app.contacts.
– luna-sysmgr-common: Fix lifecycle of json string.
– luna-sysservice: Fix lifecycle of json string, make subscribe optional for getPreferences, use json-c instead of cjson.
– app-services: Proper access to org.webosports.app.contacts, fixed globalization issue.
– luna-systemui: Drop getMigrationStatus since it’s not part of Open webOS.
– LuneOS Components: Add ClippedImage component, Sync ApplicationWindow.WindowType with the ones from LunaNext, Db8Model: add more testing capabilities, fix LS2 registration, improve DB8 stub, use B2G libphonenumber.js.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/miel/images/) to get started. Tenderloin and Mako remain our focus for now, but the emulator, Maguro & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin)[Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion](http://forums.webosnation.com/luneos/331022-pivotce-luneos-february-stable-release-cafe-miel.html) on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
