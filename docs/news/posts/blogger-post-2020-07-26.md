---
date: 2020-07-26
---

#  MySQL upgrade saturday 726
As part of our work to transition from stretch to buster for our MySQL server, we'll be migrating user data today around 9:34pm.<br />
<br />
To do this, we'll be setting up replication on the primary onto a dev instance, which we will then switch the 'mysql' hostname over to. There will be a short cutover period once we switch over the host. This post will be updated if any issues arise.<br />
<br />
EDIT: The upgrade has been completed. We were under 10 minutes of read-only time and around 5 minutes of downtime. 
