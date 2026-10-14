---
title: Chatting like its 2009!
date: 2026-10-14T22:59:00Z
author: codepoet
author_slug: codepoet
categories:
  - News
tags: []
summary: ''
featured_image: /uploads/VeerChat.png
slug: ''
archived: false
source_url: ''
wordpress_id: null
lastmod: 2026-10-14T23:29:00Z
comment_page: ''
featured_image_source: ''
---

While the on-device OS has been getting [updated](https://www.webosarchive.org/pivot/2026/09/08/webos-3.1.0-community-edition-is-here/), [ported](https://www.webosarchive.org/pivot/2026/09/20/lunacy-a-new-child-of-webos/), and [re-imagined](https://www.luneos.org) with increasing speed and success, equally important has been the effort to restore some of the back-end services that webOS expected.

At the app level, many of the open web APIs that were around 10-15 years ago have [become closed, added auth requirements, or been shuttered](https://apigraveyard.com/) or replaced. But where a solution or replacement can be found, we've been pretty successful in [restoring apps](https://appcatalog.webosarchive.org/showMuseum.php?category=Revisionist+History). Fixing an OS-level call to a web service has always been harder.

As examples: HP provided a Cloud backup service to backup and restore Touchpads. Palm provided a contact sync service, and both provided a calendar sync. Of course, both offered capabilities for delivering Over-the-Air Updates, and an App Catalog. 

With **webOS CE**, and related efforts, we've managed to restore a reasonable simulacrum of most of these. The restored [App Catalog contains about 60% of the content ](https://appcatalog.webosarchive.org)of the good old days. Developer [ACHunt](https://github.com/achunt2143) made backup and restore work offline. And the webOS Community Account allows syncing some basic app data between devices -- even Android devices, running **Lunacy**.

But one thing we lost -- one thing that's really changed on the Internet in the past 15 years -- is a peer-to-peer messaging. Of course, we have the [Discord channel](http://www.webosarchive.org/discord), bridged to [Simple Chat](https://appcatalog.webosarchive.org/app/webOSSimpleChat) on-device. And developers have had some success with Google Messages and iMessage syncing via Synergy. Herrie's [Synergy Revival](https://github.com/Herrie82/webos-synergy-revival) effort put a bunch of other services within reach -- certainly of LuneOS. But for those of us old enough to remember ICQ, AIM and MSN Messenger, those just aren't the same...

My friends and I mostly used ICQ, although I dabbled in the other two big ones over the years. That "uh-oh" sound will forever been ingrained on my subconscious brain -- it signaled a message from a friend, and sent me running to my computer to see what was up. I figured it was high time to bring it back to our favorite retro platform!

The "**webOS Chat Enabler**" for AIM can be found in Preware, and re-connects _any_ webOS device -- from the original Pre to the TouchPad -- to a [re-implemented Oscar service](https://github.com/webOSArchive/Oscar-AIM-for-webOS/) running on the webOS Archive Server.

![](/uploads/ChatEnabler.png)

You'll need a [webOS Community Account](https://appcatalog.webosarchive.org/app/webOSCommunityAccountManager), which you can create on a [TouchPad](https://shop.webosarchive.org/) or Android device running **Lunacy** -- download the app from the App Catalog.

Older (non-CE) OSes will also need a pass phrase. Because AOL's old chat protocol pre-dates any modern security, you'll have to [sign in to your account on a modern device ](https://appcatalog.webosarchive.org/admin/account.php)and generate that pass phrase, which you'll use as the password in the Account setup on classic webOS.
**Lunacy** and **webOS CE** users need no other security -- just use the webOS Community Account signed-in on your device, and webOS Chat enabled in Accounts.

However, be aware that regardless of how you sign-in, Oscar is unencrypted -- anyone on your network can intercept your messages (same for the message recipient's network!) Although there was a later implementation that provided some encryption, which I may get around to implementing, at no time should you consider AIM to be a secure chat channel.

With those caveats out of the way, I hope everyone has fun with this. My screen name is the same name I used to author this article -- send me a message if you get online!
