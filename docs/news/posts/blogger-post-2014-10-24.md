---
date: 2014-10-24
---

# Moving www.ocf.berkeley.edu to HTTPS-only
On November 22nd, all websites hosted under the www.ocf.berkeley.edu domain will begin using HTTPS instead of plain HTTP. We will redirect all requests to the corresponding HTTPS site.<br />
<br />
Virtually-hosted websites will continue to use plain HTTP, so won't be affected. There also shouldn't be any impact on sites which consist of static content.<br />
<br />
We recommend to change all of your absolute links to point to the HTTPS version. You can start doing this immediately; it's already supported! Since we will set up a 301 redirect, no links will be broken.<br />
<br />
There are a few things which some sites are currently doing which will cause problems under HTTPS:<br />
<br />
<ul>
<li><b>Including resources from non-secure pages.</b> Some browsers will refuse to load this content, while others will load it but display a degraded security icon.</li>
<li><b>POSTing to non-secure URLs.</b> If your website has forms which post to non-secure URLs, you need to update them to use https instead of http. Although we will set up a redirect, browsers will not necessarily follow this redirect when submitting forms. Additionally, browsers may give a warning if submitting a form which sends data to an insecure URL.</li>
</ul>
<div>
If your website does either of the two thing above, <b>you must fix it before November 22nd</b>, or parts of your website may break. If you use WordPress or another CMS, it is usually sufficient to update the URL in the admin panel.</div>
<div>
<br /></div>
<div>
We appreciate that this may be disruptive to many websites, and have not made the decision lightly. There are <a href="http://arstechnica.com/security/2014/10/verizon-wireless-injects-identifiers-link-its-users-to-web-requests/">m</a><a href="http://www.leviathansecurity.com/blog/the-case-of-the-modified-binaries/">a</a><a href="http://en.wikipedia.org/wiki/Firesheep">n</a><a href="http://www.washingtonpost.com/investigations/us-intelligence-mining-data-from-nine-us-internet-companies-in-broad-secret-program/2013/06/06/3a0c0da8-cebf-11e2-8845-d970ccb04497_story.html">y</a> <a href="http://searchengineland.com/google-starts-giving-ranking-boost-secure-httpsssl-sites-199446">r</a><a href="http://sectools.org/tool/sslstrip/">e</a><a href="http://www.washingtonpost.com/wp-dyn/content/article/2008/04/03/AR2008040304052.html">a</a><a href="http://www.symantec.com/connect/articles/perils-deep-packet-inspection">s</a><a href="http://www.techspot.com/news/57316-nsa-classifies-linux-journal-readers-tor-and-tails-linux-users-as-extremists.html">o</a><a href="http://www.washingtonpost.com/world/national-security/nsa-infiltrates-links-to-yahoo-google-data-centers-worldwide-snowden-documents-say/2013/10/30/e51d661e-4166-11e3-8b74-d89d714ca4dd_story.html">n</a><span id="goog_1376767756"></span><a href="http://www.nytimes.com/2009/06/23/world/middleeast/23censor.html?_r=1&hp">s</a><span id="goog_1376767757"></span> to use HTTPS by default, even for websites which don't contain sensitive information or collect passwords. This is an inevitable transition for the OCF at some point, and while it will be painful, it is easier to make it now than in another four years, when even more sites will be affected.</div>
<div>
<br /></div>
<div>
We estimate that there are about 90 OCF users (~0.3% of OCF users) with active websites which will be affected by the change. We'll try to contact them individually about the change. If you need assistance making changes to your website, don't hesitate to <a href="https://www.ocf.berkeley.edu/staff_hours">come in during staff hours</a> or <a href="https://wiki.ocf.berkeley.edu/contact/">send us an email</a>.</div>

