---
date: 2015-06-20
---

# Ongoing downtime due to server crash
At 1:07pm today, hal, our primary production server, froze. We are on-site and working to restore it. We are moving the important servers to another machine while we investigate, as hal continues to experience issues.<br />
<br />
<b>Update 2:07pm:</b> Service has been restored, but we are continuing to move servers to a different machine. There will be some downtime as we continue the migration, but it will affect single services only.<br />
<br />
Remaining to migrate: <b>(updated 5:04pm)</b><br />
<br />
<ul>
<li><strike>firestorm (ldap)</strike></li>
<li><strike>death (www)</strike></li>
<li><strike>pestilence (dns, dhcp)</strike></li>
<li><strike>supernova (admin)</strike></li>
<li><strike>maelstrom (mysql)</strike></li>
<li><strike>tsunami (ssh)</strike></li>
<li><strike>anthrax (smtp)</strike></li>
<li><strike>sandstorm (group smtp)</strike></li>
<li><strike>biohazard (apphost)</strike></li>
<li><strike>lightning (puppet)</strike></li>
<li><strike>earthquake (accounts)</strike></li>
<li><strike>typhoon (rt)</strike></li>
<li><strike>blight (wiki)</strike></li>
<li><strike>flood (irc)</strike></li>
<li><strike>reaper (jenkins)</strike></li>
<li><strike>dev-earthquake (dev-accounts)</strike></li>
<li><strike>pollution (cups)</strike></li>
</ul>
<div>
<b><br /></b>
<b>Update 5:20pm: </b>All VMs are migrated to jaws, and all services should be restored. We'll be debugging and rebuilding hal in the near future, and will be scheduling downtime some time in the next few weeks to move VMs back. We'll post a followup here when we have a date in mind.</div>

