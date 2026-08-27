---
title: 'TIP: preware.net solutions for WOSQI, Preware v1.9.13'
date: '2014-08-31T02:25:38Z'
lastmod: '2015-04-21T19:09:30Z'
author: Alan Morford
author_slug: alanmorford
categories:
- Tips
slug: tip-preware-net-solutions-for-wosqi-preware-v1-9-13
summary: You may have heard that preware.org was snatched away from webOS Internals yesterday. If not, what the heck? You live under a rock? I digress. Long story short, preware.net is…
featured_image: /images/files/2014/08/preware-featured-image.jpg
source_url: https://pivotce.com/2014/08/31/tip-preware-net-solutions-for-wosqi-preware-v1-9-13/
wordpress_id: 1994
featured_image_source: https://pivotce.com/files/2014/08/preware-featured-image.jpg
archived: true
comment_page: 2014-08-31-tip-preware-net-solutions-for-wosqi-preware-v1-9-13
---

You may have heard that [preware.org was snatched](/2014/08/29/preware-org-woes-feedssite-down-as-domain-slips-away/) away from webOS Internals yesterday.  If not, what the heck?  You live under a rock?  I digress.

Long story short, preware.net is now the new home for all things Preware to include our beloved patches, homebrew apps, etc.  Don’t bother copying and pasting that as a link because until the ducks are lined up there won’t be much to see.  I’ve been assured that the [Preware Homebrew Documentation](https://developer.palm.com/appredirect/?packageid=org.preware.docs) app and get.preware.net will all be updated in the near future.  Come on.  This stuff takes some time.  Relax.

So this domain snatching business was pretty ugly.  Turns out “preware” means something very different to the folks that grabbed the domain and they have no intention of selling it back to webOS Internals which was the initial assumption.  No, in fact they plan to use it for whatever “preware” means to them.  Like you, I am waiting with bated breath for the answer to that mind boggling riddle. 😐

But now that preware.net exists and more importantly, ipkg.preware.net, the home of patches, apps, etc., how do you fix your broken [webOS Quick Install (WOSQI)](http://forums.webosnation.com/canuck-coding/274461-webos-quick-install-v4-5-0-a.html) and Preware that point to preware.org?

# Fix WOSQI

![wosqi](/images/files/2014/08/wosqi.jpg)**UPDATE**: Jason Robitaille has released WOSQI 4.6.0 which fixes a lot and makes it work with LuneOS now too! You can [get it here](https://github.com/JayCanuck/webos-quick-install/releases/download/4.6.0/WebOSQuickInstall-4.6.0.jar). Post [in the forum](http://forums.webosnation.com/canuck-coding/274461-webos-quick-install-v4-5-0-a.html) to say thanks or to ask questions. And consider [donating](https://www.paypal.com/ca/cgi-bin/webscr?cmd=_flow&SESSION=4kdETXhHoIZ7EKwiSueB5eL4xWVqpQz7jmhwkEzvRhk9p3UR8XUnYACVtNq&dispatch=5885d80a13c0db1f8e263663d3faee8d66f31424b43e9a70645c907a6cbd8fb4)!

Changelog:

– Added adb connection support for Open webOS and LuneOS devices
– Added support for opkg for Open webOS/LuneOS devices
– Improved package info handling support
– Fixed Preware ipkg feed URLs
– Fixed issue with novacom drivers not downloading/installing

# Preware

Preware’s version was bumped yesterday to 1.9.13.  It fixes the .org problem and also the birthday icon which never got updated after last year’s Preware birthday.  Anyway, to get Preware going again you have a few options.

~~**Option #1** – If you jumped down here because fixing WOSQI seemed annoying…well, you ***can** skip to here* but IF you fix WOSQI *first*all you have to do to get the updated Preware that fixes all the old .org feeds to the new .net ones is click the globe, search for Preware, and install it.~~

**Option #2** – Uninstall Preware on your webOS device first.  On your PC grab the .ipk [here](http://ipkg.preware.net/feeds/webos-internals/armv7/org.webosinternals.preware_1.9.13_arm.ipk), plug your phone or TouchPad into your PC, open your broken WOSQI, drag the .ipk into the WOSQI window and click Install. Done. Now scroll up and ~~fix~~ download the new WOSQI.

**Option #3** – On your webOS device copy this URL http://ipkg.preware.net/feeds/webos-internals/armv7/org.webosinternals.preware_1.9.13_arm.ipk, open Preware, immediately swipe down for the menu and tap Install Package, paste the copied URL into the File box and click Install. Preware will close. Reopen it and you’re good to go.

Note: When I first fixed Preware I had old beta feeds added and some of them didn’t auto-update to the .net address.  To remedy the situation I uninstalled the new Preware, removed the beta feeds, readded the beta feeds, and reinstalled Preware.  Problem solved.

Well there you have it. Good luck!

#webosforever
