Hi guys,

Sorry for the lateness, I'll be sending all the minutes I took but 
neglected to send in a big batch, for future use :P

Sue


10/18/07
OCF BoD meeting

* indicates person is currently on BoD

akit*
jchu*
sahnn*
gcwong*
gordeon*
geo*
stevklaw*
sluo*
abhi
yury*
Chris
wln
Kevin (kevintra?)

GM AGENDA

Budget $15,134.94

Transformers movie at Wheeler tomorrow
- movie at 7 pm, dinner at 5
- or we can watch another movie if we want

Wii love Steven
- Steven has left his wii in the ocf
- we can have a wii party sometime
- you can use it any time, but:
 	- don't break it
 	- dont't leave dead batteries in remotes

Graduate Assembly has a web job
- will email staff about it
- willing to pay $2000
- good fundraising for ocf!

SM AGENDA

Top Coder competition
- Introduced by Chris
- Top Coder is a website that does weekly programming competitions online
- they're doing college tours
- trying to coordinate an event here at Berkeley, will be sponsored by 
CSUA
- hopefully Wednesday, 11/14 @ 6 pm
- or alternatively 11/16
- need a location to host the event
- actual coding will take about 1.5 hours, entire event will last about 
2.5 hours
- need to use the space maybe 5:15-7:45ish
- just need computers that can run java applets
- people can bring laptops, but want to have computers available for those 
who don't
- we dont't have enough space for laptop users in the lab, need to use 
lounge too
- there will be maybe 25 people total (we don't have that many computers, 
but if people use laptops it'll be ok)
- yury: our windows machines are kind of flaky but we can use Live CDs
- Chris: it's all just running on the java applet, so should be okay
- Top Coder will cover expenses
- yury: there could be another event in heller lounge, so you should book 
the lounge too
- the laptops will require internet access, but everyone will be a student 
so that's okay
- chris: so how do I reserve the lounge?
- he should talk to ASUC auxiliary
- stevklaw: if you really need to and have loads of money you could rent 
pauley ballroom but not really worth it

10/20 Downtime
- milki: sle wants to upgrade solaris 3 to solaris 4
- milki: we had downtime already but sle had problems with his dry run
- we lost maybe 1/10 of our home directories
- yury: suppose sle remounts it but famine tries to reinstall zones and we 
have the problems sluo had before
- sluo: no, that won't happen anymore
- sle has already done it before, so it will be okay
- yury: I'm expecting a lot more downtime
- yury: we're breaking the RAID so if something happens during that time 
we'll have no safety net through RAID
- insert technical jargon here about scuzzy, disks, breaking RAID, etc. 
etc.
- yury: I don't think we've worked out all the kinks yet
- kevin: what are we getting out of this?
- sluo: primary reason is because we want to fix the firewall on these 
systems
 	- we think it's the root cause of all these computers randomly 
freezing
 	- we can't put it off forever
- kevintra: I want a documentation from sle of exactly what he's doing
- milki: yeah, sle has documentation, and he has a time schedule
- yury: I think we need to figure all this out before we start
- milki: we do have backups though
- sluo: I suggest extending the outage window
 	- I mean, look at rescomp-- they declare 12 hour outage windows 
for a 5 min thing
 	- it wouldn't hurt, and what's worse is if we announce a short 
downtime but end up out way longer
- yury and sluo can be around for parts of saturday

UGSC
- sluo: Undergraduate Computing Services, at Caltech
- like our equivalent at caltech-- offer similar services, but we are 
larger
- their staff is very small, only 4 people
- run all Linux, with core servers Linux
- they use LDAP and Kerberos (which we should also use)
- their clients are thin in that they're all NFS root clients
- they're interested in starting a Student Computing Consortium of student 
computing facilities
- the only other one we've talked to is the Student Computing Facility at 
Cambridge (via thomson)
- there are other groups at MIT, and Williams College, Carnegie-Mellon, 
etc.
- Liz Fong at Caltech would like to get into contact with them too
- kevintra: what do we get out of it?
- sluo: uh, basically nothing
 	- we probaly have the best hardware out of all of them
 	- could start a mailing list or something
 	- we'd probably be hosting most of the infrastructure
- yury: sounds okay

Changing Root Password
- yury: this will be REALLY hard
- talk to sluo

SAMBA
- yury: was discussed in a thread with dwc
- we can get the windows machines to work!
- could get around 5 sec login and logout times, possibly even better
- this is something that needs to be done to each profile
- yury sent out an email with links
- yury: someone needs to do this soon
 	- should only require about intermediate sysadmin decal level of 
experience
- involves compiling software, writing a script, praying a lot
 	- sahnn: I could uh, try to do it by the end of the semester
 	- geo: I can help sue

Project Groups
- gordon wants to restart Web
- yury: can you do webmail
- gordeon: i don't have the permissions
Other projects:
- update postgres
- mysql
- mail
- the other database
- upgrade other servers
- LDAP-- the project that never ends (yes, it goes on and on, my friends)
- windows imaging
- bring back local netgroups

meeting adjourns at 7:45
