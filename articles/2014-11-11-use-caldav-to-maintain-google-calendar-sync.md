---
title: Use CalDAV to maintain Google Calendar sync
date: 2014-11-11 13:30:22 UTC
modified: 2015-08-12 14:39:04 UTC
author: preemptive
author_slug: preemptive
categories: [News]
tags: [C+DAV, CalDAV, Calendar, CardDAV]
slug: use-caldav-to-maintain-google-calendar-sync
source_url: https://pivotce.com/2014/11/11/use-caldav-to-maintain-google-calendar-sync/
wordpress_id: 2365
featured_image: ../images/files/2014/11/Google_Calendar21.png
featured_image_source: https://pivotce.com/files/2014/11/Google_Calendar21.png
excerpt: Some applications or apps function entirely on your device. Some interact with remote services or applications across the internet to gain additional features, others are simply mobile facades for remote…
---

# Use CalDAV to maintain Google Calendar sync

Some applications or apps function entirely on your device. Some interact with remote services or applications across the internet to gain additional features, others are simply mobile facades for remote services.

For apps to work with these services, they need to send information or make requests for data in a form the remote service can work with. This communication is therefore governed by what is known as a web “[Application Programming Interface](http://en.wikipedia.org/wiki/API#Web_APIs)” or API for short.

You may be syncing with Google’s calendar service using the webOS calendar app. Google is due to change the API that governs this process. They will move to version 3 on the 17th of this month. For your webOS device to continue to synchronise with the calendar, it needs an update!

As a webOS user, you’ve probably already started hyperventilating and mopping your brow. Relax.

~~Try to stay relaxed when I tell you that no one has made a patch to upgrade the calender app to version 3 of the API and no one is planning to~~*. There is another way. Google support another synchronisation process. It’s in common use and is an open standard. It’s called [CalDAV](http://en.wikipedia.org/wiki/Caldav).

LuneOS and webOS developer, [Garfonso](http://pivotce.com/2013/11/15/dev-highlight-garfonso/) has created and tested a CalDAV connector that will work on both systems. Many popular systems support CalDAV and it will be a key component in the future. [CardDAV](http://en.wikipedia.org/wiki/CardDAV), which synchronises contact data, is also supported. Note that you will still need your existing Google account for email and other services along with the [patch](http://forums.webosnation.com/webos-patches/327662-patch-google-sync-https-fix-unknown-error-sign.html) from [Grabber5.0](http://pivotce.com/2014/01/31/dev-highlight-grabber5-0/). Just toggle off the calendar there (and maybe contacts too) in your accounts app.

So is all well in the webOS garden? Not quite. Most of us still using webOS have devices running at least webOS 2.x. If you are using a 1.x device, it is not supported. You have a few options:

1. Use another calendar service.
2. Possibly, you can [upgrade to webOS 2.x](http://www.webos-internals.org/wiki/WebOS_2_Upgrade). This won’t work for Pixis.
3. There is always the chance that someone will create an update for webOS that will work with version 3 of Google’s API and possibly such an update would support webOS 1.x. If you think you could be that person, here are some links to Google API information: [1](https://developers.google.com/google-apps/calendar/get_started), [2](https://developers.google.com/google-apps/calendar/migration), [3](https://developers.google.com/google-apps/calendar/v3/reference/), [4](https://developers.google.com/google-apps/calendar/downloads.).

Installation instructions for the CalDAV connector are here: [C+ Dav Synergy Connector](http://webos-ports.org/wiki/C%2B_Dav_Synergy_Connector) and [here with discussion](http://forums.webosnation.com/webos-development/328133-c-dav-synergy-connector-owncloud-google-yahoo-icloud.html). [Backing up your data](http://forums.webosnation.com/webos-tips-info-resources/329239-your-big-back-up-restore-thread-2015-a.html) first is always advisable ~~and you still have a couple of months to do this with the HP servers~~.

You can donate to the LuneOS project [here](http://webos-ports.org/wiki/Donations) or buy Garfonso himself something nice. [Here is his wishlist](http://www.amazon.de/registry/wishlist/2LZNW33MSFKE4).

*Thanks to developer frantid, [this is no longer true.](http://forums.webosnation.com/webos-patches/286029-google-calendar-sync-behaviors-patch.html)
