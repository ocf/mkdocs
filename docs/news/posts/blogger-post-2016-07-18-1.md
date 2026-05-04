---
date: 2016-07-18
---

# Introducing HTTPS for virtual hosts
The staff of the OCF strongly believe in the need for encryption of everyday communication. This case has been made not just by <a href="https://www.washingtonpost.com/investigations/us-intelligence-mining-data-from-nine-us-internet-companies-in-broad-secret-program/2013/06/06/3a0c0da8-cebf-11e2-8845-d970ccb04497_story.html">invasive</a> <a href="http://www.techspot.com/news/57316-nsa-classifies-linux-journal-readers-tor-and-tails-linux-users-as-extremists.html">government</a> <a href="https://www.eff.org/nsa-spying">spying</a>, but also by <a href="http://arstechnica.com/security/2014/10/verizon-wireless-injects-identifiers-link-its-users-to-web-requests/">wireless carriers (like Verizon) maliciously modifying requests</a> to increase ad revenue.We think that the internet needs to transition to encrypting all communications whenever possible.<br />
<br />
Two years ago, <a href="http://status.ocf.berkeley.edu/2014/10/moving-wwwocfberkeleyedu-to-https-only.html">we transitioned all of www.ocf.berkeley.edu</a> (all regular user websites) to HTTPS-only. At the time, it was impractical to also transition virtual hosts, because there was no way for us to acquire the necessary SSL certificates without a lot of manual effort.<br />
<br />
With the creation of <a href="https://letsencrypt.org/">Let's Encrypt</a>, a free provider of SSL certificates that prioritizes automation, we're finally able to start offering HTTPS for virtually-host websites as well. Starting today, we'll be slowly rolling out HTTPS for our virtual hosts. We expect the full roll-out to complete within about 3 months.<br />
<br />
<b>What do I need to do?</b><br />
Most likely, nothing. We'll automatically switch your site over to HTTPS when we acquire a certificate for it. (We're unable to immediately acquire certificates for all of our ~500 virtual hosts due to Let's Encrypt's rate limits.)<br />
<br />
<b>Will this break existing links to my website? Do I need to update posters with the new link?</b><br />
No. We will issue 301 redirects to the updated URL.<br />
<br />
<b>Are you sending <a href="https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security">the HSTS header</a>?</b><br />
Not yet, but we'd like to in the future. We want to make sure we've tested the current setup for some time first, as once we start sending the header, we can never go back to plain HTTP.<br />
<br />
We do send the HSTS header for www.ocf.berkeley.edu (user websites).<br />
<br />
<b>My site broke after the switch to HTTPS, what do I do?</b><br />
It's unlikely, but possible, that some sites will break because of this. Typically, this is because of the wrong site URL set within a CMS like WordPress. You should be able to fix this by logging in to the admin panel and making sure your site URL has <span style="font-family: "courier new" , "courier" , monospace;">https://</span> at the front.<br />
<br />
If there's anything we can do to help, don't hesitate to <a href="https://www.ocf.berkeley.edu/docs/contact/">send us an email</a>.<br />
<br />
<b>Update 2016-10-09:</b> The roll-out is complete.
