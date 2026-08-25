---
title: 'How-to: Meta-Doctor – No Makefile editing'
date: 2013-11-20 03:34:17 UTC
modified: 2014-09-11 02:09:44 UTC
author: Alan Morford
author_slug: alanmorford
categories: [Tutorial]
slug: how-to-meta-doctor-part-1-no-makefile-editing
source_url: https://pivotce.com/2013/11/20/how-to-meta-doctor-part-1-no-makefile-editing/
wordpress_id: 542
excerpt: Have you ever browsed around the webOS Nation Forums and read about people installing webOS 2.1.0 on their Sprint Pres? How about installing webOS 2.2.4 on their Pre 2s? Or…
---

# How-to: Meta-Doctor – No Makefile editing

![metadoctor](../images/files/2013/11/metadoctor.png)Have you ever browsed around the webOS Nation Forums and read about people installing webOS 2.1.0 on their Sprint Pres?  How about installing webOS 2.2.4 on their Pre 2s?  Or mashing together a Sprint Pre 2 with either of the above?  Besides the hardware part of a Sprint Pre 2, this is all done via [webOS Internals](http://www.webos-internals.org/wiki/Main_Page)‘ [Meta-Doctor](http://www.webos-internals.org/wiki/Application:MetaDoctor).  This isn’t the latest news in the world of webOS, of course.  However, since the original [“how-to”](http://www.webos-internals.org/wiki/WebOS_2_Upgrade) over at webOS Internals is a bit dated I thought it fitting to provide a step-by-step to get it to work for you!  If you’ve always meant to do it but never gotten around to it, dust off that Pre, pull out your USB cable, and read on!

This tutorial is not designed to reinvent the wheel nor is it designed to be a high-level makefile-editing-behemoth (which pivotCE will cover in the Part 2).  It is designed for the user who just wants to update a webOS device to a webOS version never officially released for it.

The following guide worked for me on a PC with Windows 8 installed: YOU MAY GET DIFFERENT RESULTS.  Step 5 will dual-boot your Windows PC with Ubuntu.  Don’t worry, when you’re done with Ubuntu you can boot into Windows and navigate to Control Panel > Programs and Features, click on Ubuntu, select uninstall and the dual-boot will be removed (and so will be all the work you did below).  If you already have Ubuntu installed…YMMV (your mileage may vary) but you can log into your Ubuntu install and skip to step 9.  If you need the latest version of Java skip to step 11.  Got those two?  Skip to novacom installer at step 15.  If you already have Meta-Doctor installed (and you did it really recently) you can skip to step 25.  If you haven’t done it recently–in terminal type each of the following commands without quotes and hit enter after each: “cd meta-doctor”, “git pull”, “make clobber” and THEN go to step 25.

1. **Back up your device.** Palm backup app, save/restore (Preware), and use USB mode on a PC to drag files over.
2. Download Ubuntu. [Download Ubuntu Desktop | Ubuntu](http://www.ubuntu.com/download/desktop) I used the 64 bit version of Ubuntu 12.04 LTS
3. Mount the Ubuntu .iso using [PowerISO](http://www.poweriso.com/) or any other app that can do that OR burn the .iso to DVD using something like [ImgBurn](http://www.imgburn.com/).
4. Open up the disc from Computer if it doesn’t auto-play. If you get the User Account Control window asking if you want to allow the following program to make changes to this computer click Yes.
5. Choose your installation drive, language, installation size (webOS Internals says at least 10 GB). I chose the default for me which was 18 GB. Choose your username, Desktop environment should say Ubuntu, set a password, and click Install.  **Let it run.**
6. When the Ubuntu Installer finishes select Reboot now, close stuff you’re working on, and click Finish.
7. Your computer will reboot into Ubuntu and present you with a login screen. Type in your password from step 5 and hit enter.
8. If you’re on wifi you need to click the wifi symbol at the top right, select your network, enter your password, and click connect. (just the first time you log in) Ubuntu comes with Firefox for all of your web browsing needs (on the app launcher docked to the left of your screen).
9. Press Ctrl + Alt + T to bring up Terminal and type in or copy/paste all following commands exactly as they are written here and press enter after each one.
10. sudo apt-get install python-software-properties (you will need to enter your password which is the same as in step 5 and hit enter)
11. sudo add-apt-repository ppa:webupd8team/java (at the prompt in terminal press enter to continue)
12. sudo apt-get update
13. sudo apt-get install git (at the prompt in terminal press Y and then enter)
14. sudo apt-get install oracle-java8-installer (use the spacebar to select <Ok> when prompted and left arrow to <Yes> and hit spacebar on the license terms screen) **This step will take a while.  When it is done leave terminal open.**
15. Click here [http://universal-novacom-installer.g…taller-1.3.jar](http://universal-novacom-installer.googlecode.com/files/UniversalNovacomInstaller-1.3.jar) and on the Opening UniversalNovacomInstaller-1.3.jar window select Save File and click OK then go back to terminal.
16. cd Downloads
17. java -jar UniversalNovacomInstaller-1.3.jar
18. On the window that opens click Install Novacom
19. On the terminal window that opens type in your password from step 5 and hit enter
20. Click OK on the Message window, close the Install Novacom window, and go back to terminal
21. cd
22. git clone git://github.com/webos-internals/meta-doctor.git
23. cd meta-doctor
24. mkdir downloads
25. This is where you select the script for the custom doctor you want to use. The list of scripts is here. [https://github.com/webos-internals/m…master/scripts](https://github.com/webos-internals/meta-doctor/tree/master/scripts)  Specifically they start with test, super, meta, or old (I’d stay away from old and test).  For example, if you have a Pre 2 on Verizon and want to get it running webOS 2.2.4 you would type in terminal…
26. ./scripts/super-verizon-pre2-2.2.4 **(this takes a WHILE)**
27. When the script completes it will open the doctor for you.  Follow the on screen prompts to set your language, connect it via USB to your computer, put your phone in recovery mode and when the last Next button is highlighted click it and the doctor will then write to your phone.

That’s it!  Seems like a lot, right?  Well, it IS but it’s worth it.  My Verizon Pre+ runs webOS 2.1.0 with Govnah and Uberkernel GREAT!  If you think this tutorial needs work leave a comment and stay tuned for the Part 2 where we’ll explain how to tweak the makefile for more option-y goodness.  Also, stop by webOS Internals and [donate](http://www.webos-internals.org/wiki/WebOS_Internals:Site_support) to them for making such a great product.

Sources:
[WebOS 2 Upgrade – WebOS Internals](http://www.webos-internals.org/wiki/WebOS_2_Upgrade)
[Application:MetaDoctor – WebOS Internals](http://www.webos-internals.org/wiki/Application:MetaDoctor)
[Install Oracle Java 8 In Ubuntu VIa PPA [JDK8] ~ Web Upd8: Ubuntu / Linux blog](http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html)Jason Robataille – <http://forums.webosnation.com/canuck-coding/278224-universal-novacom-installer-uni-v1-3-a.html>

Credit to webOS Internals

#webosforever
