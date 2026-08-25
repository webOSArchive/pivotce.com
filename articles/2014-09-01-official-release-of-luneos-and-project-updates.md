---
title: Official Release of LuneOS and Project Updates
date: 2014-09-01 21:07:47 UTC
modified: 2014-10-21 02:04:35 UTC
author: webosports
author_slug: webosports
categories: [News]
slug: official-release-of-luneos-and-project-updates
source_url: https://pivotce.com/2014/09/01/official-release-of-luneos-and-project-updates/
wordpress_id: 830
featured_image: ../images/files/2014/09/luneosheader.jpg
featured_image_source: https://pivotce.com/files/2014/09/luneosheader.jpg
excerpt: It’s been a long while since we announced our Alpha 2 release back in June of 2013, but today after months of very hard work the webOS Ports team are…
---

# Official Release of LuneOS and Project Updates

![blue-white-sphere-text_1](../images/files/2014/06/blue-white-sphere-text_1.png)It’s been a long while since we [announced our Alpha 2 release](http://webos-ports.org/wiki/Main_Page#Breaking_News) back in June of 2013, but today after months of very hard work **the webOS Ports team are very proud and happy to provide our latest release to the community now named “LuneOS”.**

The first eye catching change is the new name we’ll be using for our project going forward. The distribution will be called “LuneOS” instead of “WebOS Ports Open webOS” because it wasn’t very catchy and **we felt it important to specify we are separate from Open webOS** which is it’s own project from HP and now LG. Lune is the French translation of moon and refers to the user interface we all love so much in legacy webOS, LunaSysMgr, which is named after the Latin/Spanish translation of moon.

The release model for LuneOS is a rolling one where each of the releases will get its own name from a list of coffee beverages. This first release is “Affogato”.

All work for each release is [visible to the public](https://github.com/webos-ports) and users can also update to unreleased stages to support the developers with testing and bug fixing. Our overall aim is to deliver high quality software which is stable and satisfies the needs of our users. We plan to have a new release at the beginning of each month.

# General focus

As a mobile operating system, we’re tailored for smartphones and tablets. Our main focus is not to add new devices as they appear on the market but instead to provide a stable, easy to use and easy to port software base. Porting OS pieces itself was never the real problem of our approach since we solved the most important bits by using [libhybris](https://github.com/libhybris/libhybris). The actual problem we’re facing is to get applications software implemented and to add all the back-end functionalities to the system we love and need.

**The main focus of LuneOS is to provide an operating system which is driven by the community and continues what we love(d) about webOS.** We’re not trying to reach feature comparison with Android or iOS but rather building a system to satisfy basic needs in the mobile environment. Building a good quality mobile operating system from scratch is a hard job and is built in just the spare free time everyone involved in the project has. To get the best ratio between what we want and what we can do, we’re analyzing architectural decisions from both existing solutions we can base our work on and whether we have to write things from scratch.

# Supported devices

We’re currently supporting the Nexus 4 and HP TouchPad. The Galaxy Nexus and Nexus 7 (2012 Wifi) are still supported with this Affogato release, but will not be actively maintained anymore by the project team for future releases. We would like someone to step up as maintainer for these devices. We also have started to write a [porting guide](http://webos-ports.org/wiki/Porting_Guide) to make it easier for community members to port LuneOS to other devices.

# What works

Wifi!  We also have a working settings app which includes things like wifi, screen, developer mode, and about. Apps that work include a basic browser, Preware, mail (enyo1 but it’s working albeit a tad buggy because of screen size related things), accounts (with some minor issues), memos is fully working, a stubbed contacts app, initial calendar app with no real backend functionality yet, synergy connectors for a lot of endpoints (Google, Yahoo, i*, owncloud, and more) and initial work for a phone app.  Also, contacts sync is working along with better suspend/resume handling, and a bunch of other smaller things.

This slideshow requires JavaScript.

# System/architecture improvements

After the Alpha 2 release we made the drastic decision to rewrite LunaSysMgr from scratch and name it Luna Next. This decision was made because LunaSysMgr distributed with Open webOS caused too many headaches, mainly due to the legacy device support and the overhead of code that was in there to support various things. Keeping LunaSysMgr would not allow proper hardware acceleration without a lot of work and would have made porting to other devices harder in the future.

Therefore, the team decided to start rebuilding the user interface from scratch using the latest technologies available (QT 5.2 / QML, WebKit 2, etc). This of course meant a lot of work, but also a lot of benefits because it provides design flexibility going forward. Where possible, existing code from LunaSysMgr was re-used.

As you can imagine, the rewriting has been a lot of work and there are many different scenarios to cover, so there might still be some bugs present. After this release we will focus on adding additional features to Luna Next.

Starting with this release, LuneOS has a built-in update mechanism which makes it easy for users to update to the latest build.  The implemented mechanism is similar to the one which was used in webOS before but has a different backend implementation. Right now there is no automatic notification when a new update is available. The user has to check on his own in the Settings app if a new update is available to install it.

# Ecosystem

We’re still using Preware to provide application feeds which enables the community to distribute their applications. Currently we only support one feed which is built from purely open source applications. Submitting a new application is as simple as creating a pull-request against the relevant repository which sets up the feed. On the application side we have a reworked Preware application which is now based on Enyo 2. It is faster compared to the original Preware based on the Mojo framework due to the fact it can simultaneously download multiple feeds. However, it’s back-end is still based on the same code as in the legacy webOS system.

# Improvements since Alpha 2

Overall there are a lot improvements since the last release.  Below is a list which doesn’t aim to be complete but gives a good overview what the team worked on and is still working on:

Core OS system improvements

- Built upon libhybris to enable easy portability on available Android based devices where the followings things are currently re-used from Android:
  - Telephony system (rild)
  - Graphics drivers

- We’re planning to utilize more things from Android soon like:
  - Hardware accelerated video/audio playback
  - Sensor integration
  - Functioning camera

- There is currently no plan to support running Android applications within LuneOS like ACL or AndroidChroot do.
- Using systemd as system init manager instead of Upstart, giving shorter boot times and easier control of tasks during boot.
- Emulator based on VirtualBox is available for testing and development
- Completely built by the community (OpenEmbedded build system)

# Application improvements

- Preware 2 is now working and enables users to install additional applications.
- Various bugs have been addressed in the [Memo](https://github.com/webos-ports/org.webosports.app.memos), [Calculator](https://github.com/webOS-ports/org.webosports.app.calculator) and [Email](https://github.com/webOS-ports/core-apps/tree/master/com.palm.app.email) apps.
- A new [PDF app](https://github.com/webOS-ports/org.webosports.app.pdf/) has been created based on Mozilla’s PDF.js implementation.
- A basic [file manager](https://github.com/webOS-ports/org.webosports.app.filemanager) application is available.
- [Open webOS core applications](https://github.com/webos-ports/core-apps/) are still present but a little buggy at times; this needs to be fixed or replaced by new versions of the apps.
- A system update mechanism is available to easily update to a new build once available.

# Current work in progress for future releases

- Native QML based phone application for speed & reliability
- Media Indexer Support with legacy webOS compatible API
- Support for audio and video playback
- Tweaks support
- Further Status Bar indicator support and updates
- Further improvements to the keyboard layouts
- Adding user interface features to Luna Next which were also available in webOS 3.x and LunaCE such as “Card Stacking”, “Mini Cards”, “Card Zoom Gestures”, “Stack Spread Gestures”, “Infinite Card Cycling”, “Tap-to-Maximize Edge Cards” etc.

# Help needed

As LuneOS is a large project with just a small group of people working on it, we could use help with various things. Especially on the application development front. We have a lot of parts on the service side in place but the app UIs need a lot of work from creative people. If you like webOS, know how to develop on the web and enjoy working with an enthusiastic team on a new community built mobile operating system, don’t hesitate to contact us through the available communication channels (see http://webos-ports.org/wiki/Communications). Besides doing real development we also need people spreading the word about LuneOS, working on the website or documentation for others about how to participate in the project.

Here is a rough and unsorted list of things we need help with:

- Fix bugs in existing applications (Settings, …)
- Create replacements for old Enyo 1 based applications:
  - Contacts (first draft exists)
  - Calendar (first draft exists)
  - Messaging (with Synergy integration)
- Create documentation and workflow for app developers to develop and submit new applications
- Improve the project website with a better look & feel
- Testing and bug reporting

If you’d like to get involved, [contact us](http://webos-ports.org/wiki/Communications)!

# Get started with LuneOS

Ready to start using LuneOS?  Great!  Here’s what you need to know:  there is still a lot of work in progress and the current state should be considered as being alpha even though it’s working quite nicely for the parts that are implemented already. Therefore, use is at your own risk. Currently BlueTooth, the accelerometer, camera and ALS are not implemented yet. Audio & wifi should work, though might be buggy. If you have a TouchPad you can start [here](http://webos-ports.org/wiki/Tenderloin_Info). You will want to use the “Release” version. Nightly is used for things that are being worked on and bug fixes for the next release.  If you need help installing it, go [here](http://webos-ports.org/wiki/Install_WOP_for_Tenderloin).  If you’d like to try the emulator go [here](http://webos-ports.org/wiki/Qemux86_Info). And for the Nexus 4 go [here](http://webos-ports.org/wiki/Mako_Info). All the supported devices can be found [here.](http://webos-ports.org/wiki/Devices#vendor=;)

# Found some bugs?

Once you’re happily testing, it can of course happen that you will run into some bugs. Feel free to report them at <http://issues.webos-ports.org/projects/ports/issues> so the developers can look into it. Of course you’re free to help in solving existing bugs as well!

# Have questions about the project?

No problem!  Send us an email to webosports@gmail.com or tweet to us [@webosports](https://twitter.com/webosports).  If you’re excited about the project, use the hashtag #LuneOSishere and spread the word!
