---
title: 'Comments: FIXED – Update 2: Hotmail/Outlook.com accounts misbehaving'
comment_count: 6
article_title: 'FIXED – Update 2: Hotmail/Outlook.com accounts misbehaving'
build:
  list: never
  render: never
---

**normsland** — 2014-03-03 15:20:34 UTC

The GlobalSign Root CA certificate expiry is much more than a problem then first mentioned. If you try shopping or going to a https site that’s certificate has been issued by GlobalSign the webOS 3.0.5 browser will show you that the sites https certificate is invalid. This is incorrect. webOS has an old root CA installed of which it is validating against. Thankfully some users on webosnations have come up with a fix. The fix which installs the new certificates from GlobalSign can be found here: <http://forums.webosnation.com/webos-discussion-lounge/327226-solved-microsoft-outlook-certificate-expired-8.html#post3415424>

**Cthulhu** — 2014-03-26 23:56:51 UTC

Thank you! You solve my problem with my Omnia phone! 🙂

**Debbie** — 2014-11-21 12:12:33 UTC

I can’t log-in to my hotmail account– I get the following error messages— problem establishing a secure connection—- server certificate error details: untrusted certificate unable to determine certificate origins—-AND THEN— refusing connection. This server has been previously noted as supporting http strict transport security. Due to ssl certificate warnings/errors, a connection will not be made.—– HOW DO I FIX THIS???? (PLEASE)

**omalone1** — 2014-11-25 16:03:44 UTC

I wish I knew. None of these clowns seem to be able to fix the problem with my bb kmt

**kashif ali** — 2016-02-07 06:07:39 UTC

My Hotmail account is not open because security certificate problems so this reason what shuold i solve my problem.

> **pattyland** — 2016-02-29 07:27:22 UTC
>
> Did you try <http://preware.pivotce.com/package/com.grabber.basiccertgrabber> ?
