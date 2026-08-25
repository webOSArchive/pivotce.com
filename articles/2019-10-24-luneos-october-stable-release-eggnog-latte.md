---
title: 'LuneOS October Stable release: Eggnog Latte'
date: 2019-10-24 06:28:03 UTC
modified: 2024-01-25 22:27:12 UTC
author: webosports
author_slug: webosports
categories: [News]
tags: [Developer]
slug: luneos-october-stable-release-eggnog-latte
source_url: https://pivotce.com/2019/10/24/luneos-october-stable-release-eggnog-latte/
wordpress_id: 4477
featured_image: ../images/files/2019/06/LuneOS_eggnog-latte.jpg
featured_image_source: https://pivotce.com/files/2019/06/LuneOS_eggnog-latte.jpg
excerpt: 'Happy Halloween! The long wait is finally over #LuneOS and #webOS fans! We’re back with a new release called “Eggnog Latte” which is a milestone in terms of developments and…'
---

# LuneOS October Stable release: Eggnog Latte

Happy Halloween! The long wait is finally over #LuneOS and #webOS fans! We’re back with a new release called “Eggnog Latte” which is a milestone in terms of developments and paves the way forward!

So you’re wondering what we’ve been up to since our previous stable release at the end of last year?

We have done many major upgrades to a large number of components of our stack being:

- Migration of Open webOS to webOS OSE components.

  We are [almost half way there](https://webos-ports.org/wiki/LuneOS-webOS-OSE_Migration_Status) in terms of the migration of old [Open webOS components](https://github.com/openwebos/) to their [webOS OSE replacements](https://github.com/webosose).

  This was a monumental task due to the fact that webOS OSE code was released without any history. So every component needed to be analyzed to understand what was changed in the years of development inside of LG Electronics. Our custom changes needed to be re-assessed and re-implemented into the new components where applicable. A change of direction in certain aspects in terms of architecture made the whole exercise even more complicated. We do however believe that we’re in a good state now in terms of migration. There are still quite some components to migrate and we’ll get through that in the next releases.
- Qt:

  We migrated from Qt 5.11.3 to Qt 5.12.5 which included an update for Chromium from 65 to 69 amongst other improvements.
- Yocto upgrade:

  We upgraded from the no longer supported Yocto Pyro release, via the intermediary Rocko, Sumo and Thud releases to the latest Yocto release called Warrior.

We have been working closely together with the Halium, Mer and PostMarketOS projects and have made further integrations between LuneOS and the various projects reducing duplication between the projects and using a single source where possible. This all to be more easily integrated, and to facilitate ports to newer and more devices. We have also worked on support for devices which use a mainline kernel instead of an Android based kernel. [As you might have seen, we have been working on support for the Pinephone which uses a mainline kernel](https://www.youtube.com/watch?v=G9lbXE_wWpQ). We also have been testing with the Nexus 5 (hammerhead) using a mainline kernel. All our setup has now been adjusted so we can work with both Android based targets and kernels as well as mainline kernels.

LG has a very clear vision in mind for webOS OSE as can be read on [their blog posts](https://www.webosose.org/blog/). Since the initial release of webOS OSE 1.0 in March last year, there has been a total of 11 releases of webOS OSE already with a lot of improvements and added features added with each release. This month LG has released [webOS OSE 2.0.0](https://www.webosose.org/about/release-notes/webos-ose-2-0-0-release-notes/) with a lot of new features and also [a new roadmap](https://www.webosose.org/about/roadmap/roadmap/).

The following items on our to-do list will be where we focus next:

- Migration of remaining Open webOS components to the newer webOS OSE components and assess where further synergies could be achieved.
- Migrate to Yocto Zeus release.
- Update to Qt 5.13.
- Migrate Nexus 5 (hammerhead) to use mainline kernel.
- Finalize port for Pinephone.
- Work on support for Halium 8/9/10 in order to support newer targets.
- Messaging improvements.
- Camera improvements.
- Fix known issues on the various targets.
- Bring back official support for Touchpad 4G (current build works on Touchpad 4G but only WiFi).

**Known issues:**

- Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.
- Telephony not working on the Xiaomi Android 7 based targets. We have found the root cause, but haven’t been able to solve it yet.
- Virtual Keyboard sometimes randomly doesn’t appear.

### **Changelog**

**Applications:**

- Preware IPKG Service: use postinst_ontarget
- Tweaks: Fix for LS2 from webOS OSE
- Camera: Remove RDEPEND on libhybris
- FirstUse: Fix for LS2 from webOS OSE
- Maps: Fix Google API calls
- Messwerk: Add testing app for various sensors
- Phone: Fix calling
- Settings: Fix displaying of device information, fix compatibility with LS2 from webOS OSE
- Update: Fix parsing of JSON files with update information.
- CDav: Fix issues after migration to webOS OSE

**User Interface:**

- Various minor fixes for status bar & indicators in emulators

**System Level:**

- Yocto upgrade from 2.3 Pyro to 2.7 Warrior
- Qt upgrade from 5.11 to 5.12
- Pinephone support added
- activitymanager: RDEPENDS on bootd
- add meta-qt5-compat layer
- Add VIRTUAL-RUNTIME_android-initramfs-scripts variable in machines conf
- alsa-lib: update the patches for 1.1.8
- alsa-utils: Rename bbappend to match new version from oe-core
- anbox, ashmem, binder: bump SRCREV; add COMPATIBLE_MACHINE restriction; Add elfutils to DEPENDS to solve QA issue; Add some RDEPENDS,RRECOMMENDS; fix build with boost 1.71.1; fix parallel build issue; restrict COMPATIBLE_MACHINE a bit more
- anbox-data: add recipe for retrieving android image
- android-headers: Add headers for Halium-7.1; common recipe for Halium-5.1 headers; make it possible to tweak android-config.h per machine; use Halium headers
- android-headers-halium: set preferred version
- android-headers-tenderloin: use API 22, patched to match tenderloin specific content; fix patches to match Halium’s
- android-kernel-bootimg: append DTB when specified; dedicated recipe for creating boot.img; minimal support for A/B partitions
- android-property-service, mtp-server, pulseaudio-modules-droid, qtubuntu-camera, qtvideo-node, qt5-qpa-hwcomposer-plugin, qtscenegraph-adaptation, qtsensors-sensorfw-plugin sensorfw, nyx-modules-hybris, org.webosports.app.camera: restrict to halium MACHINES; add dependency on virtual/android-headers
- android-system: Add missing groups; also mount /persist when it exists; cleanup old hal-hybris overlay code; don’t manage ramdisk unpacking; fix lifecycle of lxc container; only start after main partitions are mounted; Remove installation of non-existing files; simplify usage of Halium; start sensorfwd after android container; use pre-start.sh from Halium; wait a bit for the sensors to be ready
- android-system-image-*: bump to 20180311 Halium build; skip already-stripped QA android-system-image,base-files: use system.img directly android-system-image: Add symbolic link for wifi; Bump Halium images; bump mako,tenderloin,hammerhead; Change wop into luneos; convert the sparse image if needed; create /userdata; make \”symbols\” directory optional; Update halium bits to halium version numbers android-system-image-athene,onyx,mido,angler: bump PV android-system-image-mako: fix install; fix install script; fix typo android-system-image-rosy: use build from webos-ports android-system-image-tenderloin: bump PV; Fix checksums; Update Android image; Use a Haloum 5.1 based Android build android-system-image-tissot: bump PV; Bump PV to fix adb; Bump PV to kill qseeproxydaemon on Android side; bump to 20180302-18 android-tools: move the changes to meta-oe android-tools: remove android-tools-conf: provide whole android-gadget-setup instead of patching it in do_install; use backported recipe angler, hammerhead, mako, athene, onyx, mido, rosy, tissot: stop building ext4 images by default angler,athene,onyx,mako,hammerhead: systemd-machine-units: add rfkill unblock wifi app-services, configurator: Bump SRCREV; fix LS2 for webOS-OSE ashmem, binder: move udev rules to kernel-module-*-linux package and empty PN
- base-files,android-system: Android partitions are now mounted by Halium’s initrd
- base-files: add /system/lib64 in LD_LIBRARY_PATH
- bootd: introduce recipe from webOS-OSE; Fix systemd service file
- busybox: also build telnetd module; also create by-label entries with mdev; mdev: use /dev/disk/by-partlabel instead of by-partname; mdev-partname.sh, mdev.conf: drop trailing spaces; mdev-partname.sh: remove probablly unnecessary ACTION assignment; mdev-partname.sh: use 4 spaces for indentation instead of mix of tabs and spaces; provide busybox-mdev with custom partname symlinks; use 4 spaces for indentation instead of mix of tabs and spaces and BPN in FILESEXTRAPATHS
- cmake-modules-webos-native: Add back PV; add missing quote; Bump PV
- com.webos.service.pdm: Remove inherit webos_machine_impl_dep
- configurator: Move to webOS OSE version; Bump SRCREV
- connman: move PACKAGECONFIG modification to .bbappend, remove dependency on xl2tp in signature; refresh patches to apply cleanly; update to v1.36
- cpushareholder-stub, luna-sysmgr-ipc-messages, luna-webkit-api, rdx-utils-stub: inherit allarch before webos_cmake
- cpushareholder-stub: Migrate from OWO to OSE
- db8, filecache: Bump SRCREV, app-services: Bump SRCREV and cleanup recipe
- db8, nyx-modules: Minor fixes after OSE rebase
- db8: Add back dropped PV; Bump SRCREV and drop patch now merged in repo; cleanup a bit; fix db8-tests runtime depends; fix LS2 for webOS-OSE; Update to latest revision and remove references to com.webos.service.attachedstoragemanager
- dbus-cpp, process-cpp, properties-cpp: Switch to GitHub & latest commits
- dbus-cpp: fix compatiblity with boost 1.66.0
- defaulttunes.inc: return accidentally dropped last line; use armv8a-crc-crypto for both raspberrypi[34]-64;use cortexa8thf-neon for currently supported 32bit arm MACHINEs;use different TUNE_PKGARCH_64 for raspberrypi3-64 MACHINE
- directfb: Drop .bbappend
- distro: luneos: switch release name to Eggnog Latte
- downloadmanager: Remove recipe
- event-monitor, event-monitor-network: Add recipes from OSE
- exiv2: Update to 0.27.1
- extra-cmake-modules: Bump to latest from upstream
- filecache: Bump SRCREV
- Fix meson bbappend
- Fixup line endings
- funyahoo-plusplus: Update to latest from upstream
- Further work on webOS OSE migration; Further changes for webOS OSE; Further migration for webOS OSE
- gcc: restore gcc-7.3 from Yocto 2.6 Thud
- geoclue: backport gtk-doc.bbclass changes from Yocto 2.8 Zeus to make GTKDOC_MESON_OPTION work in Yocto 2.7 Warrior; Fix typo;fix unknown-configure-option QA issue; Rename .bbappend to be generic; Update to 2.5.3; use backported recipe; Add to meta-webos-ports for fixes & upgrade
- glib-2.0: Rename bbappend to match new version from oe-core; update 0001-gdbus-codegen-replace-plus-also-with-underscore.patch to apply on 2.58.0 version; update patch to apply on 2.54.2 version; add work around for broken ld-2.29.so when gold is used; drop bbappend; export LDFLAGS
- glm: use 0.9.9.3 version from meta-oe
- glmark2: disable wayland-gles2
- GnuTLS: Fix missing system trust
- gstreamer1.0-plugins-base: disable egl
- gtest: don’t rdepend on ${PN} from ${PN}-dev; export LDFLAGS
- hammerhead kernel: delay wifi init
- hammerhead, mako, tenderloin: Use Halium image built with Ports repos; use WOP builds of Halium
- hammerhead, mako: Add NFC as machine feature
- hammerhead.conf: use initramfs-scripts-halium
- hammerhead: temporarily disable gobject introspection
- https-everywhere: Update to latest from upstream
- hunspell-dictionaries: Update to latest from upstream; use backported recipe
- icyque: Add recipe
- Ignore generated pycache directory
- iio-sensor-proxy: introduce recipe
- imaccountvalidator, activitymanager, db8, filecache, sleepd, luna-service2: Bump SRCREV
- imaccountvalidator, imlibpurpleservice: Add icyque plugin
- imlibpurpleservice, org.webosports.service.messaging, webos-telephonyd, app-services, core-apps, nodejs-module-webos-sysbus: Bump SRCREV
- Include android-kernel-bootimg for each MACHINE that needs it
- Initial work for webOS OSE migration
- initramfs-android-image: make it possible to add content; make sure that ANDROID_EXTRA_INITRAMFS_IMAGE_INSTALL is expanded
- initramfs-android-recovery-tissot: skip file-rdeps QA as well
- initramfs-boot-android: cosmetics; disable busybox extreme symlink checks; fix image identification for rootfs on partition; import Fix-userdata-mount-options.patch from meta-hp; init.sh: be less verbose for initial user data copy; mount /dev/pts for cases when enable_adb is used; put .firstboot_done in a rw folder; reset uevent_help when stopping mdev; split halium and generic version; use mdev instead of udev
- initramfs-boot-android: fix tenderloin’s boot; Move initrd RDEPENDS from ANDROID_EXTRA_INITRAMFS_IMAGE_INSTALL to initramfs-boot-android recipe; put .firstboot_done in a rw folder; split halium and generic version; tenderloin: mount /boot as ro; tenderloin: use correct folder for media data
- initramfs-scripts-android: improve init scripts; switch from RNDIS to CDC-ECM
- initramfs-scripts-halium: move Fix-userdata-mount-options.patch to the right directory; specify needs through RDEPENDS
- initrdscripts: fix tenderloin initial data (wallpaper)
- jemalloc: Switch to OSE repo
- kernel.bbclass: drop backported bbclass; remove backported bbclass; import from oe-core/pyro and backport one fix from oe-core/rocko
- kernel: tenderloin, mako, hammerhead, onyx bump SRCREV for GCC8
- kernel_android, android-kernel-bootimg: use pkg_postinst_ontarget
- kernel_android.bbclass: fix path to the KERNEL_DEVICETREE; use ${KERNEL_PACKAGE_NAME}-image instead of kernel-image
- kernel_android: update for new KERNEL_* variables from oe-core; use the bbclass again
- keymanager: bump SRCREV
- kf5bluezqt-mer: set QT.BluezQt.module to fix compatibility with Qt 5.12
- layer.conf: Update to warrior release name series
- leveldb: move bbappend to the matching directory
- leveldb-tl: downgrade to gcc-4.7 branch; provide native version
- libbson: Bump to latest upstream release
- libcamera: introduce recipe
- libdrm: add vboxvideo to tested modules; update the patch to apply for 2.4.96
- libglibutil: fix LICENSE and LIC_FILES_CHKSUM
- libhybris, wayland: use wayland-egl from libhybris again
- libhybris: bump SRCREV and resolve the review comments; fix build with glibc-2.26; fix mido build flags; fix tenderloin build flags; provide also virtual/mesa and set PREFERRED_PROVIDER for all android devices; refresh patch; remove the already applied patch from SRC_URI; restrict COMPATIBLE_MACHINE to halium MACHINEs; use older SRCREV for tenderloin; don’t install wayland-egl; drop SRCREV
- libpalmsocket: fix build with openssl-1.1.1
- libpbnjson: restore PV and OECMAKE_GENERATOR fix
- libpng: Bump to 1.6.37
- librolegen: Add DEPENDS; Switch to OSE version + patches
- libsandbox: Migrate from OWO to OSE
- libsensmon: blacklist due to newer vala incompatibility
- libshr-glib: blacklist because of random failures
- libvpx: enable thumb to work around issue with -halium appended to TUNE_PKGARCH
- linunx-lg-mako: bump SRCREV
- linux-*: don’t use ANDROID_BOOTIMG_CMDLINE for built-in kernel cmdline linux-{oneplus-onyx,lg-mako}: fix branch parameter linux-hp-tenderloin: bump SRCREV; use a 3.4 kernel linux-lg-{mako,hammerhead},linux-hp-tenderloin: backport 2 changes to fix build with gcc8 linux-lg-hammerhead: bump SRCREV; fix some minor defconfig values linux-lg-mako: send patches upstream and bump SRCREV; switch to old ubp-5.1 branch with just 1 fix for gcc-8 from cm-14.1 branch linux-oneplus-onyx: switch to old cm-14.1-los branch with just 1 fix for gcc-8 from luneos/cm-14.1-wip branch linux-xiaomi-rosy: bump SRCREV linux-xiaomi-tissot: bump SRCREV linux-yocto: add own defconfig; backport 5.0 from master and switch from linux-yocto-dev; drop backported fixes for compatibility with older Yocto; enable few more drm drivers; squashfs: add squash kernel module for anbox; use own virtio.cfg and reinclude kernel-module-virtio-gpu as a module linux-yocto-dev: add bbappend also for -dev version; enable vboxguest in the kernel and blacklist vboxguestdrivers again lsb: rename bbappend to match any version luna-applauncher: JustType: use a relative margin for main field (got broken after Qt 5.12.5 upgrade) luna-appmanager: Bump SRCREV; fix LS2 for webOS-OSE luna-downloadmgr, applicationinstallerutility: Add recipes luna-downloadmgr: Drop MACHINE specific configuration luna-next: Bump SRCREV; LS2 fix for webOS-OSE luna-next-cardshell: bump SRCREV; merge webosose branch to master luna-next-conf: fix possible conflict between evdevtouch and evdevkeyboard; fix VBoxTouch parameters for qemu; rosy: give input devices to evdevkeyboard; update VBoxTouch params and enable input and cursor; use drm+eglfs_kms for qemux86*
- luna-prefs-data.bb: Fix Lune OS name to LuneOS
- luna-qml-launcher: fix LS2 for webOS-OSE
- luna-service2: bump SRCREV; re-enable default LS2 security policy; remove webos_machine_impl_dep inherit imported from OSE
- luna-service2-security-conf: Switch to own fork
- luna-sysmgr: explicitely put RDEPENDS on powerd; Fix branch; fix LS2 for webOS-OSE
- luna-sysmgr-common: Bump SRCREV
- luna-sysmgr-conf, nyx-conf, nyx-modules, luna-next-conf: add support for raspberrypi4(-64)
- luna-sysservice, nodejs-module-webos-sysbus, nyx-utils, luna-service2, nyx-lib, pmloglib, pmloglib-private: Bump SRCREV
- luna-sysservice: Add back dropped PV; bump SRCREV; fix LS2 for webOS-OSE
- luna-systemui: Bump SRCREV
- luna-webappmanager: bump SRCREV; fix LS2 for webOS-OSE
- luneos.inc: drop kernel-module-virtio-gpu; enable image-buildinfo; exclude DATETIME from IMAGE_NAME, KERNEL_IMAGE_BASE_NAME, MODULE_IMAGE_BASE_NAME vardeps; include all default WARN_QA in ERROR_QA; replace uvesafb with vboxvideo; set WEBOS_TARGET_MACHINE_IMPL only in webos_machine_impl_dep; simplify PREMIRROR configuration; use linux-yocto-dev also for qemux86-64; use new oe-core variable IMAGE_VERSION_SUFFIX
- luneos: add rpi-sdimg.gz IMAGE_FSTYPE; reinclude luneos-recipe-blacklist-world.inc and update it for Yocto 2.7 Warrior; use linux-yocto-dev for qemux86
- luneos_image.bbclass: remove the webos_swap_hook function
- luneos-{package,emulator-appliance}.inc: remove extra dash in filenames
- luneos-components: bump SRCREV and switch to qt-5.12 branch
- luneos-dev-image, luneui-example-image: drop mesa
- luneos-dev-image: add libdrm-tests; add more packages for testing
- luneos-emulator.ovf: move to qemux86 subdirectory and restrict to qemux86*; refresh to ovf-2.0 format with VirtualBox-6.0.8; update OSType for qemux86-64 luneos-emulator-appliance.inc: include ${IMAGE_NAME_SUFFIX} in source VMDK filename; use pigz-native instead of zip-native; switch from default VBoxVGA to VBoxSVGA luneos-image: add WKS with syslinux config file without serial luneos-package.inc: bump android-update-package SRCREV; fix SRCREV; include ${IMAGE_NAME_SUFFIX} in source rootfs filename; work around tar being killed by OOMK; work around tar being killed by OOMK even harder luneos-preferred-providers.inc: remove VIRTUAL-RUNTIME_bash; use busybox as a provider for bash and stat luneos-preferred-versions.inc: downgrade gcc from default 8 to 7 luneos-recipe-blacklist-world.inc: blacklist remmina; use weak assignment luneui-example: add emulator-appliance and android package images luneui-example-image, packagegroup-luneos-extended: add Anbox for qemux86-64 luneui-example-image,luneos-dev-image: include glmark2 only for qemuall lxc: ignore stringop-overflow= errors with gcc8 make, hammerhead, tenderloin: use mesa-gl as virtual/mesa provider; use kernel sources from shr-distribution/linux.git and fix build with gcc-7; use our Halium image mako, hammerhead: Use upstream kernels which now have our patches included mako: Fix the kernel build maliit-framework-qt5: set QT_QPA_PLATFORM=wayland mediaindexer: Bump SRCREV; Switch back to master branch mesa: backport 19.0.5 and mesa-demos 8.4.0 from oe-core; drop backported PROVIDES; enable gallium only for target builds; update old recipe; use latest mesa from oe-core mesa-gl: remove ${includedir}/KHR/khrplatform.h when using libhybris meson: override 0003_native-bindir patch with a fixed version; drop backported fix, now in oe-core revision we’re using messaging-accounts: Bump SRCREV meta-*: add LAYERSERIES_COMPAT to layer.conf files
- meta-*: add LAYERSERIES_COMPAT to layer.conf files; set PREFERRED_PROVIDER for libgl and libgbm for all android devices meta-{asus,hp,huawei,lg,motorola,oneplus,xiaomi}: remove fstab overload meta-acer, meta-asus, meta-aurora, meta-fso, meta-geeksphone, meta-htc, meta-nokia meta-openmoko, meta-osmocombb, meta-palm, meta-samsung, meta-shr-distro, meta-shr: Remove unsupported layers meta-android, meta-hp: respect IMAGE_NAME_SUFFIX variable meta-android: add FREESMARTPHONE_GIT; initramfs-android-recovery: add inc; remove leftover from android-tools removal; use separate PACKAGE_DIR for Halium-based packages meta-android-halium.inc: add halium OVERRIDE; blacklist virglrenderer, cogl-1.0, clutter-1.0, mx-1.0, clutter-gst-3.0, clutter-gtk-1.0 meta-hp: initramfs-boot-android: move Fix-userdata-mount-options.patch to meta-webos-ports; migrate tenderloin to use Halium’s init meta-luneos-backports-2.8: add layer for backports from Yocto 2.8 Zeus; Add pidgin 2.13 meta-motorola: Athene, use our own fork for now.; Fixes for athene target to make build work; Initial work for athene target meta-oneplus: Fixes for onyx target to make build work; Initial work on layer; linux-oneplus-onyx: Use herrie82 branch pending upstream merge; Update kernel for onyx (OnePlus X) meta-qt5-compat: remove meta-shr, meta-fso: remove blacklisted recipes meta-smartphone: Add meta-huawei layer with Angler target; udev-extraconf: Uniform naming scheme for device udev rules and update udev rules meta-webos-ports: Add pinephone machine meta-xiaomi: add initial support for rosy (Redmi 5); Further updates to make things work; Get image for Tissot building; Initial work for Xiaomi A1 (tissot); Initial work on layer; linux-xiaomi-mido: Fix incorrect RAM_BASE addresses; Mido enable WLAN as module; mido fix persist partition number in fstab; mido use correct wlan module name; rosy minor fixes; tissot: add initramfs-android-recovery; tissot: enable permissive SELinux; tissot: ignore other parameters from bootloader; tissot: switch to cm-14.1 kernel to fix wifi Migrate LuneOS targeted machines to using android-kernel-image mmsd: Bump SRCREV mobile-broadband-provider-info: Bump SRCREV module-base.bbclass: import from oe-core/pyro and backport the fix to support newer kernels; refresh from rocko module-base: remove backported bbclass mojo: Switch to webOS-ports/webOS-OSE branches mojomail, pmcertificatemgr: bump SRCREV mojoservicelauncher: bump SRCREV; temporary drop nodejs-module-webos-dynaload and nodejs-module-webos-sysbus mpeg2dec: ignore textrel QA issue in libmpeg2 mtp-server: bump SRCREV; fix build with glog-0.3.5 nemo-qml-plugin-dbus: Bump to latest from upstream node-gyp-native: upgrade to 4.0.0+git; fix branch parameter nodejs-enyo-dev-native: Bump SRCREV nodejs-module-webos-{dynaload,sysbus}: bump SRCREV nodejs-module-webos-dynaload: Move to OSE version nodejs-module-webos-pmlog: Add fix from upstream OSE nodejs-module-webos-service: Add recipe from OSE nodejs-module-webos-sysbus: Bump SRCREV; Fix installation of role files.; Fix work directory; Migrate to webOS OSE version; restore old security schema novacomd: Remove upstart init script; Switch to OSE version ntp: Add an empty ntp-kod file numptyphysics: fix file-rdeps QA nyx-conf: add pinephone power key config nyx-modules, nyx-conf: Fix pinephone setup nyx-modules: bump SRCREV; Changes for new nyx modules from OSE;’disable security and security2 modules and return to the image; fix build for tenderloin; fix rosy’s cmake; fixes for webOS-OSE rebase; qemux86(-64) update copyright and specify modules to build; reintroduce nyx-modules-hybris for Halium based targets; toro & toroplus: Update copyright & hybris modules; Update copyright nyx-modules-hybris: bump SRCREV for nyx-lib compatibility fixes ofono: Drop patches that are no longer used.; Update to latest from Mer; use more recent version omhacks: blacklist openssl*: update openssl.cnf u-a configuration
- openssl, gtest, leveldb: drop EXTENDPRAUTO
- openssl10: remove the bbappend and blacklist instead
- opkg: Rename bbappend to match new version from oe-core
- packagegroup: temoporary drop certmgrd, pmcertificatemgr, mojomail-imap, mojomail-pop, mojomail-smtp, nyx-modules
- packagegroup-luneos-extended: add messwerk app; Drop downloadmanager in favor of luna-downloadmgr; include DISTRO_EXTRA_RDEPENDS to install necessary kernel modules; include rng-tools for qemu*; re-enable nyx-modules-hybris; replace wireless-tools with iw; Add event-monitor & event-monitor-network
- PATCH] athene, mido, onyx: Fix display size and add ANDROID_HEADERS_DEFINES
- pdm & pdm-plugin: Add various bits to build & include in images.
- phonesim: Bump to 1.21
- pidgin, leveldb-tl, extra-cmake-modules, pmloglib-private: don’t rdepend on ${PN} from ${PN}-dev
- pidgin: Make bbappend version independent; remove the backported recipes; update purple-OE-branding-25.patch to apply cleanly; Update to 2.13; use backported recipes
- pidgin-sipe: Update to latest release from upstream
- pmloglib: Add back PV
- pmloglib-private: Add back PV
- powerstat: Update to latest upstream
- properties-cpp: add sha265sum, fix runtime dependencies
- pulseaudio: rename bbappend to apply on new version from oe-core; update patches to apply on 11.1 version
- pulseaudio-modules-droid: adapt folders for PulseAudio 11.1; bump SRCREV for 12.2 compatibility; update PULSEAUDIO_VERSION to 12.2
- purple-skypeweb: Update to latest release from upstream
- python-tz: Bump to 2019.1
- qemu: don’t enable spice for target; drop virglrenderer from target qemu as well; enable sdl and virtfs as well; enable virglrenderer spice libusb usb-redir gtk+
- qemux86: use wic.vmdk
- qt5: refresh the patches for 5.12.3 version
- qt5-plugin-generic-vboxtouch: bump SRCREV; switch to new version from Tofee
- qt5-qpa-hwcomposer-plugin: bump SRCREV and fix build; fix compatibility with qtbase 5.12; remove unneeded patch
- qtbase: allow to easily select different QPA; update PACKAGECONFIG xkbcommon-evdev -> xkbcommon
- qtlocation-luneos-plugin: replace qtlocation patch; Update plugins dir and PV
- qtvideo-node, org.webosports.app.camera: fix PV
- qtwayland: don’t use wayland-brcm; drop drm-egl-server and libhybris-egl-server PACKAGECONFIGs; fix QWaylandShellPrivate inheritance; Fix window properties; refresh patches for 5.12; fix the last patch filename in SRC_URI; update patches for 5.12.5
- qtwebengine: enable wayland-brcm for rpi, drm-egl-server for qemuall and libhybris-egl-server for the rest; fix 0001-WebContents-provide-additional-features-from-window..patch; fix patch directory; fix Sync call patch; refresh patches for 5.12; refresh patches for 5.12.5
- raspberrypi4-64: fix TUNE_PKGARCH_64
- rdxd: Drop stub and add the real thing.; Add missing PROVIDES
- README: update to depend on master branches
- Remove AOL & ICQ protocol plugins
- Revert \”hammerhead: temporarily disable gobject introspection\”
- Revert \”meta-hp: initramfs-boot-android: move Fix-userdata-mount-options.patch to meta-webos-ports\”
- SANITY_TESTED_DISTROS: drop ubuntu-16.04
- sdl2-opengles-test: build only sdl2_opengles2_test for all rpi MACHINEs; Fix typo in license file.; Switch to new repo and update to latest version
- sensorfw: bump SRCREV and make it more generic; fix orientation matrix for pinephone
- serviceinstaller: Switch to OSE version + our patch
- shadow-sysroot: rename bbappend to match new version
- sleepd: add powerd as RDEPENDS
- snappy: import from OSE and add as a dependency to leveldb; use newer 1.1.7 version from meta-oe
- storaged: Add PV
- Switch from branch= to WEBOS_GIT_PARAM_BRANCH
- systemd: disable networkd and resolved.; fix boot for old kernels; fix build without resolved; rebase patches to apply on 237 version; rebase patches to apply on 241; update Disable-ProtectHome-and-ProtectSystem-for-old-kernel.patch to apply on 239 version; Update mmc patch; update persistent-storage-rule-mmc-partname.patch to apply on 234 version
- systemd-conf: disable key handling in logind.conf
- systemd-machine-units: regroup xiaomi identical service files; fix bluetooth for hammerhead; fix bluetooth for mako; mido: fix Bluetooth; rosy: fix Bluetooth; rosy: fix wlan module loading; tissot: fix Bluetooth
- systemd-serialgetty: disable SERIAL_CONSOLES on LuneOS’s qemu; drop weird bbappend
- tzdata: rename bbappend to apply on renamed recipe
- ubx-utils: fix file-rdeps QA
- udev-extraconf: override automount.rules with empty rules file; tissot, rosy: add touchscreen0 rule
- unused: remove long unused recipes and bbclasses
- uriparser: Upgrade to 0.9.3
- Various components: Move back to webOS-ports fork
- Various fixes for systemd
- vboxguestdrivers: backport 5.2.22 from meta-oe; unblacklist but install only vboxguest and vboxsf modules
- VoiceCall: Bump SRCREV & drop patch; Bump version to latest from upstream and refresh patches; Drop patches since our changes are merged upstream; fix DEVICELOCK handling
- wayland: limit do_install_append only for target
- webos_{lttng,pmlog_config}.bbclass: move to the right layer
- webos_configure_manifest.bbclass, webos_system_bus.bbclass: replace some warnings with notes
- webos_configure_manifest.bbclass: move to the right layer
- webos_nyx_module_provider.bbclass: enable NYXMOD_OW_MSMMTP by default
- webos_test_provider.bbclass: move to meta-luneui
- webos-connman-adapter: bump SRCREV
- webos-initscripts, org.webosports.cdav, app-services, bootd, com.webos.service.pdm, db8, enyo-1.0, mojoservice-framework, mojomail: Bump SRCREV
- webos-initscripts.bb: Fix inherit
- webos-initscripts: don’t include systemd-machine-units in sstate signature; fix startup sequence for webOS-OSE; Fix whitespace issues
- webos-keyboard: fix LS2 for webOS-OSE; Bump SRCREV
- wifi-module-load: fix sleep call in systemd service
- luneos-components: Update Qt version to 5.12.5; Add stub for ieee8021x wifi network

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](http://pivotce.com/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/eggnoglatte/) to get started. Tenderloin, Hammerhead and Tissot remain our focus for now, but the emulators, Mako and Mido work too.

*Please note that in order to use the latest stable builds Nexus 4 (Mako) and Nexus 5 (Hammerhead) you need to flash the CM 12.1 images first using CWM/TWRP. In order to do so, you might be required to do a “factory reset” or at least “wipe cache”. CWM/TWRP will indicate when this is needed. After successfully flashing CM 12.1, make sure to boot it at least once before going back to CWM/TWRP to flash the latest LuneOS image! We have provided links to CM 12.1 for these 3 images on our device pages below.*

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Nexus 5 (Hammerhead)](http://webos-ports.org/wiki/Install_LuneOS_for_Hammerhead) and [Emulator](http://webos-ports.org/wiki/Emulator)are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](https://forums.webosnation.com/luneos/332533-pivotce-luneos-november-stable-release-eggnog-latte.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

We will see you shortly again with a new release!

Picture credit: [pxhere.com](https://pxhere.com/en/photo/1537203)
