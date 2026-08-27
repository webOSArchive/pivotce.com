---
title: 'Guide: Cleaning out the /var partition when full'
date: '2017-12-09T18:29:32Z'
author: George Mari
author_slug: marigx
categories:
- News
slug: guide-cleaning-out-the-var-partition-when-full
summary: Just like an older car, with any webOS device these days, you have to perform some maintenance to keep it running smoothly. And one of those maintenance items you have…
featured_image: /images/files/2017/11/Oil_Change.jpg
source_url: https://pivotce.com/2017/12/09/guide-cleaning-out-the-var-partition-when-full/
wordpress_id: 4158
featured_image_source: https://pivotce.com/files/2017/11/Oil_Change.jpg
archived: true
---

Just like an older car, with any webOS device these days, you have to perform some maintenance to keep it running smoothly. And one of those maintenance items you have to do on your webOS device is cleaning out the “var” (variable data) partition.

If your webOS device has any of the following symptoms, the trouble could be that your “var” partition is full, or nearly full:

1. Unable to download files, or play streaming media.
2. Can’t install or update webOS apps.
3. Trouble downloading new e-mails.
4. Generally sluggish, or very slow to respond to gestures.

The “var” partition is an area of the disk used behind-the-scenes by the the webOS operating system. You don’t really notice it or interact with it on a day-to-day basis.

This is a standard directory location on almost all Unix and Linux-based operating systems, which webOS of course, is. What usually goes here are files used internally by webOS during the course of its operation, such as log files, temporary and not-so-temporary database files, and other files that webOS needs to just keep track of what it’s doing from minute-to-minute.

Now as you could guess, things like operating system log files could just get bigger and bigger over time, and without any user intervention, they could eventually take up the disk on a regular PC, or flash storage partition on a mobile device. There are already utilities built-in to webOS that automatically run once in a while to delete old log files to keep this from happening.

Normally, on more recent desktop Linux operating systems, the var partition is just a part of the root partition, and can usually take up the whole hard drive.

On our webOS devices, most (but not all) of our available storage is taken up by our media partition. When you have a TouchPad with 16GB of storage, only about 15GB is available for your own use, to store music, videos, photos, documents, and other files. The other 1GB or less is so that webOS itself can have some filespace for its own needs.

Out of that less-than-1GB, only 62MB (megabytes) is set aside for the var partition. Yeah, that’s not a lot, but it’s just a consequence of trying to give as much storage is feasible to you for your own files on your webOS device.

So besides the log files that webOS automatically trims once in a while there are other directories and files that webOS does not keep in check, that can grow over time and fill up the var partition. Over the years, different people have discovered that it is safe to remove files from the following directories:

1. Browser cache and cookies
Your web browser has to save files somewhere, and you guessed it – they go in the var partition.

2. /var/luna/data/downloadhistory.db
This file is just a listing of all of the different files that have been downloaded through your browser. On the TouchPad, you can clear this list using the browser.

![Browser download list](/images/files/2017/11/browser_download_list.png)

But on phones, you don’t have that option to clear this from the browser.

3. /var/minicores
Files that go in here are stack traces of applications that have crashed. These are the kind of files that would have been useful to the folks developing webOS.

4. /var/context/pending
This directory would contain files that would get uploaded to Palm periodically, to help them spot operating system errors on devices already released. The files also controversially contain things like location data.

5. /var/palm/data/localstorage – http*.localstorage
Some websites use javascript features that create a little database on the users computer. Those database files go in this directory on webOS.

Now, if your webOS device is in a state where you cannot even launch a new app because the var partition is full, you will have to use novaterm or a similar utility to access the command line of your webOS device, and delete files from the var partition manually.

But if you have the Internalz file management app, and you can start it successfully, you can use that to navigate to each of these locations and take the following steps.

1. For browser cache and cookie files, open your webOS browser app, and access the Preferences from the menu. Press the buttons to Clear History, Clear Cookies and Clear Cache. Please note that clearing cookies will erase any passwords you may have saved for websites you might have to login to from the browser, such as Facebook or the webOSNation forums. You’ll just have to re-enter and re-save your login info the next time you visit those sites.

![Browser preferences](/images/files/2017/11/browser_preferences.png)

2. For /var/luna/data/downloadhistory.db, just navigate to this directory in Internalz and delete it there. The webOS browser will re-create it for you next time you start the browser. Even if this file is 1MB or so, remember that is 1MB out of 62MB total, so it will definitely help.

3. For /var/minicores, navigate to this directory in Internalz, and delete any and all files found there. You may not find any files here. If you don’t, no problem.

4. For /var/context/pending, navigate to this directory in Internalz, and delete any and all files found there. You may not find any files here. If you don’t, no problem.

5. For /var/palm/data/localstorage, you don’t want to delete all files here – only consider ones that start with “http”. Even those, maybe don’t delete files of websites that you visit a lot, or you may lose features saved by the website on your webOS device. There may be A LOT of files here, so here is a trick in Internalz: tap the “Size” column so that the largest files appear at the top. The display will go from this:

![Internalz unsorted](/images/files/2017/11/internalz_unsorted.png)

…to this:

![Internalz sorted](/images/files/2017/11/internalz_sorted.png)

Now you can easily delete the first few files beginning with “http” that will make the biggest impact in freeing up space for you. Keep deleting these files until you can’t stand it any more. 🙂

Now that you have freed up that precious space in your var partition, there is one final thing you need to do, if you haven’t already done it: If you had a ton of files in /var/context/pending, this means you probably haven’t installed the “EOM Overlord Monitor” from Preware. This is a patch/application that will prevent the scripts that fill up this directory from running. These scripts or background apps also try to send these files to Palm servers that no longer exist, so it makes sense to turn off these features on your device. Just install the app from Preware, and it will care of turning those things off.

With your routine maintenance complete, your classic model is ready for the road again!

[Discussion thread here](http://forums.webosnation.com/webos-tips-info-resources/318432-troubles-when-var-file-partition-gets-full.html).
