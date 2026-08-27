---
title: 'Guide: Fixing Google Synergy'
date: '2016-07-07T07:42:53Z'
lastmod: '2024-01-25T22:25:36Z'
author: Alan Morford
author_slug: alanmorford
categories:
- Tutorial
slug: guide-fixing-google-synergy
summary: 'Here’s the scenario: you’ve dug out your Pre or TouchPad and for nostalgia sake try to set it up only to find that things are a bit tougher to get…'
featured_image: /images/files/2016/07/google-wallpaper-9.jpg
source_url: https://pivotce.com/2016/07/07/guide-fixing-google-synergy/
wordpress_id: 3694
featured_image_source: https://pivotce.com/files/2016/07/google-wallpaper-9.jpg
archived: true
---

Here’s the scenario: you’ve dug out your Pre or TouchPad and for nostalgia sake try to set it up only to find that things are a bit tougher to get working. I feel ya. This guide aims to help some of that frustration as it relates to Google Synergy.

![googlebroken](/images/files/2014/05/googlebroken-300x240.jpg)If you feel like we’ve written about this before [you](/2014/05/07/tip-fix-google-account-authentication-error/) [aren’t](/2015/07/25/guide-getting-around-the-yellow-gmail-triangle-of-death/) [wrong](/2014/11/11/use-caldav-to-maintain-google-calendar-sync/). In fact, the [C+Dav solution](/2015/06/11/cdav-synergy-connector-updated-for-webos/) still works but won’t fix Google synergy. It WILL solve syncing calendar and contacts for webOS 2/3.x though and is built-in to LuneOS as well. Read up on it and [get the files here](http://webos-ports.org/wiki/C%2B_Dav_Synergy_Connector) if you’re on webOS. But this article isn’t about C+Dav, it’s about Google Synergy.

This guide will assume you don’t have a Google account on your device yet. I’m not going to tell you to delete your Google account if it’s already there, I’m just saying it’ll likely work better if it’s a clean slate anyway. YMMV! Follow these steps at your own peril!

For the advanced user, simply browse to the sources of this guide: install [OpenSSL Updater](http://forums.webosnation.com/webos-internals/330666-openssl-updater-fixing-certificate-issues.html) from the Preware Alpha Feeds and the [Oauth2 patch](http://forums.webosnation.com/webos-patches/286029-google-calendar-sync-behaviors-patch.html) from the forums.

If you have a freshly doctored or reset device and are stuck at the Palm/HP Profile creation screen you’ll need to bypass activation:
[Bypass Activation [webOS 1.x]](http://www.webosnation.com/bypass-activation-webos-1-x) (this now works for all webOS versions if you use the [devicetool.jar from here](/2015/12/13/the-ultimate-bypass-activation-tool/)).

### A couple quick notes

###### webOS 2.1.x

If you are about to accomplish this tutorial on a webOS device with version 2.1.x you should stop. OpenSSL Updater does more harm than good for 2.1.x. You’ll need to follow the C+Dav solution for Contacts and Calendar syncing (linked above) and also [download Certificate Grabber from Preware](http://preware.pivotce.com/package/com.grabber.basiccertgrabber) to get Gmail to work. Google Chat may not connect with this method though.

###### webOS 1.4.x

For those still using webOS devices on version 1.4.x you do not *have* to install OpenSSL Updater to get Gmail to work. Optionally get [Certificate Grabber from Preware](http://preware.pivotce.com/package/com.grabber.basiccertgrabber) and install the latest Google certificates with it, open the Email app, and login to Google. You will have to get new certificates using Certificate Grabber from time to time with this method but it will work. If you’d rather not use Certificate Grabber periodically then continue the guide.

Sadly, for webOS 1.4.x, email is the only Google synergy service that can still be made to work.

### Let the guide begin – OpenSSL Updater

![preware_2016-07-07_015740](/images/files/2016/07/preware_2016-07-07_015740.png)If you didn’t just bypass activation you MIGHT need to enable developer mode:

On webOS 2/3.x get your device into card view and type webos20090606 on the keyboard. You’ll see an application named “Developer Mode Enabler”. Tap on that, and when it launches, switch the toggle button for developer mode to On.

If you’re on a webOS 1.x device you’ll need the [devicetool.jar from here](/2015/12/13/the-ultimate-bypass-activation-tool/) to do it or if you already have Preware installed you can grab the [Unhide Dev Mode Icon](http://preware.pivotce.com/package/org.webosinternals.patches.app-launcher-unhide-dev-mode-icon) installer to check that it’s still enabled.

If you have Preware installed and don’t already have the Alpha Feeds enabled, you must uninstall Preware now. Trust me.

Get webOS Quick Install (WOSQI). Simply download it to your computer from [here](https://github.com/JayCanuck/webos-quick-install/releases/download/4.6.0/WebOSQuickInstall-4.6.0.jar) and save it to a location of your choice. You’ll need java installed on your computer to use it.

Read the [Enable the Alpha Feeds for Preware](http://www.webos-internals.org/wiki/Testing_Feeds#Enabling_the_Alpha_Testing_Feeds) page for warnings. To enable the alpha feeds for Preware, plug in the device to your computer and launch WOSQI. If WOSQI can’t see your webOS devices you’ve either not enabled developer mode or novacom isn’t installed. Install novacom by clicking the ‘reinstall novacom’ button. In WOSQI click Tools and then Linux Commandline and simply copy and paste these commands.

```
mkdir -p /var/preferences/org.webosinternals.preware
touch /var/preferences/org.webosinternals.preware/enable-alpha-feeds
```

![preware_2014-20-10_213512](/images/files/2014/10/preware_2014-20-10_213512.png)[Follow Step 10](/2014/10/21/guide-coming-back-to-webos-in-2014-part-1/) from our guide to install Preware then come back!

Open Preware and swipe down from the top left and tap Manage Feeds and enable the alpha-apps feed. Swipe back and update the feeds now.

In Preware search for OpenSSL Updater. See [OpenSSL-Updater – Fixing Certificate Issues](http://forums.webosnation.com/webos-internals/330666-openssl-updater-fixing-certificate-issues.html) for warnings. Install it. This should reboot your device after it finishes.

### 1.x devices only – STOP

**If you are on webOS 1.x, this is as far as you can go.**After the reboot, open the Email app and login to Google with your username and password. Email works but Contact and Calendar sync for webOS 1.x is dead! You’ll have to manually import contacts and calendar entries. If you have a webOS 2.x device too, you can [export all of your contacts from there into one file](http://www.webosnation.com/export-all-your-contacts), transfer that file to your 1.x device, and open it with [Internalz Pro](http://preware.pivotce.com/package/ca.canucksoftware.internalz) to auto-import them.

### Oauth2 patch for webOS 2/3.x

~~Now that you’ve got OpenSSL Updater installed you *could* go ahead and login to your Google account and if all you need is email (messaging also works this way) then go for it. BUT if you also want your calendar and contacts, read on.~~ Nope! I was wrong.

You need the Oauth2 patch for your device [from here](http://forums.webosnation.com/webos-patches/286029-google-calendar-sync-behaviors-patch.html). You should also read the instructions there too but in summary be warned! Put your device in airplane mode for the install and they recommend placing it on a charger as well but it’s already plugged into your computer per this guide! This patch can conflict with other patches so read about that in the first post too. Now scroll to the bottom of the first post and click on either phone version or touchpad version. This will take a little understanding but the device and webOS version are in the patch name so that should help.

Once you’ve deduced which patch you need, download it on your computer.

Plug your device into your computer and open WOSQI. Drag the patch file into it and click install. Luna should restart but if not just reboot your phone.

### Log in

![accounts_2016-07-07_015658](/images/files/2016/07/accounts_2016-07-07_015658.png)Now that OpenSSL Updater and Oauth are installed it’s finally time to login to Google Synergy! Note: make sure the date and time are right on your device before you proceed. You might also need to [enable less secure apps](https://support.google.com/accounts/answer/6010255?hl=en).

Go to Accounts and tap the Add Account button and then Google. Things split for a second in this next part.

### 2.x Phone

![accounts_2016-07-07_015540](/images/files/2016/07/accounts_2016-07-07_015540.png)Enter your email and password and tap Sign in. It’ll think for a bit and then you’ll see a pop-up about Oauth2 Not Configured. Just tap OK and then Create. It should pop you back out to the Accounts screen. Tap the Google account you just created and  tap Change login settings.

You’ll see two options. Tap Oauth2 and you’ll get a new card. Tap Get Token. Now you must enter your account email and password again. Tap Allow to give access to ubercalendar. Once you’re back to the Get Token screen again you can swipe away the card.

Back in the Google account you can now toggle Contacts and Calendar to on.

The Google Syncing Accounts… notification might pop up and go away relatively quickly. That’s normal. If contacts or calendar events don’t start showing up within a few minutes simply open their respective apps and swipe down from the top left, tap preferences and tap the Sync Now button.

### TouchPad

On the TouchPad, enter your email and password and then tap Get Token. Enter your email and password and tap Allow for ubercalendar. Tap Sign in.

You can now toggle on or off anything you’d like and then tap Create Account.

**You did it!**

### You might also consider

Step 6 from our [Coming (Back) to webOS in 2014 guide](/2014/10/21/guide-coming-back-to-webos-in-2014-part-1/) is a good idea as well but not required. Might as well get all of those certificates updated though.

Have questions? [Ask them here](http://forums.webosnation.com/webos-discussion-lounge/331284-pivotce-guide-fixing-google-synergy.html)!

#webOSForever
