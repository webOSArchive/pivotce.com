---
title: 'Guide: Coming (Back) to webOS in 2014, Part 1'
date: '2014-10-21T01:54:22Z'
lastmod: '2018-08-11T00:11:35Z'
author: Brent Hunter
author_slug: brenthunter
categories:
- Tutorial
slug: guide-coming-back-to-webos-in-2014-part-1
summary: '** PLEASE NOTE: Following the closure of the HP app catalogue, instructions in this article involving the HP servers are no longer relevant and have been crossed out. ** So,…'
featured_image: /images/files/2014/10/guidecomingbackheader.jpg
source_url: https://pivotce.com/2014/10/21/guide-coming-back-to-webos-in-2014-part-1/
wordpress_id: 2200
featured_image_source: https://pivotce.com/files/2014/10/guidecomingbackheader.jpg
archived: true
---

** PLEASE NOTE: Following the closure of the HP app catalogue, instructions in this article involving the HP servers are no longer relevant and have been crossed out. **

---

So, you’ve decided to get yourself a “new” webOS-powered smartphone (or dig one out of the closet)! Let me be the first to welcome you to the family. We have suffered some blows recently, with [HP finally shutting down app catalog purchases](/2014/10/16/hp-to-shut-down-catalog-and-cloud-services/) as of November 1, 2014, and closing down the Palm Profile servers as of April 15, 2015. But all of the devices and other services will continue to work, and many developers are making their apps available through homebrew channels.

We believe this is still the most intuitive and easiest to use mobile platform, and we still have the greatest community dedicated to keeping it that way!

This guide is the first in a series of guides that will help you get started with your new webOS smartphone, as there have been a few changes to the ecosystem since the official manuals were written. This guide focuses on getting your webOS smartphone activated and ready to use. Later guides will cover optimizing your device, available apps, and some interesting things that you can do which were never covered by the official documentation.

This guide assumes that you have either:

1. A phone that has been locked to the carrier of your choice and an appropriate SIM card; or
2. An unlocked phone and SIM card that will work on the carrier of your choice.

Here’s what I’ll cover in the guide:

1. ~~Create a new Palm Profile~~
2. Get Connected (Optional)
3. ~~Roll back the clock and update the app catalog~~
4. Enable Developer Mode
5. Download webOS Quick Install
6. Install the Root Certificate Update
7. Prepare for Patching
8. Install the Google and Yahoo Sync Patches
9. Enable Access for “Less Secure Apps” on Google (Optional)
10. Install Preware

By the end of this guide, you’ll be ready to install applications, add accounts, and get to work.

#### Before We Begin:

If you’re not familiar with webOS and the way that gestures work, I recommend watching [this video](https://www.youtube.com/watch?v=kOuvfDRBjbE) before starting this guide.

The video was originally released when the first Palm Pre came out, so the process has changed slightly, but all of the gestures and the way that you interact with the phone are still basically the same.

#### ~~Step 1: Create a new Palm Profile~~

![firstuse_2014-20-10_203941](/images/files/2014/10/firstuse_2014-20-10_203941.png)Insert your SIM card and power up your phone. As soon as the phone finishes booting, ~~it will run you through the process of creating a Palm Profile (or logging into an existing one) and doing the initial setup of your phone~~ (this will no longer work, so the next two paragraphs are now REQUIRED. See also [this information on bypassing activation](/2015/06/24/tip-how-to-bypass-activation/)).

If you have to manually configure your APN settings you’ll need to bypass activation by tapping the phone icon, tapping Emergency Call, backing out 911, and entering #*DEVMODE# and tapping the call button. Then toggle Developer Mode to on, confirm, and tap Submit. Restart your phone and then you’ll need [Impostah](http://forums.webosnation.com/webos-internals/270316-impostah.html).

![devmodeswitcher_2014-20-10_213843](/images/files/2014/10/devmodeswitcher_2014-20-10_213843.png)For those with a CDMA webOS phone, you can tap the phone icon, back out 911, and dial your carrier’s activation number. Then simply backswipe or turn off your device and turn it back on to resume setup. You can also bypass activation with ##DEVMODE# (yes that’s a second # and not a *) but you don’t have to press call.

If you’d like a bit of practice with gestures, I’d also highly recommend running through the gesture tutorial when it’s offered.

#### Step 2: Get Connected (Optional)

![wifi_2014-20-10_213230](/images/files/2014/10/wifi_2014-20-10_213230.png)Some of the things that you are going to be doing from here on will require a bit of mobile data, so if you have a Wi-Fi network available, I recommend that you connect to it.

From card view (even if you have no cards up right now), either tap on the launcher arrow or use the Up gesture to bring up the launcher, and swipe over to the “System” panel. Then, find the “Wi-Fi” app and tap on it to launch.

Make sure that Wi-Fi is turned on, and you will see a list of available networks in range. Tap on the one that you would like to connect to, and enter the network password (if necessary).

Once you’re connected, use the Up gesture to get back into card view and toss the Wi-Fi card away.

#### ~~Step 3: Roll back the clock and update the app catalog~~

![findapps_2014-20-10_214842](/images/files/2014/10/findapps_2014-20-10_214842.png)~~On July 23, 2013, the webOS root certificate expired. This means that new webOS devices cannot access the App Catalog to download and update applications or access other services such as Backup, without first installing a new certificate.~~ Please note that this procedure is only necessary until ~~January~~ April 15, 2015, at which point the services that this certificate is needed for will stop functioning.

~~HP was kind enough to push out an update to the App Catalog that included a new certificate. Unfortunately, you can’t download and install it after July 1, 2013 because the certificate to allow you to do so has already expired. Fortunately, there’s a workaround for that!~~

1. ~~Open the “Date & Time” app on your device. This is typically on the “System” or “Settings” page/tab of your launcher.~~
2. ~~Set “Network time” to Off.~~
3. ~~Set the date to July 1, 2013.~~
4. ~~Open the App Catalog. This is typically on the first page of the launcher.~~
5. ~~Type “App Catalog Update” in the search field, and hit “Enter” on the keyboard.~~
6. ~~Tap “Download for Free” to download and install the app.~~
7. ~~Go back to the “Date & Time” app.~~
8. ~~Set the date back to the current date.~~
9. ~~Set “Network Time” to On.~~

#### Step 4: Enable Developer Mode

While HP stopped most support for webOS back in 2012, there is still a vibrant developer community that works tirelessly to keep our webOS devices working in the modern world. They can do that because Palm made a commitment to make webOS devices easy to tweak and modify, and load homebrew applications onto. HP kept up that commitment.

To fix a few services that have broken over the years and get your webOS device working to it’s full potential, we’re going to take advantage of some of that work, and to do so, we need to enable a feature called “Developer Mode”, which will allow us to apply this custom work to our devices.

![Unknown_2014-20-10_213831](/images/files/2014/10/Unknown_2014-20-10_213831.png)Get your device into card view and type webos20090606 on the keyboard. You’ll see an application named “Developer Mode Enabler”. Tap on that, and when it launches, switch the toggle button for developer mode to On.

The screen may grey out for a second, but when it comes back, you should see the message: “Your device is in Developer Mode. You may use Palm Mojo SDK tools to connect to the device.” When see that, you’re good to go, and can toss the card away.

#### Step 5: Download WebOS Quick Install

NOTE: For this step, you’ll need a computer that is running Java 6 or later (available from [java.com](http://www.java.com)).

WebOS Quick Install, developed by [Jason Robitaille](http://canuckcoding.ca/) is the premier tool for getting homebrew applications, tools and patches from a computer onto a webOS device.

Simply download it from [here](https://forums.webosnation.com/canuck-coding/274461-webos-quick-install-v4-6-0-a.html) and save it to a location of your choice.

For more information on WebOS Quick Install, check out the [official thread](http://forums.webosnation.com/canuck-coding/274461-webos-quick-install-v4-5-0-a.html).

#### Step 6: Install the GlobalSign SSL Update.

Around January 28, 2014 a core GlobalSign SSL certificate expired, breaking Hotmail and Outlook.com accounts, and causing the webOS browser to stop trusting the certificates on many sites. Patch guru Matt Williams (Grabber5.0 on the webOS nation forums) quickly came up with a fix, putting together an updated certificate package to fix this problem, and making it available for download.

To install this update:

1. Download the package and save to a location of your choice: [Globalsign Root Certificate Updater](http://www.fordmaverick.com/GrabberSoftware/GlobalSignCertFix/com.grabber.globalsigncerts_1.0.5_all.ipk)
2. Plug your device into your computer, and when asked if you want “USB mode” or “Just Charge”, pick “Just Charge”.
3. Launch WebOS Quick Install by double-clicking on the file that you downloaded.
4. Make sure that your device shows up in the upper right hand corner. (If this is your first time running the tool, you may be asked to install novacom drivers. These are what the tool uses to communicate with your phone. In that case, just follow the prompts).
5. Click on the green plus icon on the right hand side of the window, navigate to the file that you downloaded, and hit select.
6. Click the “Install” button, and wait for the tool to install the package. When it is done, the list of files to install will be empty, and you’ll be good to go.

If you need more detailed information, you can check out the original thread [here](http://forums.webosnation.com/webos-discussion-lounge/327226-solved-microsoft-outlook-certificate-expired-6.html#post3413122).

#### Step 7: Prepare for Patching

![wosqi](/images/files/2014/10/wosqi.png)In order to install “Patches”, bits of code that correct problems or change behaviors on your device, as wee will need to do in the next step, you will need to install a few programs to make that possible: AUSMT Scripts, GNU Patch, and Lsdiff.

If you haven’t already, Plug your device into your computer, and when asked if you want “USB mode” or “Just Charge”, pick “Just Charge” and launch [WebOS Quick Install](/2014/08/31/tip-preware-net-solutions-for-wosqi-preware-v1-9-13/).

1. Make sure that your device shows up in the upper right hand corner.
2. Click on the “Globe” icon on the right-hand side (see thumbnail above). This gives you access to the Homebrew Catalog window.
3. Along the top of the window, you will see several options (Applications, Services, Plugins, etc.). Click on “Linux Apps”.
4. In the list on the left, find “AUSMT Scripts” and click on it. Then click the “Install” button at the bottom of the right hand panel.
5. Once the install has completed, in the list on the left, find “GNU Patch” and click on it. Then click the “Install” button at the bottom of the right hand panel.
6. Once the install has completed, in the list on the left, find “Lsdiff” and click on it. Then click the “Install” button at the bottom of the right hand panel.
7. When all of these installs are complete, you can close the Homebrew Catalog window.

#### Step 8: Install the Google and Yahoo Sync Patches

In Late March – Early April of 2014, Google and Yahoo both began requiring secure connections when synchronizing data, and this broke the contact synchronization service in webOS. Fortunately, Matt Williams and frantid were on the case and came up with a solution to the Google problem. When the Yahoo problem started a week later, Matt was able to identify it as similar to the Google problem and fix it.

To install these patches:

1. Download the Google patch from Matt’s site and save to a location of your choice: <http://fordmaverick.com/GrabberSoftware/GoogleSyncFix/gsync-1.2.patch> (Note: you may need to right click on the link and click save as, or your browser may try to open it).
2. Download the Yahoo patch from Matt’s site and save to a location of your choice: <http://fordmaverick.com/GrabberSoftware/YahooSyncFix/ysync.patch> (Note: you may need to right click on the link and click save as, or your browser may try to open it).
3. If you haven’t already, Plug your device into your computer, and when asked if you want “USB mode” or “Just Charge”, pick “Just Charge” and launch WebOS Quick Install.
4. Make sure that your device shows up in the upper right hand corner.
5. For each of the patches, click on the green plus icon on the right hand side of the window, navigate to the file that you downloaded, and hit select.
6. Making sure that both files are in the “Files to Install” list, click the “Install” button.
7. When finished, your device will restart, and you can quit webOS Quick Install.

If you need more detailed information, you can check out the original threads [here (Google)](http://forums.webosnation.com/webos-patches/327662-patch-google-sync-https-fix-unknown-error-sign.html) and [here (Yahoo)](http://forums.webosnation.com/webos-synergy-synchronization/327645-yahoo-contact-sync.html#post3417582).

#### Step 9: Enable Access for “Less Secure Apps” on Google (Optional)

If you plan to add Google accounts to your webOS device, you may need to enable this feature on each Google account that you plan to add, as webOS uses an older method of signing into Google that Google considers “less secure.”

1. Go to <https://www.google.com/settings/security/lesssecureapps>
2. Sign into your Google Account.
3. Click “Enable”
4. Click “Done”

#### Step 10: Install Preware

![preware_2014-20-10_213512](/images/files/2014/10/preware_2014-20-10_213512.png)Preware allows you to install homebrew software and patches directly from your device, without requiring the use of a computer. We just need the computer to get it on there in the first place.

1. If you haven’t already, plug your device into your computer, and when asked if you want “USB mode” or “Just Charge”, pick “Just Charge” and launch WebOS Quick Install.
2. Make sure that your device shows up in the upper right hand corner.
3. Click on the “Globe” icon on the right-hand side. This gives you access to the Homebrew Catalog window.
4. Along the top of the window, you will see several options (Applications, Services, Plugins, etc.). Click on “Applications”.
5. In the list on the left, find “Preware” and click on it. Then, click the “Install” button at the bottom of the right-hand panel.
6. When the install is complete, you can close the Homebrew Catalog window and quit WebOS Quick Install
7. On your phone, launch Preware. It will have been installed under the “Applications” panel of the launcher, right at the bottom.
8. Read the introduction, then tap the “Ok, I’ve read this. Let’s continue…” button, and wait for Preware to update its feeds.
9. When Preware asks you if you would like to associate the “.ipk” filetype, tap yes.

From here, we are no longer tethered to a computer and will be using Preware to do all of the application and patch installations. Also, now that the HP App Catalog is closed, Preware is the best way of getting new applications onto your device.

#### What Next?

You now have a webOS device that is ready to use! You can install applications, add accounts, and start using it like it was meant to be used.

From here, I recommend that you:

1. Take a look at the [manual for your device](http://kb.hpwebos.com/wps/portal/kb/common/article/72880_en.html) to learn how to use some of the core applications. Or, if you’re more of a visual learner, you can watch some of webOS Nation’s (formerly PreCentral) walkthrough videos ([email](https://www.youtube.com/watch?v=CAhcWCbz0T4); [Preferences](https://www.youtube.com/watch?v=h968SVJBjwU); [Contacts, Calendar, Tasks and Memos](https://www.youtube.com/watch?v=NUOV9zzxYqQ); and [Messaging](https://www.youtube.com/watch?v=ZJ9xDsyfEVg).) Again, these videos were originally released when the first Palm Pre came out, so things have changed somewhat, but are still very similar.
2. Sign up for an account on the [webOS Nation forums](http://forums.webosnation.com). It’s the largest gathering place for those running and working on webOS, and has a huge backlog of answers to problems, as well as many knowledgeable users who can help you if you run into a new one.
3. Take a good look through the Preware catalog and the [webOS Nation App Gallery](http://www.webosnation.com/app-gallery/homebrew) (all of the apps there are available through Preware) to see what applications you might find useful. They’re all free, but don’t forget to donate to the developers for all of their hard work!

Even though your device is working now, you can make it work better. Take advantage of homebrew tweaks and optimizations in the next installment of this guide.

[Join the conversation about this article!](http://forums.webosnation.com/general-news-discussion/328756-pivotce-guide-coming-back-webos-2014-part-1-a.html) Or you can [read part 2](/2014/11/02/guide-coming-back-to-webos-in-2014-part-2/).
