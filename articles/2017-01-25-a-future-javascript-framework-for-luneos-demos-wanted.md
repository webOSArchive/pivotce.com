---
title: A future JavaScript framework for LuneOS – Demos wanted!
date: 2017-01-25 21:59:27 UTC
modified: 2017-12-04 20:00:52 UTC
author: preemptive
author_slug: preemptive
categories: [News]
tags: [App, Developer, apps, enyo]
slug: a-future-javascript-framework-for-luneos-demos-wanted
source_url: https://pivotce.com/2017/01/25/a-future-javascript-framework-for-luneos-demos-wanted/
wordpress_id: 3988
featured_image: ../images/files/2017/01/MeccanoBridge3255515.jpg
featured_image_source: https://pivotce.com/files/2017/01/MeccanoBridge3255515.jpg
excerpt: This article is unusual for pivotCE. Most of our articles are aimed at the general reader, but this one is specifically aimed at those with knowledge of javascript frameworks –…
---

# A future JavaScript framework for LuneOS – Demos wanted!

This article is unusual for pivotCE. Most of our articles are aimed at the general reader, but this one is specifically aimed at those with knowledge of javascript frameworks – specifically frameworks designed for app development. We hope this article will reach such people in our community and beyond in the hope that the [LuneOS](https://pivotce.com/tag/release/) project can benefit from a range of experience and insight and even perhaps recruit some new contributors.

Long time webOS fans will be aware that one of it’s features was the ease with which apps could be created using methods more associated with web design. Most (non-game) apps were in fact mixtures of HTML & javascript. This and the ‘synergy’ of connecting data from various remote services into common user interfaces is what gave the system the name of webOS.

In the early days, webOS was at the cutting edge of using web technologies, but performance was not as responsive compared to more traditionally coded apps. Since the days of legacy webOS, many improvements have been made in app development frameworks and their implementation to bring speed up towards that of ‘native’ apps or at least fast enough for the user to see little difference. Increasing speed, power and multi-core processors have also helped, though performance is beginning to plateau as the physical limits of current hardware is reached.

The first (proprietary) development framework for webOS was called ‘Mojo’. After the purchase by HP, the (Open-source) ‘Enyo’ framework was introduced to target more varied screen sizes. Version 1 ran on the webOS 3.0 HP TouchPad and was back-ported to phones. Version 2 became a cross-platform framework also.

Of course, we all know about the end of hardware at HP and the eventual sell off of all parts of webOS. Officially, the [Open-webOS project](http://www.openwebosproject.org/) is still maintained by LG & HP and [LG’s Silicon Valley lab](http://www.lgsvl.com) have continued to develop the [Enyo JS](https://www.enyojs.com) framework. The part used to make the UI for mobile apps is called ‘Onyx’. To make apps suitable for Television screens, LG developed a new UI library called, ‘Moonstone’. Enyo itself has developed through version 2.5 to now stand at version 2.7 and LGSVL now looks to the [next generation of Enyo](http://blog.enyojs.com/post/142040626224/a-new-era) ([Forum comments](http://forums.enyojs.com/discussion/comment/10494/#Comment_10494)). But this brings with it potential problems for LuneOS.

To begin with, the various iterations of Enyo are not entirely backwards compatible. This is not a big problem as each version can be installed and recent versions are even able to package up modular parts of the framework with the app itself. But to take advantage of the latest improvements, each app needs some rewriting. At this time, apps written specifically for LuneOS are almost all system apps and have been written in whichever version of Enyo was current at the time.

Secondly, the Enyo team are assessing developments in web app development and technology and considering where to next take the framework. This project is currently called, ‘Enyo-next gen’ and will be based in part on the [React.js](https://facebook.github.io/react/) framework. This means that compatibility will again be broken – likely to a greater extent than previously. For this reason, updates of existing LuneOS apps have been put on hold until the Enyo situation becomes clearer. As the Onyx UI library is built on Enyo 2.x, it will not work on React.js unless it is re-engineered. The team’s priorities are obviously lead by LG’s webOS product line: Televisions (briefly [a watch](https://pivotce.com/2015/02/27/lg-outs-webos-watch-urbane-lte/)) and now [refrigerators](https://pivotce.com/2017/01/04/lg-at-ces-2017/). It seems that the next generation Enyo will [target mobile devices](http://lists.webos-ports.org/pipermail/luneos-dev/Week-of-Mon-20160411/000022.html), but Onyx will not be part of the package. It remains to be seen what the replacement will be like.

To avoid remaining in a backwater, LuneOS will need apps. The time is approaching when developer attention must turn from the core OS to the app ecosystem. Millions of apps aren’t needed, but a decent range of modern apps will be. LuneOS has a modern browser based on Chrome. All modern JS frameworks support it and therefore many web apps can be run on LuneOS: old Legacy favourites, apps from similar systems and standalone web apps. Of course, the latter examples won’t necessarily resemble or act like webOS apps and LuneOS will still need a framework for original apps; One that will ‘feel’ and hopefully look like webOS. In short, the LuneOS project needs to make a choice of javascript framework for the future and standardise upon it.

What are the options?

1. webOS Ports could stick with Enyo 2.7. It will be supported for a while. The problem is that this version will not be updated as technology moves forward and the Ports team lack the resources to maintain the framework in addition to the OS.
2. If Enyo-next gen works well (It is certainly expected to be a contender), but lacks the UI elements suitable for LuneOS, the team could attempt to maintain a version of the Onyx or Mochi UI libraries for dedicated use, but again human resource issues mean this option will probably be overlooked in favour of a more ‘off the shelf’ solution.
3. Enyo-next gen could provide an ideal solution, offering the option of creating webOS-style mobile apps.
4. Another suitable framework may need to be found – one that can offer modern performance and which will be supported for the foreseeable future. A popular framework could also deliver a range of apps from sources beyond the small webOS community.

The webOS Ports team are soliciting demo web apps that show the “feel” of webOS can be duplicated by candidate frameworks. What is needed from a javascript framework suitable for LuneOS? LuneOS developer, Doug Reeder of [Hominid Software](http://www.hominidsoftware.com) suggests some requirements:

> 1. A single app is usable on both phone- and tablet-sized screens.
> 2. A layout widget to organize multiple panes, like Enyo Panels, but possibly behaving differently.
> 3. A list with 500 items.
> 4. …whose items can be swiped left or right
> 5. …and whose items can be rearranged by dragging.

A fuller list can be found at [this wiki page](http://webos-ports.org/wiki/New_JavaScript_framework).

Most of our articles link back to the forum at webOS Nation, but in this special case, we are going to link to the archive of the webOS Ports mailing list and invite those interested to join the list and the IRC channel.

Here are archives of the discussion so far:
[Enyo EOL 1](http://lists.webos-ports.org/pipermail/luneos-dev/Week-of-Mon-20160328/000021.html), [2](http://lists.webos-ports.org/pipermail/luneos-dev/Week-of-Mon-20160411/000022.html), [3](http://lists.webos-ports.org/pipermail/luneos-dev/Week-of-Mon-20160411/000023.html).
[Choosing a new JavaScript framework and UI library 1](http://lists.webos-ports.org/pipermail/luneos-dev/Week-of-Mon-20161226/000042.html), [2](http://lists.webos-ports.org/pipermail/luneos-dev/Week-of-Mon-20170102/000043.html), [3](http://lists.webos-ports.org/pipermail/luneos-dev/Week-of-Mon-20170116/000044.html).

If you are familiar with JS frameworks, you are invited to share your experiences of development and performance and suggest candidates for testing. Please [click here](https://pivotce.com/2014/09/22/webos-ports-help-wanted/) for information on the IRC channel and how to join the webOS Ports mailing list. Please share this article with anyone who may have useful insights.

Image credit: [Working on the Meccano Bridge by David Dixon](http://www.geograph.org.uk/photo/3255515).
