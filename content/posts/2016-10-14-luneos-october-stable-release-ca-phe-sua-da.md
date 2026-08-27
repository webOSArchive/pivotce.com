---
title: 'LuneOS October Stable Release: Ca phe sua da'
date: '2016-10-14T20:03:48Z'
lastmod: '2016-12-25T23:48:56Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- Developer
slug: luneos-october-stable-release-ca-phe-sua-da
summary: We’re already back with another stable release, “Cà phê sữa đá” also known as “cafe sua da”! A nice Vietnamese coffee recipe 🙂 For this release we’ve been focusing on…
featured_image: /images/files/2016/10/CaPheSuaDa.jpg
source_url: https://pivotce.com/2016/10/14/luneos-october-stable-release-ca-phe-sua-da/
wordpress_id: 3890
featured_image_source: https://pivotce.com/files/2016/10/CaPheSuaDa.jpg
archived: true
---

We’re already back with another stable release, “Cà phê sữa đá” also known as “cafe sua da”! A nice Vietnamese coffee recipe 🙂 For this release we’ve been focusing on system stability as well as adding new features 🙂

We have worked hard to make sure the startup order of services is correct. We had a lot of errors and warnings in the system logs and many things were not working (properly) on a first boot. It turned out quite some things needed tweaking, so that’s what we did! As a result everything that should work on a first boot, now works as it should 🙂 We did a lot of housekeeping that’s not directly visible to the users, to make sure that the system logs are lot cleaner and don’t provide distractions while debugging issues.

We have also reworked the handling of the cards to become a bit more snappier and we brought back some more features from LunaCE like “[Card Zoom Gestures](http://webos-ports.org/wiki/About_LunaCE#Card_Zoom_Gestures)” and “[Stack Spread Gestures](http://webos-ports.org/wiki/About_LunaCE#Stack_Spread_Gestures)“.

We have also re-arranged the icons in the launcher a bit. Preware can now be found in the “Downloads”-tab, Settings, Tweaks, Testr, C+DAV Sync App and the SDL OpenGL ES test apps can now be found in the “Prefs”-tab.

Many other small items have been fixed as well, see below for more details of all the changes!

**Known issues:**

- Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.
- Focus bug on input fields. You can work around this by hiding the virtual keyboard and pressing the input again.

### **Changelog**

**Applications:**

- Browser (org.webosports.app.browser): Move browser parts used elsewhere as well to LuneOS Components, update Top Level Domain list, don’t set the user agent in the browser itself, but through LuneOS Components instead, dropped Checkbox, reworked browser settings toggles and hooked them up, fixed spelling & fixed vkb toggle button.
- FirstUse (org.webosports.app.firstuse): Fix checkbox & password character the proper way.
- Maps (org.webosports.app.maps): Unify layout of toggle with QML & Enyo 1.
- Messaging-Accounts: Don’t show empty options in UI but maintain them in backend for compatibility.
- Preware (org.webosinternals.preware): Add systemd service file.
- Settings (org.webosports.app.settings): Unify layout of toggle with QML & Enyo 1.
- Testr (org.webosports.app.testr): Adds test of window.webkitRequestFileSystem(), Clarifies success message for webkitRequestFilesystem() test, Changes File API test to write file, and improves error reporting, Unify layout of toggle with QML & Enyo 1, Move things to subfolders for clearer structure, File APIs: added test: delete all, File APIs: tweaked \”write file\” test, to allow for overhead.

**User Interface:**

- luna-next-cardshell: Cleanup: fix some QML interpreter warnings, NotificationArea: fix notification removal, CardView: have a snappier card swiping behavior, CardView: realign the card if the height of the CardView changes, CardView: use a simple Flickable instead of a ListView for card swiping, CardView: fix swipe-down scenario, CardView: keep size bindings when initializing card delegate, added card stack spreading gestures & card zoom.

**System Level:**

- org.webosports.app.tasks: Fix syntax error in com.palm.tasklist.
- mediaindexer: com.palm.media.misc.file: Fix syntax error, mediaindexer.service: Make sure we start only after configurator.
- luna-applauncher: Fix the input not working when multiple lines.
- luneos-components:  Add UserAgent handling to LuneOS Components, Set httpUserAgent in the WebEngineView already, Add stub values for db/merge, UniversalSearch & Browser Prefs, Test NotificationManager: add missing iconPath property to notif object.
- luna-service2: Add systemd service files.
- webos-connman-adapter: Add systemd service file.
- filecache: Add systemd service file.
- db8: Switch to own fork, tempdb.conf: Fix syntax error, mediadb.conf: Fix syntax error, maindb.conf: Fix syntax error, Add systemd service file & script, Add com.palm.mediapermissions service as admin for maindb (applied patch directly to our fork).
- powerd: Add systemd service file, replace cjson with json-c (applied patch directly to our fork).
- activitymanager: Add systemd service file, Fix build with newer boost 1.58.0 (applied patch directly to our fork).
- sleepd: Add systemd service file.
- luna-universalsearchmgr: Added & renamed systemd service file.
- luna-sysservice: Drop patch that’s no longer needed, added & renamed systemd service file.
- luna-next: Remove unused signal, make sure we use the new names for luna-sysmgr and luna-appmanager service files.
- luna-webappmanager: Drop UserAgent bits and use the ones from LuneOS Components instead, Only set userAgent when it’s provided in appinfo.json, Formatting cleanup, Fix issue with reloading the webView, Start LunaWebAppManager with –allow-file-access-from-files, Rename systemd service file.
- qtwebengine-chromium: FIXUP: Improve path handling in gyp’s ninja generator, [Backport] Include CoreBluetooth.h from files that need it, Detect more ARM FPU models.
- configurator: Switch to own fork, replace cjson with json-c (applied patch directly to our fork), Add systemd service files.
- luna-sysmgr: launcher-conf.schema: Fix syntax error, Update launcher apps, Added & renamed systemd service file, Rename the luna-sysservice service file, Launcher: moves test apps to Prefs tab, and Preware to Downloads, restructure repository layout & added com.palm.contextupload db kind & permissions.
- qtwebengine: Update to latest from upstream Qt 5.6 (28-Sep-2016), Implement RequestQuotePermission.
- core-apps: com.palm.calendarevent: Fix syntax error, disable call to non existing com.palm.accountservices (Palm Profile service). Add high resolution launcher icons for Calendar app.
- mojoloader: Disable require of deprecated sys.
- luna-appmanager: Provide an errorText for non existing apps for launch & open, Run app-install even though we don’t have a proper cryptofs setup, Added & renamed systemd service file, Run configurator for Activities after First Use & Local Profile creation, Pass correct parameters for clearMemoryCaches call.
- webos-systemd-services: LunaSysMgr.service: Make sure we start only after configurator, moved the majority of systemd service files to their individual components.
- qtquickcontrols: Drop patch for setting password character that now part of standard QT.
- storaged: Add RDEPENDS on bash.
- app-services: Add additional dirs to avoid configurator warnings, add additional paths to fix more warnings, add the /var/palm/data/com.palm.appInstallService/ folder.
- packagegroup-luneos-extended: Add phone infrastructure to all targets.
- luneos-emulator.ovf: Configure serial ports correctly.
- luna-init: Fixed various issues with region & locale files, updated default-dock-positions to use the org.webosport.* variant of the apps.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/ca/) to get started. Tenderloin and Mako remain our focus for now, but the emulator, Maguro & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](http://forums.webosnation.com/luneos/331429-pivotce-luneos-october-stable-release-ca-phe-sua-da.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
