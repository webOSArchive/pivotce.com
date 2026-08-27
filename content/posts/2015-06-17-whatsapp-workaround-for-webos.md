---
title: Whatsapp Workaround for webOS
date: '2015-06-17T18:31:21Z'
author: Alan Morford
author_slug: alanmorford
categories:
- Tips
slug: whatsapp-workaround-for-webos
summary: webOS Nation’s forum user, TheOneill (author of the YouTube client fix patch for webOS), has tested and proven a solution for the now defunct Whatsapp client, MojoWhatsup for webOS. It involves…
source_url: https://pivotce.com/2015/06/17/whatsapp-workaround-for-webos/
wordpress_id: 3062
archived: true
---

![vnc](/images/files/2015/06/vnc.jpg)

webOS Nation’s forum user, TheOneill (author of the [YouTube client fix patch](/2015/06/16/guide-how-to-fix-youtube-for-webos-2-x/) for webOS), has tested and proven a solution for the now defunct Whatsapp client, [MojoWhatsup](http://forums.webosnation.com/webos-apps-games/318833-mojowhatsup-whatsapp-client-webos.html) for webOS. It involves using your computer and VNC on your device. It’s not pretty but it works.

You’ll need a computer, the Genymotion free version, and a VNC client on your webOS device.

I copied [his forum post](http://forums.webosnation.com/webos-apps-games/318833-mojowhatsup-whatsapp-client-webos-139.html#post3438292) for you below and added some links:

***The Genymotion part :***

- *get and install [Genymotion](https://www.genymotion.com/#!/download) free version*
- *once installed, chose one device, for instance Google Galaxy Nexus, and setup a custom screen res (for the veer, I chose 320×400 – 160 dpi, with the Pre3 you can have much better)*
- *run the device, install google apps (download [gapps-jb-20130813-signed.zip](https://www.google.com/search?q=dl+gapps-jb-20130813-signed.zip&oq=dl+gapps-jb-20130813-signed.zip&aqs=chrome..69i57.335j0j4&sourceid=chrome&es_sm=122&ie=UTF-8#q=gapps-jb-20130813-signed.zip)*[Author: that’s a google search] *on the net for API18 devices) to access the store and download whatsapp, or just directly download whatsapp apk if you can find it on the net. To install gapps or apk directly drag and drop files on the device window (further instructions [here](http://www.techrepublic.com/article/pro-tip-install-google-play-services-on-android-emulator-genymotion/) if you need)*
- *setup whatsapp (will end you an SMS on your phone for activation, just copy/paste the URL in the android browser to proceed with the activation)*
- *if you’re google account is properly configured, you should be able to use whatsapp normally on the emulator*

***The VNC part :***

*I use TightVNC but any VNC server should work. VNC has the nice functionnality allowing to crop the screen portion you want to share on a specific port TightVNC service configuration/Extra Ports/Add…) so you can share just the android screen if you want.*

- *Use any VNC client on you WebOS device*
- *If you have no VNC client to use, you can use my novnc experimental port (see [here](http://forums.webosnation.com/webos-development/329749-novnc-webos-phones.html)) or use the specific version that I attach to this post (this version maximizes the window size but you lose the top bar and you cannot move in the VNC so you have to set the screen size carefully. A way of improvement could be to add the abililty to use the ctrl key to switch between panning and interaction in the page, but I don’t know if I can change the useMouseEvents attribute of a webview after setup. I will try it. If you use novnc, do not forget to use websockify to bridge VNC server with a socket (download from [here](https://github.com/kanaka/websockify/downloads), then start typing for instance websockify.exe 192.168.0.1:5901 192.168.0.1:5900, assuming the first param is the IP and port of the socket you create and the second one is the one of the VNC server.*

On a related note, the [Jolla](https://jolla.com/) (think [SailfishOS](https://sailfishos.org/)) folks have a [nice Whatsapp client themselves](http://www.jollausers.com/2015/03/a-new-whatsapp-client-called-whastup-too-hit-sailfish-os-soon/). And since their system uses [QT/QML](http://doc.qt.io/qt-5/qtqml-index.html) it may be possible to port their work over to [LuneOS](/2015/06/06/luneos-june-stable-release-cafe-cubano/) if it’s open source. Time will tell. Happy Whatsapp-ing!

#webosforever
