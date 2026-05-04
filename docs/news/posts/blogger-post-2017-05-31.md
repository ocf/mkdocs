---
date: 2017-05-31
---

# Announcing HTTPS for web apps
<a href="http://status.ocf.berkeley.edu/2016/07/introducing-https-for-virtual-hosts.html">Last summer</a>, we introduced automatic HTTPS for all OCF-hosted websites with virtual hosting, helping keep private data sent to these websites safe from government spies and would-be password thieves. Today, we are announcing the same feature for our <a href="https://ocf.io/docs/services/webapps">web application hosting service</a>.<br />
<br />
This enhancement has already been rolled out for existing web apps, and it will come out-of-the-box for new ones. For more info, check out the <a href="http://status.ocf.berkeley.edu/2016/07/introducing-https-for-virtual-hosts.html">original announcement</a> as well as the updated FAQ below.<br />
<br />
<h4>
What do I need to do?</h4>
Most likely, nothing. Thanks to greatly increased <a href="https://letsencrypt.org/">Let's Encrypt</a> request rate limits, we can download certificates and configure your website to use SSL almost immediately.<br />
<br />
<h4>
Will this break existing links to my website? Do I need to update posters with the new link?</h4>
No. We will issue 301 redirects to the updated URL.<br />
<br />
<h4>
Are you sending the <a href="https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security">HSTS header</a>?</h4>
Still not yet, but it's certainly on the agenda now that we've been using HTTPS on regular virtual hosts for almost a year. We already send the HSTS header for www.ocf.berkeley.edu, including all websites for individual accounts.<br />
<br />
<h4>
What even is app hosting? How do I get it?</h4>
<a href="https://ocf.io/apphost">Web application hosting</a> is a relatively new service we offer which allows groups to develop sophisticated websites using modern web technologies not available with regular virtual hosting. The eligibility requirements are the same as for regular virtual hosting, and you can apply be emailing <a href="mailto:hostmaster@ocf.berkeley.edu">hostmaster@ocf.berkeley.edu</a>. Please read the <a href="https://ocf.io/apphost">help page</a> for more information.<br />
<br />
If you have any more questions, please <a href="https://ocf.io/contact">email us</a>.<br />
<br />
Finally, you can log into your website at ease!
