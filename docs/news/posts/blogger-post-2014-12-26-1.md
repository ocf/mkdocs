---
date: 2014-12-26
---

# Update on scheduled downtime Dec 27-28 and Jan 3-4
<b>Update Jan. 04: </b>The outage is over; all services have been restored.<br />
<b><br /></b>
<b>Update Jan. 02:</b> We've just migrated most services to the offsite server, and taken the others offline for the second (and last) scheduled outage. We expect to be back online for good Sunday evening.<br />
<b><br /></b>
<b>Update Dec. 28: </b>Power was restored at 7pm PDT as expected, and all services are now back online. Everything we had planned (powering on the servers remotely via IPMI, copying files/db from the offsite host, etc.) worked great during both the transition to and away from the offsite server. We will do the same thing next weekend. If you still notice any problems, please <a href="https://ocf.io/contact">contact us</a>.<br />
<br />
As we found out <a href="http://status.ocf.berkeley.edu/2014/12/scheduled-downtime-dec-27-28-and-jan-3-4.html">earlier this month</a>, there will be a power outage in Hearst Gym during the weekend of December 27-28 and January 3-4.<br />
<br />
Normally, this would result in all services being completely unavailable. However, we've put in a lot of effort to reduce the impact by transferring as much content to an off-site server as possible. Here's a summary of what to expect:<br />
<br />
<ul>
<li><b>Web hosting will keep working for most accounts.</b> All student group websites have been copied, and almost all individual accounts.<br /><br />We copied all individual accounts which have had web traffic in the past month.<br /><br />We copied all student groups websites, but student groups with email virtual hosting will not be able to use the offsite server, and will be down during the weekends. Unfortunately, we aren't able to switch A records for these virtual hosts, so there's no way for us to keep these sites available during the downtime while complying with university policy on off-site hosting. Only about 7% of student groups are using email virtual hosting; the rest will be able to use the off-site server.</li>
<li><b>Email hosting and forwarding will be unavailable.</b> There's not much we can do about this, unfortunately. Mails will be delayed by the sending server automatically, and you'll receive them shortly after the outage ends.</li>
<li><b>MySQL will be available on the off-site server.</b> If your website requires MySQL, it will continue to work.</li>
</ul>
<div>
The main OCF website will be available, but the wiki will not. Other services (like SSH, F/OSS mirrors, etc.) will be unavailable.</div>
<div>
<br /></div>
<div>
We've spent a lot of time trying to minimize the impact of the power outage, but there are some things we can't do (we're extremely limited by the university's policies on off-site hosing, and our own lack of resources).</div>
<div>
<br /></div>
<div>
If you have any questions, you can email us at help@ocf.berkeley.edu; we'll be able to view and respond to mail during the outage.</div>

