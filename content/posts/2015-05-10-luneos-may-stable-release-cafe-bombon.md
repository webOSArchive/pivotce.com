---
title: 'LuneOS May Stable Release: Café Bombón'
date: '2015-05-10T07:03:05Z'
lastmod: '2015-06-07T04:01:22Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- bombon
slug: luneos-may-stable-release-cafe-bombon
summary: It’s been a short while since our April LuneOS stable build, “Café au lait”, but we’re very pleased to already present you our latest monthly stable release, Café Bombón or…
featured_image: /images/files/2015/05/bombonfeatured.jpg
source_url: https://pivotce.com/2015/05/10/luneos-may-stable-release-cafe-bombon/
wordpress_id: 2937
featured_image_source: https://pivotce.com/files/2015/05/bombonfeatured.jpg
archived: true
---

It’s been a short while since our April LuneOS stable build, “Café au lait”, but we’re very pleased to already present you our latest monthly stable release, Café Bombón or “Bombón” in short. As you can imagine our release notes are not very long, but we’ve still been able to make solid progress on a number of features which have been in the works for quite some time now and there is more to come in the next releases!

The key highlights for this month are rotation/orientation support in the UI, including rotation lock and the capability to send SMS messages directly to a number once entered (non-contacts). We were able to get the build for the Nexus 7 (2012 WiFi) version a.k.a. Grouper working again! There is one little caveat: It will only start to work from the 2nd boot!

More good news on the emulator front as well: We’ve found the cause for the serious performance issues, it should run a lot better now!

Grab your Nexus 4, HP TouchPad, Nexus 7 (2012 WiFi) or emulator and load up our latest builds!

### Changelog

- **Nexus 7 2012 WiFi (codename: grouper) is working again! Please make sure to boot it a 2nd time because it doesn’t work at first boot yet.**
- **Emulator: Fixed a bug that caused very high CPU usage.**
- **luna-sysservice: Reduced a large number of error messages in logs.**
- Preware: Minor UI tweaks to Settings, Feeds and application dialogs.
- Settings: Add support for PIN & Password screen lock.
  luna-sysmgr-common: Reduced a large number of error messages in logs.
- luna-sysmgr-common: Added initial support for LEDs.
- C+DAV: Updated to 0.3.29, fixing broken Google sync & various other minor fixes.
- Messaging: Various minor UI fixes.
- Messaging: Rework of chatthreader to allow sending messages to non-contacts.
- luna-next: Added initial support for LEDs.
- Testr: Added tests for HTML5 Geolocation API, Responsive images (using srcset, SVG and -webkit-image-set).
- **luna-next-cardshell: Added UI rotation support & rotation lock!**
- luna-next-cardshell: Added tabbed launcher, including the possibility to drag icons to other tabs. Various options for tab-settings available via Tweaks (including number of tabs, arrows etc). Made the layout look more like legacy webOS (mixture of 2.x and 3.x)
- luna-next-cardshell: Various UI tweaks, mainly related to the lockscreen and it’s size.
- webos-keyboard: Fixes to make it work correctly with UI rotation.
- Some rebranding from WebOS Ports to LuneOS in the sideload installer for Nexus 4 and Nexus 7.
- Reboot works again
- Corrected major performance issue with emulator. 140% CPU usage to 8%!

### Current work in progress for next releases:

- Further sensor support (ambient light sensor etc)
- Implement LED-support so it’s visible to user.
- Further improvements/options for Tabbed launcher
- Telephony support
- SMS & IM improvements & support
- Fix data connection on TP4G
- Support for custom APN’s for oFono
- Bluetooth support
- Keyboard enhancements for different layouts

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

Feel free to [download the updated builds](http://build.webos-ports.org/releases/bombon/images/) to get started. Tenderloin and Mako remain our focus for now and the emulator works too.

Installation instructions for [TouchPad (Tenderloin)](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to join the discussion on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month! We’re getting closer and closer to being able to use LuneOS as a daily driver.
