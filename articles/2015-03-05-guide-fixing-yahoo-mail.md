---
title: 'Guide: Fixing Yahoo mail.'
date: 2015-03-05 17:23:45 UTC
modified: 2016-04-21 15:58:16 UTC
author: preemptive
author_slug: preemptive
categories: [Tips]
tags: [certificates]
slug: guide-fixing-yahoo-mail
source_url: https://pivotce.com/2015/03/05/guide-fixing-yahoo-mail/
wordpress_id: 2706
featured_image: ../images/files/2015/03/Fix_Yahoo.png
featured_image_source: https://pivotce.com/files/2015/03/Fix_Yahoo.png
excerpt: If you connect your webOS email app to Yahoo mail, you may have noticed that you stopped receiving mail late last week (around the 26th of February). The typical error…
---

# Guide: Fixing Yahoo mail.

If you connect your webOS email app to Yahoo mail, you may have noticed that you stopped receiving mail late last week (around the 26th of February). The typical error message is, “Requested encryption not supported by server”. On Yahoo’s forums, there were complaints from general users about a problem that seemed to occur on the 25th and it seemed possible it was an issue at Yahoo’s end. Forum user, [markar did some research](http://forums.webosnation.com/webos-discussion-lounge/329474-problems-yahoo-mail-2.html#post3435218) and suggested a solution. This seems to work for most users, so this article will detail some steps. There are implications of this process and it maybe useful in solving similar, future problems.

In this guide you will:

- Check the certificate chain.
- Download OpenSSL for windows
- Request the certificates and save them as files.
- Transfer, install and trust the certificates

# Disclaimer

Note that this fix seems to work and as such, suggests what the problem might be, but it is not entirely clear what the exact issue is. This method involves installing security certificates on your device to enable it to connect to the server. New certificates are usually accepted by existing, ‘root’ certificates (installed by the manufacturer) via a cryptographic process. Installing manually is possible, but you should be sure of the source and validity of the certificates to avoid compromising your device’s security. I don’t know enough to assure you of this and I’m just ‘some person’ on the internet. Do this at your own risk. [Follow the thread](http://forums.webosnation.com/webos-discussion-lounge/329474-problems-yahoo-mail.html) to see if there are new insights. Currently, this does not seem to work on 1.x devices, though it’s not clear why.

# Check with Digicert

[Digicert](https://www.digicert.com/) is a Certificate Authority (issuer). It offers a [tool to query internet servers](https://www.digicert.com/help/) for information on certificates. You can see from the settings in the email app that the server webOS contacts for email is palm.imap.mail.yahoo.com or imap.mail.yahoo.com if you’ve set it up as a generic account. The server is accessed via port 993, so that is appended to the address in the form, **palm.imap.mail.yahoo.com:993**. The Digicert page will accept addresses in this form and return a report on the certificate chain and it’s validity. Hopefully, you will see the server certificate for *imap.mail.yahoo.com. The ‘*’ indicates a wild card so the certificate should match to any sub domain including ‘palm.’. You will also see two intermediate certificates that are part of a chain of certification (or trust).

# The method

Linux and other open source systems use OpenSSL (Secure Sockets Layer) to perform needed cryptographic security operations. Linux-based webOS itself uses it. Proprietary systems might have their own version of SSL.

1. Instructions for querying OpenSSL on Linux are [here](http://www.cyberciti.biz/faq/test-ssl-certificates-diagnosis-ssl-certificate/), but the process is basically the same as follows.
2. If you are running windows, the most commonly installed desktop OS, you will first have to download openSSL for windows. Here is an [archive of 32 & 64bit versions](http://indy.fulgan.com/SSL/).
3. After unzipping, You’ll find openssl.exe in the bin folder. Run it for a command line interface. You will see the prompt, **OpenSSL>**
4. Type this command: **s_client -showcerts -connect imap.mail.yahoo.com:993** (enter).
5. You should see a response that includes three blocks of code. These are the certificates.
6. To get a copy of the output, right-click on the OpenSSL window icon (top left) for an edit menu. Select all and copy it.
7. Open a text editor (notepad will do), paste in the text, then select each block in turn from (and including) the header and footer lines.
—–BEGIN CERTIFICATE—–
(data here)
—–END CERTIFICATE—–

Paste each block into a new file & save them separately as, “yahoo1.pem”, “yahoo2.pem”, “yahoo3.pem”. Any name will do, but the .pem suffix makes it a certificate file webOS will recognise. If you wish to make backups, the proper description and expiry date might make a good naming scheme.
8. You can now transfer these files to each of your webOS devices via USB. The downloads folder is as good a place as any. The rest of the process takes place on the device.
9. Certificate Manager is in the app menu of the ‘Device info’ app. When you press the button at the bottom left, it may find the certificates. You can tap on each one and continue. If you just get a card that says, “Your document list is empty.”, don’t panic.
10. You can use Internalz Pro (available in Preware) to open each certificate in turn. On opening, Certificate Manager will be opened and it will ask if you want to trust the certificate. Tap “Trust”.
11. To send mail, you need the certificate chain for the smtp servers. The expiry dates may differ, but the process is the same, so repeat from step 4. You’ll see the address to use for this is **palm.smtp.mail.yahoo.com:465** (or whatever is shown in the email account settings).
12. Restart your device. It’s possible you may need to re-enter your password in the email app.

Your email should now work.

Big thanks to markar for the instructions!

# Implications

It is possible for some servers to offer dual certificates so an older (and vulnerable) SHA1 certificate is presented as a fallback, but this will not always be the case and will likely soon be deprecated. Apparently Google is pushing for this upgrade: [SHA1-deprecation: What you need to know.](https://community.qualys.com/blogs/securitylabs/2014/09/09/sha1-deprecation-what-you-need-to-know)

Although the version of OpenSSL (0.9.8j & k) in webOS should support SHA256, it is not enabled by default. It is not clear if webOS enables it. The problem may be that webOS does not perform the algorithmic check to install presented SHA256 certificates. The solution would be to somehow enable this or upgrade the OpenSSL version. A work around is to manually trust certificates as above.

The process began by querying the server about it’s certificate chain, revealing a server certificate & two intermediates. The root certificate was not displayed. These are usually issued with the OS or as updates. webOS has had no updates for some time…

The problems then are that the root certificates on webOS may be out of date. Even if they are replaced, it could be that the system will not authenticate them. Solutions are of course to update the root certificates and the version of OpenSSL in webOS. The first may be easier than the latter. This work around will hopefully suffice as the community narrows down the issues and possibly fixes them.
UPDATE: [A fix for OpenSSL](http://forums.webosnation.com/webos-internals/330666-openssl-updater-fixing-certificate-issues.html) is now available from forum user, Thibaud! Read and install *carefully*. It should be used in conjunction with this [root cert updater app](http://preware.pivotce.com/package/com.palm.rootcertsupdate) from forum user, frantid.

# Yahoo Expiry dates

These are dates for the diary. If something breaks again, if it happens at these dates, we will know what to do.

UPDATE: Note that [Grabber5.0’s Cert Grabber app](http://preware.pivotce.com/package/com.grabber.basiccertgrabber) will now update Yahoo IMAP & SMTP certificates in addition to Google ones, but this isn’t needed if you’ve done the updates above.
**IMAP** *.imap.mail.yahoo.com ~~Valid from 24/Feb/2015 to 24/Feb/2016~~ Valid to **25/01/2018** Issuer: Symantec Class 3 Secure Server CA – G4
**SMTP** *.smtp.mail.yahoo.com Valid from ~~26/Jan/2015 to 26/Jan/2016~~ Valid to **13/01/2017** Issuer: Symantec Class 3 Secure Server CA – G4
**POP** legacy.pop.mail.yahoo.com ,~~Valid from 04/Nov/2014 to **04/Nov/2015** Issuer: VeriSign Class 3 Secure Server CA – G3~~

# Request for assistance

Please [follow the thread](http://forums.webosnation.com/webos-discussion-lounge/329474-problems-yahoo-mail.html). If you can improve the above process or add information and fixes, please post there. I have also decided to start a general thread on these issues [which is here](http://forums.webosnation.com/webos-tips-info-resources/329502-sha256-root-certificates-openssl-future-security.html).
