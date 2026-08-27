---
title: How to Fix Old Game Issues
date: '2015-11-28T02:26:18Z'
lastmod: '2015-11-28T04:56:30Z'
author: Alan Morford
author_slug: alanmorford
categories:
- News
tags:
- apps
- buzz
- fix
slug: how-to-fix-old-game-issues
summary: So the catalog is dead. Oh well. Finding random ipks online, whether they be in a shared directory somewhere or from a friend hooking you up can be frustrating. Getting…
source_url: https://pivotce.com/2015/11/28/how-to-fix-old-game-issues/
wordpress_id: 3335
archived: true
---

![image](/images/files/2015/11/wpid-img_20151114_140552.jpg)

So the catalog is dead. Oh well. Finding random ipks online, whether they be in a shared directory somewhere or from a friend hooking you up can be frustrating.  Getting apps for webOS devices is left to the back alley ways of the darkest recesses of private forum messaging and dropbox links. I don’t care how you get them. I won’t judge.

But there are those who have loaded those apps to their TouchPad or Pre and find some not working correctly. Chances are those non-functioning or partially working apps are games.

I recently instructed a friend to the wonders of the metadata.json fix. He had no idea what I was talking about. What? It’s 2015! But if there is one, there are many. So I went digging for my favorite explanation. I found it on the now defunct webosbuzz.com. Don’t bother going there, it’s offline. But using archive.org I managed to resurrect it. I have pasted it in its entirety below to save it from death. Thanks to their forum user, dtsp, for the original writeup. Download a metadata.json file in step three. Enjoy!

——————

Here is the way to get games not running in landscape mode (worms, dead runner…) or not showing textures properly (dungeon hunter, …) :

How to:

1) install game

2) reboot device or restart luna

3) copy the [metadata.json](https://app.box.com/s/rhcmu7hpb0bif8nuvq13r3rzw6tyd6uj) file in the app directory
(use Internalz pro available in Preware)
(ex: /media/cryptofs/apps/usr/palm/applications/com.gameloft.app.dungeonhunter)

Device 101 (fully compatible):
{“version”:1,”devices”:[101]}

Device 601 (Quality increase!, but not work on all games):
{“version”:1,”devices”:[601]}

If you want to switch between 101 fix and 601 fix, just edit the file in the app directory via Internalz pro

Known working games with 601 fix: Worms, Dead runner, Angry birds season

4) always launch the game in PORTRAIT mode, otherwise it will crash at start
(i’ve seen this bug only in Dungeon hunter for now)

———————————————————

Explanation:

101 fix: force the app to emulate as a Pre (320*400 resolution). That’s why the quality is so bad, it’s scaled so you have a lot of aliasing.

601 fix: force the app to emulate as a TouchPad. Quality is better but not the best because it’s not only a problem of resolution.

However it’s a very simplified explanation… it’s a little bit more complicated in fact… (see Duke 3D release, it’s a LowRes game but looks great).

If you want to see a good example get the Worms game and test the 2 fix. You will immediately see the differences.

———————————————————

Technical:

Listing of recognized devices through the metadata.json file:
-1 HARDWARE_UNKNOWN
101 HARDWARE_PRE
102 HARDWARE_PRE_PLUS
201 HARDWARE_PIXI
301 HARDWARE_VEER
401 HARDWARE_PRE_2
501 HARDWARE_PRE_3
601 HARDWARE_TOUCHPAD

———————————————————

Speculation:

So you want to go further and porting your own HiRes fix, i want too but I’m stuck at this point. However I will share my investigation here. Note that it’s only theory, some of the things written may be completely wrong.

1) Find the problem

After reading a lot of forums, the problem can be near this: SDL_SetVideoMode must be set to a width&height of 0

Code:
Display=SDL_SetVideoMode(320,400,0,SDL_OPENGL);
Display=SDL_SetVideoMode(0,0,0,SDL_OPENGL);
It can also be a texture positioning problem too, doubling texture size doesn’t seems to be a solution. Also the rotary option as to be fixed. And it can be more…

Well, I wanted to start testing all of this, so I’ve downloaded Doom source code and started porting it for the TouchPad (I won’t release it, it’s only for testing)I

Beyond this point, if you have no skill in Linux command line and coding, it may be hard.

If you want to do the same you need:
VirtualBox
HP webOS SDK/PDK
Doom SDL source code
Eclipse (optional)

2) Fix the problem in a existing game

Unfortunately, when a game is compiled, it compresses most of the files project in an executable binary ELF file, unreadable with a text editor. Devs don’t share their uncompiled project unless it’s opensource.

The only way to modify it: use a reverse-engineering program (like IDA) and have the skill to use it (I don’t).

The other way is a dream: a system patch that overrides SDL settings when a game launches with 101 fix. I don’t know even if it’s possible…

—————

OK that’s it! Here forever! [Talk about it](http://forums.webosnation.com/showthread.php?t=330835).

#webosforever
