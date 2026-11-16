tirumari
anreiser*
mwilliams*
mandytri
kmock*
kedo*
benortiz*
amloessb*
kfang*
waf*
sanjayk*
daradib*
* = on BoD

Meeting starts at 7:15 PM.

Summer hours?
We will be open from 10 AM to 3 PM.
anreiser and amloessb will be here over summer.

End-of-Semester Banquet:
Saturday, April 30th at 7 PM at Joshu-Ya Sushi
Action item: Email Sherry if you're interested in going but did NOT fill out the Google form.

Cal Day:
sherryg talks about the rules for the Brawl portion. People sign up for shifts. It's decided that we should only give out pages (10, 20, 30, 40, 50) and candy as prizes (i.e. we would not offer increased web space).

Motion to allocate $40.12 to purchase Amazon toolset
Seconded by Aaron
Unanimously in favor.
Action item: kfang is purchasing it

Marketing event with boxes
Plan to put a box fort on Sproul

Printing
Felix: mySQL improperly writing and only leaving two jobs
There may be an issue with config because it's set to not logging history.

Conversation about getting a new server and plans for consolidation:
Mail will have a lot of network usage
We just need to tackle mail and web
Can we put them on separate?
Dara: We wanted one machine separate that would still run. We need wiki to rebuild everything and mon to monitor. We still want to have one server. If the machine is in the lab someone could accidentally turn it off.
Felix: Do we want to host wiki on Dreamhost?
Dara: Could use it as backup
Can automatically sync

List of services:
In the lab:Can keep biohazard/cataclysm, hurricane, experiments

In the server room:
logging - use a lot of CPU
logins-flood, supernova, tsunami - can virtualize
mail/spam/AV - use a lot of CPU
wiki/mon - critical
irc - easily virtualized, can go in the lab
web - use a lot of CPU
MySQL/Posgres - virtualized, should be with web server
consoles (snowstorm, lightning) - axed
DNS - critical
LDAP/Kerberos - critical

Kevin: Can we move death to pandemic?
Dara: Makes logical sense, because if web is still FreeBSD, it will work well with Sparc
if we wanted to virutalize everything possible, how many machines would we need?
Ben: Goal is two racks
Sanjay: Want to put these on separate network cards. We don't want the network to be saturated.
If "critical" is gone, would be very bad, so we want them up all the time
Sanjay: we had divided up mysql and web because the vast majority of important data is on mysql, if web goes down, people may want to access mysql
Kevin: What can mysql live with? Consoles?
Sanjay: death, no to consoles
Dara: either run it on death or something or run it on one of the VMs (about mySQL)
Sanjay: would probably be with a web server
Kevin: If you were to virtualize mysql, what else could you put with it?
Aaron: we need famine, pollution, epidemic for sure
Sanjay: We could buy loms? Hypervisor may not support lom card
Ben: We want to get rid of consoles it seems, combine wiki/mon, mysql/posgres
Ben proposes combining DNS, LDAP, Kerberos
Aaron: can we put mysql and death separate
Dara: mysql isn't intensive right now, it's user data, don't want it to fail
Sanjay: Mail is tricky because it was supposed to be blackhole, we should put it on the new server, we should probably separate mail, spam, and AV on separate VMs
Dara: Mail can especially at one point take a lot of CPU because spam and email increase a lot
Are we keeping earthquake and pox?
Sanjay: pox and coupdetat are nice
We can move domain controller to the lab
Sanjay: logging can be put on its own server
Dara: pandemic seems like a waste for only DNS, Kerberos, LDAP
Sanjay: it's unknown what could be put there
FreeBSD is not supported on that machine
Debian in theory could work
problem with famine: was restarting death a lot
Dara: pollution is backup, epidemic is disk array
jaws is supposed to replace wildfire
Felix: I thought we'd put wiki on jaws
Dara: wildfire is being DOSed daily
Felix: jaws could work for logging
Kevin: why don't we put it on blizzard
Sanjay: Decal server was donated for the purpose of decal
Felix: Jordan said Nick's intention was to be used for the decal
Ben: we'll only talk about blizzard if we get Nick's permission so use it
Dara: coupdetat, I think disk controller is unreliable, so it would be terrible for logging
we're running the service that is most reliable on the potentially buggiest system (pandemic)
Sanjay: we should plan without pandemic
Aaron: in the case that pandemic doesn't work
Sanjay: we could put it on the new server
Felix: could we put DNS, Kerberos, and LDAP on conquest?
Sanjay: no
So we need new server to take care of mail, I think 16 GB is enough
Ben: So we're getting one new server and definitely one next semester

[Break because there was just too much to write down]

Sanjay: we just need to find a reliable server for logging
Problem with wildfire may be misconfiguration or not powerful enough
Aaron: if someone configures something so that only critical things are logged
RAM and CPU are what matter for the new server for mail, etc. and login
Sanjay: why don't we allocate 6K
Dara: we can allocate 7K

List of servers we have; the numbered ones are the ones we can work with:
1. famine
pandemic - axed
2. new server
8. pox
3. monsoon
wildfire - going to be on pox
jaws - axed
4. epidemic
5. pollution
6. UPS
coupdetat axed
blizzard - not considered
7. netsplit

Resulting distribution:
Pox will take logging
Monsoon will take DNS and LDAP/Kerberos
Famine will take wiki/mon, mysQL, and death (web)
New server will take mail, etc. login
The lab will take biohazard/cataclysm, hurricane, experiments, and IRC

Motion to allocate $8K for a new server. All funds leftover will go to SM/Gm discretionary. If more funds are needed, we are willing to use money from the Misc. fund.
Seconded by Dara.
All in favor: unanimous

Action item: Send any quote you find for a server to staff@ocf.
Action item: Contact Nick about what exactly he intended blizzard for.


CalSec:
we have 5 towers not being used because we got the new Dell computers for Linux
We're thinking about giving 2 to CalSec
Changing the conversation to what we want to do with all old towers
The plan:
5th needs PSU, avalanche - Kenny is taking avalanche
Aaron and Felix want a box
Ben is taking a case from ragnarok

Motion to allocate 2 old linux machines to CalSec, 3 for staff personal use.
Seconded by Felix.
Unanimously in favor.

Action item: Please pick them up by next week or theyre going away.


Dara: About the hoser rack. Some of those IPs are going to be changed. We want to use hostnames for the new Linux boxes alphabetically and add doom and eruption to maintain this pattern.
Everyone seems okay with this.
Sanjay suggests destruction instead of doom.
Ben: riot will be the only public IP to access new staff rack
Names: avalanche, bigbang, cyclone, destruction, eruption, fallingrocks
Hosers will be behind riot

Motion to adjourn by Sanjay.
Seconded.

Meeting ends at 9:39 PM.


