---
title: The Story So Far
date: 2026-11-27T13:36:00Z
author: codepoet
author_slug: ''
categories:
  - Editorial
tags:
  - webOS
  - TouchPad
  - Palm
  - Lunacy
  - LG
  - LuneOS
summary: ''
featured_image: /uploads/hp-touchpad.png
slug: ''
archived: false
source_url: ''
wordpress_id: null
lastmod: ''
comment_page: ''
featured_image_source: ''
---

In socializing recent innovations for the platform, I began to realize that there are people out there who don't really know what webOS _was_. I guess I've lived with it so long that it never occurred to me that the rest of the world has moved on. While I had intended to write a post about the future for the platform, maybe a little primer on the past is in order -- for the more casual explorer...

Long before the iPhone, the Palm Pilot was the "it" gadget that everyone wanted to have. Palm's own OS made these devices useful and responsive, but by 2004, both the company and its platform were in a tough place. Efforts began to re-imagine both, and a completely new "webOS" was a contemporary of the original iPhone.

![Palm Pilot](/uploads/palm-pilot.png)

Under Apple alum [Jon Rubinstein](https://www.youtube.com/watch?v=Gen_FHi4hx8), Palm attracted some of the best designers and developers (many even from Apple), to create a fluid and beautiful new experience on limited hardware, by leveraging open technologies, like Linux, WebKit and JavaScript. The original Palm Pre, with its slide-out keyboard, was followed up by the Pre 2, Pixi while they were still Palm, but the valiant efforts of the team were not enough to take on Google and Apple. They needed a new home, with a bigger wallet.

![Job Rubinstein holds a Palm Pre at launch](/uploads/PreLaunch.jpg)

[HP decided to be that home](https://investor.hp.com/news-events/news/news-details/2010/HP-to-Acquire-Palm-for-12-Billion/default.aspx), and [acqui-hired the Palm team](https://investor.hp.com/news-events/news/news-details/2010/HP-Completes-Palm-Acquisition/default.aspx). Work resumed on the diminutive Veer slide-out, the impressive Pre3, and the TouchPad tablet line, under HP's brand. The leadership promised webOS everywhere, and it looked like there might be a chance. The TouchPad launched against the iPad, with an updated version of webOS, innovative features that wouldn't be copied by others for years, and a small but useful App Catalog... and then disaster struck.

HP had a leadership change, and [foolishly decided to write off the Palm purchase](https://www.cnet.com/tech/mobile/hps-former-ceo-leo-apotheker-killed-webos/). The dev team worked quickly to spin off a fully Open Source derivative, [Open webOS](https://github.com/openwebos), and accelerated efforts to make the [SDK libraries](https://github.com/enyojs) usable cross-platform. The [TouchPad went on fire sale](https://www.zdnet.com/article/hps-touchpad-fire-sale-the-fallout/), and most of the Pre3s never made it to market. The little group of innovators who dared to take on the Apple/Google Duopoly were defeated.

LG bought what was left of the commercial OS, and moved quickly to make it the platform for their Smart TVs. Other experiments, including a Smart Watch, only briefly glimpsed daylight. The Palm brand moved to TCL, and HP moved on to selling crappy Android and Windows 8 tablets. It seemed like the end...

But the famously active and dedicated Community weren't willing to give up. webOS had been [defined by Homebrew and the hacker ethos](https://webos-internals.org/). Community members archived as much of the App Catalog as they could salvage before it was shut off. Open webOS was promptly picked up and became LuneOS -- a community re-write that worked on the TouchPad and could be ported to other hardware. Even webOS itself carried on through Luna Community Edition, providing features Palm never got to deliver.

Over the ensuing decade, though, the small contributions of the community were not enough to fight back the tide of progress. The ancient Linux kernel, WebKit and OpenSSH stacks became a challenge for the modern web. Previously open APIs that enabled apps and features got closed off as Meta and Google consolidated their iron-fisted control over our eyeballs. And app devs moved on to more profitable platforms.

In 2018, shortly before the world got shut down by Covid, I started work on [restoring the SDK](https://sdk.webosarchive.org). I _liked_ the fact that my TouchPad and Pre3 couldn't do much -- that meant Google wasn't tracking my every move. It became a challenge to find a way to proxy, re-route, or update calls so I could keep apps alive, or restore them to functionality.

Community members with app archives, and a partially implemented App Museum, were quick to engage in my novice efforts, and work began in earnest to restore what we could. Coordinating on the [(now dead, but archived) forums](https://forums.webosarchive.org/), and in occasional Zoom meetings, we collected our preserved bits into the "webOS Archive." A new version of the App Museum made downloads "just work", and I poured over repositories and zip files and questionable MegaUpload links to piece together binaries with their meta data.

Then a virus locked us all indoors, and I _really_ started coding. Publishing as either [webOS Archive](https://appcatalog.webosarchive.org/author/webOS%20Archive) (for platform-wide features) or [codepoet](https://appcatalog.webosarchive.org/author/codepoet) (for hacks and restorations), I began building new functionality again. With a working app delivery mechanism, we started to get an idea of how many people were interested. I committed to making sure the platform was never as creepy as Google or Meta, but anonymous stats, opt-in features, and self-identifying users on our Discord server, gave us a [picture of a small, but very real community](https://appcatalog.webosarchive.org/WebService/reports/) still using their devices.

![LuneOS Launcher](/uploads/20180212002610-square.png)

Still, it was a tough road. The move to TLS 1.3 increasingly made it difficult to do anything online, and while I hosted a SSL-bump proxy that made anonymous access possible (but insecure), actually logging-in to anything was also limited by so called "modern sign-in" like OAuth2 flows, that couldn't render in the ancient browser. By 2024, I was about to give up...

Then two things happened, almost at once:

- Out of the LuneOS effort, long-time community member Herrie gave us an OpenSSH update. 
- AI assisted coding got good -- and it had in its training data all the documentation I'd built and restored for the platform.

There's lots bad to be said about AI, and in my personal life, I'm conflicted about it. But the fact that Claude knows my passion project as well as I do has been an incredible accelerator. A decades worth of ideas started coming together in weeks or even days. The foundation we'd preserved, and the tools we'd put together, made it possible to do new things with our 15-year old platform.

While Palm's phones died a different death, with the 3G shut downs, WiFi-enabled devices, and particularly the TouchPad -- which was remarkably powerful for its time -- sprung back to life, as problems were knocked down one-by-one.

![HP TouchPad store display](/uploads/touchpad.jpg)

The Pre3 got a modernization suite that largely brought its original functionality (sans the mobile carriers) back online. The TouchPad got all that and more. This past summer I released webOS Community Edition 3.1.0, replacing HP's final system image (usually 3.0.5) with a firmware bundle including all of the Community's additions, updates and fixes. Using that as a foundation, I started work on the last still-broken piece: the update server.

With Claude's help, we reverse-engineered the signed and secure communication between the device and Palm/HP's servers. A new key, included in 3.1.0, made sure that TouchPad's would trust community server's instead, and the new OS baseline made it possible to compute a delta update between the initial release, and a bundle of updates.

[webOS Community Edition 3.2.0](https://github.com/webOSArchive/webOS-Community-Edition) is available as flashable firmware OR as an Over the Air Update to TouchPad users running 3.1.0. Every non-commercial part of the platform has an open source, community run equivalent. webOS, as originally envisioned by Palm, lives on!

But even with bit-rot addressed through community software. The reality remains that the TouchPad, while the last and best Palm device, is showing its age. The CPU is slow, the RAM ceiling low, and the WiFi chip can't connect to WiFi 6 and newer, faster networks. We need a way to run webOS on _other_ hardware.

[Lunacy for Android](https://www.webosarchive/lunacy), and [LuneOS](https://webos-ports.org/) from webOS Ports, are that way forward. In Part 2, I'll talk more about how the community can engage in those efforts...
