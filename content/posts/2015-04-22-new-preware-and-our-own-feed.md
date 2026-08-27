---
title: New Preware and Our Own Feed
date: '2015-04-22T22:48:00Z'
lastmod: '2015-08-05T23:27:46Z'
author: Sören Müller
author_slug: pattyland
categories:
- Tips
tags:
- apps
slug: new-preware-and-our-own-feed
summary: As of right now there is an update to Preware. Version 1.9.14 is available to the masses. pivotCE has worked closely with the nice folks at webOS Internals and Ports for…
featured_image: /images/files/2015/04/pivotcepreware.jpg
source_url: https://pivotce.com/2015/04/22/new-preware-and-our-own-feed/
wordpress_id: 2642
featured_image_source: https://pivotce.com/files/2015/04/pivotcepreware.jpg
archived: true
---

As of right now there is an update to Preware. Version 1.9.14 is available to the masses. pivotCE has worked closely with the nice folks at webOS Internals and Ports for a while now and coupled with [our last announcement](/2015/04/17/bye-bye-app-catalog-hello-preware-catalog/) about the new Preware Catalog Search via browser service we started, **we also would like to introduce the pivotCE app feed now built-in to Preware!**

### Preware update

With today’s Preware update including our feed, you can already browse some awesome apps like [QuickChat for Facebook](http://www.webosnation.com/app-review-quickchat-facebook), [FTPit!](http://forums.webosnation.com/webos-apps-games/279383-ftpit-ftp-client-webos-phones-touchpad.html) and [LastPass](http://www.webosnation.com/lastpass-password-manager-coming-webos-beta-now) to name a few. You can get the new Preware [here](http://preware.pivotce.com/package/org.webosinternals.preware) or by opening Preware on your webOS device and updating the feeds.

### App access

You may be wondering, “But isn’t LastPass already available to download from its own site?” Yep. I designed our Preware feed to act like a bridge between the internet and Preware. We link to IPKs and images elsewhere on the web, collecting them into a single Preware feed. Think of it like a link directory for apps.

### Add more apps

Now it’s your turn! Ask your favorite webOS developers to add their apps to it if they aren’t available on other Preware feeds yet. If they have already provided an official public download for the IPK and likely will not add it to our feed themselves, you may then do it for them. You must notify the developers so they know there is still interest in their apps.

If you would like us to link to your app or an app that you are allowed to host, contact us! Additionally, pivotCE can host a limited number of apps with no home of their own, but the costs associated with hosting many files will rise, so linking is our preferred method.

### How to use the feed

1. Go to <http://feed.pivotce.com/>, click on “Add App” and fill out all the requested info. You’ll get a private link where you can manage/update your app
2. We will test and verify the app and the info, descriptions, email etc.
3. Once we verify it, we’ll flag the packages as “ok” and it’s added to the feed

### Security and anti-piracy

There are two databases, one for the management and one for the feed generation. Only approved packages are copied to the second database and are written in the package file periodically. Every update on a package, whether the maintainer has a new version, fixed a typo, or a hacker got the private link and writes malicious code it flags the package as “changed” and the update is not copied to the feed till someone flags it as “ok” again.

Please don’t upload any apps on a server and add them to our feed without the author’s permission, even if the apps are
free. Free of charge doesn’t mean public domain, and the developers and companies still hold all the rights on their apps. Feel free to ask them for a download link or the permission to upload a link to their app. We will check this before we flag it “ok”!

### Donations

Thanks for all the donations that enables us to provide these services for the webOS community. The donate link is on the left of this page.

Stay tuned, our third service is already in testing. If you’ve got any problems or question regarding our feed, feel free to [contact us](/contact/)!

[Discuss our new feed on the forums.](http://forums.webosnation.com/general-news-discussion/329667-pivotce-new-preware-our-own-feed.html#post3437057)
