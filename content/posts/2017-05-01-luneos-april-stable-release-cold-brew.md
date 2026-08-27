---
title: 'LuneOS April Stable Release: Cold Brew'
date: '2017-05-01T20:05:33Z'
lastmod: '2017-07-23T14:28:47Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- Cold Brew
- Developer
slug: luneos-april-stable-release-cold-brew
summary: A bit later than expected but we’re back! Over 2 months passed since the last release and we’re finally back with a new release called “Cold Brew”. We have been…
featured_image: /images/files/2017/04/LuneOS_Cold_Brew2.jpg
source_url: https://pivotce.com/2017/05/01/luneos-april-stable-release-cold-brew/
wordpress_id: 4029
featured_image_source: https://pivotce.com/files/2017/04/LuneOS_Cold_Brew2.jpg
archived: true
---

A bit later than expected but we’re back! Over 2 months passed since the last release and we’re finally back with a new release called “Cold Brew”. We have been working very hard behind the scenes in the past 2 months!

So you’re asking what we have done? Most importantly we now have an initial setup for camera working on both the N4 and N5 with an initial version of the app written in Qt (QML). It’s still pretty rough, but it will do basics for now.  Further improvements will come once we upgrade Qt to 5.7/5.8.

Behind the scenes we’ve been working on getting our Yocto updated to Pyro. This brings quite some challenges due to glibc (2.24) not being compatible with linux kernels < 3.2. Also the newer systemd version (232) brings some challenges in terms of kernel requirements, but we’ve been able to work around those for now.

For Mako (N4), Hammerhead (N5) this isn’t really a problem because we have a 3.4 based kernel, for the Tenderloin (Touchpad) there are 3.4 based kernels available as well, so we’ll be aiming to migrate to a 3.4 based kernel for Tenderloin.

For Maguro (Galaxy Nexus) the situation is unfortunately more problematic because there’s no real working 3.4 based kernel available currently. It’s therefore likely that as of next release we will be forced to drop support for the Galaxy Nexus.

[We’re also taking part in in the Halium Project that was announced last week](https://halium.org/announcements/2017/04/24/halium-is-in-the-air.html). There are already a lot of synergies between the various OS-es based on Android and also still quite some minor tweaks for each OS. By joining forces in the project we aim to have a common base for the various Android based OS-es.

We have the following items on our to-do list to focus on:

- Work on Yocto Pyro upgrade
- QT 5.7/5.8 Upgrade
- Various UI tweaks
- Messaging improvements
- Camera improvements

**Known issues:**

- Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.
- Focus bug on input fields. You can work around this by hiding the virtual keyboard and pressing the input again.

### **Changelog**

**Applications:**

- Testr (org.webosports.app.testr): Adds test of HTML5 camera API (navigator.mediaDevices); Removes erroneous component from HTML5 camera test; Camera test works correctly with portrait video; HTML5 camera test: adds list of user media devices & requests rear camera.
- Camera (org.webosports.app.camera): Initial app writen from scratch in QT.

**System Level:**

- qtubuntu-camera: add missing dependencies for Qt.
- packagegroup-luneos-extended: put the camera recipes in LIBHYBRIS_RDEPENDS.
- mobile-broadband-provider-info: Add LIC_FILES_CHKSUM.
- qtbase_git.bbappend: Use = for PACKAGECONFIG_DISTRO.
- hunspell: remove – it is in meta-oe.
- mesa: do not move around libGLESv2.so.
- qtvideo-node: Use webOS-ports repository.
- meta-webos-ports: Add org.webosports.app.camera and the camera infrastructure packages.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/coldbrew/) to get started. Tenderloin, Mako, Hammerhead and Maguro remain our focus for now, but the emulator & Grouper work too.

*Please note that in order to use the latest stable builds on the Galaxy Nexus (Maguro), Nexus 4 (Mako) and Nexus 5 (Hammerhead) you need to flash the CM 12.1 images first using CWM/TWRP. In order to do so, you might be required to do a “factory reset” or at least “wipe cache”. CWM/TWRP will indicate when this is needed. After successfully flashing CM 12.1, make sure to boot it at least once before going back to CWM/TWRP to flash the latest LuneOS image! We have provided links to CM 12.1 for these 3 images on our device pages below.*

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Nexus 5 (Hammerhead)](http://webos-ports.org/wiki/Install_LuneOS_for_Hammerhead), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](http://forums.webosnation.com/luneos/331670-pivotce-luneos-april-stable-release-cold-brew.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

We will see you shortly with a new release!
