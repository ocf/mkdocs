OCF Board of Directors (BoD) Meeting
30 October 2003

Tonight's BoD		Present (y/n)?
---------------------------------------
akopps			n
jkit			y
eleen			y
geo			y
remlluf			y
cpfeyh			y
jones			y
elliot			y
sajmm			n
yonathan		n
mbh			y
njstahl 		n
phlee			y
kitajun			n

Total members: 14
Needed for Quorum: 10
Present: 9

Tonight is First Consecutive Absence
-----------------------
akopps
sajmm
yonathan
njstahl
kitajun

Tonight is Second Consecutive Absence
---------------------------------
(n/a)

Present but not on BoD
---------------------------------------
kaisenl

BoD for Next Meeting
Name		Absenses going into this mtg
----------------------
akopps		1	
jkit			
eleen			
geo			
remlluf			
cpfeyh			
jones			
elliot			
sajmm		1	
yonathan	1		
mbh			
njstahl 	1		
phlee		
kitajun		1	

Total Members: 14
Needed for Quorum: 10

--------------------------------

Minutes

GM Message
	Paper and toner
		Paper and toner is located in the big filing cabinet next
		to the desk and printer

		The key to this cabinet is in the lockbox near the medium
		sized filing cabinet
	
	Printing Alias
		We've been using the pimp@OCF e-mail
		We should start using the printing@OCF e-mail
		printing@OCF used to bounce messages sent to it
			this has been fixed

	Wireless Access
		ASUC wirelesss has been set up by Fullmer
			It's done but is not ready yet because it
			has to "gel"

			This wireless is not airbears
			It's not a closed network, it should just
				show up on your computer without
				special access
			
	Air Conditioning
		Was supposededly fixed but is actually not
		Jimmy is working on it
		If you need AC but the circuit breaker has tripped,
			e-mail sm@OCF or gm@OCF

	Account Names
		Put the exact name off of UCB ID onto the account forms
			and into the approve script

		Must have the full name off the card, feel free to add
			nicknames, but *no less than full name from ID card*

		This problem will be solved soon by using CalNet user IDs
			- Using CalNet, full name is not private info
			- Eventually we'll have login via CalNet and
			be able to reset password online

	Printer Settings
		Users currently have ability to delete their printer
			settings, especially on the Macs
		How do we restrict modification to printer settings?

	Paper Theft
		Don't let users steal paper from the printer.

	Scanner
		We have a good scanner.  It works.
		It's hooked up to the Dell in the Southwest corner

SM Message
	Do we have toner on order?  (Unknown/No answer)
	Is there a way to check how many pages have been printed
		using current toner cartridge?

		- There is an absolute page counter, you can
		record how many pages have been printed when you
		replace the cartridge
			- Then subtract that number from the number
			of pages currently printed

	When was the last time the printer was serviced?
		No one knows.

	A staff member got mad and quit OCF staff
		Good for him.

	Getting more responsibility and access at OCF
		jones: If you're in the lab enough and it would
		be useful there's no problem getting more access

		If you use it for the power for good.

		Reading logs and have access = no problem

		E-mail Devin or talk to him at meetings

	ASUC Cluster
		1 computer has been installed in ASUC cluster
		Couldn't figure out how to make other computers work
		Devin has decide he hates NIS+ and wants to do away
			with it.

	NIS+ Replacement: LDAP
		NIS+ is old and unsupported.  Documentaiton doesn't
		make sense, and there is no documentation on OCF's
		implementation of NIS+

		LDAP is NIS+'s replacement.  LDAP is:
			- Being used by campus to distribute public
			and private info
			- Better.
			- Useful for other things like
				- Authentication with CalNet
				- Allowing users to self-service
				password changes

		There are other people on campus working on LDAP		
		Devin will also work on it

		There is a campus committee on LDAP
			Not only for CalNet
			Just about LDAP in general
			There's a majordomo list

		LDAP is built into new Microsoft software
			- Is it made by microsoft?
			- It's supported by Microsoft and Apple
			- Designed to be interoperable between systems
			- So we don't have to make homegrown connections
			(i.e. between NIS+ and Samba)

	Purchases
		More RAM for servers?
		ASUC's money was frozen
			- We don't get our cash until they elect a lot of new
			people
		We're currently left with $2814
			Phone bill will be $360 max
		Fullmer needs an invoice for the Dell for $600 to reimburse OCF
			and forms to deal with purchose of old AC unit
		Webcam
			Cheap capture card has been found
			Willing to try it
		SSL Certs
			Some certs found for about $100
				but some cheap certs aren't recognized
				by all software
			Hopefully will cost $200-300 max
				- our e-mail cert needs to be good
					- i.e. more expensive
					- b/c e-mail cert needs to be
					recognized by everyone
				- webserver cert onlyl needs to cover 90%
				of browsers
					- not as big of a deal as e-mail cert
		Power supply for Athlon box in server room
			We need one.
		SM Contingency FUnd
			- So SMs can just buy stuff
			- We can't get quoroum often enough, so SMs need
			some leeway to make purchases fast, if need be
			- Has this contingency fund been routinezed somewhere?
	Software (UNIX):
		- Our UNIX software is out of date
			- remove mozilla and netscape
				- get Firebird
		- abiworld - old
		- GAIM - old
		- install via packages
			- look around for where to install
				- opt/local/package
				- opt/src/user
			- jones will show mbh how to do this.
		- mbh knows how to configure blackbox to look nice
		- cpfeyh says: always test stuff, don't ever take down
			something that works.
			- jones: standard procedure is to install in
			a new directory and ask people to try it out
	Software (Windows):
		- If you want to work on the windows machines,
		and are comfortable administrating them,
		talk to jones about the administrator password
		- Things to install:
			- Powerpoint, OpenOffice, Exceed
		- We need to update the Gateway hard disk image
			- We can do this as a day when people
			learn how do a clean new windows installation
		- We have a Samba mounted windows directory with
			an entire image in it.
		- Things to uninstall?
			- McAfee (Dells) - is this auto-updating?
				- Replace with Norton?
					- We have a campus license for Norton
		- E-mail ideas of things to install to staff@OCF
	Proxy
		- The library has classified OCF as on campus
			- Thus disabled proxy access
		- CNS has classified OCF as insecure
			- Thus has disabled full access to campus network
			- This is technically correct.
		- Thus we currently do not have full access to the library's
			resources.
		- Someone needs to talk to the library and get them to give
		us proxy access.
		- Tell users "we're working on it."
	Spam
		- War has been running really high loads b/c of SpamD
			- spamd is CPU intensive
		- Jeremy's been talking about making the new spamd server
		- Our mail server is running slow
			- worst case: messages being delayed several hours
			- Other people have been taking care of this
				besides Devin
				- People have been disabling spam-assassin
				if the server load gets too high
		- SpamAssassin
			- Marks a message as spam or not
				- If deactivated, no spam is marked.
			- You filter to check for spam marking level
				and decide wat to do w/spam
			- The spam server's being worked on and
				is almost done (thanks to Jeremy)

	Printing
		- Dells are having problems selecting double-sided printing
		- Bem says this is a driver problem.
		- Printing Accounting
			- 6-up double sided pages count as 12 pages
			- simply dividing by 2 doesn't work
			- people are becoming more aware of this issue
			- who knows how to fix this stuff?
			- What do we tell users?
		- You can't sell paper to users.
			- jones: could we make this legit?
				- jkit: As long as it doesn't go in
					your own pocket!
				- we've researched this in the past and
					decided against it
				- cpfeyh: we'd have to send people to the
					4th floor accouting offices
				- Integrate with CalOne debit plan or CARS?
					- remlluf: The debit card hardware is
					already installed in the building.
						- You would just need to
						 install a card swiper
						 in the OCF lab.
						- Talk to Greg Snow @ rescomp
		- Quota Error Messages (or lack thereof)
			- When you're out of quota it kills your job
				 and doesn't tell you why.
			- We need to notify users that they're out of
				 print quota.
			- We could just make people aware to check their quota.
		- Print History Checker
			- Why don't we have one?
			- Why is our print history a secret?
				- The logs are hidden away on supernova
				- The print history doesn't show filenames
				- Does show who printed when.
	Documentation
		- Write down all questions and how you solved them.
		- Wiki
			- Need to research security options
			for restricting editing and viewing
		- Intelligibility
			- Users have not been understanding all
			of our helpful responses.
			- Surveys?
				- We need to survey users to figure out
				which explanations are useful and which
				are not.
					- Then evaluate responses
		
	Passwords
		- We need to emphasize strong passwords.
		- People think OCF is just a printing account,
		they don't relaize that the account will exist forever
		is a full shell access acount.
			- They don't realize an unbreakable password
			is important.
		- Jeremy has been running a password checker w/sorry
		- Devin: It's safe to tell users that if they pick
			a bad password that their accounts imght be turned
			off.
	
	Service, Windows Machines and User Quality in the modern age
		People expect a certain level of service...
		The kind of level of service where they don't
		know anything and expect themselves to not know anything.
		
		We didn't used to have Windows.
			- Windows is good, but
			90% of our users are exclusively interested
			in Windows and free printing.

			This is bad.

		It detracts from our ability to provide good service 
			if we're constantly dealing with everyone's
			stupid issues.

		Consider the following: No windows machines?
			No printing?  No free printing?
			Free printing is the jackpot for most users.
			They're willing to get an OCF account solely
			for the free printing, and ignore everything else.
				
				What is exactly *is* everything else we do?
					- ASUC and everyone else loves
					our free printing

				What is our purpose?
					Besides free printing?

					These days, none of our services
					are unique.

				If we drop our newbie windows services
				we'll be declared a geek club and screwed.
				ASUC will never let us use MLK.

			If all they want is free printing, they don't
			even need/want an account.
				
				But we need accoutning to prevent
				print abuse.

				Fullmer: We can set up windows to reject
					big printing jobs
						- Limits abuse
						- If you have a really
						big job you have to 
						manually print each
						section.

				Devin: printing only accounts?
					- Crappy passwords owulnd't matter
				
		Patrick: We can try to provide but we're
			definitely limited.
	
		It's not worthy getting freaked out
			over.

		The Dells were never supposed to be Windows.
		All windows machines are totally impacted.
		Staff can't even sit down.
		Our UNIX machines suck.
		Devin: Plans to convert Dells to Linux, just to piss
			people off!
		mbh: We could really nice, user friendly Linux
			Xandros
		Patrick: have something people use and like
		We always fail to converting to Linux b/c of NIS+
		ppl complain about geeks and EECS
		ASUC tells us we must use windows.
		Linux is okay but it's got to be clean enough
		for end users.
		Problems between NFS and SUN
		We are one of the most high profile groups in ASUC AUX

		We need to fix our website
		What is our desired level of service
		Making signs to be useful things for users
		jkit: help points--you can only ask for help X number
			of times

		Question tracking
			If the same questions keep coming up
				is something broken
				or is the process to complex

			Fix the computers vs. fix the users

			Help pages
				Ther's no reason why we have to exist
				Online we communite

		bBay- it will be our new purpose!


