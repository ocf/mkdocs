---
date: 2014-06-04
---

# Subnet move
We'll be moving from our trusty old subnet, <span style="font-family: Courier New, Courier, monospace;">169.229.172.64/26</span>, to a brand new subnet 4x the size: <span style="font-family: Courier New, Courier, monospace;">169.229.10.0/24</span>. All hosts should be fully migrated by Tuesday, June 10th.<br />
<div>
<br /></div>
<div>
There may be small periods of downtime for all servers during Monday evening/Tuesday morning, but we don't anticipate extended downtime. All services should be otherwise unaffected.</div>
<div>
<br /></div>
<div>
If you access OCF servers via SSH, you may notice a warning that the IP address for <span style="font-family: Courier New, Courier, monospace;">ssh.ocf.berkeley.edu</span> has changed. The host key will not change, so you can continue to verify against our SSH fingerprints (available via HTTPS on <a href="https://wiki.ocf.berkeley.edu/services/shell/">our wiki)</a>. The new IP address for the public login server (<span style="font-family: Courier New, Courier, monospace;">tsunami</span>) will be <span style="font-family: Courier New, Courier, monospace;">169.229.10.25</span>.<br />
<br />
<b>Update 2014/06/06: </b>All OCF servers are now assigned both their old and new IP addresses. Old IPs have been removed from DNS, and servers will soon be assigned only their new IP. This may break existing connections (such as SSH).</div>

