---
title: 'LuneOS July Stable Release: Cortado'
date: 2017-07-23 10:56:58 UTC
modified: 2017-12-04 19:57:20 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [Developer, enyo]
slug: luneos-july-stable-release-cortado
source_url: https://pivotce.com/2017/07/23/luneos-july-stable-release-cortado/
wordpress_id: 4047
featured_image: ../images/files/2017/07/cortado.jpg
featured_image_source: https://pivotce.com/files/2017/07/cortado.jpg
excerpt: That took a while, but lots of ground has been covered! We’re finally back with a new release called “Cortado”. We have been working very hard behind the scenes during…
---

# LuneOS July Stable Release: Cortado

That took a while, but lots of ground has been covered! We’re finally back with a new release called “Cortado”. We have been working very hard behind the scenes during the past couple of months!

So you’re asking what we have done? Most importantly we now have all our supported targets on at least a 3.4 kernel which was a critical requirement in order to update Yocto to Pyro. Both glibc and systemd required this.

So the Touchpad, Nexus 4 and Nexus 5 are now all on a 3.4 kernel and on an Android 5.1-based build!

For the Touchpad we were able to already use the work done by the  [Halium project](https://halium.org/) and we’re now mainly using [Halium 5.1](https://github.com/Halium/android_build/tree/halium-5.1) as a source for building the required Android bits!

This release is a bit of an intermediary release, so it’s not as stable as we would like it to be and as you are used to. We expect to address the remaining issues with the next release. We wanted to get this release out since it marks quite a milestone with all the underlying updates to the system.

We have also updated some of the UI bits and there is now a tablet layout similar to what was available on webOS 3.x with notifications at the top of the screen! Preware is now also working properly on targets with a landscape orientation like the Touchpad & VirtualBox (qemux86).

Due to the fact there’s no suitable 3.4 kernel available for the Galaxy Nexus (Maguro) we were forced to drop this as a porting target. We have also dropped support for Nexus 7 WiFi 2012 version (Grouper) due to the fact that none of the devs actually had this device and therefore we couldn’t test any updates.

We’re already full speed ahead with the update of QT from 5.6 to 5.8. This brings quite some challenges and requires quite some rework in various bits, but it seems things are progressing well.

Once the 5.8 upgrade has been completed we’ll be looking into updating to 5.9.1 in the near future as well since this will be a LTS (Long Term Support) release of QT. The upgrade from 5.8 to 5.9.x should be fairly straight forward since the changes aren’t that major.

We have the following items on our to-do list to focus on:

- QT ~~5.7/~~5.8/5.9.1 Upgrade
- Various UI tweaks
- Messaging improvements
- Camera improvements
- Fix known issues on the various targets
- Bring back official support for Touchpad 4G (current build works on Touchpad 4G but only WiFi).

**Known issues:**

- Nexus 4 (Mako): Sound is broken on current build.
- Nexus 5 (Hammerhead): Vibration doesn’t seem to work, backlight doesn’t turn off.
- Qemux86: Mouse input doesn’t seem to work.
- Touchpad (Tenderloin): Screen doesn’t always turn off, bug with switching between input fields leading to screen turning off or not responding. No official support for the 4G Touchpad yet, but the build should work.
- Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.
- Focus bug on input fields. You can work around this by hiding the virtual keyboard and pressing the input again.

### **Changelog**

**Applications:**

- Preware (org.webosinternals.preware): Fix Panel behavior in landscape orientation.

**User Interface:**

- luna-next-cardshell: Notifications: separate view and model, Initial work on tablet style statusbar, Fix NotificationAreaTablet height, StatusBar: fix tablet TweaksClock visibility.

**System Level:**

- meta-smartphone: linux-lg-hammerhead: fix some minor defconfig values, android-system: only start after main partitions are mounted, android-system-image: make “symbols” directory optional, android-headers-tenderloin: use API 22, patched to match tenderloin specific content, linux-hp-tenderloin: use a 3.4 kernel, android-system-image-tenderloin: use a Halium 5.1 based Android build, android-system-image-tenderloin: Fix checksums, linux-hp-tenderloin: bump SRCREV, android-system-image-tenderloin: update Android image
- pulseaudio-modules-droid: migrate to PulseAudio 10.0
- systemd: Disable ProtectHome and ProtectSystem for old kernels
- ofono: Use Mer’s 1.19 and include fix
- libhybris: test_hwcomposer: add support for newer hwcomposer versions
- pulseaudio-modules-droid: match build flag for audio.h header
- libhybris: bump SRCREV and remove unneeded patches
- pulseaudio-modules-droid: define QCOM_HARDWARE
- pulseaudio-distro-conf: for tenderloin, avoid loading the alsa module
- purple-skypeweb: Update to 1.4 release
- yocto: Update from Krogoth to Pyro Release
- bitbake: Update from 1.30 to 1.34

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/cortado/) to get started. Tenderloin, Mako and Hammerhead remain our focus for now, but the emulator  works too.

*Please note that in order to use the latest stable builds on the Nexus 4 (Mako) and Nexus 5 (Hammerhead) you need to flash the CM 12.1 images first using CWM/TWRP. In order to do so, you might be required to do a “factory reset” or at least “wipe cache”. CWM/TWRP will indicate when this is needed. After successfully flashing CM 12.1, make sure to boot it at least once before going back to CWM/TWRP to flash the latest LuneOS image! We have provided links to CM 12.1 for these 2 images on our device pages below.*

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Nexus 5 (Hammerhead)](http://webos-ports.org/wiki/Install_LuneOS_for_Hammerhead) and [Emulator](http://webos-ports.org/wiki/Emulator) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](http://forums.webosnation.com/luneos/331736-pivotce-luneos-july-stable-release-cortado.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

We will see you shortly with a new release!
