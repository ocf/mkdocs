---
date: 2018-01-17
---

# Downtime on 1/17/18
We're currently recovering from a multi-drive RAID failure on one of our servers. Currently logins, MySQL, printing, account creation, and our internal DNS will all not work. We'll post status updates as we bring things back up.<br />
<br />
Downtime was on 1/17 from 13:27 to around 18:00 in total.<br />
<br />
<b>Note</b>: MySQL and accounts created are being rolled back to a backup as of <b>2 AM this morning (1/17)</b>, so any accounts created since then or database changes will be rolled back.<br />
<br />
<b>Update 1/17 15:25</b>: MySQL, logins, and DNS are all in the process of being restored. Database restoration will likely take around another hour, perhaps more, but logins and DNS are both close to being fixed.<br />
<br />
<b>Update 1/17 16:22</b>: Logins (LDAP/Kerberos) and DNS have been restored, MySQL is getting closer to being restored, probably will be about half an hour on restoring that. Printing is still a work in progress, but getting closer. Account creation is still down.<br />
<br />
<b>Update 1/17 18:09</b>: Everything except account creation should be back up again. We are working on restoring all accounts created today and then we will re-enable account creation. MySQL databases have been restored from our most recent backup (2 AM this morning). We have noticed some lingering issues with DNS that we will keep checking and update here if it stays a problem. Let us know if you encounter any other problems with our services!<br />
<br />
<b>Update 1/17 19:58</b>: Account creation has been re-enabled, although any new accounts made today still need to be re-created, but new accounts made from this point on should work fine. We also fixed a DNSSEC issue that was preventing valid DNS responses in some cases. <a href="https://ocf.io/contact">Contact us</a> if you notice any other problems!<br />
<br />
<b>Update 1/18 03:21</b>: All the missing accounts have been re-created again, but they will need to reset their passwords, since we purposefully do not log those for security and they were lost in our Kerberos rollback. These accounts can reset their passwords <a href="https://ocf.io/password">through our website</a>.
