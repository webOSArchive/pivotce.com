---
title: 'LuneOS June Stable Release: Café Cubano'
date: 2015-06-06 13:22:43 UTC
modified: 2015-10-21 18:15:48 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [cubano]
slug: luneos-june-stable-release-cafe-cubano
source_url: https://pivotce.com/2015/06/06/luneos-june-stable-release-cafe-cubano/
wordpress_id: 3007
featured_image: ../images/files/2015/06/cubano.jpg
featured_image_source: https://pivotce.com/files/2015/06/cubano.jpg
excerpt: We’re very pleased to present you our latest monthly stable release, Café Cubano or “Cubano” in short. The key highlights for this month are the virtual keyboard & bug fixes!…
---

# LuneOS June Stable Release: Café Cubano

We’re very pleased to present you our latest monthly stable release, Café Cubano or “Cubano” in short.

The key highlights for this month are the virtual keyboard & bug fixes! We’ve been focusing heavily on the virtual keyboard after last month’s orientation support implementation.

The old keyboard had been bugging us and our users for quite some time already, so we decided to get started. We have taken webOS 3.0.5, LunaCE and Open webOS virtual keyboards as inspiration.

For tablet layouts we have now done the following:

- Added an additional row with numbers.
- Added a trackball like in LunaCE.
- Added support for multiple keyboard sizes (XS, S, M and L).
- Added alternate keys while long pressing a key (indicated by …) so you can get é ë è etc while holding e.
- A large number of UI tweaks to make it look very similar to the legacy webOS 3.0.x virtual keyboard.

For phone layouts we have done the following:

- Created a complete new layout inspired by the virtual keyboards as it was included in Open webOS and featured on [webOSNation.](http://www.webosnation.com/checking-out-galaxy-nexus-open-webos-port-virtual-keyboard-video)

This is currently only available for the English keyboard layout. We will work on the layouts for the other languages in the near future, as well as further fine tuning of the various keyboard layouts and features!

We also have been reworking the update mechanism to allow updating nightly releases.

Grab your Nexus 4, HP TouchPad, Nexus 7 (2012 WiFi) or emulator and load up our latest builds!

### Changelog

- webos-keyboard: Large rework to have separate layouts for phones & tablets.
- webos-keyboard: Brought back different keyboard sizes, number row and trackball for tablets.
- webos-keyboard: Removed all Ubuntu references and cleaned up unneeded files.
- webos-keyboard: Created Qt Creator test framework to be able to more easily develop on desktop.
- webos-keyboard: Made keyboard items more flexible by using Units.gu instead of pixel values.
- Settings: Add search preferences.
- luna-next: Fix screen recorder state
- Messaging: Possibility to delete individual messages via context menu.
- Testr: Add dashboard tests.
- qtwayland: Disable mouse grabber as it prevents compositor items from getting press event notifications.
- FirstUse: Fixed font display bug on emulator.
- Luna-Next-Cardshell: CardView: improved CardWindowWrapper initiation.
- Update: Allow system updates in testing tree.

### Current work in progress for next releases:

- Further sensor support (ambient light sensor etc)
- Implement LED-support so it’s visible to user.
- Further improvements/options for tabbed launcher
- Telephony support
- SMS & IM improvements & support
- Fix data connection on TP4G
- Support for custom APN’s for oFono
- Bluetooth support
- Further keyboard enhancements for different layouts & languages

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

Feel free to [download the updated builds](http://build.webos-ports.org/releases/cubano/images/) to get started. Tenderloin and Mako remain our focus for now and the emulator & Grouper work too.

Installation instructions for [TouchPad (Tenderloin)](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to join the discussion on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
