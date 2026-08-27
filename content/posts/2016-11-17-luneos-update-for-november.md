---
title: LuneOS Update for November
date: '2016-11-17T16:52:41Z'
lastmod: '2016-11-17T21:17:12Z'
author: webosports
author_slug: webosports
categories:
- News
slug: luneos-update-for-november
summary: No release this month folks! We’re doing some long overdue maintenance on our build servers and related services. They were still running Ubuntu 14.04 so we have now updated them…
source_url: https://pivotce.com/2016/11/17/luneos-update-for-november/
wordpress_id: 3923
archived: true
---

No release this month folks!

We’re doing some long overdue maintenance on our build![ambox_warning_blue_construction-svg](/images/files/2016/11/Ambox_warning_blue_construction.svg.png) servers and related services. They were still running Ubuntu 14.04 so we have now updated them to the latest Ubuntu LTS release 16.04.1. Most of the updates went fine but we still have a few loose ends to address, specifically with some build issues for the Touchpad kernel.

In the meanwhile we were able to fix some of the MediaWiki issues that happened after we upgraded MediaWiki earlier which broke templates and the change log.

We have also started to do initial testing for migrating to the latest Yocto 2.2 release called Morty and initial (local) testing is underway for a Qt 5.7 migration as well. These are not expected to hit the next release yet, but it’s all work in progress for now. It’s not included in the nightlies yet for now.

We are also venturing in paving the way for updating some of our builds to a CM 12.1 (Android 5.1) and CM 13.0 (Android 6.0) build. This should also help for future ports to more recent devices.

In the meantime you can get our [latest nightly releases](http://build.webos-ports.org/luneos-testing/images/) and help us test and [report your findings.](http://issues.webos-ports.org/projects/ports/issues?set_filter=1)

We’re always looking for energetic volunteers to [join the team](/2014/09/22/webos-ports-help-wanted/).

See you next month!
