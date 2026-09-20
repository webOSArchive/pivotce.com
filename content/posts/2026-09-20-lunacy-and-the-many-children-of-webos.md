---
title: Lunacy, and the Many Children of webOS
date: 2026-09-20T16:43:00Z
author: codepoet
author_slug: ''
categories:
  - News
tags:
  - Lunacy
  - webOS
  - Android
summary: ''
featured_image: /uploads/Lunacy-256.png
slug: lunacy-a-new-child-of-webos
archived: false
source_url: ''
wordpress_id: null
lastmod: ''
comment_page: ''
featured_image_source: ''
---

The question came up recently on the Discord chat: what's with all these new versions of webOS? How do I know which is right for me? Today's announcement only adds to that confusion, so it seems worth some explanation -- but first the news!

[**Lunacy**](https://github.com/webOSArchive/Lunacy) is a new project to bring a webOS environment to Android devices.

It might be most helpful to explain what it is not.

- Lunacy is _not_ a new version of webOS (that's below) and Lunacy is not [LuneOS](https://www.webosarchive.org/pivot/author/webosports/) (more on that below too!)
- Lunacy is _not_ an emulator -- [we have one of those](https://sdk.webosarchive.org/#cEmulatorNotes), it’s not great, but it works.
- Lunacy is _not_ an app-compat wrapper for individual apps.

So what is it?

Lunacy is a webOS application environment for Android. If you're familiar with the WINE project for running Windows apps on Linux (WINE stands for Wine Is Not an Emulator), it's in a similar vein.

webOS and Android share a lot of similarities, but had different ways of building apps and allowing them to interact with the hardware. webOS used web technologies on top of Linux, and a Plug-in Development Kit that allowed more direct hardware access. Android was also based on Linux, but provides a Java runtime environment and a HAL (Hardware Abstraction Layer). What an application can expect from its environment is known as the application "contract."

In recent AI-assisted efforts, I've been successful in fulfilling simple parts of the [Android app contract on legacy webOS](https://github.com/webOSArchive/Android-to-webOS-Ports), enabling ports of early Android games like [Plants vs Zombies](https://appcatalog.webosarchive.org/app/PlantsvsZombies), or [Temple Run 2](https://appcatalog.webosarchive.org/app/TempleRun2). Lunacy does something similar in reverse: it provides the webOS app contract on top of Android.

![](/uploads/NotATouchpad.png)

_One of these tablets is NOT a TouchPad!_

For SDK apps (those based on web technology) this is a simple proposition on its surface -- make the webOS web frameworks (Mojo and Enyo) work on Android. It's obviously more complicated than that, since webOS also provides non-web capabilities, and a service bus for inter-process communication. But the principle holds. PDK apps will be a little (lot) harder, but we'll get there.

So Lunacy is three things right now:

- A Luna-like shell, called **AndroidLuna** (which will eventually be offered as an Android launcher)
- An app contract environment (**LunaRuntimes**) that hosts patched Enyo (and soon Mojo) framework libraries and a simulated service bus that allows existing webOS apps to run as-is.
- A webOS style keyboard (**LunaKeyboard**) that can be optionally installed to complete the experience

The end result is something that hopefully looks and feels _exactly_ like webOS, and runs many webOS apps -- at full speed, without interpretation or emulation.

This then, is a new third-generation descendant of Palm and HP's mobile webOS! The family tree looks like this...

- **Palm**'s webOS begat **HP**'s webOS
- HP's webOS gave us **Open WebOS** and LG's commercial **webOS for TV**s (which sometimes contributes to [**webOSE**](https://github.com/webosose/website))
- Open webOS birthed **LuneOS**, **webOS CE**, and now **Lunacy**

**The Family Tree Illustrated**

![webOS Family Tree](/uploads/webOS-FamilyTree.png)

LuneOS has been around a long time, but has been dramatically accelerated recently by AI assisted dev tools. It's available for (and easily ported to) many Android devices with an unlockable bootloader.

[webOS Community Edition](https://www.webosarchive.org/pivot/2026/09/08/webos-3.1.0-community-edition-is-here/) compiles all the community-built improvements to the original webOS into a new, modernized system image specifically for TouchPad.

Lunacy brings a webOS compatibility environment to Android devices via an app -- no unlocking required. Its just an app!

For now, Lunacy is available for Android 5.0.1 tablet devices -- but development is still very early, and we plan to target phones and more modern versions of Android over time. If you want to help, check out the project on GitHub: [https://github.com/webOSArchive/Lunacy](https://github.com/webOSArchive/Lunacy)
