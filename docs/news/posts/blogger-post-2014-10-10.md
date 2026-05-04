---
date: 2014-10-10
---

# mirrors.ocf.berkeley.edu - outdated Debian package repos
Today we noticed that <a href="http://mirrors.ocf.berkeley.edu/">our Debian package mirrors</a> had not receive updates since October 2nd, although syncs had been completing successfully. This was due to an issue with mirrors.kernel.org, our upstream mirror, which had not synced in the past week.<br />
<br />
Since our syncs were completing normally, we weren't alerted to the problem until today when apt warned us that our mirror was out-of-date. We didn't really consider the possibility that mirrors.kernel.org, which is a top-tier Debian mirror (and one of several which ftp.us.debian.org can resolve to) would receive no updates for an extended period of time. We'll add additional health checks to make sure that not only are syncs completing, but that we're receiving updates.<br />
<br />
We contacted the mirrors.kernel.org admins to report the problem, who were <i>very</i> responsive and fixed the problem within 30 minutes. Our mirror is now up-to-date.
