---
date: 2006-10-17
---

# Status Update
All user data has been restored to the disk array. I'm currently running a fsck on the array just to make sure that the array hasn't already corrupted it. We'll be keeping very regular backups of user data until we can figure out what's wrong with our disk array or until we can get it serviced, so there shouldn't be any future extended downtime like this again (at least as a result of the disk array).<br /><br />We're on track for the OCF coming back online sometime tonight or tomorrow morning. As an added safety precaution, I'm currently setting up a two-way RAID-1 mirror with hot-spare on our primary NFS server (basically the computer that  serves all user files) to make everything triply redundant.<br /><br />Thanks for all your support through this process!
