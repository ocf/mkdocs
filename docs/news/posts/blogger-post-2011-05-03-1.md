---
date: 2011-05-03
---

# Login server, webmail, and wiki down
The login server (tsunami aka ssh.OCF), webmail, and wiki are not accessible since 1:01pm today.<br /><br />These services are provided by virtual machines. The physical hypervisor in which the virtual machines are run has issues accessing its data store, and we are investigating SCSI failure with the hard drives and controller.<br /><br />No user data is stored on these machines, so your data is not affected. We apologize for the inconvenience.<br /><br />If you need SFTP/SSH access, you may temporarily connect to one of the desktops, pileup.OCF.Berkeley.EDU, instead of connecting to ssh.OCF.Berkeley.EDU which is currently unavailable.<br /><br /><span style="font-weight:bold;">UPDATE 6:45p:</span> The login server (SFTP/SSH) is back up.<br /><br /><span style="font-weight:bold;">UPDATE 6:52p:</span> Webmail and wiki are back up.
