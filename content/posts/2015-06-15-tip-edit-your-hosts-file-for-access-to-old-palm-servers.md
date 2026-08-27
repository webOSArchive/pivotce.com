---
title: 'Tip: Edit Your Hosts File for Access to Old Palm Servers'
date: '2015-06-15T15:20:45Z'
lastmod: '2018-09-20T13:54:53Z'
author: Alan Morford
author_slug: alanmorford
categories:
- Tips
slug: tip-edit-your-hosts-file-for-access-to-old-palm-servers
summary: Since the shutdown of the HP/Palm servers our ability to access webOS doctors, manuals, and other goodies that used to be up for the masses is pretty much non-existant. The…
source_url: https://pivotce.com/2015/06/15/tip-edit-your-hosts-file-for-access-to-old-palm-servers/
wordpress_id: 3049
archived: true
---

![637x414xsshot20100831205149.png.pagespeed.ic.X1hUmP29Dr](/images/files/2015/06/637x414xsshot20100831205149.png.pagespeed.ic_.X1hUmP29Dr.png)Since the shutdown of the HP/Palm servers our ability to access webOS doctors, manuals, and other goodies that used to be up for the masses is pretty much non-existant. The good news is there’s a fix. Edit your hosts file!

Editing the host file is different for every system but below are a couple of how-to links for varying OSs.

- [webOS](http://forums.webosnation.com/hp-touchpad/308643-possible-edit-hosts-file-manually.html#post3264763)
- [Windows 7/8.1, Mac OSX, Ubuntu](http://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/)

Just put the lines below in your hosts file, save, and depending on your system…reboot! The old links should now work again!

23.4.17.24 cdn.downloads.palm.com
195.22.200.42 downloads.help.palm.com
15.217.96.16 help.palm.com
23.141.224.193 ipkg.preware.org (20th September 2018: This entry redirects to preware.net. The IP address is updated as the servers have now moved. The latest versions of Preware and webOS Quick Install should automatically connect correctly via [DNS](https://en.wikipedia.org/wiki/Domain_Name_System). If using older apps, update the former entry of 140.211.169.161).

#webosforever
