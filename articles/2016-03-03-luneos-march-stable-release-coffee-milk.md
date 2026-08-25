---
title: 'LuneOS March Stable Release: Coffee Milk'
date: 2016-03-03 20:21:32 UTC
modified: 2016-04-07 16:25:35 UTC
author: webosports
author_slug: webosports
categories: [News]
slug: luneos-march-stable-release-coffee-milk
source_url: https://pivotce.com/2016/03/03/luneos-march-stable-release-coffee-milk/
wordpress_id: 3510
featured_image: ../images/files/2016/02/Coffee_Milk.jpg
featured_image_source: https://pivotce.com/files/2016/02/Coffee_Milk.jpg
excerpt: Hello and welcome to March, LuneOS fans! WOW has time gone quickly since our last update. But never fear, your beloved WebOS Ports team is still hard at work. Only…
---

# LuneOS March Stable Release: Coffee Milk

Hello and welcome to March, LuneOS fans! WOW has time gone quickly since our last update. But never fear, your beloved WebOS Ports team is still hard at work. Only 3 short weeks, but still lots of news! We’re adding skilled members, working on stability/features/bugs, and generally aligning all of the 1s and 0s to make LuneOS better everyday.

Check out what we’ve been up to and get to the builds!

We have been working hard on polishing the phone app. Integration with Contacts is there. As well as up to date geocoding using Google’s i18n libphonenumber source data. This will tell you the location of the caller’s phone number in case it’s not a contact.

You can now also connect to hidden wifi networks (this was a feature request that was outstanding for a long time and has finally been implemented).

We also focused on getting some of the old bugs fixed, making sure stability improved.

Qt has released the release candidate of Qt 5.6 last week and we are planning to move to this after we finish pushing out this release. Also our sibling project Sailfish OS has put out a new release for the Nexus 4 based on CM11. This will also allow us to move to a CM11 based build as well hopefully.

Since you have been asking about the Raspiberry Pi 2 port: We have also been able to solve the obstacles we had to set it up in our build environment, so you can expect nightlies to be available shortly! A Raspberry Pi 3 port will be attempted too as soon as the dev receives his!

**Main Changes:**

– Phone App polished to have contact integration, geolocation support, basic USSD, keypad vibration (enabled via Tweaks).
– Location Services updated to latest GeoClue 2 release and using Google Location Services instead of Mozilla (still wifi only).
– Various minor UI improvements in Luna-Next-Cardshell.
– Settings can now connect to hidden wifi networks.

**Known issues:**

– Splash screen disappears too quickly (though it has improved a lot since we fixed some high CPU usage problems).
– Device lockups: These seem to be due to some bugs in QT’s DBUS implementation which will be addressed in QT 5.6.
– Ringtone & Audio Routing: Audio routing for calls needs fine tuning and there is no ringtone playback yet.
– We broke the AppMenu for apps, but will get that sorted in the next nightly.

### **Changelog**

**Applications:**– Phone: Rework of call history page & add geocoding support, Added Tweak for dialpad vibration feedback, Use valid phone numbers as fake test data, Improve incoming & active call pages, Add basic USSD support.
– Settings: Bluetooth improvements for debugging, WiFi code cleanup & support for connecting to hidden networks.
– Photos: Add Apache 2.0 license.
– Testr: Add Apache 2.0 license.
– Browser: Moved Tweaks Support to LuneOS Components & add serviceName in the calls to Tweaks.

**System Level:**
– luna-init: Change wallpaper location to /media/internal/
– luna-webappmanager: Don’t stop unit if luna-next exits on its own.
– luna-appmanager: Disable call to create FAKEFS since we don’t have the JSON file for it anyway.
– luna-systemui: Disabled appInstallStatus for now untill we have a working Download Manager, Disable call to com.palm.storage since it’s not available.
– luna-sysmgr-common: Disable RadioType check, Return carrierAvailable as true instead of relying on m_radioType.
– luna-sysgr: Disabled call to postNovacomStatus, Enabled ALS for various targets.
– loadable-frameworks: Add support for geocoding.
– luneos-components: Add Tweaks.qml & stub values for Tweaks, Add Geocoding support (location lookup based on phone number), Stub compositor: fixed warning.
– luna-next-cardshell: Add mask for lockscreen background, Moved Tweaks Support to LuneOS Components, Add mipmap for images to improve quality, Fixed App Menu display conditions, Add PadLock at proper position & device type dependant, Added lockscreen gradient, Provide visual feedback on screenshot (right swipe), Centralized Tweaks declaration in AppTweaks singleton, WindowManager: Introduce DockMode & LockScreen mode, Sanitized z-indexes & made visual feedback for screenshots working.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/milk/images/) to get started. Tenderloin and Mako remain our focus for now, but the emulator, Maguro & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin)[Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion](http://forums.webosnation.com/luneos/331082-pivotce-luneos-march-stable-release-coffee-milk.html) on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
