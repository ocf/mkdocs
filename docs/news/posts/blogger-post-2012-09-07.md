---
date: 2012-09-07
---

# Incorrect CGI ownership on webserver
<div dir="ltr" style="text-align: left;" trbidi="on">
For approximately 8 hours, (between 7:15am and 3:30pm on Sep 5), CGI scripts were running as shared user www-data. This may have broken CGI scripts during that time and if directories were world-writable (not recommended for web directories), may have created files owned by www-data. We are investigating and will correct any bad file ownerships as needed.<br />
<br />
PHP (more commonly used than CGI) was not affected. <br />
<br />
<b>Edit 01:00am:</b> File ownerships were corrected. Only one user was affected.</div>

