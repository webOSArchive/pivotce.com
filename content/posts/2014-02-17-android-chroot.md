---
title: Android chroot
date: '2014-02-17T18:53:47Z'
lastmod: '2014-02-23T18:24:09Z'
author: preemptive
author_slug: preemptive
categories:
- News
tags:
- Android
- chroot
slug: android-chroot
summary: Root is the base level directory on a Linux system. webOS is at base, a Linux system. All branches of the file system and therefore the whole system stem from…
source_url: https://pivotce.com/2014/02/17/android-chroot/
wordpress_id: 1530
archived: true
comment_page: 2014-02-17-android-chroot
---

![Android in a card!](/images/files/2014/02/AndroidChroot.jpg)
*Android screen grab: Nikolay Nizov*

Root is the base level directory on a Linux system. webOS is at base, a Linux system. All branches of the file system and therefore the whole system stem from the root. Android is also a Linux based system that runs from a root directory. There is a technique known as [chroot](http://en.wikipedia.org/wiki/Chroot) (change root) that enables you to run a second system within another by creating a subsystem in which the secondary system appears to have the root directory.

If you pay much attention to the shifts and changes in the mobile phone market, you will be aware that over the past couple of years there has been increasing consolidation. These days the market is dominated by Apple’s iphone and most of all, by the many models running the Android operating system. This system – at least in its basic form is open source software. Naturally, many developers therefore take advantage of this ‘off the shelf’ operating system. New entrants and existing challengers in the market have tried to leverage Android and specifically, it’s large app catalogue to gain an advantage. This includes Blackberry, Jolla (sailfishOS) and there are reports that even Microsoft are considering a means to run Android apps on Windows phone. There are also projects that offer existing Android users the opportunity to install a customised version. The most notable of these is [Cyanogenmod](http://www.cyanogenmod.org/), which can now be installed on a wide range of hardware.

Within the world of webOS, there have been a few Android projects. Hewlett Packard experimented with Android on it’s Touchpad and when a few were accidentally released with this system, the included drivers allowed Cyanogenmod to be offered as a dual-boot addition to the Touchpad. Other projects have run [Android on the Veer](http://forums.webosnation.com/android-webos/314562-flash-andoid-your-veer.html) and the [Pre2](http://forums.webosnation.com/other-oss-devices/320469-android-palm-pre2-i-success.html).

Of course, the easiest way to have Android on your device is… buy an Android device! But of course, we prefer webOS, so for this community, the dream has been to run Android as an app in a card. It was an early plan of the [PIC group](http://www.phxdevices.com) which as you may know, eventually translated into the Kickstarter campaign to bring the [ACL to the Touchpad](/2014/02/14/acl-release-part-2/). A bold, early (and problematic) project was to run [Android as an app on the Touchpad](http://forums.webosnation.com/android-webos/302291-test-ipk-released-android-touchpad-special-applicaiton.html) by Chinese developer, Chomper. Functionality was limited and the two systems conflicted as they both tried to control the hardware.

You may recall a previous report on pivotCE about a project to run [Android in a card on the Pre3](/2013/12/06/android-in-a-card-pre3/). We were waiting for Mr Nizov to find the time to write instructions for the install and he has [delivered as promised](http://forums.webosnation.com/android-webos/327344-pre3-androidchroot-run-android-inside-webos.html) with a beta version 1.0 release. What we have here is the long hoped for ‘Android in a card’. It supports CM7 which is the equivalent of Android 2.3 and is therefore on a par with the current ACL technology. Yes, you can install Google play with this project.

There are some signs that this work can be ported to both the Veer and Touchpad. Developer, Herrie contributed some adaption for these devices to a bootloader originally developed by [K3dar](http://forums.webosnation.com/other-oss-devices/278450-android-pre.html#post2909904) & [Slyon](https://github.com/k3dar/bootr-nofob/blob/master/doc/AUTHORS). However, mobile devices are only really intended to run one OS at a time and limitations on RAM means that Android performance is not at a ‘native’ level. A swap file is required and complex apps may slow it considerably. There is no guarantee that this can improved. Forum member Ananimus has assisted in getting the project to work with the hardware keyboard. Both he and Nikolay Nizov work in physics.

Before you get too excited, remember the caveats that apply to all such projects – especially in the early stages. Running two operating systems is extremely difficult and this is beta software. If you have any warranty left, the above mentioned projects WILL void it. They may result in you having to [doctor your device](/2014/01/02/the-ninth-day-of-webos-mas-webos-doctor/) and could possibly break it permanently.

If you know what you are doing, then [take a look](http://forums.webosnation.com/android-webos/327344-pre3-androidchroot-run-android-inside-webos.html) and if you can, help the effort. The rest of us can watch the thread on webOS Nation and support development. The first post has a donation link and there is a [post](http://forums.webosnation.com/android-webos/327344-pre3-androidchroot-run-android-inside-webos-3.html#post3414040) on how to negotiate the Russian paypal link to donate.
