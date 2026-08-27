---
title: 'LuneOS September Stable Release: Cafe Zorro'
date: '2016-09-17T22:27:42Z'
lastmod: '2016-11-14T15:03:44Z'
author: webosports
author_slug: webosports
categories:
- News
slug: luneos-september-stable-release-cafe-zorro
summary: Time flies while working hard it seems, another month passed and we’re already back with another stable release, Cafe Zorro or “Zorro” for short! A bit later then usual, because…
featured_image: /images/files/2016/09/Cafe-Zorro.jpg
source_url: https://pivotce.com/2016/09/17/luneos-september-stable-release-cafe-zorro/
wordpress_id: 3836
featured_image_source: https://pivotce.com/files/2016/09/Cafe-Zorro.jpg
archived: true
---

Time flies while working hard it seems, another month passed and we’re already back with another stable release, Cafe Zorro or “Zorro” for short! A bit later then usual, because we were busy wrapping up some bits to be included in the release 🙂

So what have we been up to for this release? We’ve been working on getting IM services into shape which required quite a bit of work in the back end, but things are starting to look good. We still need to do more work to make it usable on a daily basis though.

We have also given some love to the browser in order to make the code work more reliably. The restructuring of the code will allow us to more easily add new features in the future as well because it has become more modular. The fullscreen mode is now working properly as well!

For the Touchpad we fixed an issue relating to the device not being able to resume in certain cases after the screen was off. We also fixed the screen going off when it shouldn’t.

Many other small items have been fixed as well, see below for more details of all the changes!

**Main Changes:**

- Touchpad: Suspend/resume bug & screen turning off while it shouldn’t issues have been sorted.
- Browser reworked, added full-screen mode and refactored code.
- FirstUse: Removed WiFi page for devices without wifi, refactored the handling of timezones & added 12/24h selection in FirstUse.
- Messaging: Incoming messages will now play a sound, lots of back end work to get IM support in better shape.
- Phone App: Ringtone from Settings will now be used instead of a hardcoded one.
- Added fullscreen mode support for applications.
- Luna Next Cardshell: Making sure dashboards are closed after the application is launched, added time display to lockscreen.
- C+Dav accounts can now be added from the Calendar app.

**Known issues:**

– Node-SQLite3 is currently not working. Components using Node-SQLite3 have switched to an alternative storage method for now.

### **Changelog**

**Applications:**

- Testr (org.webosports.app.testr): Differentiate between sounds for different tests.
- Phone (org.webosports.app.phone): Rename ApplicationWindow to LuneOSWindow, Move the Ring management to a dedicated service, PhoneWindow: hide the IncomingCallAlert window when the call is ended, RingManager: little cleanup, Tests: move Meego.QOfono and org.nemomobile.voicecall to luneos-components, RingManager: get ringtone from preferences.
- C+DAV (org.webosports.service.contacts.carddav): Add access for all com.palm.* apps (fixes issues with adding a C+Dav account from Calendar app).
- Browser (org.webosports.app.browser): Add proper fullscreen mode call to cardshell, Allow “about:”-urls, Rename ApplicationWindow to LuneOSWindow, Refactor code, Remove some useless top-level properties, Reorganize panels, Refactor SearchSuggestions related code, HistoryPanel: switch to Db8Model, AppTweaks: fix invalid tweaks key, Split util.js and create dedicate models for history & bookmarks, Move subcomponents in their own directory, There is no “states” on a Quick Window, Remaining fixes after refactoring, Fix suggestion list overlapping action tooltip, Fix size of cut/copy/paste tooltip, Also show search suggestions if default search is set, Fix fullscreen behavior after rework, NavigationBar: use onClicked instead of onPressed/onReleased, Use WebEngineView’s contextual menu, BrowserWebView: rely on WebEngine to open new cards, Cleanup unneeded js files, fixed behavior of progress bar after rework.
- Clock (core-apps, com.palm.app.clock): Minor code cleanup.
- FirstUse (org.webosports.app.firstuse): Show WiFiPage only on device with WiFi, Fix connecting to open networks from FirstUse, fix incorrect timezone selection & code cleanup, added time format selection & minor layout tweaks, fix handling for DST.
- Messaging (org.webosports.app.messaging): Add soundClass notifications for the notification so we have sound playback on incoming messages.

**User Interface:**

- luna-qml-launcher: Add $QT_IMPORT_QML/LunaWebEngineViewStyle as an import path to allow overloading of the QML definition of the UIDelegates of the WebEngineView instances.
- luneos-components: Use new luna://org.webosports.luna/enableFullScreenMode service, Add stub call for device info, Fix typo in battery_challenge, Rename ApplicationWindow to LuneOSWindow, Small fixes to remove warnings, Tests: move Meego.QOfono and org.nemomobile.voicecall to luneos-components, Tests: add hardcoded com.palm.db/find result for com.palm.browserpreferences:1, Db8Model: cancel running LS2 call upon destruction, QtWebEngine: add our overload of the WebEngineView UI Delegates, Components: remove useless ContextMenuExtras, Add proper results for com.palm.browserpreferences & region. Additional preference call stub results & timezone table update.
- luna-next-cardshell: Add a LS2 service enableFullScreenMode to let apps require fullscreen mode, CardView: fix fullscreen mode for apps, Add body to the notifications, close notifications after launching app, added clock to lockscreen, fixed banners showing incorrect : at the end.

**System Level:**

- nyx-lib: Added systemd target file.
- nyx-modules: Wait for touchscreen device before reaching nyx.target.
- webos-systemd-services: LunaSysMgr: wait for nyx.target.
- qtwebengine-chromium: Update to latest from upstream (30-Aug-2016).
- qtwebengine: Update to latest from upstream Qt 5.6 (03-Sep-2016), fix crashes on new windows, added custom styled context menu.
- luna-next: Add fileUtils to check for existence of files from QML.
- FreeImage: Fix compatibility with GCC 6.0.
- luna-webappmanager: Implement PalmSystem.enableFullScreenMode.
- luna-sysservice: Fix typo in battery_challenge.
- imlibpurpleservice: Make getServiceNameFromCapabilityId generic, LibPurpleAdapter: remove conversions to and from Mojo-typed usernames, Add com.palm.config.libpurple db kind & permissions, Remove all hard-coded SERVICENAME_xxx occurrences, Add config management and refactor code, IMServiceHandler: merge implementations for onCreate and onDelete, Fix purple’s config dbkind
- messaging-accounts: Update templates to have onCreate and onDelete, cleanup of duplicate suffixes.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

### Download and Install

Feel free to [download the updated builds](http://build.webos-ports.org/releases/zorro/images/) to get started. Tenderloin and Mako remain our focus for now, but the emulator, Maguro & Grouper work too.

Installation instructions for [TouchPad (Tenderloin),](http://webos-ports.org/wiki/Install_LuneOS_for_Tenderloin) [Galaxy Nexus (Maguro)](http://webos-ports.org/wiki/Install_LuneOS_for_Maguro), [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_LuneOS_for_Mako), [Emulator](http://webos-ports.org/wiki/Emulator), and [Nexus7 (Grouper)](http://webos-ports.org/wiki/Install_LuneOS_for_Grouper) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

Don’t forget to contact us with any questions and feel free to [join the discussion](http://forums.webosnation.com/luneos/331398-pivotce-luneos-september-stable-release-cafe-zorro.html#post3448468) on the webOS Nation forums. Catch us on Twitter [@webosports](https://twitter.com/webosports) on IRC: Freenode:#webos-ports or email webos.ports@gmail.com.

See you next month!
