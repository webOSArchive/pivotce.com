---
title: The search for real 4G on the TouchPad
date: '2014-01-27T01:39:37Z'
lastmod: '2015-04-21T18:50:13Z'
author: Herrie
author_slug: herrie
categories:
- Tips
slug: the-search-for-real-4g-on-the-touchpad
summary: A commonality among webOS enthusiasts is their ability to maintain the usefulness, applicability, and capabilities of their favorite aging hardware. The GSM Pre3 and Veer were touted as having 4G…
featured_image: /images/files/2014/01/Webhosting-Internet-13.jpg
source_url: https://pivotce.com/2014/01/27/the-search-for-real-4g-on-the-touchpad/
wordpress_id: 1283
featured_image_source: https://pivotce.com/files/2014/01/Webhosting-Internet-13.jpg
archived: true
comment_page: 2014-01-27-the-search-for-real-4g-on-the-touchpad
---

![4gtouchpad](/images/files/2014/01/4gtouchpad-291x300.png)A commonality among webOS enthusiasts is their ability to maintain the usefulness, applicability, and capabilities of their favorite aging hardware.  The GSM Pre3 and Veer were touted as having 4G capability but truly only have “FauxG” speeds.  That same fact resounds for owners of the HP TouchPad 4G or the much more rare and GSM-capable HP TouchPad Go.  Oh well, speeds are slower but we don’t really care because we love these devices, right?  Sort of!  We DO love the devices but who can leave “well enough” alone?  Grab your favorite spudger and torx screwdriver set because what I’m about to show you will have you clamoring to replace the old Ericsson card inside your “4G” TouchPad and you’ll be surprised just how simple it is to do.

# Greetings!

Even though webOS products were not widely available in Europe and not officially available in quite a few European countries, **there is still a considerable amount of very dedicated users all over Europe**. So for those of you in Europe, like me, I’d like to [highlight a patch](http://forums.webosnation.com/webos-patches/326601-patch-sierra-mc7710-support-webos-3-0-x.html) that is proving VERY useful (I’m in the Netherlands).  You might know me from some of the patches I’ve published in the past and for the unofficial updates to 2.2.3/2.2.4 for the HP Veer.  **But this is about how I upgraded my AT&T HP TouchPad 4G** (well actually FauxG as I mentioned (but more about that later)) **to actual 4G speeds in Europe!**

# About the HP TouchPad 4G

The TouchPad 4G was originally tested for various carriers around the world including AT&T and Verizon in the US.  Unfortunately, due to the cancellation of webOS by HP, none of these devices were officially released.  The AT&T TouchPad 4G was produced in quite some quantity and they eventually found their way to the market mainly via eBay and CraigsList, etc.

The AT&T HP TouchPad 4G is equipped with an Ericsson F5521gw Mini PCI-Express Card allowing up to 21Mbps, which AT&T labelled 4G when it’s actually HSDPA or also called FauxG. During testing, HP used Mini PCI-Express Cards from various manufacturers including the Sierra Wireless MC7700 for the US (GSM) market. There also exists a Sierra MC7750 for Verizon in the US and a Sierra MC7710 for European 4G bands.  The Sierra Wireless MC77XX series offers up to 100 Mbps download speeds which is proper 4G. You can read all about Sierra cards [here](http://www.sierrawireless.com/productsandservices/AirPrime_Wireless_Modules/Essential_Modules/~/media/Data%20Sheet/AirPrime_datasheets/Sierra_Wireless_AirPrime_MC_Series_Intelligent_Embedded_Modules.ashx) (.pdf).

A number of US-based users on the forums of webOS Nation have successfully replaced their Ericsson F5521gw card with a Sierra MC7700 for proper 4G speeds (webOS 3.0.x fully supports both the Ericsson and Sierra cards out of the box).

# Open it up

The procedure for opening the tablet is *not incredibly* easy, but the procedure is described in detail on [iFixit](http://www.ifixit.com/Guide/HP+TouchPad+Battery+Replacement/6082).  **Please note:  the TouchPad 4G has 8 clips instead of the 7 mentioned for the WiFi version.**  It’s a bit of fiddling, but once you have the TouchPad open, replacing the Mini-PCI Express card is a piece of cake!  Forums user, aboutblank, kindly uploaded some more pictures of their opened TouchPad 4G showing the opened device and the card taken out [here](http://forums.webosnation.com/hp-touchpad/313055-touchpad-4g-unlocked.html). In the event you happen to have a rare TouchPad Go it’s *a lot* easier because it has a removable back and replacing the module includes removing a piece of tape, 2 cables and 2 screws!

# A roadblock on the way to cell signal

I got my TouchPad 4G at the back end of last year from the US and after the successful reports from the people who replaced their Ericsson F5521gw with a Sierra MC7700 and the confirmation that a Sierra MC7710 **should** work as well, I also bought a Sierra MC7710 and tried to get it working.  Unfortunately, the TouchPad 4G with webOS wouldn’t recognize the Sierra MC7710 (no signal bar, no carrier name, diagnostics app couldn’t do GPS test, etc).  I dual-booted Android on the tablet and interestingly it worked fine though. So it had to be something on the webOS side that wasn’t working properly.

Initially I worked together with community members and TP 4G/Go experts, NewbyJE and TopTongueBarry, to get the Sierra MC7710 working, but to no avail.  After many attempts to figure out the problem and trying different solutions, NewbyJE suggested that webOS might only recognize the MC7700 properly (as it was designed with ATT in mind) and not the MC7710.

# Researching the fix

Running some tools to search for MC7700 within the webOS file structure yielded 2 files that had the MC7700 string in them.  Being /usr/lib/libTelephonyInterface.so and /usr/bin/PmMdmQxdmLogger. The fix in the end was actually quite simple:  **all we had to do was replace the  references of MC7700 with MC7710 in both files**. I restarted the TouchPad 4G and all is working!

# Cost

The upgrade to a Sierra MC7710 is not very cheap and will set you back EUR 100,- to EUR 150,- depending on the source you get it from. It *will* give you a nice boost in speed and you can enjoy your legacy webOS device until you can run Open webOS on another device with built-in 4G!

# For the US

Theoretically the same results might be achieved with Verizon in the US when you place a MC7750 and patch the 2 files above to read MC7750 instead of MC7700, but this hasn’t been tested yet, so cannot be confirmed.  Also the CDMA network that Verizon uses might mean that you cannot activate your device properly on the network, so no guarantees can be given that it will work at all!  If you do decide to test it out let me know!

# Speed test results

After I patched my TouchPad 4G and swapped for the MC7710 it was time to test it out.  I chose 12 locations in Amsterdam with the Dutch carrier Vodafone to see what speeds I could get using [Ookla Speedtest.net](http://www.speedtest.net/).  Vodafone is not known to be the fastest 4G carrier in the Netherlands, so the speeds are somewhat lower compared to what some of the US based users are getting or what can be achieved on other carriers, but it’s still a very big improvement over the FauxG speeds that the Ericsson card offered!  In fact, I also did the same speed tests with the Ericsson card installed for comparison.![](https://i0.wp.com/pivotce.com/wp-includes/js/tinymce/plugins/wpgallery/img/t.gif?w=800)

As you can see, the **average download speed of the Sierra** was much faster at a ***69.7% increase*.** **Upload speeds averaged** at an incredible ***961.9% increase***!  It’s also important to note that even though it isn’t captured on the graph below, the **ping was reduced from 164 ms average on the Ericcson to just 65 ms average on the Sierra**!

![Speed Comparison Chart](/images/files/2014/01/speedgraph.png)

![Ericcson Speed Test](/images/files/2014/01/ericssonookla.png)

*Ericcson Speed Test*

![Sierra Speed Test](/images/files/2014/01/sierraookla1.png)

*Sierra Speed Test*

# Final thoughts

This is just one of dozens of solutions concocted by the webOS community.  Hopefully, you enjoyed the read and if you choose to take the plunge understand that your mileage may vary (especially if you go for the MC7750 on Verizon in the US).  If you’d like to get in on the discussion you can join us in the webOS Nation forums [thread](http://forums.webosnation.com/webos-patches/326601-patch-sierra-mc7710-support-webos-3-0-x.html). Feel free to leave a comment below!

Featured image: [getmesoftware.com](http://www.getmesoftware.com/Industries/InternetPublishing.aspx)
