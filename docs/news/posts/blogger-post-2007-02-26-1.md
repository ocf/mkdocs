---
date: 2007-02-26
---

# Oops
Some of you may have noticed that we had prolonged downtime on Wednesday, Feb 21.  Long story short, I screwed up.<br /><br />I was trying to fix our continuing file server problems by making changes to our server configuration and applying some Solaris patches. I brought the server and our core services down for a reboot, applied some patches, and booted up the system. Unfortunately, the boot process hung, so I waited a few minutes and tried rebooting. No dice.<br /><br />After a few cycles of rebooting, monitoring, and various attempts at server black magic, I had pretty much given up when sluo, a former OCF Site Manager signed on and helped bring the server backup.<br /><br />We're pretty sure a Solaris patch was to blame. The patch had worked on other OCF machines, but apparently our bleeding-edge SunFire T2000 didn't like it.
