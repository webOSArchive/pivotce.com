---
title: 'LuneOS November Stable Release: Doppio'
date: '2018-11-28T05:48:53Z'
lastmod: '2019-06-26T15:03:04Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- Developer
slug: luneos-november-stable-release-doppio
summary: 'The very long wait is over #LuneOS and #webOS fans! We’re finally back with a new release called “Doppio” which we believe will be a milestone in terms of developments…'
featured_image: /images/files/2018/10/Doppio2.jpg
source_url: https://pivotce.com/2018/11/28/luneos-november-stable-release-doppio/
wordpress_id: 4454
featured_image_source: https://pivotce.com/files/2018/10/Doppio2.jpg
archived: true
---

The very long wait is over #LuneOS and #webOS fans! We’re finally back with a new release called “Doppio” which we believe will be a milestone in terms of developments and the way forward!

So you’re wondering what we’ve been up to for the past year?

Well, actually a whole lot to be honest! We have upgraded the bluetooth stack from BlueZ4 to BlueZ5 which required quite some work to the kernels. This has been successfully completed for the Nexus 4 (Mako) and Nexus 5 (Hammerhead); unfortunately to date we haven’t been able to get this to work on the Touchpad (4G) (Tenderloin).

We have been working closely together with the Halium project and have made further integrations between LuneOS and Halium reducing duplication between the projects and using a single source where possible. This all to be more easily integrated, and to facilitate ports to newer devices. We have upstreamed our kernel patches (mainly to fix GCC 5/6/7/8 compatibility) to Halium so we can use a shared kernel for our targets.

Talking about new devices we’ve been working on: Since Google dropped the (budget) Nexus line and launched the (premium) Pixel line, we’ve been looking for other targets that are easily available, budget friendly and have good community support. We quickly ended up with Xiaomi which makes phones with decent specs, unlockable bootloader (the process is a bit tedious, but it’s do-able) and the phones give very good value for money.

This has resulted in us independently working on 3 different Xiaomi devices being the RedMi Note 4x (Mido), RedMi 5 (Rosy) and Mi A1 (Tissot).  These are all Aarch64 devices using the Snapdragon 625 chipset. We didn’t have any Aarch64 devices before and also they are based upon Halium 7.1 (Android 7.1) while all our previous targets were based upon Halium 5.1 (Android 5.1), so this brought a whole bunch of new challenges. There are still a few rough edges, but audio, sensors, wifi and bluetooth are now working. There was also quite some porting work done for some of the other Halium supported targets such as the OnePlus X (onyx), Google/Huawei Nexus 6P (angler) and Motorola G4 (athene). These are currently in various stages of development, whereby OnePlus X is the most mature.

The Xiaomi Mi A1 is a strategic device for us which we chose in cooperation with LG, to get LuneOS running on it and also as a target for LG’s webOS OSE (Open Source Edition).

[LG’s release of webOS OSE](/2018/03/19/open-source-webos-now-brought-to-you-by-lg/) came as a surprise to us, however it has great potential. Though the initial release of webOS OSE was very limited and therefore limited use case for people not being very familiar with webOS, it does offer a lot of potential for us. webOS OSE is basically 5 years of development of the core webOS bits since Open webOS was released. It has been deployed in millions of LG TV’s since and offers great improvements in terms of reliability and functionality. The big downside however is that there’s no record of the changes between Open webOS and webOS OSE, so this is making the migration a bit more challenging.

Early June the LuneOS team met with LG in Paris to discuss collaboration between our teams. As a result of this we have chosen the Xiaomi A1 as a device to port LuneOS to. This is now at a level similar to our other targets.

After this release we will therefore focus on migrating our Open webOS components to the updated components provided by webOS OSE. This will bring quite some challenges and hurdles along the way, however we’re positive that we can complete this migration and it will bring a lot of improvements in terms of code quality, stability, functionality and reducing the need for maintaining a lot of these components ourselves since we can share a common codebase with LG’s webOS OSE going forward.

LG has a very clear vision in mind for webOS. Since the initial release in March, a [roadmap has been published](http://webosose.org/discover/webos-ose-roadmap/) and [LG has pushed out 4 releases since the original release of webOS OSE.](http://webosose.org/blog/about-webos-ose-releases/5th-release-2018-october-2018/)

The following items on our to-do list will be where we focus next:

- Migration of Open webOS components to the newer webOS OSE components.
- Make the VirtualBox image work with a newer MESA.
- Migrate to Yocto Sumo/Thud release.
- Messaging improvements.
- Camera improvements.
- Fix known issues on the various targets.
- Bring back official support for Touchpad 4G (current build works on Touchpad 4G but only WiFi).

**Known issues:**

- Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.
- Focus bug on input fields. You can work around this by hiding the virtual keyboard and pressing the input again.
- Random issue with virtual keyboard not showing on Aarch64 devices.

### **Changelog**

**Applications:**

- Settings: Add QML variant, enable manual time and date in Setings.
- org.webosports.cdav: Add CLEANBROKEN

**User Interface:**

- luna-{sysmgr,sysmgr-common,appmanager,next}, mediaindexer: fix build with Qt 5.11.
- luna-{webappmanager,qml-launcher} org.webosports.app.{browser,firstuse}: fix build with Qt 5.11.
- luna-next-cardshell: add runtime dependency on qtmultimedia-qmlplugins, luneos-components.
- luneos-components: drop build time dependency on qtwebengine, switch to Mer’s bluezqt

**System Level:**

- luna-next: Add config for onyx, Add QT_OPENGL_NO_BGRA and remove QT_ENABLE_GLYPH_CACHE_WORKAROUND
- android-gadget-setup: fix functionfs test
- android-tools: fix compatibility with adb 5.1.1
- android-tools-conf: Fix the machine check, Don’t patch script for tenderloin
- base-files: provide a common fstab for all LuneOS devices
- bluez: switch from bluez4 to bluez5
- bluez5: Fix patch so it will work for RaspberryPi3, make firmware search case insensitive
- connman: Add connman-tools, connman-tests and connman-wait-online, Update to 1.35
- distro: luneos: switch release name to Doppio
- environment.conf: Add QT_ENABLE_GLYPH_CACHE_WORKAROUND=1
- fingerterm: Update to upstream and drop patch, use LiberationMono font
- funyahoo-plusplus: Bump SRCREV
- https-everywhere: Bump SRCREV
- hunspell-dictionaries: Update to latest version
- imaccountvalidator, imlibpurpleservice: Drop unsupported protocols
- initramfs-boot-android: add A/B partition support, boot into built-in recovery when no skip_initramfs, get Halium’s init script from GitHub, improve panic scenario in init.sh, use /userdata instead of /android/userdata, Various fixes to init.sh
- kf5bluezqt-mer: fix package content with empty QT_DIR_NAME
- libconnman-qt5: fix initial value of “connected” property
- libhybris, qtbase: don’t use += together with _append
- libhybris: Bump SRCREV, Set –enable-arch=arm64 for aarch64, Drop –with-default-hybris-ld-library-path and bump SRCREV
- libpbnjson: use Unix Makefils OECMAKE_GENERATOR
- lsb: fix luneos-version content
- luna-(web)appmanager: use /etc/luna-next/qtwebengine.conf
- luna-init, luna-sysmgr: Bump SRCREV and adjust file installs
- luna-init: Fix incorrect {, Install CustomerCareNumber.txt and cust-preferences.txt
- luna-prefs-data: Bump PV to be in sync with luna-prefs
- luna-sysmgr: Cleanup recipe
- luna-sysmgr-conf, nyx-modules: fix rosy values, Add initial files for athene and onyx target, Cleanup recipe and fixup defaultPreferences-platform.txt
- luna-universalsearchmgr: inherit webos_systemd
- luna-webappmanager: bump SRCREV
- luneos.inc, connman: Build & deploy VPN plugins
- luneos: inherit remove-libtool
- luneos: update SANITY_TESTED_DISTROS
- luneos-dev-image: tell Halium to mount rootfs rw
- luneos-emulator-appliance: update a bit
- luneos-features, connman: Add support for NFC using neard
- luneui-example-image: add few more packages, add more packages for testing, add vboxguestdrivers, v86d, add very small (fast to build) test image
- maliit-framework-qt5: set XDG_RUNTIME_DIR in conf file
- meta*: enable gbm
- meta-webos-ports: Add configuration files for Tissot, Update classes with info from webOS OSE
- mido, tissot: Fix path for CHARGER_AC_SYSFS_PATH
- mido: Initial configuration files
- mobile-broadband-provider-info: Bump SRCREV
- mojomail: bump SRCREV to fix build with boost-1.67.0, Switch back to webOS-ports/master branch
- nemo-qml-plugin-dbus: Update to latest version from upstream, fix package content with empty QT_DIR_NAME
- node-sqlite3: Bump version
- nyx-conf: do not let keys module watch over the touchpanel
- nyx-modules: Fix devices names in cmake files
- ofono: Update to latest version from upstream and enable Python 3 tests
- onyx: Enable power button
- packagegroup-luneos-development: include QML settings app
- packagegroup-luneos-extended: add android-kernel-bootimg,
- Add qtconnectivity, Add WIP targets and more documentation,
- Build bluez5 for all targets, include libpci for qemux86, move android-kernel-bootimg
- phonesim: Fix build with empty QT_DIR_NAME, refresh patches with devtool, update to latest revision from git
- pidgin-sipe: backport a patch to fix build with gcc8
- pulseaudio-distro-conf: Add support for Xiaomi A1 (tissot), Add webos-system.pa for mido target
- pulseaudio-modules-droid: bump to 10.0.73, refresh patches with devtool, remove tenderloin CFLAGS
- purple-skypeweb: Bump SRCREV
- python-tz-native: Update to 2017.2, Fix typo in SRC_URI
- qt5: upgrade to 5.11, upgrade to 5.11.1
- qt5-qpa-hwcomposer-plugin: fix package content with empty QT_DIR_NAME, hwcomposer_backend.h: Fix cast from ‘void*’ to ‘unsigned int’, remove tenderloin CFLAGS
- qtbase: Add patch to fix quirks with newer Adreno GPU’s, refresh patches, remove TLS patch on Halium 7.1 targets, temporary fix for SIGBUS crash on Android devices
- qtlocation: refresh patch
- qtscenegraph-adaptation: Bump SRCREV
- qtsensors-sensorfw-plugin: fix build with empty QT_DIR_NAME
- qtvideo-node: fix package content with empty QT_DIR_NAME
- qtwayland: add qwayland-server-surface-extension.h, wayland-surface-extension-server-protocol.h to sync.profile, bring QWaylandExtendedSurface back for luna-next, drop patch applied in 5.9.3, refresh patches for 5.11.2
- qtwebengine: add libpci to RDEPENDS, Drop patch for libEGL and libGLES2, fix filename in SRC_URI, Fix patch for additionalFeatures, refresh patches, Remove PalmServiceBridge, replace EXTRA_QMAKEVARS_CONFIGURE with PACKAGECONFIG, squash a few of chromium patches for easier maintenance
- recipes: drop unnecessary FILES_${PN}-dbg variables, use oe.utils.conditional instead of deprecated base_conditional
- sensorfw: Bump SRCREV and drop patches now merged upstream
- voicecall: Update to latest version from upstream
- webos-systemd-services: Drop installation of luna universalsearchmgr.service
- android-headers: Add headers for Halium-7.1, common recipe for Halium-5.1 headers, make it possible to tweak android-config.h per machine, Use Halium Headers
- android-headers-halium: set preferred version
- android-headers-tenderloin: fix patches to match Halium’s
- android-kernel-bootimg: dedicated recipe for creating boot.img, minimal support for A/B partitions
- android-system: Add missing groups, also mount /persist when it exists, cleanup old hal-hybris overlay code, don’t manage ramdisk unpacking, fix lifecycle of lxc container, Remove installation of non-existing files, simplify usage of Halium, start sensorfwd after android container, use pre-start.sh from Halium, wait a bit for the sensors to be ready
- android-system-image: use system.img directly, Change wop into luneos, convert the sparse image if needed, create /userdata, Update halium bits to halium version numbers
- base-files: use system.img directly
- android-tools: remove, since now in meta-oe
- base-files,android-system: Android partitions are now mounted by Halium’s initrd
- base-files: add /system/lib64 in LD_LIBRARY_PATH
- hammerhead, mako: Add NFC as machine feature
  Include android-kernel-bootimg for each MACHINE that needs it
- initramfs-android-image: make it possible to add content
- libhybris: provide also virtual/mesa and set PREFERRED_PROVIDER for all android devices
- linux-lg-{mako,hammerhead},linux-hp-tenderloin: backport 2 changes to fix build with gcc8
- mako, hammerhead: Use upstream kernels which now have our patches included
- mako: Fix the kernel build
- meta-*: set PREFERRED_PROVIDER for libgl and libgbm for all android devices
- meta-{asus,hp,huawei,lg,motorola,oneplus,xiaomi}: remove fstab overload
- meta-android: initramfs-android-recovery: add inc, remove leftover from android-tools removal
- meta-hp: migrate tenderloin to use Halium’s init
- meta-oneplus: Fixes for onyx target to make build work
- meta-smartphone: Add meta-huawei layer with Angler target,
- udev-extraconf: Uniform naming scheme for device udev rules and update udev rules
- meta-xiaomi: add initial support for rosy (Redmi 5), Get image for Tissot building, Initial work for Xiaomi A1 (tissot), mido fix persist partition number in fstab, mido use correct wlan module name, tissot: add initramfs-android-recovery, tissot: enable permissive SELinux, tissot: ignore other parameters from bootloader, tissot: switch to cm-14.1 kernel to fix wifi
- Migrate LuneOS targeted machines to using android-kernel-image
- systemd-machine-units: fix bluetooth for hammerhead, fix bluetooth for mako

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/doppio/) to get started. Tenderloin, Mako, Hammerhead and Tissot remain our focus for now, but the emulator, Mido & Rosy work too.

*Please note that in order to use the latest stable builds Nexus 4 (Mako) and Nexus 5 (Hammerhead) you need to flash the CM 12.1 images first using CWM/TWRP. In order to do so, you might be required to do a “factory reset” or at least “wipe cache”. CWM/TWRP will indicate when this is needed. After successfully flashing CM 12.1, make sure to boot it at least once before going back to CWM/TWRP to flash the latest LuneOS image! We have provided links to CM 12.1 for these 3 images on our device pages below.*

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Nexus 5 (Hammerhead)](http://webos-ports.org/wiki/Install_LuneOS_for_Hammerhead) and [Emulator](http://webos-ports.org/wiki/Emulator)are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](https://forums.webosnation.com/luneos/332313-pivotce-luneos-november-stable-release-doppio.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

We will see you shortly again with a new release!

Picture Credit: [Chevanon](https://pixnio.com/food-and-drink/coffee/hot-espresso-coffee-machine-coffee-mugs-beverage-caffeine). Cropped & flipped. Text added.
