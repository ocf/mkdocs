---
date: 2017-02-18
---

# MySQL read-only Saturday 2/18
As part of our work to transition from jessie to stretch for our MySQL server, we'll be migrating user data today around 5pm.<br />
<br />
To do this, we'll put the existing jessie server into read-only mode, then make a final import to the new stretch host. We believe this will take about an hour and don't anticipate any issues (we've already tested imports from our regular backups without problems).<br />
<br />
Read-only mode is necessary during the import to ensure we get a consistent backup, and so that writes made during the transition are not lost.<br />
<br />
Some sites may experience downtime while the server is in read-only mode (if they require writing to the database to show pages). Most sites will experience some level of degradation (e.g. can't log in to admin or edit posts).<br />
<br />
<b>Update 5:01pm:</b> We have entered read-only mode.<br />
<b>Update 5:58pm:</b> The backup has completed, we are now importing it into the new database server. Probably another 45 minutes or so.<br />
<b>Update 6:07pm:</b> ETA 25 minutes.<br />
<b>Update 6:15pm: </b>ETA 16 minutes<br />
<b>Update 6:25pm: </b>Unfortunately we hit a snag during the import and have to start it over.<br />
<b>Update 6:29pm:</b> ETA 37 minutes.<br />
<b>Update 6:40pm:</b> ETA 21 minutes.<br />
<b>Update 6:46pm:</b> ETA 10 minutes.<br />
<b>Update 6:56pm:</b> Import has finished, we're now switching back into rw mode. This will involve a few seconds of downtime.<br />
<b>Update 6:59pm: </b>MySQL is now available as usual. Total time in read-only mode was about two hours. Total downtime was less than a minute.
