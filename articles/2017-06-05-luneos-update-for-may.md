---
title: LuneOS Update for May
date: 2017-06-05 10:31:10 UTC
modified: 2017-06-05 10:32:14 UTC
author: webosports
author_slug: webosports
categories: [News]
slug: luneos-update-for-may
source_url: https://pivotce.com/2017/06/05/luneos-update-for-may/
wordpress_id: 4040
excerpt: No release this month folks! We’re in the middle of a major upgrade op the underlying Yocto project from Krogoth (2.1) right away to Pyro (2.3) while skipping Morty (2.2)…
---

# LuneOS Update for May

No release this month folks!

We’re in the middle of a major upgrade op the underlying Yocto project from Krogoth (2.1) right ![ambox_warning_blue_construction-svg](../images/files/2016/11/Ambox_warning_blue_construction.svg.png)away to [Pyro (2.3)](https://wiki.yoctoproject.org/wiki/Yocto_2.3_Features) while skipping Morty (2.2) which means we need to update all our kernels to at least 3.4 in order to be able to use the latest upgrades to systemd and glibc.  So far this has been successful for the Nexus 4 (Mako), Nexus 5 (Hammerhead) and we’re now in the process of doing the same for the Touchpad (4G) (Tenderloin). All these targets have a 3.4 kernel available, so the process is relatively straight forward.

However it seems that the Galaxy Nexus (Maguro) doesn’t have a working 3.4 kernel available (only 3.0) and it’s therefore likely we’ll be forced to drop support for the Galaxy Nexus going forward.

[In the meanwhile the Halium project is making solid progress as well](https://twitter.com/HaliumProject/status/871592584136622081)! This starts to look like a very promising start for an united Android base for various alternative operating systems like LuneOS, SailfishOS, Ubuntu Touch, AsteroidOS, Plasma Mobile etc!

We’re always looking for energetic volunteers to [join the LuneOS team](https://pivotce.com/2014/09/22/webos-ports-help-wanted/).

See you with the next release!
