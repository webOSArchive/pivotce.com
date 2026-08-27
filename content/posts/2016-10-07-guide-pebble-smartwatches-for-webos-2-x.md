---
title: 'Guide: Pebble Smartwatches for webOS 2.x'
date: '2016-10-07T23:27:34Z'
lastmod: '2017-12-05T17:44:16Z'
author: Alan Morford
author_slug: alanmorford
categories:
- Tutorial
slug: guide-pebble-smartwatches-for-webos-2-x
summary: Hey! Got a Pebble smart watch? Or more specifically a Pebble (1st Gen) or a Pebble Steel? I’ve got a sweet you-might-have-missed-it tutorial for you! Grab your favorite webOS 2.x…
featured_image: /images/files/2016/10/suite.png
source_url: https://pivotce.com/2016/10/07/guide-pebble-smartwatches-for-webos-2-x/
wordpress_id: 3753
featured_image_source: https://pivotce.com/files/2016/10/suite.png
archived: true
---

Hey! Got a Pebble smart watch? Or more specifically a Pebble (1st Gen) or a Pebble Steel? I’ve got a sweet you-might-have-missed-it tutorial for you! Grab your favorite webOS 2.x phone and your smartwatch and keep reading!

Thanks to [MetaView](https://twitter.com/MetaView), you can use your webOS 2.x phone with Pebble watches on firmware 3.x and below.

### G![Preware](/images/files/2016/10/preware_2016-07-10_145022.png)et the stuff you need

1. Point your browser [to the forums](http://forums.webosnation.com/webos-homebrew-apps/331159-connecting-pebble-webos-using-mwatch.html) and grab the patch file.
2. On your webOS 2.x phone open [Preware](/2014/01/04/the-eleventh-day-of-webos-mas-preware/) and install [MWatch](http://preware.pivotce.com/package/de.metaviewsoft.mwatch).
3. Use [WOSQI](http://forums.webosnation.com/canuck-coding/274461-webos-quick-install-v4-6-0-a-65.html) to install the patch file.
4. [Grab this file](https://app.box.com/s/v3y8m08xjefj85mn02ihhnxupj1qpe7c) to make each notifcation option toggle-able in [Tweaks](/2014/01/03/the-tenth-day-of-webos-mas-tweaks/). Then copy the file to your device and use [Internalz Pro](/2013/12/29/the-fifth-day-of-webos-mas-internalz-pro/) to copy it to /media/cryptofs/apps/usr/palm/services/org.webosinternals.tweaks.prefs/preferences.
5. **If this is a brand new watch to you, you *might* need an Android or iOS device to get you set up before using it with webOS.**

### Connect your Pebble

1. On the Pebble, hit the center button and then navigate to Settings > Bluetooth then leave it there.
2. On the phone open bluetooth preferences and turn bluetooth on.
3. Tap +Add Device
4. Select other from the drop down menu
5. Tap on Pebble
6. Confirm on both the watch and the phone.

   ![Bluetooth settings](/images/files/2016/10/IMG_20161007_131153.jpg)

   *Bluetooth settings*

   ![Pair the watch](/images/files/2016/10/IMG_20161007_131334.jpg)

   *Pair the watch*

   ![Pair the phone](/images/files/2016/10/bluetooth_2016-07-10_131403.png)

   *Pair the phone*

   ![The result](/images/files/2016/10/bluetooth_2016-07-10_131316.png)

   *The result*

### ![mwatch](/images/files/2016/10/mwatch.png)MWatch

Now simply open MWatch. You should see the red line turn green.

Note: the mwatch service has to remain open. If you close it, it will reopen itself when you get a notification but it may not reconnect. If it ever has trouble reconnecting, try these steps.

- Tap on the MWatch notification icon and hit the red circle to ping the watch.
- Toggle bluetooth off and then on.
- Swipe away the MWatch process from the notification area and close and reopen the app.

### What works

Everything below works great IF you’re using a Pebble watch with PebbleOS 3.x or below, yes, even on the Pebble models released after the Pebble Steel.

* Notifications (email, text, calls, Macaw, and Calendar with the [UberCalendar patch from Preware](http://preware.pivotce.com/package/org.webosinternals.patches.calendar-ubercalendar))
* Call rejection
* Time setting
* Music control (but sometimes it takes some time to see the current song on your watch)

### What doesn’t work

* Anything at all if your watch firmware is 4.x and up otherwise…
* App installations
* Firmware updates
* Reply to messages
* Everything a Pebble app needs to access the phone’s sensors or internet

### webOS Watchface

If you have an Android or iOS phone laying around, you can install different watch faces. The Pebble stores an unknown amount of watchfaces on the device but I doubt more than 3 or so. If you’re looking for a cool watchface for webOS…well I know one pretty awesome one that looks a lot better on the color Pebble Time (3rd gen) but not so much on the black and white Pebble and Steel.

[Check out](https://apps.getpebble.com/applications/570ddc3cbf385c2ad200000d) Grabber’s ([Matt](/2014/01/31/dev-highlight-grabber5-0/)) webOS watchface! [Link if you’re on Android/iOS and have the Pebble app installed](https://appstore/570ddc3cbf385c2ad200000d).

> First draft of my webOS watch face for my [@Pebble](https://twitter.com/Pebble?ref_src=twsrc%5Etfw) Time Steel [pic.twitter.com/qUdGcVe3aZ](https://t.co/qUdGcVe3aZ)
>
> — Matt Williams (@Grabber5_0) [April 15, 2016](https://twitter.com/Grabber5_0/status/721067881677459456?ref_src=twsrc%5Etfw)

### Tweaks

![tweaks](/images/files/2016/10/tweaks_2016-07-10_185749.png)Get Tweaks from Preware if you don’t have it already. If you chose to grab  and copy over the .json file from the top section then you can open up the Tweaks app and pick your toggles. Calls can’t be toggled. Don’t forget to Luna restart after you’ve made your selections.

### The result

![Email on a Pre2 or Pre+ w/2.x](/images/files/2016/10/Pre2.jpg)

*Email on a Pre2 or Pre+ w/2.x*

![Project Macaw on Veer](/images/files/2016/10/Veer.jpg)

*Project Macaw on Veer*

![Text on Pre3](/images/files/2016/10/Pre3.jpg)

*Text on Pre3*

[YouTube video](https://www.youtube.com/watch?v=azUdn-XBjQU)

In the event MetaView can update the app to support 4.x firmware, we’ll update.

[Talk about it or get support here.](http://forums.webosnation.com/webos-homebrew-apps/331159-connecting-pebble-webos-using-mwatch.html)

#webOSForever
