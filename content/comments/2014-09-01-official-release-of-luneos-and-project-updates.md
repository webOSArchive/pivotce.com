---
title: 'Comments: Official Release of LuneOS and Project Updates'
comment_count: 23
article_title: Official Release of LuneOS and Project Updates
build:
  list: never
  render: never
---

**Evacaf** — 2014-09-01 21:49:42 UTC

So exciting! I can’t wait to get a hold of either Nexus 4 or Touchpad that I can port LuneOS to. Great work everyone! Keep it up.

> **Alan Morford** — 2014-09-02 00:16:54 UTC
>
> Wait, you don’t have TouchPad? The dual boot is pretty harmless if you’re worried.

**John Margarone** — 2014-09-02 01:41:32 UTC

I have a Galaxy nexus 32 Meg. What are the chances of using moot 0.3.8 to dual boot the phone between android and this LuneOS?
I am not going to mess with my Touchpad. I am smitten with JC Sullins 20140625 cm 11 and I live on the thing but the Galaxy Nexus has been taken off the cell network for an S5 but I still need it to boot android on it. Let me know. Thanks.

> **drfandroid** — 2014-09-02 06:04:06 UTC
>
> Seconded! Anyone know if dual-booting on the Gnex works well? All I’ve seen on the web has been dual-booting for the Touchpad. Maybe I missed a link, but it would be great to hear back with some input! 🙂 Currently left running a CM11 nightly on the Gnex and would like a nice change of pace, but without losing Android to fall back on while the port matures.

> **Alan Morford** — 2014-09-02 12:12:06 UTC
>
> I know webOS Ports was working on the GNex but they lost their maintainer. If there is a build floating around for it it’s probably old. However, that doesn’t mean that once the foundation for LuneOS is laid for mobile phones it won’t be back ported. Might be a while but stay tuned.

> **webosports** — 2014-09-02 12:46:54 UTC
>
> Dual boot for the Nexus is not possible currently, the Touchpad can dual boot. The image for the Nexus is a couple of weeks old and not actively maintained going forward by the project team, but we’re happy to have someone take care of this going forward to keep it supported.

> **drfandroid** — 2014-09-02 18:24:04 UTC
>
> Yeah, I saw a kernel floating around for dual-booting but that was for Android ROMs. Shame, hopefully there’s a dev out there with an old Gnex lying around and willing to help out with the project. Maybe even bring it to the 2013 Nexus 7, which I happen to have around as well haha. I did notice going through the builds that the most recent one was back in mid-August :/ Well my device shouldn’t be going anywhere anytime soon, so I’ll definitely keep my eyes and ears open. Thanks for the replies, everyone!

> **Paul oberman** — 2014-12-02 06:34:05 UTC
>
> another gnex on cm11. Been lamenting the loss of webos.
>
> Hopefully they find someone to maintain that device. Xda?

**Evacaf** — 2014-09-02 03:26:53 UTC

Alan, I do have a TouchPad (of course 🙂 ). I didn’t know I could dual boot with LuneOS though. I have to try that. Currently I am dual booting LunaCE and Android. I’ll see if I can change it to dual boot with LuneOS and Android. Thanks.

> **webosports** — 2014-09-02 05:30:54 UTC
>
> You can triple boot it 🙂 LuneOS is installed on an ext3fs partition 🙂 Size wise it’s quite small anyway 🙂

> **Alan Morford** — 2014-09-02 12:12:58 UTC
>
> As far as I know and you might want to check with Herrie on Twitter but you can triple boot.

**Beeber** — 2014-09-02 09:40:04 UTC

Whoa. I’ve literally waited YEARS for this moment. I hope I can get it running soon. (Hint: create an idiot-proof installation process, like the Doctor)
PS: Excuse my caps, I’m just very excited

> **Alan Morford** — 2014-09-02 12:14:34 UTC
>
> I think there is a doctor in the works. Might be a while though. If you doctor, it will wipe your TouchPad though! Dual booting allows you to keep both. I’ll look into creating a tutorial that’s more my speed (aka dummy-proof)!

> **Beeber** — 2014-09-03 13:31:27 UTC
>
> OK, I tried to install LuneOS on my TP and… failed miserably. Feeling like a noob. I guess I’ll have to wait for instructions for dummies from either you or webos-ports (huge thank you btw!), or wait for the LuneOS Doctor.

**Christopher Price** — 2014-09-02 10:55:11 UTC

So it would be fair to say that the Open webOS project no longer is working with you guys?

LG has, in my view, failed to deliver on every facet of their commitment when taking over the Open webOS project and driving that project forward in an open manner.

This appears to be the last nail in that long-dead coffin. Best of luck with LuneOS.

> **webosports** — 2014-09-02 15:01:24 UTC
>
> It’s not that black and white to be honest. Open webOS is still actively being developed by LG (SVL) (almost daily commits on <https://github.com/openwebos> for example). Most core components of the OS are still actively being updated and used in LG’s webOS for TV’s as well as in LuneOS
>
> The big difference being that LG has replaced the LunaSysMgr UI by their own UI that is being used on the TV’s currently. This hasn’t been made open source and there are for sure other parts of LG’s TV webOS that have not been made open source (yet) either. We would welcome more components to be open sourced by LG of course, however that’s not our call to make.
>
> LunaSysMgr as it was can therefore be considered “dead” since neither LG or WebOS Ports is developing on this anymore (this is mainly due to the fact that it was optimized for webOS specific hardware + drivers and wouldn’t work properly with non-webOS (read in our case Android) hardware + drivers.
>
> WebOS Ports decided to rewrite the UI from scratch with Luna Next to overcome this problem and also get rid of a lot of legacy code that was in there and “not needed”. This of course had some setbacks but also quite some advantages because we could take proper design decisions for a lot of things and go back to the drawing board where needed.
>
> Furthermore we have decided to also look at other technologies that are available and where needed we have replaced the existing parts in Open webOS with a more proper variant (in our views). A good example for this is that we use Maliit instead of the EFIGS that was supplied in Open webOS for the virtual keyboard.

> **Christopher Price** — 2014-09-02 15:53:54 UTC
>
> “We would welcome more components to be open sourced by LG of course, however that’s not our call to make.”
>
> Certainly, but LG said at the time it was full steam ahead with Open webOS. That isn’t what has happened. LG has internalized all the components needed to get a buildable stack. Yes, code is being accepted to core components, but is there one single device you can build Open webOS today on (aside from an Ubuntu PC – and I’m not even sure if that counts, let alone works)?
>
> Perhaps it’s for the best, mismanagement of Open webOS may be sealed off and LuneOS could take off on its own, implement a Dalvik/Bionic layer and Android compatibility.
>
> Again, best of luck, but LG should be offering to incorporate LuneOS into Open webOS… not creating a wall of separation. At least, if they wanted to stay true to their commitments when they acquired webOS.

**Philippe Elsass** — 2014-09-02 13:45:46 UTC

Can I install that on a Nexus 4 using Multirom?

**Omar Naggar** — 2014-09-02 14:07:51 UTC

Thanks mate for putting the pieces through months of hard work…I will clean the dust and try to install this today …

Glad I could ditch android and start from scratch with webOS,need a change mate.

**John Margarone** — 2014-09-03 01:06:54 UTC

Someone needs to contact jcsullins. He has a utility called to toolbox. It single instance loads via Web OS recovery mode. Once recovery mode on the Touchpad is up, it is loaded via a .bat provided in the top toolbox directory. Once you run the .bat with novacom drivers up on the pic with Touchpad in recovery mode, to toolbox is streamed in via USB and launched.

The toolbox can install various Android roms AND Web OS. It will also allow a complete removal of Web os if desired.

I suspect a dev of JC’s skillz set could easily adapt his toolbox to properly partition for and install LuneOS as well as Android and Web OS.

Goo.im/devs/jcsullins/cmtouchpad/tptoolbox
That is where you will find toolbox

JC Sullins is on rootzwiki and XDA

Search HP Touchpad The Super Easy Way and you will hit info on JC Sullins and his awesome dev efforts and his tptoolbox

As far as Android on the Touchpad goes jcsullins cm11_20140625 is an excellent rom. Please donate if you decide to use it

The tptoolbox supports a bunch of different roms and knows if it is a data/media rom or standard and partitions / formats appropriately.

Thus I suspect it would take VERY LITTLE WORK to get tptoolbox supporting LuneOS and Web OS AND Android simultaneously via the moot 0.3.8 menu. Seems to me to be a perfect tool for you guys and gals.

If I knew JC I would ask, but I do not. I am just another grateful fanb0y hehe.
Much better for one of the project heads here to contact him and ask him about the possible viability and for his permission/help in getting tptoolbox installing Lune…..you freakin Lun3yT00n3y freakshows! !

8)

**Ian Miller** — 2014-09-05 19:51:51 UTC

Nexus 4 ordered. Can’t wait to try this out.

**moe** — 2014-09-14 15:42:05 UTC

Can I triple boot my touchpad? I have webOS and cyanogen mod android 4.0.2 they are both stable and I dnt want to remove any of them. But I want to try the new luneOS so if there is a way to add lune to my boot list please help me. I have 32gb version so I have a lot of space to save.

> **Alan Morford** — 2014-09-14 19:58:01 UTC
>
> Check out this thread. <http://forums.webosnation.com/luneos/328536-triple-boot-cm9-webos-ce-luneos.html>
