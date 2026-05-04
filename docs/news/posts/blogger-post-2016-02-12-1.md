---
date: 2016-02-12
---

# MySQL downtime Feb 11 to fsck disks
MySQL will be offline for about 10 minutes tonight for emergency maintenance.<br />
<br />
This is in response to unscheduled downtime about an hour ago due to a kernel deadlock which took down all MySQL services. We don't really think it could be caused by filesystem corruption, but because of recent corruption at the OCF which affected nearly all servers (caused by <a href="https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=788062">Debian #788062</a>) we think it's worth checking.
