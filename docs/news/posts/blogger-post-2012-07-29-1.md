---
date: 2012-07-29
---

# File server and user directory migration
<div dir="ltr" style="text-align: left;" trbidi="on">
We will be migrating the NFS disk array (file server) and LDAP server (user directory) to new hardware after 8pm tonight. This is necessary to maintain uptime and acceptable performance as much as possible during and after <a href="http://ocfblog.blogspot.com/2012/06/moving-to-hearst-gym.html">our move to Hearst Gym in August</a>.<br />
<br />
We will attempt to keep files <i>read-only where possible</i> so that services including web hosting will not be as severely affected.<br />
<br />
We lack the extra hard drives on hand (we will be using the same hard drives in the new hardware, which means they must be backed up, formatted, and restored), so partial downtime of all OCF services will be unavoidable.<br />
<br />
<b>Edit 07/29 02:00am:</b>  LDAP migration completed successfully without service interruption. NFS migration (during which file access will be read-only) postponed to later today.<br />
<br />
<b>Edit 07/29 06:00pm:</b>  NFS migration started. Mail service is offline. Web hosting and SSH are read-only.<br />
<br />
<b>Edit 07/30 01:10am:</b>  All services except mail restored.<br />
<br />
<b>Edit 07/30 01:25am:</b>  All services restored. NFS disk array may require minor downtime in the near future. Good night.</div>
