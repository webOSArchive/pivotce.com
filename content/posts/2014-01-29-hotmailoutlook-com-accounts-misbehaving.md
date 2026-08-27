---
title: 'FIXED – Update 2: Hotmail/Outlook.com accounts misbehaving'
date: '2014-01-29T17:41:32Z'
lastmod: '2014-01-31T01:38:55Z'
author: maninwhitecoat
author_slug: maninwhitecoat
categories:
- News
slug: hotmailoutlook-com-accounts-misbehaving
summary: For those of you still using a Pre or TouchPad as daily drivers and have email accounts with either Hotmail or Outlook (like me), and are having problems accessing those…
source_url: https://pivotce.com/2014/01/29/hotmailoutlook-com-accounts-misbehaving/
wordpress_id: 1390
archived: true
comment_page: 2014-01-29-hotmailoutlook-com-accounts-misbehaving
---

![SSL Error](/images/files/2014/01/email_2014-29-01_103620-180x300.png)For those of you still using a Pre or TouchPad as daily drivers and have email accounts with either Hotmail or Outlook (like me), and are having problems accessing those accounts today I’m certain you’re as alarmed as I am.  All too often during these last few rocky years of webOS use, we have come to know the dreaded “no longer supported” cloud that hangs over our heads.  ~~Could this be the latest in a string of end-of-life functionality for webOS?~~  **No!****This issue has a fix!  Read on!**

**UPDATE 1:**webOS Nation forums user Jerry Van Hoy pointed us in the right direction for the fix.  Users toto-w and Grabber5.0 discovered the links to use for the fix and user DMeister made a short tutorial that is pasted below. Thanks all!

1) Go to [https://s.outlook.com](https://s.outlook.com/) or [https://m.hotmail.com](https://m.hotmail.com/)
2) When prompted, Trust Certificate
3) Go on Email and sync the email accounts and all will properly sync again

I came home from work to find two error messages, each one associated with my Hotmail and Outlook email account: “Security Certificate Expired”.  Users on the webOS Nation forums started reporting early this morning that their Hotmail and Outlook.com accounts were giving certificate errors.  It seems the issue is not prevalent across the board as some users claim to not have the same problem.

**UPDATE 2:**As it turns out, Microsoft was hit with the surprise as well.  Many companies use the GlobalSign Root CA for certificate authentication and it was that CA that expired.  You can [read about it here.](https://support.globalsign.com/customer/portal/articles/1426272-expiration-of-old-globalsign-2014-root-ca-certificate)

![Cert Error](/images/files/2014/01/email_2014-29-01_101753-180x300.png)It seems the issue is quite self explanatory really, ~~but this means that on Microsoft’s side, the certificates they issued for webOS’s method of accessing the server to sync emails expired on 28 January 2014. All we can hope is for Microsoft to issue a new one~~. **If** that is in fact the case and **if** they will fix it are the important questions. The issue has already been [brought up to Microsoft](http://answers.microsoft.com/en-us/outlook_com/forum/oemail-oapps/palmpre-issues-with-hotmail/38929384-919e-4547-add9-61de2e64fd9f). Otherwise, we’ll look to the homebrew community to save the day…again.

We’ll keep the updates coming to this post.  Stay tuned.  Feel free to [join the conversation](http://forums.webosnation.com/webos-discussion-lounge/327226-microsoft-outlook-certificate-expired.html) or leave a comment below.

Images: Matt Williams
