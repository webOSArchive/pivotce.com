---
title: 'To Doctor or Not To Doctor: A Call to Stop “Lazy Troubleshooting”'
date: '2014-01-30T01:38:20Z'
lastmod: '2015-04-21T18:54:18Z'
author: Alan Morford
author_slug: alanmorford
categories:
- Editorial
tags:
- doctor
slug: to-doctor-or-not-to-doctor-a-call-to-stop-lazy-troubleshooting
summary: The forums on webOS Nation are hands-down the place for webOS community interaction. Battery jumps to 0%? Stuck on the HP logo? All you have to do is ask for help.…
featured_image: /images/files/2014/01/doctor.jpg
source_url: https://pivotce.com/2014/01/30/to-doctor-or-not-to-doctor-a-call-to-stop-lazy-troubleshooting/
wordpress_id: 1334
featured_image_source: https://pivotce.com/files/2014/01/doctor.jpg
archived: true
comment_page: 2014-01-30-to-doctor-or-not-to-doctor-a-call-to-stop-lazy-troubleshooting
---

The forums on webOS Nation are hands-down *the* place for webOS community interaction. [Battery jumps to 0%](http://forums.webosnation.com/hp-pre-3/302416-instant-battery-drain-pre3.html)?  [Stuck on the HP logo](http://forums.webosnation.com/hp-pre-3/326267-memboot-not-working-stuck-hp-logo.html)? All you have to do is ask for help.  That’s the best part of our community!  We *support* each other.

While the level of help you will receive on the forums varies with the subject matter, there are always those issues which seem to gather more “just doctor and be done with it” responses than actual troubleshooting steps. **That’s a problem.**  Too often, help was just a bit too late to get there before someone pulled the “doctor it” trigger.  Let me be frank…if that’s you, **quit it**. *Seriously*.  And read on…

# “I tell people to doctor, so what?”

**The problems are not being solved, but being delayed instead.**  For issues that result from actual hardware failure, sure…”doctor away”. But for the rest (and majority) of the cases, it isn’t the *best* way to go. **Doctoring should not be the standard response to problems.**  It should be the ***last course of action*** when all options have been exhausted. Instead, what should happen is the issue should be thoroughly diagnosed and identified and a solution proposed. Only after possible solutions have been attempted should the last effort be doctoring.  Here’s an example:

# A case study – GMMan from the forums

*“Here’s my story.  I have Doctored my TouchPad for two times **total** for the same problem.  It was the bad WiFi issue, where after using the TP successfully for a few months, out of the blue it would quit connecting to my home network.  I did try to diagnose the problem by swapping out some binary files for others.  I eventually ended up using the support chat where they told me to doctor.  I ended up doing a “delete data” and after a bit of difficulty managed to get things working again.  A few months later, the same problem occurred.  Knowing the solution to the problem the last time, I doctored again.  It worked…for* [one]*day.  I tried other doctor versions, then “OTAing” off of whatever signal I got.  Nothing worked.  I then went on to search the problem out, and on an Android forum it was discovered that the TouchPad only likes wireless channels 2-4, and had trouble connecting to most other channels.  I changed my router channel to 2, and presto, it worked fine ever after.  I regretted doctoring and I wasted lots of time and internet bandwidth by having to reconfigure my TouchPad and downloading back apps.  I’ve learned my lesson, and I now rarely suggest doctoring, and even when I do suggest so, I use a qualifier such as “may”.”    -GMMan*

What you can take from that is regardless of what tech support tells you, doctoring may not fix certain problems and may rather be a waste of time.  **In fact, it is likely to be overkill for many problems.**

Got a botched patch and device won’t boot?  Track down the bad file and push a new copy from the doctor archive (note: I did not say “doctor the device”).  Got a corrupted file system? [Boot from the installer ramdisk](http://forums.webosnation.com/hp-pre-3/324235-pre3-gsm-stuck-load-ramdisk-when-doctoring.html) and run “fsck”.  Stuck on USB Recovery mode and can’t boot? Use the command line to boot and start ordering replacement parts (doctoring won’t even help in this case). Sometimes it’s just those really simple root causes that create problems, and by knowing the right thing to do one can save a trip to the doctor.  Also, once the issue has been addressed and concluded it becomes historical data for others to reference in the future.

# We do it to ourselves

This problem stems from the fact that most of us here are just consumers, taking advantage of the “homebrew goodness”.  But when things turn for the worse, the consumers are stuck not knowing how to fix the problem, and in turn implore the knowledge of the forums.  **Since HP discontinued their chat support, we are effectively the only readily available resource for helping solve webOS problems.**

# Can our devices (and us) take the abuse?

Doctoring can be quite detrimental for several reasons.  Every time a device is doctored which overwrites and formats the flash and writes new firmware, it potentially wears out the chips that store those data just a little bit more than the last time.  Additionally, all configurations on the device are lost and only so much can be restored from the cloud backup, Save/Restore, etc. Not to mention all the *time it takes* to restore all the apps.  **Come on, we’re homebrewers!**  *Someone* knows how to dig into the problem!  The doctor is a great tool, but using it as a catch all…let’s face it, it’s abuse (and lazy).

# The need for standards

Too many people think the standard procedure for fixing webOS problems is to just doctor the device and hope for the best.  I see quite a few help requests indicate that the owner has already doctored their device, and their issue isn’t fixed.  What a waste!  The issue is compounded by the fact that HP/Palm recommends doctoring both on their support site and on their chat.

Don’t get me wrong, it’s great to see everyone help out, but there is a fundamental lack of standard procedures to diagnosing problems.  That leads to random guesses (*which is OK*) but that quickly falls to “doctor it” solutions (*which is not OK*).  There are those that like to poke around at the insides of webOS and love to help too, but aren’t always available.  So it’s incredibly important that the error, steps taken already, the device info, and any other pertinent information is provided to start diagnosing the problem.

To avoid the “just doctor it” hassles try following these **6 simple guidelines to making a great support request**:

1. **Make a detailed description of the problem.**  That means describe what you’re trying to accomplish, what is preventing you from accomplishing it, and what you have done to try to solve the problem.  Is the device on (power off, standby, or active)? Can it recognize your input? Is there an error message, and if so what exactly is the message, and along with it what sort of visual cues are there?  What app is this?  What makes you think something is wrong?
2. **If the problem is difficult to describe, include a picture.**  It is especially helpful when there is an error message of some kind, as in addition to seeing the original error, the surrounding area may provide clues to what program or part of the program the problem is stemming from.  That said, don’t include a screenshot for really common errors, such as “Too Many Cards”, “Application Database Full”, and “Not Enough Space”, as these are all too common and don’t actually provide any useful info.
3. **Search around.** If you found some posts that may relate to the problem, link to them.  And that includes anything external to webOS Nation.  I’m not a moderator, but I feel that the more relevant resources are available, the more helpful it will be to people who are trying to diagnose the problem. If you’ve found some troubleshooting instructions, follow them and report what you’ve done and the results.  If the steps have modified your problem, reflect that.
4. **Attach logs.**  Try to obtain logs if you can.  Logs provide additional information about a problem that may help in identifying the source of the error. If your device is in general working order, follow [this detailed guide](http://forums.webosnation.com/hp-touchpad/319218-troubleshooting-how-collect-logs.html) on how to post logs.
5. **Be clear.**  You’re asking others to help you solve a problem, so be sure that other people can read it.  By writing “sumthng dat lookz lk thss, plsssszzszs11!!1!” will not help.  To the best of your ability write out full sentences and be as clear as possible.  Messages that lack an attempt to write something comprehensible might be ignored due to it being hard to read. If your native language isn’t English, just try your best and feel free to attach a message in your native text.  webOS Nation is global, and chances are someone can read your language and help you solve your problem or translate.
6. **Follow forum rules and etiquette.**  Don’t post the same question multiple times in different sub-forums, and be patient while getting an answer.  If your post doesn’t get responded to in a couple days, giving it a “bump” is acceptable.  Just be sure to engage in the problem solving process.  We can’t do all the work for you.

Conclusion

So in the end, let’s adopt some proper problem reporting techniques and stop defaulting to “just doctor it”.  It’ll result in less wasted time restoring data and better educated and more knowledgeable users. By following this guide you can better help yourself which will in turn allow us to better help you.  And from this non-programmer-end-user to you, I need all the help I can get!

#webosforever

This article is a re-purposed [thread](http://forums.webosnation.com/webos-discussion-lounge/319068-nation-excess-doctoring.html#post3355960) by GMMan from the webOS Nation Forums and was used with his permission.
