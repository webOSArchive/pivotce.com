---
title: 'LuneOS February Stable Release: Chai Latte'
date: 2017-02-24 13:11:41 UTC
modified: 2017-05-09 17:16:50 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [Chai Latte, Developer]
slug: luneos-february-stable-release-chai-latte
source_url: https://pivotce.com/2017/02/24/luneos-february-stable-release-chai-latte/
wordpress_id: 4001
featured_image: ../images/files/2017/02/LuneOS_Chai_Latte2.jpg
featured_image_source: https://pivotce.com/files/2017/02/LuneOS_Chai_Latte2.jpg
excerpt: So that’s been a long while already! 2 months passed since the last release and we’re finally back with a new release called “Chai Latte”. We have been working very…
---

# LuneOS February Stable Release: Chai Latte

So that’s been a long while already! 2 months passed since the last release and we’re finally back with a new release called “Chai Latte”. We have been working very hard behind the scenes in the past 2 months upgrading our various builds & build infrastructure!

So you’re asking what we have done? We have been doing lots of work to make our build & porting process more stable and straightforward. It’s now easier to create a new port for devices having a CM 12.1 (Android 5.1) based build available. Also initial work has been done in order to be able to use CM 13.0 (Android 6.0) based builds.

We have updated our Galaxy Nexus (Maguro) and Nexus 4 (Mako) build to a CM 12.1 based build. For the Maguro this solved the garbled audio issue that was present on our previous CM 10.1 based builds.

**We also have a new target device running on CM 12.1 based build, the Nexus 5 (codename Hammerhead)!**

*We are fully aware that Cyanogen Inc stopped development of Cyanogen OS and also supporting the development of CyanogenMod by the community and all builds have been taken offline. At the time of writing the successor of CyanogenMod, LineageOS, is still in early stages of their setup and has just it’s initial builds, however this is not available for all target devices (yet). We’ll be re-assessing our source for builds at some point in the near future. The change to support LineageOS and/or AOSP directly should be fairly straight forward.*

Our RaspberryPi2 and RaspberryPi3 builds are currently building again and are included in the release this time. The UI is still not working for the RaspberryPi devices, but at least you should be able to get it to boot and connect via console.

Many other small items have been fixed as well, see below for more details of all the changes!

**Known issues:**

- Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.
- Focus bug on input fields. You can work around this by hiding the virtual keyboard and pressing the input again.

### **Changelog**

**Applications:**

- Messaging (org.webosports.messaging): Conversion to Enyo 2.7, package.json: Add missing icon.png, replaced Contact Picker with Address Picker, Renamed AddrModel to MsgAddrModel, Made Message Address Search list more compact (Mojo-style), return addr picker dynamically populated in threadview, fix back gesture, unified use of guillemets.
- Contacts (org.webosports.app.contacts): Fixed bug where first IM address wouldn’t have type, updated messaging service picker to align with supported account types, removed obsolete entries.
- Settings (org.webosports.app.settings): Clarify keyword: AutoCompletion->AutoCorrection.

**System Level:**

- meta-rpi-luneos: Fix build issues.
- jenkins-jobs: Add Hammerhead as target v2.3.9.
- webos-telephonyd: telephonyservice_sms.c: Use timestamp in milliseconds for legacy compatibility.
- luna-sysmgr: autoCompletion->autoCorrection.
- webos-keyboard: autoCompletion->autoCorrection, fix various typos mSpellchecing -> mSpellchecking.
- luna-init: autoCompletion->autoCorrection.
- pulseaudio-modules-droid: fix build when using android-headers from Ubuntu.
- qt5-qpa-hwcomposer-plugin: fix build for 4.4.2 with Ubuntu’s android headers.
- nyx-conf: add hammerhead configuration.
- luneos-package: use KERNEL_IMAGETYPE for the image name.
- initramfs-boot-android: improve initrd’s kernel logging.
- luna-sysmgr-conf: externalize machine-specific configuration files.
- nyx-modules: externalize machine-specific configuration files.
- luna-next-conf: add hammerhead environment file.
- luna-sysmgr-conf: have better GridUnit for hammerhead.
- VoiceCall: Update to latest from upstream (28-Jan-2017).
- pulseaudio-modules-droid: Update to latest from upstream (28-Jan-2017).
- sensorfw: Update to latest from upstream (28-Jan-2017).
- mobile-broadband-provider-info: Switch to Mer variant & bump SRCREV.
- qtbase_git.bbappend: Use += for PACKAGECONFIG_DISTRO.
- hunspell: removed from meta-webos-ports using the one from meta-openembedded instead.
- libhybris: Bump SRCREV, together with fixes for issues.
- Add qtubuntu-camera as backend.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/chailatte/) to get started. Tenderloin, Mako, Hammerhead and Maguro remain our focus for now, but the emulator & Grouper work too.

*Please note that in order to use the latest stable builds on the Galaxy Nexus (Maguro), Nexus 4 (Mako) and Nexus 5 (Hammerhead) you need to flash the CM 12.1 images first using CWM/TWRP. In order to do so, you might be required to do a “factory reset” or at least “wipe cache”. CWM/TWRP will indicate when this is needed. After successfully flashing CM 12.1, make sure to boot it at least once before going back to CWM/TWRP to flash the latest LuneOS image! We have provided links to CM 12.1 for these 3 images on our device pages below.*

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Nexus 5 (Hammerhead)](http://webos-ports.org/wiki/Install_LuneOS_for_Hammerhead), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](http://forums.webosnation.com/luneos/331603-pivotce-luneos-february-stable-release-chai-latte.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

We will see you in March with a new release!

We have the following items on our to-do list to focus on:

- Get the camera working
- Work on Yocto ~~Morty/~~Pyro upgrade
- Investigate feasibility of QT 5.7/5.8 Upgrade
- UI tweaks
- Messaging improvements

Image credit: [And the prize for best dressed chai latte goes to… by Lachlan Hardy](https://www.flickr.com/photos/lachlanhardy/29654271634/).
