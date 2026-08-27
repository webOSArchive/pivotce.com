---
title: 'LuneOS January Stable Release: Breve'
date: '2015-01-09T19:58:35Z'
lastmod: '2015-02-05T03:04:58Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- Breve
slug: luneos-january-stable-release-breve
summary: The team is growing and LuneOS is improving. We’ve made significant progress this month. We do our best to get a new release out near the first of every month.…
featured_image: /images/files/2015/01/breve.png
source_url: https://pivotce.com/2015/01/09/luneos-january-stable-release-breve/
wordpress_id: 2600
featured_image_source: https://pivotce.com/files/2015/01/breve.png
archived: true
---

The team is growing and LuneOS is improving. We’ve made significant progress this month. We do our best to get a new release out near the first of every month. The holidays put us a week behind but allow us to introduce the latest build, Breve.

### Changelog

- Initial support for IM and SMS messaging
- Mobile data usage is now functional but needs an unlocked SIM card and be manually enabled through the settings app
- Extended dashboard support
- Location service with WiFi based position source only (using Mozilla’s location service; see <https://location.services.mozilla.com/>)
- Charger status on Nexus 4 is now correctly detected
- Improved image quality in some apps and the card shell
- Screen recording support (see <https://github.com/webOS-ports/luna-next/pull/93> for details)
- Backend support for MMS messages but not yet integrated with LuneOS services
- Several metadata cleanups

### Build notes

Meta-webos-ports repository now contains 2 layers:
**meta-luneui** – minimal set of recipes needed to build luna-next (later
will had some minimal image as well)
**meta-luneos** – everything else needed to build our current images and OE distro definition

The OE distro was renamed from webos to luneos to continue with our re-branding. You need to do 1 manual step next time you call “make update”:

sed -i ‘s/DISTRO=”webos”/DISTRO=”luneos“/g’ luneos-*/webos-ports/setup-local and export DISTRO=”luneos” if you’ve already sourced setup-env.

Also, starting now all images are called luneos-* instead of webos-ports-*. Update your shell aliases accordingly.

### Gallery

This slideshow requires JavaScript.

### The usual

1. [Sign up for the bug tracker](http://issues.webos-ports.org/projects/ports/issues?set_filter=1)

2. [Get involved](/2014/09/22/webos-ports-help-wanted/) and

3. [Join the mailing list](http://lists.webos-ports.org/mailman/options/luneos-dev)

Feel free to [download the updated builds](http://build.webos-ports.org/releases/breve/images/) to get started. Tenderloin and Mako remain our focus for now and the emulator works too.

Installation instructions for [TouchPad (Tenderloin)](http://webos-ports.org/wiki/Install_WOP_for_Tenderloin) and [Nexus 4 (Mako)](http://webos-ports.org/wiki/Install_WOP_for_Mako) are on the [wiki](http://webos-ports.org/wiki/Main_Page). And remember we [don’t do timelines](http://webos-ports.org/wiki/ETA).

See you next month! We’re getting closer and closer to being able to use LuneOS as a daily driver.

Don’t forget to contact us with any questions and feel free to [join the discussion](http://forums.webosnation.com/luneos/329231-pivotce-luneos-january-stable-release-breve.html) on the webOS Nation forums. Also, continue spreading the word! #LuneOS
