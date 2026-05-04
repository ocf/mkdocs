---
date: 2016-03-19
---

# MySQL read-only Saturday 3/19
As part of our work to transition from Percona to MariaDB for our MySQL server, we'll be migrating user data tonight around 9pm.<br />
<div>
<br /></div>
<div>
To do this, we'll put the existing Percona server into read-only mode, then make a final import to the new MariaDB host. We believe this will take about an hour and don't anticipate any issues (we've already tested imports from our regular backups without problems).</div>
<div>
<br /></div>
<div>
Read-only mode is necessary during the import to ensure we get a consistent backup, and so that writes made during the transition are not lost.</div>
<div>
<br /></div>
<div>
Some sites may experience downtime while the server is in read-only mode (if they require writing to the database to show pages). Most sites will experience some level of degradation (e.g. can't log in to admin or edit posts).<br />
<br />
<b>Update 10:01pm: </b>We have entered read-only mode.<br />
<br />
<b>Update 10:10pm:</b> The backup is complete and is being imported into MariaDB now.<br />
<br />
<b>Update 10:14pm:</b> ETA 35 minutes.<br />
<br />
<b>Update 10:35pm:</b> The import was interrupted when the new server ran out of memory. We're increasing memory / reducing memory use by mysqld and starting the import again. Still in read-only mode.<br />
<br />
<b>Update 10:45pm: </b>ETA 38 minutes.<br />
<br />
<b>Update 11:11pm:</b> Import has finished, we're now swapping out MariaDB for Percona (which will involve about 2 minutes of downtime).<br />
<br />
<b>Update 11:16pm:</b> We've noticed some issues with the import (views were not correctly copied) so we'll need to re-do the import. Still in read-only mode, expect another hour or two in this state. Sorry for the trouble!<br />
<br />
<b>Update 11:44pm:</b> The view problem is fixed, so we're proceeding to move MariaDB into production. Expect about 2-3 minutes of downtime now.<br />
<br />
<b>Update 11:55pm: </b>All work is completed and we are now on MariaDB. Total downtime was about 3 minutes, with read-only mode lasting about two hours.</div>

