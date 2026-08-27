---
title: 'UPDATE: Forums and Communities fixed (webOS 2.x and up) for webOS Nation browsing'
date: '2017-12-24T18:41:11Z'
lastmod: '2018-01-14T16:29:56Z'
author: Alan Morford
author_slug: alanmorford
categories:
- News
tags:
- App
- communities
- fix
slug: forums-fix-for-webos-nation-communities-fix-forthcoming-hopefully
summary: If you have Forums and/or Communities (ipk download) for the TouchPad, you’ll notice webOS Nation forums aren’t working. The good news is, there’s a fix for it for Forums AND…
source_url: https://pivotce.com/2017/12/24/forums-fix-for-webos-nation-communities-fix-forthcoming-hopefully/
wordpress_id: 4298
archived: true
---

If you have [Forums](http://preware.pivotce.com/package/com.grabber.forums) and/or Communities ([ipk download](https://app.box.com/s/254mgwre7p2m9x3jcgg40rr1jitkvht1)) for the TouchPad, you’ll notice webOS Nation forums aren’t working. The good news is, there’s a fix for it for Forums AND Communities (now). ~~The bad news is there’s no fix for it in Communities…yet~~.

Sadly Forums is dead for webOS 1.x with the change to https. No amount of backup from a working 2.x device and restoration to a 1.x device will help. It was already pretty crippled anyway but this is the nail in the coffin. 🙁

webOS Nation forum user, Fred Zyphal, [noted the Forums app wasn’t connecting to the webOS Nations forums anymore](https://forums.webosnation.com/webos-apps-games/331931-forums-app-can-t-connect.html) and others jumped in to confirm and to test some solutions.

### ![](/images/files/2017/12/forums_home.png)Forums

It turns out Forums just needs the entry for webOS Nation updated from http to https. So swipe away your old entry for it and add a new one with the “s” after http. That’s it!

### Communities

For this next part you can [download a modified communties.json file](https://app.box.com/s/7djf6oya9bv3b1flviu68yly8vyrpoi3) if don’t mind plugging in your TouchPad to a computer and copying it over to /media/internal. If so, skip down to step 8 and don’t forget to add your username too. If you’d rather do it all on the TouchPad, read on.

![Export your forum list](/images/files/2017/12/forums_2017-31-12_103451.png)
*Export your forum list*

To fix Communities do the following:

1. Open Preware on your TouchPad
2. Install Forums
3. Add the webOS Nations forums to Forums and login (don’t forget the ‘https’ from above)
4. Swipe back to the forum list view (pic above) and tap the save button on the bottom right
5. Open Internalz Pro (get it from Preware if you don’t have it)
6. ![Rename the file](/images/files/2017/12/internalz_2017-31-12_103541.png)
   *Rename the file*

   Find forums-export.json in /media/internal, tap it once, and choose Info
7. In the field at the top rename the file “communities.json” (no quotes) and hit enter for the name change to take effect
8. Now open the file to make a few edits.
   1. Change “forum_url” to read “normalizedUrl”
   2. Your username should be there but your password will be encrypted from Forums. That won’t work here so update the user_password field to have your actual forum password
   3. Save File and Close
9. ![Import the forum](/images/files/2017/12/communities_2017-10-11_212655.png)
   *Import the forum*

   Open Communities and swipe down from the top left and choose Preferences & Accounts
10. Tap the Import button and you’re done! Note: If you don’t have an Import button, you don’t have the patched Communities app. [Grab the patched ipk](https://app.box.com/s/254mgwre7p2m9x3jcgg40rr1jitkvht1) for it and install it and then you’ll have an Import button.

You might have to tap the lock icon on the bottom left to finish login. There are a few things in Communities that no longer work for webOS Nation. Namely; Unread Conversations, My Conversations, Search, and Browse. But it’s great to have the forum back in there and working for the most part.

#webOSforever
