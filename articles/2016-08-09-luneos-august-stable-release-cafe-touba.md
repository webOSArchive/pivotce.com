---
title: 'LuneOS August Stable Release: Café Touba'
date: 2016-08-09 19:27:14 UTC
modified: 2016-09-18 01:48:42 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [august, calls]
slug: luneos-august-stable-release-cafe-touba
source_url: https://pivotce.com/2016/08/09/luneos-august-stable-release-cafe-touba/
wordpress_id: 3785
featured_image: ../images/files/2016/07/Caf_-Touba.jpg
featured_image_source: https://pivotce.com/files/2016/07/Café-Touba.jpg
excerpt: Those were a quick 2 months! As you know during summer things always slow down a bit due to people taking holidays. Some of our devs had some well deserved…
---

# LuneOS August Stable Release: Café Touba

Those were a quick 2 months! As you know during summer things always slow down a bit due to people taking holidays. Some of our devs had some well deserved time off as well, but others kept working hard on bringing bug fixes, improvements & new features to the OS! We’re very pleased to present you our latest monthly stable release, Café Touba or “Touba” for short.

We were able to crush quite a few annoying bugs that occurred in the lower system level that were leftovers of the Yocto migrations we did earlier. It turned out some of our NodeJS components were using deprecated functions that weren’t available anymore in our NodeJS 4.4.x version. These have now all been addressed and as a result stability is back where it used to be. Contacts can sync properly again for example.

We have also implemented a lot of the back end bits to make instant messaging (IM) work again (including Skype). You can now add IM accounts successfully using the accounts app and *receive* messages. Sending still has some issues which need to be sorted and are on our radar to be done for the next release. There is also more work to be done in the back end to deal with deletion of messages, group chats, and new contact requests, etc.

We have also done some major rework on banner handling, notifications and dashboards, and their icons and sounds. The behavior should now be very similar to legacy webOS.

Incoming phone calls will now play a ringtone and the call audio by default isn’t on speakerphone anymore.

The browser should now take up a bit more screen real estate when in full screen mode. We’re working on a full and proper full screen mode for a next release. We have also addressed some of the scaling issues on various websites and are now using Prelude at places where it wasn’t working properly before on both websites and apps.

We’ve also gotten MTP working properly, so you can connect your device to your PC and simply copy & paste files to and from your device. The UI for this still needs a little polishing, but the functionality is working well. We’ve tested Windows & Linux systems on various devices and it works.

We have also fixed a lot of the PNG images which had an incorrect sRGB profile which previous caused spamming in the logs.

**Main Changes:**

– Incoming calls will now have proper audio routing & a ringtone playing.
– Issues with various NodeJS services have been solved, so things like Contact sync will work again.
– MTP can now be used to cut, copy & past files when connected to a PC/Laptop.
– The Browser app now can use full screen more properly, Prelude is used in more places and the scaling issues on some websites has been resolved.
– A lot of work has been done on the IM (instant messaging) backend. Adding an account and receiving messages now works.

**Known issues:**

– Splash screen disappears too quickly (though it has improved a lot since we fixed some high CPU usage problems).
– Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.

### **Changelog**

**Applications:**
– Calculator (org.webosports.app.calculator): Fixed PNG images with incorrect sRGB profile.
– Maps (org.webosports.app.maps): Fixed PNG images with incorrect sRGB profile.
– Browser (org.webosports.app.browser): Fixed PNG images with incorrect sRGB profile, make fullscreen mode behave more properly.
– luna-applauncher (Just Type): Fixed PNG images with incorrect sRGB profile.
– luna-systemui (Just Type): Fixed PNG images with incorrect sRGB profile.
– Preware: Nudge users to enter https feeds instead of http, fixed PNG images with incorrect sRGB profile.
– Tweaks: Fixed PNG images with incorrect sRGB profile.
– core-apps: Fixed PNG images with incorrect sRGB profile.
– Settings: Fixed PNG images with incorrect sRGB profile.
– Flashlight (org.webosports.app.flashlight): Initial work on an app to play with the leds (not included in images yet).
– Testr (org.webosports.app.testr): Added additional banner sound & vibration scenarios.
– luna-universalsearchmgr: Fix build with libxml-2.9.4
– Messaging: When launched handle an URL, parse and use URL, add missind db kinds & permissions for com.palm.app.messagingprefs, com.palm.carrierdb.settings.current, fixed permissions for com.palm.chatthread and com.palm.message, fixed PNG images with incorrect sRGB profile.
– Contacts (org.webosports.app.contacts): Tapping an IM addr in details sends the IM type, URL and Note editing fields have correct width, Fixed PNG images with incorrect sRGB profile.
– Phone: Add ringtone management for incoming calls.
– Fingerterm: Use monospace as font to fix cursor issues.
– Browser: Make fullscreen mode work more properly (hide space normally used by navigationbar).

**User Interface:**
– Luna-Next-Cardshell: Fix behavior of rotationLock & muteSound, add management for popup overlay type, update Keys.forwardTo on cardRemove, fixed playback of banner sounds, renamed ringtone.wav references to ringtone.mp3, scan assets folder for sounds (used by Enyo 2 apps), launcher doesn’t take action on tap gesture, fixed PNG images with incorrect sRGB profile, handle icons, sounds & vibration for banners, dashboards and notifications properly.
– qtwayland: qwaylandwindow: fix inputDevice for setPopup.
**System Level:**
– imlibpurpleservice: Fixed db kinds & permissions for imbuddystatus, added permissions for both org.webosports.* and com.palm.*, fixed various JSON syntax errors, moved LS2 role file to correct location, made getServiceNameFromCapabilityId generic and removed conversion to and from Mojo-typed usernames.
– imaccountvalidator: Fix a lot of small things to make things work.
– audio-service: Fixed type to make sure audio routing works correctly in phone app
– messaging-accounts: Updated & fixed IM templates so they work properly.
– luna-webappmanager: Move handling of icon paths to luna-next-cardshell.
– Enyo-1.0: Fixed PNG images with incorrect sRGB profile.
– webos-keyboard: Fixed PNG images with incorrect sRGB profile.
– luna-next: Add FileUtils plugin to allow checking for file existence in QML, CompositorWindow: add isPopup property to test the Qt window type, Compositor: set the WindowType to Overlay for a popup window, add support for various bits required for proper sound playback through Luna-Next-Cardshell.
– app-services: Drop use of existsSync since it’s deprecated in NodeJS 1.x +, add directory to solve error for contact_linker_plugins.
– luna-sysmgr-common: Cleanup of whitespace mess.
– luna-sysmgr: Fixed PNG images with incorrect sRGB profile.
– nyx-modules: Implement MassStorageMode module
– mtp-server: Adjust systemd service configuration for com.palm.storage, stop service when session is closed. Update to newer mtp-server from Ubuntu upstream to make it work with Windows clients and fix a large number of bugs.
– storaged: Make it work with nyx, added Android udev rules, replaced cjson with json-c, added systemd service configuration & intergrated it into image.
– pidgin-sipe: Add SIPE IM plugin for IM
– whatsapp-purple: Add WhatsApp plugin for IM
– purple-skypeweb: Add SkypeWeb plugin for IM
– pidgin: Fix issues with ICQ password > 8 chars, drop discontinued MSN support & include Yahoo plugin.
– binutils: Fix issue with IPKG’s containing empty items.
– qtwebengine-chromium: Various upstream fixes, made Prelude the default font instead of monospace.
– Preware 2: Use secure (https) feeds where available.
– org.webosports.service.devmode: Fixed deprecated fs.existsSync calls that aren’t compatible with NodeJS 4.x
– mojoservicelauncher: Fixed deprecated fs.existsSync calls that aren’t compatible with NodeJS 4.x
– mojoloader: Fixed deprecated fs.existsSync calls that aren’t compatible with NodeJS 4.x
– org.webosports.service.downloadmgr: Fixed deprecated fs.exists and fs.existsSync calls that aren’t compatible with NodeJS 4.x
– keymanager: Fixed deprecated fs.exists calls that aren’t compatible with NodeJS 4.x
– activitymanager: ConnectionManagerProxy: merge the “wire” activity status into “wifi”.
– imlibpurpleservice: Made getServiceNameFromCapabilityId generic and removed conversion to and from Mojo-typed usernames.
– webos-connman-adapter: Drop patches that are not needed anymore from repo. Improved the management of wired interfaces.
– qtwebengine-chromium: Update to latest Chromium 45 from upstream.
– qtwebengine: Update to latest from QT 5.6 (August 5, 2016)

### Public Service Announcement:

As you might have noticed, [our website](http://www.webos-ports.org) was [down for a little while](https://pivotce.com/2016/07/25/webos-internalsports-sites-offline/). We were able to get the website back up and are working hard to bring all functionality back to normal. So if something looks out of place, you can always use the copy available at the [Internet Archive’s WayBack Machine](https://web.archive.org/web/20160418183325/http://www.webos-ports.org/wiki/Main_Page) and then be sure to let us know.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/touba/images/) to get started. Tenderloin and Mako remain our focus for now, but the emulator, Maguro & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion](http://forums.webosnation.com/luneos/331330-pivotce-luneos-august-stable-release-cafe-touba.html) on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
