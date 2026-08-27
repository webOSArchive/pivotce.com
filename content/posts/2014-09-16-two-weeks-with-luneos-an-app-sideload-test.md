---
title: 'Two weeks with LuneOS: An app sideload test'
date: '2014-09-16T02:47:51Z'
lastmod: '2014-10-21T02:01:29Z'
author: Alan Morford
author_slug: alanmorford
categories:
- Reviews
slug: two-weeks-with-luneos-an-app-sideload-test
summary: Here we are two weeks into the LuneOS initial release and I find myself staring at the install on my HP TouchPad wanting it to do more. Don’t get me…
featured_image: /images/files/2014/09/enyoappheader.jpg
source_url: https://pivotce.com/2014/09/16/two-weeks-with-luneos-an-app-sideload-test/
wordpress_id: 2088
featured_image_source: https://pivotce.com/files/2014/09/enyoappheader.jpg
archived: true
comment_page: 2014-09-16-two-weeks-with-luneos-an-app-sideload-test
---

Here we are two weeks into the LuneOS initial release and I find myself staring at the install on my HP TouchPad wanting it to do more.  Don’t get me wrong, I’m patient enough to wait for a functioning OS of core app integration.  And I’m not in a hurry for all of the “I wish it had \<app name\>” whining.

Although, since LuneOS supports Enyo apps, isn’t it possible that it could run current webOS apps built from the technology?  I set out to find out.  Read on for the results.

# Finding some apps to test

I was able to backup all of my apps some time ago using the [donotdelete IPK patch](http://forums.webosnation.com/webos-tips-info-resources/322549-how-retain-app-ipks-app-catalog.html) from webOS Nations forums user, GMMan. So I just browsed through my collection looking for Enyo apps and here’s what I found:
1. [Apollo 1.2.5](https://developer.palm.com/appredirect/?packageid=com.jmtk.apollo)
2. [ACL Documentation 1.3.2](https://developer.palm.com/appredirect/?packageid=com.phxdevices.acl.doc)
3. [Neato 2.0.0](https://developer.palm.com/appredirect/?packageid=com.zhephree.neato)
4. [Shortcut Launcher 2.0.2](https://developer.palm.com/appredirect/?packageid=net.wackware.shortcutlauncher)
5. [QuickChat for Facebook 1.0.11](https://developer.palm.com/appredirect/?packageid=de.pcworldsoftware.fbchat)
6. HP App Catalog 5.0.3500
7. [USA Today 1.2.0](https://developer.palm.com/appredirect/?packageid=com.usatoday.webos)
8. [Just Draw 1.2.0](https://developer.palm.com/appredirect/?packageid=com.volatile.nuances.justdraw)
9. [Communities 1.0.8](https://developer.palm.com/appredirect/?packageid=com.newness.communities)
10. [Project Macaw (enyo) 2.2.12](https://github.com/minego/macaw-enyo)
11. [Box for TouchPad 1.0.21](https://developer.palm.com/appredirect/?packageid=com.box.webos)
12. [Facebook Tablet 2.0.35](https://developer.palm.com/appredirect/?packageid=com.palm.app.enyo-facebook&applicationid=9193)13. [Maps (Bing) 3.1.32](https://developer.palm.com/appredirect/?packageid=com.palm.app.maps)14. [FeedSpider (enyo) 2.0.0](https://github.com/OthelloVenturesLtd/FeedSpider2)

# Setup

Now that I had some apps to test I needed to get the .ipk files onto my TouchPad.  Uh, wait…plugging in the USB cable to my laptop netted me a media device called TouchPad but when I open it there’s nothing there.  Copying over files results in an error message.  Well poo.  Oh yeah!  LuneOS uses a certain amount of Android “magic” soooo in command line on my PC I tried:

> adb push nameofmyapp.ipk /media/internal/downloads

Success! I then opened up Preware, hit the menu, clicked Install Package, browsed for and selected the file, and hit Install.

I’ll note here that installation always worked but some apps caused Luna-Next to restart. Despite the glitch the app always installed. Also, the Preware success dialog still sports a back button which isn’t necessary since the gesture area is there and the spinning “working” symbol never quits. Just minor issues for now.

For the results, I divided them into 3 categories: Fully Functional, Partially Functional, and Non-functional.

# Non-functional

As I mentioned, every app installed fine but this category means the app won’t open.  Those apps were the HP App Catalog (duh no surprises there), Communities, and Facebook Tablet. Facebook disappointed me since it’s such a great example of what an enyo app can look like and do but no dice.  [Communities has been broken](http://forums.webosnation.com/hp-touchpad/327501-help-communities-app.html) for a while anyway so even if it had opened it wouldn’t be very usable. Bummer.

# Partially Functional

This category is a bit wider in interpretation but essentially if tapping on the app icon gained a card, that was enough for me to say it at least did *something*. This means that the app opens or you can tap, move, or manipulate the UI in some way. Those apps were Apollo, Maps, ACL Documentation, Just Draw, QuickChat for Facebook, Shortcut Launcher, Box for TouchPad, USA Today, FeedSpider, and Project Macaw.

- Apollo only opened the card and never progressed beyond the splash logo.
- Maps opened and immediately showed a “could not locate” notification below which is no surprise since the WiFi TouchPad I’m using to run these tests didn’t ship with GPS functionality. Everything seemed great until I swiped away the notification and the app suddenly scrunched into super widescreen view. Closing the app, reopening it, and leaving the notification there let the app display properly. Search and directions all worked fine.
- ACL Documentation opened and displayed properly but many of the buttons did not work. Presumably it’s because of the webkit changes in LuneOS over webOS.
- Just Draw opened but that’s about it. The page to draw in is a small box in the upper left corner which didn’t draw and the color selector won’t select color.
- QuickChat for Facebook opened and showed the top line of what I remember from my webOS devices to be the web view of the “authorize app on Facebook” page. That view doesn’t populate but again most likely because of the webkit changes.
- Shortcut Launcher opened fine and the buttons functioned and the fields took text input but browsing didn’t go well. No amount of backswipe worked and the app remembers your last directory! So reopening the file browser function only allowed you to go a level deeper and never back up. That’s a problem as you can imagine. So I could never try to add a shortcut.
- Box for TouchPad opens but that’s it. The login screen is halfway on the screen and the input boxes do nothing. That’s another app that is [broken](http://forums.webosnation.com/hp-touchpad/327476-box-net-account-settings-says-credentials-incorret.html) anyway.
- USA Today opened, pulled down new stories, scrolled properly and I thought I had a 100% functional winner! Oh! But videos didn’t play.  So close. I have always liked that app though. Pretty neat implementation with Enyo 1.
- FeedSpider works amazingly well. I was able to get an early copy and I was impressed. The interface is clean and familiar from his previous work and I could log in and pull down new stories with ease. It’s on the partial list though because the back swipe didn’t take me back and some things just haven’t been coded yet. VERY promising indeed. Perhaps this will find its way into a release of LuneOS in the future. Yup, it’s that good and it’s not even done.
- Macaw is an early build of the enyo version but everything seemed kosher there too. There were some visual glitches but something tells me that’s LuneOS since it surrounded the virtual keyboard use. Multi-account use was a bit wonky but overall the app functioned to view and post to Twitter rather well. It’s not done either but it’s pretty darn good as it is so I imagine the final release product will be amazing.

# Fully Functional

That leaves Neato! Neato opened, logged in, and not only could successfully send text or URLs to my webOS devices and browser but if you sent a message to the TouchPad, Neato would display the page! Cool!

This is what I’ve done with LuneOS over the last 2 weeks. Do you have an Enyo app I didn’t try? Let me know your results in the comments below.

#webosforever
