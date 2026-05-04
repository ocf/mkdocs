---
date: 2016-03-11
---

# MySQL and printing unavailable for 34 minutes (resolved)
MySQL and printing were unavailable today for about 34 minutes due to an unscheduled outage.<br />
<br />
<b>Why it was down</b><br />
For background, all of the OCF's production infrastructure is supposed to live on two physical servers: jaws and pandemic. There's a third legacy physical server named hal which hosts some testing machines and our backups.<br />
<br />
Due to a problem removing a backup logical volume which led to a deadlock and many processes in uninterruptable sleep after Tuesday (believed to be a kernel bug), a staff member gave 15 minutes warning before restarting hal today (Thursday) to try to fix the issue. Since hal isn't supposed to hold important services, this should be totally safe and is considered an acceptable warning period, since normally the only people who will even notice are other staff.<br />
<br />
Unfortunately, two servers, pollution (the print server) and maelstrom (the MySQL server) were on hal due to some temporary migrations. They should have been moved back to jaws about a week ago, but weren't.<br />
<br />
When hal went down, it took down these production services, killing MySQL (which also took down many websites, the OCF's website, Request Tracker, ...) and printing in the lab. This was realized as soon as monitoring triggered, and the staff member phoned another staffer currently in the lab after hal wasn't coming back up.<br />
<br />
Due to a misconfiguration, hal entered maintenance mode, and the other staffer had to enter the root password and fix the filesystem configuration before hal would boot. As soon as hal booted, MySQL and printing were started and service was restored.<br />
<br />
<b>Timeline</b><br />
<br />
<ul>
<li><b>6:35pm</b> "15 minutes until hal restart" email goes out froms taffer at home</li>
<li><b>6:50pm</b> hal is restarted remotely</li>
<li><b>6:52pm</b> staffer realizes hal had production VMs and isn't coming back online; phones another staffer in the lab</li>
<li><b>7:04pm</b> staffer in lab fixes boot config, hal is restarted; remote staffer leaves home toward ocf</li>
<li><b>7:09pm</b> hal is back on and services are available</li>
<li><b>7:15pm</b> original staffer arrives in lab to find everything already fixed</li>
</ul>

