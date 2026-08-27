---
title: 'LuneOS December Stable Release: Cappuccino'
date: '2016-12-26T06:39:56Z'
lastmod: '2017-02-22T18:42:22Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- Developer
slug: luneos-december-stable-release-cappuccino
summary: Merry Christmas! And we’re finally back with a new release called “Cappuccino”, just in time for Christmas and the New Year. We have been focusing on improving the underlying system…
featured_image: /images/files/2016/12/Christmas-16.jpg
source_url: https://pivotce.com/2016/12/26/luneos-december-stable-release-cappuccino/
wordpress_id: 3965
featured_image_source: https://pivotce.com/files/2016/12/Christmas-16.jpg
archived: true
---

Merry Christmas! And we’re finally back with a new release called “Cappuccino”, just in time for Christmas and the New Year. We have been focusing on improving the underlying system stability, adding new features and upgrading various system components.

The release is a bit later compared to what you’re used to this which is due to a combination of some technical, logistical and personnel issues.

We have worked hard to make the OS even more stable and smooth.

We have been focusing on some of the back-end bits for Instant Messaging. Instant Messages aren’t working yet fully in our Enyo 2 rewrite of Messaging, but things start to look better with each change. We have also updated various IM plugins for Skype & Yahoo.

We have also reworked the handling of the notifications to become a bit more snappier and we brought back some more features from LunaCE like “[Card Zoom Gestures](http://webos-ports.org/wiki/About_LunaCE#Card_Zoom_Gestures)“.

We have also re-worked the handling of the icons in the launcher a bit. We now have a Calendar icon showing the correct day for example.

We have also started the work to migrate our Nexus 4 (Mako) build from Android 4.2.2 (CM 10.1) based to Android 5.1 (CM 12.1) based. The image for this is working, we’re now looking to integrate this into our build environment, which is scheduled for just after the holidays. This will also make new ports of more modern targets like the newer Nexus  and OnePlus targets a lot easier.

At the same time we’re also looking at updating our Yocto release from Krogoth to Morty, however we ran into some roadblocks there, so we’ll revisit that after we have completed our CM 12.1 build integration.

Many other small items have been fixed as well, see below for more details of all the changes!

**Known issues:**

- Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.
- Focus bug on input fields. You can work around this by hiding the virtual keyboard and pressing the input again.

### **Changelog**

**Applications:**

- Contacts (org.webosports.app.contacts): Allow searching in Favorites, as in webOS 1.x and 2.x, cleanup of un-needed controls, width of search field is limited to about 14 characters, Tweaks visuals, increase targetWidth or search field. Added Enyo 2.5 People Pick from Messaging for future use.
- FirstUse (org.webosports.app-firstuse): Various graphic improvements 2, use #4db2ff as link color.
- Preware (org.webosinternals.preware):  Refactors global functions & vars into local, removes unused code & generally cleans up.
- Messaging: org.webosports.app.messaging: Fix empty PalmSystem.launchParams, Use 13 digit Javascript timestamp to be legacy compatible, Fix JSON syntax errors & add contacts mock data, ThreadView.js: Fix Uncaught TypeError, Refactors and removes unused files, in preparation for Enyo 2.7.
- Preware (org.webosinternals.preware): Add systemd service file.

**User Interface:**

- luna-next-cardshell: LaunchBar: Let Phone app depend on Settings.tabletUi instead, fix arrangement of icons like legaycy, CardView Correctly center the current card/group in the screen, CardView: take spread value from card group model, CardView: fix some issues when maximizing a card from a stack, CardView: Implement pinch-to-zoom on a single card, Notifications: Use the same swiping logics as for cards, LaunchBar: Dynamically populate icons & update application JSON files, LaunchBar: Have usefull apps for desktop testing, LaunchBar: Use a common ApplicationModel instance for all the launchers, CardView: avoid artefacts after card swiped out, LaunchBar.qml: Don’t use asc: true since it’s invalid, fix default-app-icon.png artifacts.

**System Level:**

- build: Corrected upload path for builds.
- qtwebengine-chromium: add missing include, fix detection of MSVC 2015 Express, fix accessibility crash on view destruction, when a popup is open.
- webos-telephonyd: com.palm.mmsmessage:1 db kind & permissions for com.palm.& apps.
- qtwebengine: Update to latest from upstream 5.6 (22-Nov-2016).
- messaging-accounts: Update Yahoo template for new plugin, removed unneeded logging, removed MySpaceIM template.
- jenkins-job.sh: Show number of openssl archives before and after sstate-cache-management.sh, add few more extra archs to sstate cleanup.
- luna-sysmgr: Add default-dock-positions for filling QuickLaunch Bar.
- luna-webappmanager: BluetoothManager: Add paringDone function.
- qtsensors-sensorfw-plugin: Update to latest QT 5.6.2 code.
- luneos-components: Return locale as well while subscribing, add missing apps to test data, Test apps list: fix icon paths and ids to get correct launchers.
- meta-webos-ports: mojomail: drop patches and move to own fork, qt5-qpa-hwcomposer-plugin: switch to upstream and add rotation patch, sensorfw: Update to latest upstream (30-Oct-16), nemo-qml-plugin-dbus: Switch to mer git and bump SRCREV, mobile-broadband-providers-info: update to latest from upstream (02-Nov-2016), lxc: Update to 2.0.5, libhyrbis: update to latest from upstream (02-nov-16), https-everywhere: update to latest from upstream, hunspell-dictionaries: update to latest, hunspell: Update to 1.4.1, python-tz-native: Update to 2016.7, uriparser: Update to 0.8.4, Update Preware feed for Feedspider and use secure URL, purple-skypeweb: Update to latest from upstream (19-Dec-16), funyahoo-plusplus: Add recipe, More robust building & cleaner logging of enyo-dev apps, imaccountvalidator: Add new Yahoo plugin & remove old ones, imlibpurpleservice: Add new Yahoo plugin & remove old ones,

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/cappuccino/) to get started. Tenderloin and Mako remain our focus for now, but the emulator, Maguro & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion on the webOS Nation forums](http://forums.webosnation.com/luneos/331529-pivotce-luneos-december-stable-release-cappuccino.html). Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

There will be a major upgrade of our build infrastructure over Christmas and New Year, so we’ll need some time to make sure everything is working properly during January, so there won’t be a release in January. We will see you in February with a new release!
