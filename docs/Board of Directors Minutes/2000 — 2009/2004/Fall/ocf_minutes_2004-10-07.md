Meeting Minutes taken by jkit


Meeting held in 223 Dwinelle, opened at 7:30pm

Attendance:
jkit, geo, eleen, kaisenl, mattfong, yury, dima, griffin,
huiran, frank, rwaliany, aoshi, chai, thomas, adrianl 

[GM Message]
Matt installed a new toner cartridge into the printer, and stocked two
more cartridges in the server room.  In addition to that, another
cartridge is currently in transit.  If the toner gets low, shake the
cartridge, if that stops working, then email paper@ocf and someone will
take care of it.

A battery was ordered for death, but we were just informed that the
purchase order was incomplete, so we have to fill out some more paper work
before the order actually goes through.  
	
Later in the meeting, we will need to vote on the issue of allocating
money to fix/maintain the iMac/printer.

Building ops came in recently, and informed us that the building had a
thermostat installed incorrectly which caused hot air to be produced when
the intention was to produce cold air.  This has been corrected.  Also,
they raised the temperature setting on the AC to 74 in order to say
electricity.


[SM Message] 

We have two new staffers, Chai (chaic) and Thomas (seunghun).

Akop came into lab today and finished up the monthly backups for
September.

Virtual hosts have been processed, accounts have been created for this
week.

The broken dell has been fixed.  Both the power supply and the
motherboard/cpu had to be replaced (thanks to brando and geo).


[General Meeting]

Some users have complained that they are unable to create a windows
roaming profile.  Originally this problem was blamed on the exhaustion of
i-nodes on supernova.  To remedy this problem, the profiles were migrated
to death.  However, the issue still remains, but this time the cause is
not the lack of i-nodes.  Anybody interested in looking into this issue?
(Thomas said he would like to look into it).


Staff gets a lot of email, and sometimes its hard to keep track of which
emails have been responded to to, and which have yet to be handled.  There
has been some discussion of installing a mail ticketing system.  smcc
suggested that we use a program called 'rt', Eleen says she'll look into
the details.  

Other possible solutions:

Bugzilla -  ruled out because its too complicated and bloated for such a
	simple task. 
Online web form - the details of how this would help are not clear since
	it just changes the method in which users input their problems,
	but not how we address/respond to them. 
Same system as CNS - they have some sort of email ticket program that is
	in use when we submit virtual hosting requests.
Matt suggested that procmail might somehow be used to help as well.


Currently, the 7th floor Eshelman library has 4 Dells that we supplied
them.  Those computers are capable of only web browsing since we were
specifally asked not to install anything else but a web browser on them.
Eleen heard that publications no longer wanted those computers on the 7th
floor, but Xavie explained to her that it was a miscommunication, and 
that the computers were wanted but that no more were wanted.
	On a similar subject, the ASUC has asked the OCF if we could
provide the second floor with some computers.  So, what we might want to
do is this.  Replace the 4 Dells on the 7th floor with 4 ultra1s, since
all the computers there need to do is browse the web (kind of a waste of
resources to have those Dells doing just that).  Install the four Dells in
the lab in place of 4 gateways, since there is a lot of usage there.  Take
the 4 gateways and install them in the 2nd floor.  We should ask old staff
which ultra1s we can spare to give up. 


The iMac has been broken for a while, and the printer has been somewhat
broken for a while.  Ryan moved that we allocate $1000 for TSW to diagnose
the printer and iMac.  Rany seconds.  The motion passes.


recessed 8:17 - 8:47

Yury has a webform that take syou to the calnet authentication site, after
you enter your calnet id and passphrase, you get redirected to page on
Yury's website that currently prints the full name of the user and whether
or not the user is a registered student.
	Security is an issue (partly because the first version of the
program was quickly found to be vulnerable).  However, Yury is confident
in his code and welcomes an audit by the staff.  Aside from security
issues, integratoin with the current system may cause some problems.
The current system has some nice aspects to it: it is a nice introduction
to unix and some of the procedures of the OCF for new staff members, and
it doesn't require us spending time on developing a new system.  We should
seriouslly consider that the time that would be spent on making this
online approval process work may be better spent on other projects, such
as a more extensive help system, or fundraising, or LDAP.  Also, how much
more convenient is an online approval system.
Dima moved to table the issue, Adrian seconded, the motion to table the
issue was passed.

Frank thinks that the OCF should start tabling again.  In general, the OCF
should try to be more visible to the campus.  This may increase the number
of users we have and also the number of staff we have.  Other methods of
advertisement include fliering, posters, chalking, newspaper adds.
Frank says that from his experience, fliering is not effective.  Chalking
is apprently prohibitted, so we should avoid that.  In the past, the OCF
used to set up a table on the corner of bancroft and telegraph and recruit
users.  This brought in a lot of users, especially during the first few
weeks of school.

	
We should have a way to clearly identify staff on-duty in lab.  Possible
solutions include a desktop that identifies you as staff.  A sign that
identifies you as staff sitting on your monitor.  Pictures of on-duty
staff posted clearly near the entrance.  Perhaps having pictures of the
staff on the website would also help.


We should have instructions clearly posted in lab so that when users come
in, they have an idea of how to get there problems answered.  Perhaps a
big sign on the southern wall of the lab would be appropriate.  

Chai, Thomas, and Kaisen are elected to BoD.
