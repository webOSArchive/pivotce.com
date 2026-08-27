---
title: 'Tip: How to Bypass Activation'
date: '2015-06-24T14:30:42Z'
lastmod: '2017-07-01T21:54:54Z'
author: preemptive
author_slug: preemptive
categories:
- News
tags:
- Bypass Activation
slug: tip-how-to-bypass-activation
summary: When powered on, a ‘new’, reset or doctored webOS device will attempt to contact HP’s servers to allow a user to log in to an existing Palm Profile account or…
featured_image: /images/files/2015/06/Airport_Flyover_Brisbane.jpg
source_url: https://pivotce.com/2015/06/24/tip-how-to-bypass-activation/
wordpress_id: 3080
featured_image_source: https://pivotce.com/files/2015/06/Airport_Flyover_Brisbane.jpg
archived: true
---

When powered on, a ‘new’, reset or doctored webOS device will attempt to contact HP’s servers to allow a user to log in to an existing Palm Profile account or create a new one. In the past, this allowed access to the app catalog and other services such as cloud backup & remote wipe.

Now, [the HP servers are gone](/2015/04/16/over-and-out/). You can read articles on these pages about the various community fixes for issues that have arisen over the years and how to set up the device and install apps. But if starting afresh, you’ll hit an apparent brickwall: webOS wasn’t designed to skip the activation if contact isn’t made. Palm naturally assumed that everyone would want to download apps & use the services, so the machine waits for contact, advising the user to check the connection or contact HP.

In reality, it has always been possible to bypass this process – for software developers. Those making apps on preview devices didn’t want to set up multiple cellular accounts. Palm made a ‘device tool’ that would run on a computer and tell a connected device to forget about all the profile stuff and just start up so the prototype apps could be tested. The tool worked on webOS 1.x phones and with the release of webOS 2.x, it was possible to simply bypass activation by entering the developer mode code in the phone app (accessed from the start screen). In 2011, Adam Marks posted two guides on webOS Nation:
[Bypass Activation [webOS 1.x]](http://www.webosnation.com/bypass-activation-webos-1-x) (applies to Pre, Pixi & Plus versions)
[Bypass Activation [webOS 2.x]](http://www.webosnation.com/bypass-activation-webos-2-x) (applies to Pre2 & 3, Veer)

In this state, there’s no profile or app catalog, but they are gone now anyway, so it doesn’t matter. If you have an active SIM card, stick it in for cellular service.

But where to get that device tool if the servers are off? They aren’t gone entirely, some old resources are hidden, but still available. Try this [direct link](http://cdn.downloads.palm.com/sdkdownloads/ActivationBypass/2010-04-16/devicetool.jar). If this isn’t working for you, try editing your HOSTS file ([article here](/2015/06/15/tip-edit-your-hosts-file-for-access-to-old-palm-servers/)).

Most legacy webOS devices in use today are TouchPads. Here, the phone app is not so easily accessed and the old device tool doesn’t support it. That devicetool.jar file will run under Java to bypass activation, but a jar file is also an archive, like a zip file – a collection of files. To work on a Touchpad, an additional file needs to be added to it. This item can be extracted from the [webOS doctor](/2014/01/02/the-ninth-day-of-webos-mas-webos-doctor/) for your device.

Note: Do not expect the files linked here to be available forever. Download all the doctors you think you might need and the device tool – anything you can get. Although the files are free to download, the code is proprietary and owned by HP. They probably don’t care, but file sharing may be a legally gray area & you can reasonably trust that HP is a trustworthy source – more so than some random account on dropbox. I never heard of webOS malware, but then, these are Java programs that run on your computer. It’s also more convenient to have your own copies of these useful items. File them carefully for future use.

If you have adjusted your HOSTS file, the webOS doctors are still accessible. A useful listing was supplied some time ago by webOS Internals. You can use it to access the files: [Webos Doctor Versions](http://webos-internals.org/index.php?title=WebOS_Doctor_Versions). You most likely want wifi only, version 3.0.5. unless you have the 4G version from AT&T.

Having made the above caveat about random dropbox accounts, I’ll point out that long-time webOS Nation forum member and prolific patcher, [Grabber5.0](/2014/01/31/dev-highlight-grabber5-0/) offers a version of Device tool pre-modified for all devices. ~~If you are technologically nervous or simply can’t be bothered to make your own tool, click here.~~ There’s a new version that includes the TouchPad Go. Get this all inclusive devicetool.jar [from here](/2015/12/13/the-ultimate-bypass-activation-tool/).

Armed with these files, you can now follow the instructions from fuddy78 in this thread: [HP TP server error](http://forums.webosnation.com/hp-touchpad/329655-hp-tp-server-error.html). The detailed instructions start at post 13, but there are clarifications, so reading it all will help. Basically, you open both archives & transfer a file from the doctor to the tool. The modified tool is then run to bypass activation on the Touchpad.

Note that the reset means you have lost your palm profile data and you will need to re-login to other cloud accounts – you’ve probably also lost your apps. If you can, always back up before a reset.

This article may be useful to set up again: [Guide: Coming (Back) to webOS in 2014, Part 1](/2014/10/21/guide-coming-back-to-webos-in-2014-part-1/). This is a list of fixes you can apply to maintain access to services such as Google, Yahoo, Dropbox etc.: [webOS service pack](http://forums.webosnation.com/webos-discussion-lounge/327892-webos-service-pack.html).

Please post any corrections or queries on the [HP TP server error](http://forums.webosnation.com/hp-touchpad/329655-hp-tp-server-error.html) thread.

Image: [Kgbo](https://en.wikipedia.org/wiki/File:Airport_Flyover,_Brisbane.JPG).
