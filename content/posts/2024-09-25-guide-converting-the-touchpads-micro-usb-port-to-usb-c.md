---
title: 'Guide: Converting the TouchPad’s Micro USB Port to USB C'
date: '2024-09-25T14:16:21Z'
lastmod: '2024-12-05T23:03:27Z'
author: Alan Morford
author_slug: alanmorford
categories:
- Tutorial
slug: guide-converting-the-touchpads-micro-usb-port-to-usb-c
summary: Well, it’s 2024 and technology continues to advance. The TouchPad isn’t new by any means, but that doesn’t mean it can’t be slightly modernized to be more convenient today. Specifically,…
featured_image: /images/files/2024/09/20240923_101836-scaled.jpg
source_url: https://pivotce.com/2024/09/25/guide-converting-the-touchpads-micro-usb-port-to-usb-c/
wordpress_id: 4616
featured_image_source: https://pivotce.com/files/2024/09/20240923_101836-scaled.jpg
archived: true
---

Well, it’s 2024 and technology continues to advance. The TouchPad isn’t new by any means, but that doesn’t mean it can’t be slightly modernized to be more convenient today. Specifically, it is entirely possible to convert the TouchPad’s Micro USB port to USB C for charging and USB storage access. I’ll show you how.

This is a tough mod which requires micro-soldering and modifying a PCB which you will have a hard time sourcing a replacement for without buying another TouchPad. Proceed at your own peril.

## **Tools for the Job**

To do this mod you’ll need a few things for tools and parts. Here’s a list of what I used:
– Needle nose pliers/tweezers
– USB C boards with 5.1k resistors [Amazon](https://www.amazon.com/gp/product/B0CB2VFJ54)
– Soldering iron, solder, flux and a hot air station
– Flush cuts [Amazon](https://www.amazon.com/Hakko-CHP-170-Micro-Cutter/dp/B00FZPDG1K)
– Dremel with cutting or sanding wheel
– 28 AWG wire or smaller. 30 AWG is pretty good but any wire around 0.25mm to 0.5mm should work.
– Small file and screwdriver set
– Painter’s and kapton tape
– Metal spudger

## **Disassemble the TouchPad**

This is where you’re going to want to get that metal spudger out and be very careful not to snap clips. I can’t explain it better than iFixit already did so go check out their [disassembly guide for the USB connector board](https://www.ifixit.com/Guide/HP+TouchPad+USB+Connector+Board+Replacement/6077) and then come back here.

## **Modify the USB Connector Board by Removing the Micro Port**

There are a few ways to remove the Micro USB port. I added a bunch of flux and coated all the connectors in fresh leaded solder and then used a hot air station set to 800 degrees while wiggling the port very slightly with needle nose pliers. You don’t have to be particularly careful here so if you want to cut the port off with the dremel or the flush cuts or just rip it off with the pliers, (I don’t recommend it but…) that’s fine. We’re not using the pads it’s soldered to anyway. You should STILL be careful not to crack the board. Go slow. Be patient.

![I used hot air to remove the micro port.](/images/files/2024/09/20240921_133333.jpg)

## **Trim the USB C Board**

We need to expose the USB C port a bit on this board so let’s cut it down. Grab the painter’s tape and flip the USB C board upside down. You’ll see a small trace between the front and rear anchor points on the right side, which we don’t want to cut. Mark the tape just on the other side of that trace like I did. Dremel along the tape line until you get to the port. You can then use needle nose pliers, a flat file, and/or flush cuts to remove the rest of the board from the bottom of the port.

![Cover the trace with tape.](/images/files/2024/09/2020_0103_225601_003.jpg)

![A good clean cut.](/images/files/2024/09/2020_0103_230157_005.jpg)

![It's ready.](/images/files/2024/09/2020_0103_230504_006.jpg)

## **Prepare the USB Connector Board for the USB C Port**

We need to slide the port into the old space so grab the painter’s tape again and mark off the area I marked to make room for the USB C port. You can place the port up to it like I did and use that as a guide. Grab your dremel again or a similar tool and cut out what you marked off. When you’re done, the USB C port should slide easily into the groove. It will fit tighter when we add the kapton tape in a later step.

![Line it up](/images/files/2024/09/2020_0103_231712_008.jpg)

![Tape it off and cut it out](/images/files/2024/09/2020_0103_232126_009.jpg)

![Check that it fits.](/images/files/2024/09/2020_0103_232523_010.jpg)

## **Make Room in the TouchPad for the Added Thickness of the USB C Board**

The USB C board will sit underneath the USB connector board so we have to make room by trimming away the plastic underneath. For this you’ll need to use flush cuts or any other tool you have to chip away. You could use the dremel for this if you’d like. Be careful to not go beyond the first inner layer. Beyond that is the outer shell of the TouchPad. There’s no real method here, just cut out the screw posts and chip away. Use the pictures below as a guide.

![Before the layer removal.](/images/files/2024/09/20240922_085618.jpg)

![After the layer removal.](/images/files/2024/09/20240922_091303.jpg)

![Like a glove.](/images/files/2024/09/2020_0103_231230_007.jpg)

## **Cut the USB C Hole from the Old Micro USB Hole**

To open the micro USB hole enough to fit the USB C port, take a rounded file to the left and right of both sides and just file a little bit at at time. Use a small flat file to widen the top and bottom of the port. This process is just trial and error. File a little and then grab the USB C board to test. The port will need to fit inside the hole a bit so you can push it through from the outside to test the hole size if that’s easier. Note: the USB C board will likely not rest on the bottom of the TouchPad and will float a little. This is good because it makes room for your wires and a little kapton tape underneath.

![This TouchPad was already cracked.](/images/files/2024/09/20240922_082925.jpg)

## **Tape the USB C Board**

Since we hacked away at the USB connector board it’s possible we’ve provided the perfect environment for creating shorts! Oh no! So get out the kapton tape because we’re going to add a layer on both sides. You’ll see how I did it on one side below. Do it on both sides. You’ll also notice how I did not cover those two small square contacts just at the bottom of the tape. That’s because we need them.

![Flip it over and do the same on the other side.](/images/files/2024/09/2020_0103_232814_012.jpg)

## **Where To Get Power and Data**

You’ll see the diagrams below which I’ve marked with VBUS (power), data in, data out, and ground. Obviously the old port is gone and most if its pads, but I wanted to show that both sides of the board have the connections. You could possibly do this mod differently, and if you so choose, hopefully these help.

A quick note: this mod can be done with a 4-pin USB C port. That would give you power and data just like with the USB C board I’m using in this guide, however, a 4-pin USB C board will not charge with a USB C charger (ie USB 3.1). The board I’m using in this guide provides the ability to use any charger because it comes pre-built with 5.1k resistors wired to CC1 and CC2 to ground. This is the trick that tells the USB C chargers to send power to the device.

![The top of the USB connector board.](/images/files/2024/09/front-pcb.jpg)

![The bottom of the USB connector board.](/images/files/2024/09/rear-pcb.jpg)

## **Solder the USB C Board into the USB Connector Board**

This isn’t a “how to solder tutorial” so hit up youtube and find a good tutorial that works for you. In general though, use flux, pre-tin the VBUS, Ground, D-, and D+ pads on the USB C board as well as the points on the bottom of the USB connector board.

Now for the tricky part, I didn’t list it in the Tools section above, but it would really help to have magnification or a digital microscope for this. I have these things and I used both. You might have steadier hands and better eyes than me. The picture below was my first attempt of the three TouchPads I modded, and it’s not my best soldering work, but fundamentally, this is what yours should look like.

![You don't do anything with CC1 or CC2.](/images/files/2024/09/2020_0103_233035_013.jpg)

![Ignore the quality of my first attempt.](/images/files/2024/09/2020_0103_220016_001.jpg)

## **Put the Pieces Together**

You can use a bit of kapton tape to secure the wires in place a bit more if you’d like but it’s not required. It won’t short since it’s only plastic underneath. This is all press fit into place, but if you’re uncomfortable with that, you can add a little hot glue under the board as you put it back into the TouchPad. You don’t have to put the metal shield back into place if you don’t want to. It’s all a pretty tightly fit and if you find the TouchPad screen isn’t as flush as you want, just leave the metal shield off. A little kapton tape right on top would be fine instead.

![Almost looks stock!](/images/files/2024/09/2020_0104_000942_015.jpg)

![A little kapton holds it in place.](/images/files/2024/09/2020_0104_001134_016.jpg)

![Fits pretty well.](/images/files/2024/09/20240922_125730.jpg)

## **Congrats, You Now Have USB C**

I did this mod on three TouchPads and each one works fine with any USB charger I could find, including USB C port having USB 3.1 chargers. I can also confirm the data connection works just like it should to connect via USB mode on PC. Sadly, this doesn’t do anything to stop webOS from telling you the charger you’re using isn’t the original TouchPad barrel charger, but you can make a custom cable to stop that which I’ll cover in a future article on pivotCE.

![](/images/files/2024/09/DHkCxMu3-1.jpg)

![](/images/files/2024/09/5wpmePxM-1.jpg)

![](/images/files/2024/09/CNf2pkZ3-1.jpg)

[Talk about it on the Legacy webOS Forum](https://forums.weboslives.eu/d/67-pivotce-guide-converting-the-touchpads-micro-usb-port-to-usb-c)

#webOS4ever
