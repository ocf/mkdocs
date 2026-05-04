---
date: 2016-02-29
---

# mirrors.ocf.berkeley.edu read-only for about 20 hours
We're moving <a href="https://mirrors.ocf.berkeley.edu/">mirrors.ocf.berkeley.edu</a>, our free-and-open-source software mirror, from its current hardware (a recycled desktop with some extra hard drives) onto a new server (with server-grade harddrives, RAID, etc.).<br />
<br />
To do this with the minimum amount of downtime, we're going to be copying the disk from our current mirror to the new server. To ensure consistency, we need to first make it read-only. We expect the copy to take about 8 hours, after which point we'll make the replacement server the main mirror. At this point, mirrors will be about 8 hours old, but will quickly catch back up when the cronjobs start running.<br />
<br />
<b>Update 8:30pm 2/28: </b>This is starting now.<br />
<br />
<b>Update 5:33pm 2/29:</b> Maintenance is complete.
