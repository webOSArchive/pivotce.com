---
title: 'LuneOS February Stable release: Eiskaffee'
date: 2024-02-15 17:18:32 UTC
modified: 2024-02-15 17:38:14 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [Developer]
slug: luneos-february-stable-release-eiskaffee
source_url: https://pivotce.com/2024/02/15/luneos-february-stable-release-eiskaffee/
wordpress_id: 4565
featured_image: ../images/files/2021/02/Eiskaffee.jpg
featured_image_source: https://pivotce.com/files/2021/02/Eiskaffee.jpg
excerpt: Sooo that was a really long time since a release, but webOS Ports are still around and active as ever! We have continued making updates and producing testing images. But…
---

# LuneOS February Stable release: Eiskaffee

Sooo that was a really long time since a release, but [webOS Ports](https://webos-ports.org) are still around and active as ever!

We have continued making updates and producing testing images. But a lot happened that resulted in us not putting out a proper release out in the past few years.

Those who have stayed in touch with the community will know there has been some turmoil with the closure of the webOS Nation forums last year. Things stabilised over the last year as people converged around the [webOS Archive](https://www.webosarchive.org/) and made plans on the associated [Discord server](https://docs.webosarchive.org/?/docs/community). Much of the old information from webOS Nation was preserved thanks to the [internet archive](http://forums.webosarchive.org/) and can still be accessed, if imperfectly. We have now set up a [new community forum](https://forums.weboslives.eu) that largely replicates the old layout and is ready for fresh content.

If you are eager to find out what we’ve been working on and to try out the new release, read on…

The (Jenkins) builder infrastructure we had available previously decided to have a number of malfunctions, leading it to be no longer available to us. So for now we’re back to our own builders for building all the images, which isn’t great, but at least we’re still building and providing images! We are now using [Yocto “kirkstone”](https://www.yoctoproject.org/development/releases/), which means newer base components like systemd, pulseaudio and wayland.

Since the last release LuneOS has gone through a major rework under the hood. To summarize:

- We moved from Qt5 to [Qt6](https://www.qt.io/product/qt6) (6.5.2 included in this release).
- We have moved away from our own compositor (luna-next) to the one provided by LG in [webOS OSE](https://www.webosose.org/) called luna-surfacemanager.
- We are now using LG’s WAM (WebAppManager) instead of our own custom one together with LG’s fork of Chromium (94).
- A major rebase of all components shared with webOS OSE to be based on the [webOS OSE release 2.23.0](https://www.webosose.org/blog/2023/09/07/webos-ose-2-23-0-release/) now.
- This included a migration to Enhanced ACG which provides a lot tighter security for LS2 calls from apps and services.

This all was an enormous amount of work behind the screens but little visible to the end user, however this does offer clear benefits going forward being:

- A shared code-base with LG, which means less custom components and maintenance.
- Years of field tested code on LG production devices which offers more stability.
- In this process we were able to keep backwards compatibility for apps and services.
- Easier to upgrade to latest OSE components, since we have migrated almost all remaining components that were still not based on the latest webOS OSE or on Open webOS. (125 components were migrated in total, 15 components are still to be migrated).

In the meanwhile we have also been working hard to support the newly released [Pine64](https://pine64.org/devices/#_phones_and_tablets) devices such as the PinePhone, PinePhonePro and PineTab2 which are affordable devices which can run a very close to mainline kernel and a multitude of OS-es. We now support booting off [tow-boot](https://pine64.org/documentation/PinePhone_Pro/Software/Bootloaders/) on Pinephone.

The new close to mainline kernel for the Pine64 devices allows them to run things like [Waydroid](https://waydro.id/) out of the box!

All other supported Android devices are now based on [Halium/Android](https://halium.org/) 9.0.

So what is ahead for the near future?

Our focus will be on the mainline devices and emulator ([qemux86-64](https://www.qemu.org/)), however we will try to keep support for the Android/Halium based targets as well.

- Upgrade to latest Chromium 108 released by LG recently
- Work on audio & multimedia infrastructure provided by webOS OSE to get it working in LuneOS
- Work on camera infrastructure
- Try to get a mainline kernel working for Tenderloin, Hammerhead, Mido and Tissot.
- Improve/add QML components and add new basic apps to be used such as Camera, Flashlight, Audio Player, Video Player
- Piggyback off some of the work done by the [LG TV homebrew community](https://github.com/webosbrew/).
- Provide a GSI image for newer Android (9.0+) based devices, this would allow a standard image to boot on most modern Android devices v.s. building a device specific one for each device.

---

**Known issues:**

- Battery usage is on the high side
- No audio in webapps (we decided not to spend time on this, seeing we plan to update Chromium soon anyway)

The Usual:

1. Sign up for [the bug tracker](https://github.com/webOS-ports/luneos-testing/issues).
2. [Get involved](https://pivotce.com/2024/02/15/luneos-help-wanted-2024/) and…
3. [Download and Install](https://webos-ports.org/wiki/Devices)

Feel free to download the updated builds to get started. Currently supported targets: PinePhone, PinePhonePro, PineTab2, Qemux86-64 (Virtualbox), all with mainline kernel. Tenderloin, Hammerhead, Tissot, Mido, Rosy, Mako (Android 9.0/Halium based with their respective Android kernels (3.4 and newer)). RaspberryPi 3 and RaspberryPi4 might work too, however we haven’t tested this ourselves.

[Installation instructions are on the wiki](https://webos-ports.org/wiki/Devices). And remember we don’t do timelines.

Don’t forget to contact us with any questions and feel free to join the discussion on the [webOS Lives forums](https://forums.weboslives.eu/d/41-eiskaffee-luneos-stable-release-february-2024). Catch us on Twitter @webosports on IRC: Libera:#webos-ports, [Telegram](https://t.me/luneos_dev) or email [webos.ports@gmail.com](mailto:webos.ports@gmail.com).

We will see you shortly again with a new release!

Picture credit: [roDesignment](https://pixabay.com/users/rodesignment-733094/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=3663166) from Pixabay
