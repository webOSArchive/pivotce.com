---
title: A Quick Tour of webOS OSE on the Raspberry Pi
date: '2018-03-22T03:12:45Z'
lastmod: '2018-03-22T03:14:13Z'
author: preemptive
author_slug: preemptive
categories:
- News
tags:
- Developer
slug: a-quick-tour-of-webos-ose-on-the-raspberry-pi
summary: The release of fresh webOS code from LG in the form of webOS Open Source Edition was unexpected. There’s been some interest in what exactly it is. Fortunately, web developer,…
featured_image: /images/files/2018/03/webOSOSE-RPi3.png
source_url: https://pivotce.com/2018/03/22/a-quick-tour-of-webos-ose-on-the-raspberry-pi/
wordpress_id: 4381
featured_image_source: https://pivotce.com/files/2018/03/webOSOSE-RPi3.png
archived: true
---

The release of fresh webOS code from LG in the form of webOS Open Source Edition was unexpected. There’s been some interest in what exactly it is.

Fortunately, web developer, [Garrett Downs](http://preware.pivotce.com/maintainer/Garrett+Downs) has the Raspberry Pi 3 needed to run the code and we have a guest post with his first impressions:

> What’s that? Pining for webOS? Build and install on your Raspberry Pi! <https://t.co/3Eslofgb1x> and <https://t.co/GxY3yWnJlz>
>
> — webOS DevRelations (@webOSdev) [March 20, 2018](https://twitter.com/webOSdev/status/975958009653362688?ref_src=twsrc%5Etfw)

When I saw a tweet from @webOSdev announcing webOS OSE was available to install on a Raspberry Pi 3, I knew what I’d be doing that night after work. Unfortunately, the process to build it requires hours of time and a computer running Linux natively (virtual machines are not recommended). I didn’t have either of those things. Luckily, someone had already built it and made the [image available to download](https://github.com/webosose/build-webos/issues/1#issuecomment-374301048). Sweet! I put the image on a SD card, loaded it into my Pi, and powered it up.

After booting, you’re greeted with a nice splash screen with the webOS OSE logo in the corner. The recommended first thing to do is go into settings and connect to ethernet or Wi-Fi, so that’s what I did. That’s actually the only thing you can do in the settings right now. The only other section contains some basic info about the OS and that’s it. Alright, how about apps?

As this is the very first version of the project, I wasn’t expecting much here. Pressing F1 on the keyboard triggers the app menu to slide in from the right side of the screen. There are three “apps” in there, but they’re nothing more than website wrappers. ‘[Enact](http://enactjs.com/)’ and ‘[webOS OSE](http://webosose.org/)’ will bring you to two sites with lots of info about the OSE project and how to get started developing. The third is ‘YouTube’, which is obviously a YouTube app. I haven’t tried signing into my Google account, but videos on the landing page work just as they should.

The interface doesn’t have cards like we know them from old webOS or the small tiles of webOS TV. I’m not sure how webOS OSE handles switching between apps. They only really told us how to open the app list. I’m curious to learn more about this.

I’d say that this is a pretty barebones OS in its current form. It seems to be the TV OS with a lot of the stuff removed (or just not accessible yet?), like the apps along the bottom of the homescreen, content store, most of the settings, etc. I think it’s enough for developers to start poking around though. I don’t know if it’s touchscreen-enabled, but I would assume so.

So, that’s all there is to see for now, at least from an end user’s point of view. If you happen to be an app developer like me, there are already some [tools on the webOS OSE site](http://webosose.org/develop/app-service-app-developer/web-app-dev/building-your-first-web-app/) to get started tinkering. I’ve had some limited success getting a couple of my apps up and running. If you’re looking to dig deeper than app dev, the entire project is open source so feel free to dive right in! The documentation for app development seems to be pretty decent considering how new this project is.

If you don’t want to bother setting up a Raspberry Pi, I made a short video showing most of what I mentioned above.

[YouTube video](https://www.youtube.com/watch?v=98Sthe-JB4U)
