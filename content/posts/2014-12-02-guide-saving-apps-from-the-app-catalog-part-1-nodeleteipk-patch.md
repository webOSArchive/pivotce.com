---
title: 'Guide: Saving Apps From The App Catalog Part 1: nodeleteipk patch'
date: '2014-12-02T19:15:01Z'
lastmod: '2015-04-17T03:51:27Z'
author: Brent Hunter
author_slug: brenthunter
categories:
- Tutorial
tags:
- App
- backup
slug: guide-saving-apps-from-the-app-catalog-part-1-nodeleteipk-patch
summary: '** PLEASE NOTE: Following the closure of the HP app catalogue, the instructions in this article are no longer relevant. It is now of historical interest only. ** The time…'
featured_image: /images/files/2014/12/ipksaveheader.jpg
source_url: https://pivotce.com/2014/12/02/guide-saving-apps-from-the-app-catalog-part-1-nodeleteipk-patch/
wordpress_id: 2352
featured_image_source: https://pivotce.com/files/2014/12/ipksaveheader.jpg
archived: true
---

** PLEASE NOTE: Following the closure of the HP app catalogue, the instructions in this article are no longer relevant. It is now of historical interest only. **

---

The time has come; HP has finally shut off the App Catalog payment service. This means that as of November 1, you can no longer purchase new paid apps from the App Catalog. However, you can still download apps that you have previously purchased and can acquire new free apps until January 15th. After that point, the App Catalog will be gone for good (at least the official one will…) and you’ll have no way to restore your apps. So, you’ll want to make sure that you’ve backed them up. This guide will walk you through the primary app backup method: saving IPKs when you download and update apps.

There are several ways to backup in webOS. Since this is just one of them, expect subsequent howto articles on other methods.

#### What is an IPK?

Named for their file extension (.ipk), an IPK is a package that contains all of the bits that make up an app, as well as all of the information necessary to successfully install the app on a webOS device. Its name includes the company’s name, the app name, the version of the app and the device architecture (ie. the IPK file for the latest version of the phone Facebook app is named com.palm.app.facebook_1.5.62_all.ipk). “com.palm.app” represents the company (Palm/HP), facebook represents the app name, 1.5.62 is the version of the app, and all of it means that this is a package that will run on all architectures that webOS will support.

When you download an app (either paid or free) from the App Catalog, your device will download the IPK from HP’s servers, install the app, and then remove the IPK so that it doesn’t take up extra space.

#### Why this method of backup?

This method is the preferred method because it allows you to take a backup of the “cleanest” version of the app – the package issued directly from the manufacturer. Other methods will attempt to rebuild the IPKs using data from an already installed app, so you run the risk of it not working quite right, especially if the app does something quirky as part of its setup process. So, they should only be relied upon if the IPK is not available from the App Catalog, or if you will lose critical data and do not have another device that you can download the IPK to.

#### Let’s Get Started

This guide assumes that you have followed the instructions in [the welcome back guide](/2014/10/21/guide-coming-back-to-webos-in-2014-part-1/), and that your device is ready for patching. Please note that we will be using webOS Quick Install for this process as Preware does not support installing patches that don’t come from an official feed.

Here’s what you have to do:

1. Download and install the nodeleteipk patch.
2. Check App Availability.
3. Delete Apps.
4. Re-download Apps.
5. Save downloaded IPKs.

#### Step 1: Get the nodeleteipk patch

Typically, after installing an app, the App Catalog will delete the IPK that it came from. However, early last year, forum user GMMan learned that there was a configuration file option that would tell your device not to delete the IPK, allowing you to keep it for backup. He put together some detailed instructions, and also built a patch to make things nice and easy.

![WOSQI](/images/files/2014/12/WOSQI.png)

To install this patch:

1. Download the patch from the first post of [this webOS Nation Forum thread](http://forums.webosnation.com/webos-tips-info-resources/322549-how-retain-app-ipks-app-catalog.html) and save it to a place that you can access.
2. Plug your device into your computer and when asked if you want “USB Mode” or “Just Charge”, pick “Just Charge”.
3. Launch webOS Quick Install.
4. Make sure that your device shows up in the upper right hand corner. If this is your first time running the tool you may be asked to install novacom drivers. These are what the tool uses to communicate with your phone. In that case, just follow the prompts.
5. Click on the green plus icon on the right hand side of the window, navigate to the file that you downloaded, and hit select.
6. Click the “Install” button and wait for the tool to install the package. When it is done, the list of files to install will be empty, and you’ll be good to go.

#### Step 2: Check App Availability

In the meantime since you originally purchased the app, it may have been pulled from the App Catalog. Open the App Catalog app on your device and run a search for each app that you plan to back up. If the search comes up empty, the app has been pulled for some reason and is no longer available. DO NOT DELETE IT FROM YOUR DEVICE. There are other methods of backing up these apps, which will be covered in a later guide.

If you do find it, you are good to proceed.

#### Step 3: Delete Apps

*NOTE: Deleting an app will remove all of it’s data from your device. This means that you will lose data such as game progress, logins, settings and other data when you remove it. Make sure that the application’s data is backed up before you delete it. If you do not have a way to back up the application data, there are other methods of backing up these apps, which will be covered in a later guide. As a start check out [Save/Restore](http://www.webosnation.com/understanding-homebrew-save-restore-app).*

For each app that you plan to re-download, delete it. This can be done by:

1. Opening the “Software Manager” application
2. Scrolling to the application that you wish to delete
3. Swiping right to delete
4. Confirming that you would actually like to delete the app from the dialog.

![Delete](/images/files/2014/12/Delete.png)

On a phone you can also hold down the Opt key and touch the app you want to delete. A confirmation pop-up will appear. TouchPad users can also delete applications by holding their finger down on the application icon until a little “x” appears. They can then tap the “x” and confirm that they want to delete the app.

#### Step 4: Re-download apps

![enyo-findapps_2014-01-11_234807](/images/files/2014/12/enyo-findapps_2014-01-11_234807.png)

Open up the App Catalog app, search for any apps that you would like to re-download, and tap the download button beside them (on TouchPad) or open up the app’s details page and tap download (other devices). This will trigger the app to start downloading and installing, while saving the IPK.

#### Step 5: Save Downloaded IPKs

At this point, you should have a collection of IPKs stored on your device representing all of the apps that you wanted to save.

![Unknown_2014-01-11_232905](/images/files/2014/12/Unknown_2014-01-11_232905.png)

Plug your device into your computer, and when asked if you want “USB Mode” or “Just Charge”, pick “USB Mode”. The USB Mode icon will appear on your device’s screen, and a new drive with your device’s model name will appear where your USB drives normally do. (Desktop for Mac users, My Computer for Windows users).

Open up this drive and navigate to the “downloads” directory. This is where everything that your device downloads, including IPKs, gets stored. Copy any file that ends in IPK to your computer as a backup, and I also recommend copying them to an additional place, such as a CD/DVD, flash drive, or cloud storage drive, as a further backup.

![Apps](/images/files/2014/12/Apps.png)

At this point, you’re done. You’ve successfully backed up your apps, and can delete the IPKs from your device to clear up some storage space. Just make sure that they’re kept in a safe place in case you ever need them.

#### What’s Next?

Preware and webOS Quick Install allow you to take IPKs that you backed up from the App Catalog or downloaded from other sources (such as homebrew) and install them on your device, meaning that you will be able to reinstall your apps after the App Catalog shuts down.

In the meantime, you have two and a half months to get anything that is both free and interesting from the App Catalog. Download and back up whatever you can.

While [some apps](http://forums.webosnation.com/webos-development/328732-developers-post-here-if-your-apps-will-available-after-hp-catalogue-closes.html) will continue to be available through the [webOS Nation App Gallery](http://www.webosnation.com/apps), for most of these apps, when January 15th rolls around, they will be gone for good. Save them while you can.

[Join the Conversation!](http://forums.webosnation.com/webos-tips-info-resources/328996-pivotce-guide-saving-apps-app-catalog-part-1-nodeleteipk-patch.html)
