---
date: 2012-06-12
---

# Web server replaced
<div dir="ltr" style="text-align: left;" trbidi="on">
<h2>






Web serving or: How We Learned to Stop Worrying and Love Debian</h2>
The OCF web server, which hosts <a href="http://www.ocf.berkeley.edu/">http://www.ocf.berkeley.edu</a> and hundreds of <a href="http://docs.ocf.berkeley.edu/wiki/Virtual_hosting">virtual hosts</a> for group accounts, was migrated over to our newest (and fastest) server running Debian GNU/Linux on June 9.

<br />
<h4 style="text-align: left;">





The Good</h4>
<div style="text-align: left;">
Websites, especially with dynamic content, should be loaded (much) faster. Features might be added later down the road.</div>
<h4 style="text-align: left;">






The Bad</h4>
This is possibly our most visible non-lab-related (intentional) change in the past few years, and when that happens, stuff tends to break. We made the change over summer to allow us the most time to fix things with minimal disruption, and before we are moved out of the basement of Eshleman Hall (sometime during or after August).

<br />
<h4 style="text-align: left;">






The Ugly</h4>
It might take us a while to fix things. <a href="http://docs.ocf.berkeley.edu/wiki/Contacting_OCF_staff">Contact us</a> if something doesn't work that worked before.

<br />
<h3>






Known unresolved issues</h3>
<ul style="text-align: left;">
<li>phpMyAdmin (web-based MySQL management) access from <a href="https://secure.ocf.berkeley.edu/pma/" rel="nofollow">https://secure.ocf.berkeley.edu/pma/</a> does not currently work, use <a href="https://webmail.ocf.berkeley.edu/pma/" rel="nofollow">https://webmail.ocf.berkeley.edu/pma/</a> in the meantime.</li>
</ul>
<h3 style="text-align: left;">


Troubleshooting </h3>
<ul>
<li>Are your CGI scripts returning an "Internal Server Error"? Some users have hard coded the path to old Perl or Python interpreters. We recommend changing the first line of these scripts to "#!/usr/bin/env perl" or "#!/usr/bin/env python", respectively.</li>
<li>Does your CGI script or binary depend on a particular architecture? If so, it may need to be compiled again for amd64 (Debian squeeze).</li>
</ul>
<ul style="text-align: left;">
</ul>
</div>
