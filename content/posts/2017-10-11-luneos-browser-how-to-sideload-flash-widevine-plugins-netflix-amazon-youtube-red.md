---
title: 'LuneOS Browser: How to sideload Flash & WideVine plugins (Netflix, Amazon, YouTube Red)'
date: '2017-10-11T07:44:24Z'
lastmod: '2017-12-04T19:59:15Z'
author: webosports
author_slug: webosports
categories:
- News
tags:
- apps
slug: luneos-browser-how-to-sideload-flash-widevine-plugins-netflix-amazon-youtube-red
summary: Since the most recent release of LuneOS called “Decaf” which includes Qt 5.9.2, support for 3rd party browser plugins (such as Adobe Flash and Google’s WideVine CDM) has been added…
featured_image: /images/files/2017/10/009-Netflix.png
source_url: https://pivotce.com/2017/10/11/luneos-browser-how-to-sideload-flash-widevine-plugins-netflix-amazon-youtube-red/
wordpress_id: 4090
featured_image_source: https://pivotce.com/files/2017/10/009-Netflix.png
archived: true
---

Since the [most recent release of LuneOS called “Decaf”](/2017/10/08/luneos-september-stable-release-decaf/) which includes Qt 5.9.2, support for 3rd party browser plugins (such as Adobe Flash and Google’s WideVine CDM) has been added to the Browser App and has been enabled by default.

However the source code of these plugin binaries is not available and therefore these binaries cannot be compiled and provided in the LuneOS images.

The users would therefore need to manually install (sideload) the required plugin files from a source that has them available. Luckily there are ChromeOS recovery images available for the ARMv7 instruction set which is the same instruction set used by our HP Touchpad, Nexus 4 and Nexus 5. [Looking at the list of ChromeOS devices located here and checking their specifications](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices) I believe that the Samsung Chomebook from 2012 with Codename “Snow” is a suitable candidate for example. Others that might work are:

- Samsung Chromebook 2 – 11″, codename “Pit”
- Samsung Chromebook 2 – 13″, codename “Pi”
- HP Chromebook 11 G1, codename “Spring”
- HP Chromebook 11 G2, codename “Skate”
- ASUS Chromebook Flip C100PA, codename “Minnie”
- ASUS Chromebook C201, codename “Speedy”
- AOpen Chromebase Mini, codename “tiger”
- Asus Chromebit CS10, codename “Mickey”
- AOpen Chromebox Mini, codename “fievel”

In order to get Adobe Flash & WideVine CDM support you need to do the following:

1. 1. Download a ChromeOS ARM Recovery image, the best would be the one using the same Chrome/Chromium version, so 56. For example for the Samsung Chromebook codename “Snow” mentioned above as per [this link.](https://dl.google.com/dl/edgedl/chromeos/recovery/chromeos_9000.91.0_daisy_recovery_stable-channel_snow-mp-v4.bin.zip)
   2. Extract the “chromeos_9000.91.0_daisy_recovery_stable-channel_snow-mp-v4.bin.zip” file.
   3. Once done, open “chromeos_9000.91.0_daisy_recovery_stable-channel_snow-mp-v4.bin” with a file archiver (for example 7-Zip on Windows).
   4. Open the ROOT-A.img file.

![](/images/files/2017/10/001-7zip.png)

1. 1. Go to “/opt/google/chrome/”
   2. Extract “libwidevinecdm.so” and “libwidevinecdmadapter.so” into a separate folder.

![](/images/files/2017/10/002-7zip.png)

1. 1. Go to “/opt/google/chrome/pepper/”
   2. Extract “libpepflashplayer.so” to the same folder as under 6.

![](/images/files/2017/10/003-7Zip.png)

1. 1. You will now have 3 files in this folder: “libwidevinecdm.so”, “libwidevinecdmadapter.so” and “libpepflashplayer.so”.
   2. Open a command prompt and go to folder with the 3 files.
   3. Now push each of the 3 files to “/usr/lib/chromium/” by means of “adb push libwidevinecdm.so /usr/lib/chromium/”, “adb push libwidevinecdmadapter.so /usr/lib/chromium/” and “adb push libpepflashplayer.so /usr/lib/chromium/”
   4. Restart your LuneOS device!
   5. Now go <http://get.adobe.com/nl/flashplayer/about/> to see if Adobe Flash works. It will display you the supported version of Flash as per screenshot here:

![Flash Version](/images/files/2017/10/007-flash.png)

1. Now go to <https://shaka-player-demo.appspot.com/demo/> to see if WideVine works. It will show you the WideVine options in the dropdown in black instead of grey. When they show in black the WideVine plugin is properly installed and working.

![Without WideVine Plugin](/images/files/2017/10/008-widevineNotOK.png)
*Without WideVine Plugin*

![With working WideVine Plugin](/images/files/2017/10/008-widevineOK.png)
*With working WideVine Plugin*
