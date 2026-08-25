---
title: 'LuneOS September Stable Release: Decaf'
date: 2017-10-08 11:30:19 UTC
modified: 2018-03-25 15:29:17 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [Developer]
slug: luneos-september-stable-release-decaf
source_url: https://pivotce.com/2017/10/08/luneos-september-stable-release-decaf/
wordpress_id: 4070
featured_image: ../images/files/2017/09/LuneOS_decaf.jpg
featured_image_source: https://pivotce.com/files/2017/09/LuneOS_decaf.jpg
excerpt: 'The long wait is over #LuneOS and #webOS fans! We’re back with a new release called “Decaf” which we believe will be a milestone in terms of developments and the…'
---

# LuneOS September Stable Release: Decaf

The long wait is over #LuneOS and #webOS fans! We’re back with a new release called “Decaf” which we believe will be a milestone in terms of developments and the way forward!

So you’re wondering what we’ve been up to the past 2+ months?

Well, actually a whole lot when you look at our changelog! We’ve been able to migrate from Qt 5.7 via 5.8 to 5.9.2 which is a long term support (LTS) release of Qt. This brings our web capabilities a lot more up to date! We’re on Chromium 56 based release now which dates back to January this year. This brings a lot of interesting new and modern HTML5 features such as Web Components that are used by Google’s Polymer framework, for example. It also offers us better plugin support. It’s now technically possible to sideload Flash & WideVine plugins and the sites using these can see and use the plugins. The plugins cannot be distributed in the image due to licensing issues, but users are free to sideload them.

This opens up the possibility to watch DRM protected content on sites like Netflix, YouTube etc.

The migration to Chromium 56 caused a lot of layout issues for all Enyo 1.0 apps which needed to be addressed at the same time as we made sure that the Enyo 1.0 apps we’re using can be run and debugged in Chrome on the desktop.

The new version of Qt also brings a simplified API for Wayland.

Work has been done on the stability issues with the Touchpad and it’s a lot more stable now. The backlight being always on for Hammerhead (Nexus 5) has been solved too and the VirtualBox image is working properly again!

We have been able to migrate our Mako (Nexus 4) and Hammerhead (Nexus 5) to use Project Halium. This means that all our Android & webOS based targets are now using Project Halium as a basis. In the near future we plan to work more closely together with Project Halium and use their kernels with our patches instead of maintaining the kernels by ourselves. This is expected to be completed by the next release. Using Halium kernels will also allow LuneOS ports for supported Halium devices to become a lot more easy and straightforward.

Quite a number of the UI bits in various QML apps have been reworked to use QtQuickControls2 styling for LuneOS. This will allow to have unified components to be used across various QML apps. It will also allow a better experience on HiDPI and retina screens.

The following items on our to-do list will be where we focus next:

- Various UI tweaks
- Messaging improvements
- Camera improvements
- Fix known issues on the various targets
- Bring back official support for Touchpad 4G (current build works on Touchpad 4G but only WiFi)
- Migrate to Halium kernels
- Migrate from BlueZ4 to BlueZ5

**Known issues:**

- Nexus 5 (Hammerhead) / Nexus 4 (Mako): Issue with sensors causing rotation to not work for example.
- Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.
- Focus bug on input fields. You can work around this by hiding the virtual keyboard and pressing the input again.

### **Changelog**

**Applications:**

- FirstUse (org.webosports.app.firstuse): Use QtQuickControls 2.0 and LuneOS styling; Change LuneOSStyle to LuneOS; NetworkConnectPage: fix Connect button; Convert WifiPage and NetworkConnectPage to QtQuickControls 2; NetworkConnectpage: fix focus handling; FeedsPage: improve layout.
- Testr (org.webosports.app.testr): Adds Web Components platform tests.
- Browser (org.webosports.app.browser): Add precompiled files to gitignore; BrowserWebView: begin adaptation for Qt 5.8; BrowserWebView: fix for contextual menu; Migrate to QtQuickControls2 and simplify code; BrowserWebView: improve handling of load errors; appjson: Activate LuneOS style for QtQuickControls2; Quit when a main QNL file can’t be loaded; AppMenu: use LuneOSMenu attached property; Fix SearchSuggestion appearance; Fix dialogs sizes; SettingsPage.qml: Fix undefined errors; NavigationBar.qml: Fix UserAgent overrides again; NavigationBar.qml: Make sure we override useragent for history & bookmark items too.
- Core-apps: Add initial missing bits for running & debugging properly; Add mock account templates and point to right path; com.palm.app.notes: Add mock data; com.palm.app.calendar: Add mock for new events; com.palm.app.calendar: Make -webkit-border-image work with Chromium 51 and higher; com.palm.app.clock: Various minor fixes & mock data; com.palm.app.clock: Make -webkit-border-image work with Chromium 51 and higher; com.palm.app.contacts: Make -webkit-border-image work with Chromium 51 and higher; com.palm.app.notes: Make -webkit-border-image work with Chromium 51 and higher; com.palm.app.email: Make -webkit-border-image work with Chromium 51 and higher; com.palm.app.email: Remove duplicated code in 2-folder; com.palm.app.accounts: Add mock data for desktop debugging

**User Interface:**

- luna-systemui: Adjust the PowerOffAlert popup height to 30 units.
- luna-next-cardshell: Adapt for Qt 5.8; LunaSysAPI: fix displayOn/Off; CardView: simplify pinch-to-zoom.
- luneos-components: QtQuickControls2: fix .pro module for QML files; QtQuickControls2: change style name to LuneOS; QtQuickControls2: add images to qmake’s project; QtQuickControls2: HighDPI compatible Button and Switch; QtQuickControls2: prepare Hi-DPI tests; TabButton: add possibility to put an image as content; LuneOSWindow: now inherits ApplicationWindow from QuickControls2; QtQuickControls2: improve layout for some components; QtQuickControls2: add appMenuStyle for Menu; LuneOS.Components: merge deployment.pro and add missing qml file; QtQuickControls2: TextField: improve background; UserAgent.qml: Update QtWebEngine & Chrome version;

  UserAgent.qml: Make sure all urls are lowercase before we start to do anything.
- Enyo-1.0: Make -webkit-border-image work with Chromium 51 and higher; Revert back to original Enyo 1.0 spinner; util.js: Fix libPath for testing on desktop

**System Level:**

- luna-webappmanager: Migrate to Qt 5.8; main: add options for disabling advanced sandboxing; Fix WebEngine UserScript includes; Option to disable OpenGL ES3 in Chromium; WebApplicationWindow: remove mLaunchedHidden; Revert “Option to disable OpenGL ES3 in Chromium”; Revert “main: add options for disabling advanced sandboxing”.
- luna-appmanager: Add dummy logCrashRegisterContext for aarch64.
- luna-sysmgr: DisplayManager: always turn off backlight before blanking hwc; DisplayManager: shorten the powermenu timeout to 1.5s; Add dummy logCrashRegisterContext for aarch64
- nyx-modules: keys: treat KEY_HOMEPAGE as HOME key; nyx-modules: Add cmake file for qemux86-64; nyx-modules: Add cmake file for qemux86-64; Remove machine specific cmake files; Remove machine specific cmake files II.
- db8: MojConfig.h: allow to build for aarch64 (raspberrypi3-64)
- android_luneos_hal: Switch to Halium 5.1; tenderloin: fix vendor patch; Apply_patches: abort previous git am in case of failure; hardware/libhardware: revert patch for QCOM_BSP
- android: First commit based on Halium-5.1, with support for TP and N5; Add mako and simplify remotes; Fix mako repo; Add luneos-hal repo, to patch the vendor trees; wop_targets.xml: Update repos to webos-ports; wop_targets.xml: Update branch from wop-12.1 to halium-5.1; wop_targets.xml; Fix comment for luneos-hal
- meta-rpi-luneos: raspberrypi2: prefer linux-raspberrypi 4.9.%; raspberrypi3: add config for raspberrypi3 and raspberrypi3-64 from meta-raspberrypi; systemd: Don’t override whole USERADD_PARAM
- luna-next: Migrate code to Qt 5.8; CompositorWindow: focusOnClick=false for overlays; Fix window deletion; Compositor: make hasProcessMultipleWindows more robust; Compositor: make window deletion more robust; Don’t use unimplemented SendFullKeyEvent; CompositorWindow: wait for window type to be set; Compositor: remove Qt’s version from includes; compositor: add a default output mode; compositor: use QtKeyExtensionGlobal
- android_hardware_qcom_display-caf: ionalloc: if alloc failed, don’t trust errno
- qtsensors-sensorfw-plugin: Update to latest 5.8 code
- meta-smartphone: mako, hammerhead, tenderloin: use kernel sources from shr-distribution/linux.git and fix build with gcc-7; hammerhead kernel: delay wifi init; android-system-image-*: skip already-stripped QA; mako,hammerhead,tenderloin: use our Halium image; android-system-image-mako: fix install script; android-system-image-tenderloin: fix checksums; hammerhead, mako, tenderloin: Use Halium image built with Ports repos; libhybris: fix tenderloin build flags; android-system-image-tenderloin: bump PV; android-system-image: Add symbolic link for wifi; android-system-image-mako: fix typo
- meta-qt5: Update to Qt 5.9.2 including QtWebEngine based on Chromium 56.
- meta-webos-ports: qtscenegraph-adaptation: Adapt for 5.8 and use mer-project repo; qtwebengine: adapt to Qt 5.8; qtwayland: adapt to Qt 5.8; packagegroup-luneos-extended: disable camera bits; libconnman-qt5: bump to version 1.2.3; luna-next: switch to Qt 5.8 version; luna-next-cardshell: switch to Qt 5.8 version; luna-webappmanager: switch to Qt 5.8 version; luneos-components: switch to Qt 5.8 version; qtwebengine: remove a patch harmful for Qt 5.8 version; qtwebengine: Fix a crash in PalmServiceBridge; leveldb-tl: fix build with gcc7; pidgin-sipe: Update to 1.22.1; pidgin: Update to 2.12.0; libotr: Update to 4.1.1; pidgin: Add patches to local build pending upstream upgrade; libotr: Add patches pending update in upstream; qtwebengine: add patch to disable some sandboxing; luneos-components: add qtquickcontrols2 dependency; qtwayland: fix window mask; qtsensors-sensorfw-plugin: Update to QT 5.8; qtsensors: correct path for sensors config file; luneos-components: add QtQuickControls2 support; libpng: Add to meta-webos-ports layer since oe-core version is broken; qtwebengine(-chromium): Migrate to QT 5.9 and Chromium 56; qtwayland: Upgrade to QT 5.9; nyx-conf: add event0 to the keys managed by nyx.; luna-webappmanager: Updates for QT 5.9; luna-sysmgr-conf: Add luna-platform.conf for qemux86-64; presage: fix build with gcc-7; packagegroup-luneos-development: drop mdbus2; lxc=v2.0.8; nyx-modules: Add qemux86-64 file; qtwebengine: Add -embedded configuration; qtubuntu-camera: fix and re-enable camera related recipes; luneos.inc: don’t restrict QEMU_TARGETS; sdl2-opengles-test: build only gles2 version for rpi; qtwebengine: add LuneOS specific switches; ofono: fix QA issue; qtubuntu-camera: fix few issues; nyx-modules: add cmake file also for raspberrypi3-64; luneos.inc: fix UVESA_MODE; qtwebengine: fix crash with WebGL2 textures; luna-next-conf: qemu*: workaround for mouse pointer; luneos-emulator-appliance: use virtio-net for Ethernet; jemalloc: fix build for aarch64 (raspberrpi3-64); nyx-modules: bump SRCREV and fix build for MACHINEs with dash in name; db8: bump SRCREV to fix build for aarch64 (raspberrypi3-64); node-gyp-native: fix incorrect symlink; pmcertificatemgr: fix u-a config; crash-handler: fix ldflags QA issue; sdl2-opengles-test: fix ldflags QA issue; luneos-emulator.ovf: Fix Adapter Type to virtio; qtscenegraph-adaptation: Drop patch & bump SRCREV; qtscenegraph-adaptation: fix URI; mako: avoid loading conflicting Alsa driver; environment.conf: Add QT_QPA_EGLFS_INTEGRATION=none; pulseaudio-distro-conf: use MACHINE_ARCH; pmcertificatemgr: drop webos_machine_impl_dep inherit; meta-luneos: exclude ofono-conf from signatures as abi safe; core-apps: drop allarch; org.webosports.service.update: drop allarch; loadable-frameworks: drop allarch; cordova: inherit allarch; luneos.inc: apply uvesafb config and vboxvideo blacklist also to qemux86-64; qtwayland: Fix QtKeyExtensionGlobal’s export; qtubuntu-camera: fix missing .qmake.conf; qtsensors: From Qt 5.9, settings follow XDG standard paths.;ofono-conf: Make sure we don’t use RIL on qemu; systemd: Add patch to disable “Failed to set invocation ID on controlgroup”;qtwebengine: Add /usr/lib/chromium already
- bitbake: cooker: add BB_CMDLINE to enable access to UI command line with memres; cooker.py: Fix layer priority processing; toaster: recipe links broken for default layers; toaster: edit column list not sorted; toaster: set default pokydirname if no external layers; toaster: debug message for lists layers missing separators; toaster: Order column in Tasks selectable; toaster: display error when the fstype select is empty; cooker: ensure monkey-patching in collect_bbfiles() gets undone on error; cooker: fix watching empty directories; cooker: Track directories searched for bbappend/bb files; toaster: noweb should init database; toaster: get_last_build_id not called correctly; toaster: add getMessage to MockEvent; toaster: fail on layers with sub-layer; toaster: add ID’s to build menu links; toaster: add ID’s to navigation links
- openembedded-core: image.bbclass: Sorted ctypes to avoid basehash error; gcc-6.3.inc: Use ucontext_t not struct ucontext; linuux-yocto/4.1: update to 4.1.43 plus bluetooth CVE-2017-1000251; libproxy: use stable download URL; linux-yocto/4.9: bluetooth: CVE-2017-1000251; linux-yocto/4.4: bluetooth: CVE-2017-1000251; linux-yocto/4.10: bluetooth: CVE-2017-1000251; linux-yocto/4.9: update to v4.9.49; linux-yocto/4.4: update to v4.4.87; (PRE)MIRRORS: fix pattern for npm:// without slash; waffle: fix REQUIRED_DISTRO_FEATURES and PACKAGECONFIG virtual/libgl dependencies; rootfs-postcommands: add test for unsatisfied RRECOMMENDS; rootfs-postcommands: remove empty line; rootfs-postcommands.bbclass: Filter out dangling symlinks in ssh_allow_empty_password(); alsa-utils: Do not hardcode path to /lib/udev; package_rpm.bbclass: disable generation of .build-id links; package_rpm.bbclass: use multithreaded xz compression; rpm: allow arch-dependent binaries in noarch packages; bitbake.conf: add bzr to HOSTTOOLS_NONFATAL; glibc-locale: add runtime dependency on glibc; Revert “expat: Don’t use getrandom() in the -native case”; grub: Fix build with gcc7; staging: Fix a logic error which caused dependency removal; staging: Ensure dependencies are removed before being added; staging: Avoid sysroot removal races; classes/license: drop erroneous sha256 parameter in LIC_FILES_CHKSUM; linux-yocto/4.4: update to v4.4.85.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/decaf/) to get started. Tenderloin, Mako and Hammerhead remain our focus for now, but the emulator & Grouper work too.

*Please note that in order to use the latest stable builds Nexus 4 (Mako) and Nexus 5 (Hammerhead) you need to flash the CM 12.1 images first using CWM/TWRP. In order to do so, you might be required to do a “factory reset” or at least “wipe cache”. CWM/TWRP will indicate when this is needed. After successfully flashing CM 12.1, make sure to boot it at least once before going back to CWM/TWRP to flash the latest LuneOS image! We have provided links to CM 12.1 for these 3 images on our device pages below.*

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Nexus 5 (Hammerhead)](http://webos-ports.org/wiki/Install_LuneOS_for_Hammerhead) and [Emulator](http://webos-ports.org/wiki/Emulator)are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](http://forums.webosnation.com/luneos/331837-pivotce-luneos-september-stable-release-decaf.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

We will see you shortly again with a new release!

Picture Credit: [Decaf……is like kissing your brother?](https://www.flickr.com/photos/tripelle/9309252961) ©Angie Born. (CC BY 2.0) Cropped for article.
