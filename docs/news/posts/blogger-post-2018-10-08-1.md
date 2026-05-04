---
date: 2018-10-08
---

# IPv6 Connectivity Issues on October 8
Starting last night, the OCF has been experiencing some connectivity issues to our public SSH server over IPv6. If you are having trouble logging in to ssh.ocf.berkeley.edu, please try using IPv4 to connect. To do this, you can add <span style="font-family: "courier new" , "courier" , monospace;">-4</span> to your SSH connection command, like so<br />
<br />
<span style="font-family: "courier new" , "courier" , monospace;">ssh -4 <OCF username>@ssh.ocf.berkeley.edu</span><br />
<br />
If your SSH client does not support the -4 flag, you can also connect directly to our server's IPv4 address. To do this, just connect to `169.229.226.25` instead of `ssh.ocf.berkeley.edu`.<br />
<br />
Some other services such as MySQL may also experience issues over IPv6. If neither IPv6 nor IPv4 is working for you, please <a href="https://ocf.io/contact">let us know</a>.<br />
<br />
Thank you for being patient while we restore full connectivity.<br />
<br />
<b>UPDATE 2018-10-09 1:45AM</b>: IPv6 connectivity should be restored to all our user-facing services. 
