---
title: 'Guide: Coming (Back) to webOS in 2014, Part 2'
date: '2014-11-02T15:46:25Z'
lastmod: '2015-04-21T19:09:41Z'
author: Brent Hunter
author_slug: brenthunter
categories:
- Tutorial
tags:
- coming back
slug: guide-coming-back-to-webos-in-2014-part-2
summary: So, you’ve got your new webOS-powered smartphone set up with the latest fixes from my Coming (Back) to webOS Guide, Part 1 and you’re ready to get started? Great! You…
featured_image: /images/files/2014/11/comingbackwebos.jpg
source_url: https://pivotce.com/2014/11/02/guide-coming-back-to-webos-in-2014-part-2/
wordpress_id: 2205
featured_image_source: https://pivotce.com/files/2014/11/comingbackwebos.jpg
archived: true
---

So, you’ve got your new webOS-powered smartphone set up with the latest fixes from my [Coming (Back) to webOS Guide, Part 1](/2014/10/21/guide-coming-back-to-webos-in-2014-part-1/) and you’re ready to get started? Great!

You may have noticed that webOS can be a bit slow at times but don’t worry, the community has got your back and has released a slew of patches and tips designed to speed your device right up!

This guide will walk you through the steps necessary to tune and optimize your device including detailing the patches necessary to make sure that you have the best webOS experience possible.

This guide assumes that you have completed the previous guide, and have an activated webOS smartphone that you have already installed Preware on.

Now that your phone is running, here are my recommendations to tune it up and turn it into the shiniest new phone on the block:

1. Disable Excess Logging
2. Install the Tweaks Application
3. Install Patches and Tweaks
4. Install UberKernel
5. Install Govnah and Overclock Your Device

#### Step 1: Disable Excess Logging

Note: This step could cause troubleshooting down the road with apps like [Lumberjack](http://forums.webosnation.com/webos-internals/259538-lumberjack.html) to be a bit harder. If you’re ok with that, proceed.

![Logs](/images/files/2014/10/collectlogs_2014-01-11_213855.png)One issue with webOS devices is that out of the box, there is a lot of excess logging going on which causes the device to run a bit slower than it should be. None of this logging is necessary, so we’ll just turn it off.

On your phone, open up the phone application and punch in #*5647# (##5647# on CDMA devices ie. Verizon) on the dial pad and press the call button. This will launch the “Collect Logs” application. On a TouchPad, just type “Dialler” or “Phone” to get a launcher icon, select the phone tab and press the dialpad button. Use ##5647#.

Next, tap the “Clear Logs” button, and then “OK” when it warns you about clearing the logs, and “OK” again when you get the success message.

Finally, tap the “Change Logging Levels” button, then the “Set Logging to Minimal” button, and “OK” at the warning, and “OK” again at the success message. You can then close the logging and phone apps.

#### Step 2: Install the Tweaks Application

![Tweaks](/images/files/2014/10/tweaks_2014-01-11_214232.png)The application, Tweaks,  allows you to enable modifications for various applications and preferences that let you turn on and off certain options that are either added by homebrew developers or are hidden by the system. We will install the application here, and add some tweaks later.

1. Open up Preware if you don’t have it open already.
2. From the main screen, just start typing and then hit enter to search. Type **tweaks**, which should bring up the Tweaks application by WebOS Internals.
3. Tap on Tweaks, then tap “Install” at the bottom.
4. Preware will download and install the application, then let you know when the installation is complete. When it is complete, tap the “OK” button.
5. Use the back gesture until you get back to the main screen.

#### Step 3: Install Patches and Tweaks

![Patches](/images/files/2014/10/preware_2014-01-11_215012-180x300.png)Next, we’ll install a series of patches and tweaks designed to make your phone work faster, better, and more smoothly. After you install the patches, you don’t have to do anything more. The tweaks can be toggled on and off by using the Tweaks application.

Each of the patches and tweaks that we install will follow the same general procedure:

1. Open up Preware if you don’t have it open already.
2. From the main screen, just start typing the name of the patch or tweak and then hit enter to search.
3. Tap on the patch or tweak, then tap “Install” at the bottom.
4. Preware will download and install the patch or tweak, and then let you know when the installation is complete.
5. Some patches require a device or Luna restart. When the installation is complete, tap the “Ok” button, to acknowledge the application installation or to restart your device (as necessary).
6. If you did not need to restart the device or Luna, use the back gesture until you get back to the main screen.

Repeat this procedure to install the following patches and tweaks:

1. EOM Overlord Monitoring – This stops your device from uploading information such as the list of installed applications, wifi access points, and other information to the Palm servers. This is both unnecessary and a waste of system resources.
2. Muffle system logging – This works with the logging fix in step 1 to make sure that your device is not wasting system resources by logging unnecessary information.
3. Remove Dropped Packet logging – another patch to stop unnecessary logging, this time from the firewall.
4. Unset CFQ IQ scheduler – A patch to help with installing custom kernels and overclocking (covered in more detail later.)
5. Quiet powerd messages – another patch to stop unnecessary logging, this time from unnecessary sleep/wake messages. NOTE: powerd is the correct spelling, not a typo.
6. Unthrottle Download Manager – Removes the artificial limit stopping downloads from going more than 64kb/sec.
7. Buttah – Makes scrolling and other behaviors more precise and smoother – eliminates some of the jitteriness that webOS sometimes displays when scrolling or loading elements/apps.
8. Faster Card Animations HYPER Version – Speeds up the loading animations on applications and new cards.
9. Mojo Flick Regulator – Lowers scrolling speed to match that of the browser, making for a more unified experience.
10. Mojo FPS Booster – Increases UI smoothness by increasing Mojo’s FPS to 60.
11. Mojo Tap Responsiveness – makes button taps more responsive.
12. Ad Blocker **OR** Max Block – Block annoying ads in your browser. Install Max Block. Remove and install Ad Blocker only if you have problems. **NEVER** install both.
13. Behavior and Options tweaks – Add a private browsing mode to the browser, as well as several options available through the tweaks application.
14. Uber Cycling Email Dashboard – When multiple email messages have been received, cycles through them on the dashboard instead of only displaying the most recent one.
15. Google Sync Behaviors Patch – If you plan to use a Google account, this resolves some synchronization issues.

Feel free to browse around the Preware catalog to discover other apps and patches by going to “Available Packages” from the main menu, and install anything that looks like it might improve your webOS experience. Make sure to read the descriptions before you install things so that you have a good idea of what they do.

[Here’s a great thread](http://forums.webosnation.com/hp-pre-3/324767-big-patch-thread-tbpt-pre-3-a.html) on the forums about setting up a Pre3 but it can be used as a template for other webOS devices as well.

#### Step 4: Install UberKernel

![Uberkernel](/images/files/2014/10/preware_2014-01-11_215431.png)Now that your phone has been sped up as much as the vanilla version of webOS will allow, and you’ve installed some patches to improve and customize your experience, it’s time to take the next step – installing a new kernel. This package (relatively) safely replaces the core software on your device with the best homebrew has to offer, improving memory management, and giving you the ability to overclock your device. You can read more about it [here](http://forums.webosnation.com/webos-internals/242728-webos-internals-uber-kernel.html).

That being said, while this is a reasonably safe procedure, it does have the potential to void your warranty if something goes wrong, so proceed at your own risk. If you’re not sure about this, feel free to skip to the “What’s Next?” section of this guide.

1. Open up Preware if you don’t have it open already.
2. Type “UberKernel”, and this should bring up the “UberKernel” kernel by WebOS Internals.
3. Tap on “UberKernel”, then tap “Install” at the bottom.
4. Preware will download and install “UberKernel”, and then let you know when the installation is complete.
5. When the installation is complete, tap the “Ok” button to restart your device.

#### Step 5: Install Govnah and Overclock Your Device

![Govnah](/images/files/2014/10/govnah_2014-01-11_215510.png)Now that you have the new kernel, you’re ready to overclock your device. Overclocking allows us to get a bit more speed out of the device by asking the processor to run faster than the system originally specifies, making everything go faster. We do this using an [application called Govnah](http://forums.webosnation.com/webos-internals/244701-govnah.html) that allows you to tweak some settings very deep inside your device, giving you some incredible customization options. Fortunately, while the power is there, there are some conveniently available presets for us.

1. Open up Preware if you don’t have it open already.
2. Type “Govnah”, and this should bring up the “Govnah” application by WebOS Internals.
3. Tap on “Govnah”, then tap “Install” at the bottom.
4. Preware will download and install “Govnah”, and then let you know when the installation is complete.
5. When the installation is complete, tap the “Ok” button to acknowledge that the application has been installed.
6. Hit the “Launch” button to launch Govnah.
7. Read the introduction, then tap the “Ok, I’ve read this. Let’s continue…” button.
8. Tap on “Profile”, which should read “UberKernel Default” right now. This will give you the option to choose an overclocking profile.
9. Choose a profile and close the app.

Overclocking is very device-specific, so this will require a bit of experimentation to figure out what speed your device is stable at. In general, you should be able to use the OnDemandTcl profile with the highest number, but if you run into crashes, overheating or poor battery life, you’ll want to go back into Govnah and set your profile down a few notches until you find one that works for you.

#### What’s Next?

So that’s it! You have a fully tweaked webOS phone with a shiny new overclocked kernel that is now fully optimized for everyday use.

From here, I recommend that you:

1. Take a good look through the Preware catalog to see what patches you might find useful. They’re all free, but don’t forget to donate to the developers for all of their hard work!
2. Start adding accounts, if you haven’t done so already.
3. Learn more about webOS! The [webOS Nation archives](http://www.webosnation.com/content/articles) and [forums](http://forums.webosnation.com/) are a great place to start.
4. Last but not least, stay tuned to this space, where we will cover some of the cool things that you can do with your device.

[Join the conversation about this article!](http://forums.webosnation.com/general-news-discussion/328836-pivotce-guide-coming-back-webos-2014-part-2-a.html)
