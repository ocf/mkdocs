OCF Board of Directors Meeting
Thursday, 4 March 2004

BoD For Tonight:
eleen - present
jkit - present
elliot - present
adrian - absent (1st)
yehfang - absent (1st)
rahat - absent (1st)
hkim - present
akamike - present
phlee - present
kainsenl - present

# members total: 10
# members required for quorum: 7
# members present: 7

Quorum achieved!

Attendance:
name - login
---------------
jimmy - jkit
eleen - eleen
mike - akamike
shiva - shivab
kaisen - kaisenl
hugh - huiran
elliot - elliot
george - geo
joydip - joydip
patrick - phlee
harry - hkim
devin - jones

Present but not on BoD:
shivab
geo
huiran
joydip
jones

BoD For Next Meeting:
eleen
jkit
elliot
adrian - 1 absence
yehfang - 1 absence
rahat - 1 absence
hkim
akamike
phlee
kaisenl

# members total: 10
# required for quorum: 7

-------------------

Introductions:  name, login, pizza preferences and misc. info

jimmy - jkit
likes chicken, sundried tomatoes and mushrooms
jimmy is the site manager

eleen - eleen
general manager
handles money stuff
social stuff
people stuff
likes the same thing.

mike - akamike
(login soon to be leemike)
likes anything in terms of pizza

shiva - shivab
a vegetarian
but is okay with chicken

kaisen - kaisenl
doesn't care

hugh - huiran
Found about ocf b/c he's a websmaster for two clubs
3rd year
cogsci major
he's in 188
wants to join staff
likes whatever kind of pizza

elliot - elliot
likes anything, suggests pesto for the heck of it.

george - geo
anything except anchovies and olives

joydip - joydip
likes any kind of pizza

patrick - phlee
anything with meat
no vegetables!

harry - hkim
anything's fine

devin - jones
he likes chicken and sundried tomatoes

ORDERING PIZZA
Jimmy would like to point out that
sun dried tomatoes are a fruit
and mushrooms are a fungus

GM MESSAGE
- Not much!
- We have money in our miscellaneous fund, which the fund that we get to keepforever; they won't take it away.
- $600 - because Fuller bought some Dells from us.  We put the money in our misc. fund

ASUC FUNDING INFO
- ASUC gives us money for specific purposes; our usage of it is restricted.  (Specifically not food or socials)
- We bought Dells with this fund.
- We have another fund called miscellaneous.  We can use this for anything.

FUNDRAISING
It is good

T-SHIRTS
- Do it?
- Does anyone know how to make t-shirts?  No.
- T-shirt designs
- It's cooler if one of us does it.
- T-shirt contest?

SM MESSAGE
- Jimmy changed keyboard on one of windows machines b/c it was broken
- Locked down (old kbd).
- Old keyboard is on top of tower.

NEW BUSINESS
- STAFF STUFF 
	- Wiki is updated
	- Account creation is updated
		- Individual accounts
		- Group accounts
		- Logins
			- 50% of characters have to be from real name
			- we recommend that they are in order but are not strict.
				- use your judgment.

	- Making new accounts
		- fist them first

	- Changing passwords
		- make sure they actually know their login.
			- use fist.

	- Synching Windows Passwords	
		- To do this, log user in question on to:
			- hurricane.ocf.berkeley.edu
		- Refer users to password people  if it doesn't work.
			- (see http://www.ocf.berkeley.edu/staff_hours
			to find out who password people are)
	- Getting sudo access
		- ask GM or SM if you want to sudo

- JSP
	- Are we supporting it?
		- jjlin says no
			- worried about resources
		- Temporarily might be okay, but long term has to be brought
		 up at Bod?
	- What does this involve?
		- Install tomcat on webserver
	- Pros and cons?
		- Pros
			- supports jsp
		- Cons
			- takes up a lot of resources, depending upon
			# of users using JSP.
			- Shivab says:
				- JSP only issues 1 thread for each process,
				and doesn't spawn a lot of processes.
				- not a lot of people use JSP
	- More Performance Details
		- JSP has a performance advantage with larger or frequently
		used programs b/c it's compiled instead of interpreted each
		time
	- What is it?
		- It's a scripting language, like ASP, PHP.  
	- What does it do?
		- Runs java servletts
			- server side computing
	- Human issues
		- Would we have to provide tech support for people programming
		in JSP?
			- We don't particularly know much about it.
	- Security
		- Not a significantly more insecure than other scripting
		language servers.
	- Can you install the server on your own account?
		- Should be doable?
		- Except problems with talking to Apache?
			- Apache needs to register tomcat services
	- Conclusion:
		- jkit: talk with jeremy, if it's okay with him, feel free.

- PROFILES AND GHOSTING
	- Windows profiles are the settings for your windows.
		- Those profiles are stored on supernova, which is a unix box.
	- Supernova
		- unix file systems need inodes.
		- supernova's out of inodes.
		- We don't know what to do.
	- Background question:
		- When/where is the # of inodes set?
	- Possible solutions
		- Set up a samba server on another machine?
			- akamike: I've done it at home, but not securely.
			- jkit: You wouldn't be doing it by yourself.
		- Move windows profiles to home directories on death?
			- If we moved profiles to death, it would just transfer
			the issue to death.
			- Why are windows profiles on a different machine from 
			main server in the first place?
				- fact that they're on death suggests someone
				had a reason for the separation at some point
				in time
		- Other solutions: getting more disk
			- jones recommends: buy a really big hard disk running
			an operating system/filesystem that can handle a lot
			of little files
				- ex: xfs, razorfs
		- Filesystem change
			- What filesystem are we running?
			- If we upgraded it, would it solve the problem?
			- Is it possible to convert file systems?
		- Delete files
			- Look at internet explorer caches?
				- Each one may have thousands of small files.
				- Disable IE cache
					- it's possible to disable cache
					globally but realistically it's
					difficult to change all the settings
					for everything (e.g. all browsers on
					all computers)
				- deletion:
					-  make a cron job to delete temp
					 internet files daily
			- Clear inactive accounts?
		- Quotas
			- It is possible to set inode quotas.
			- But users probably won't understand inodes quotas.
	- Immediate solution: get rid of cache
	- Talking of converting current filesystem.
	- Do we even need windows profiles?
		- it's useful for customization
	- eleen: does anyone know how to do this?
		- joydip and shivab are recruited to work on this issue.
	- Who has power to decide these kinds of issues?
		- We should check the consitution
		- Believe that technical issues at discretion of sm
		- Talk of electing a policy dude ...to know policy.
			- e-mail psb with policy questions

- COURSE ACCOUNTS
	- There is no current policy
		- We've never really done them
		- In practice we've done them for decal courses and groups that are
		recognized by departments
	- Who owns courses?
		- Instructor or head ta?
	- What about simultaneous classes?
		- e.g. two different lectures for calc 1a?
	- Issues
		- shivab: would this generate a lot more traffic?
			- not significantly
		- the biggest burden that this would create is more people
		asking for accounts.
		-  a lot of courses change hands often,
		- at the beginning of the semester there would be chaos
			- e.g. new TAs wouldn't get the password from old TA.
			- jkit: Would we we want to reset passwords every
			semester anyway?
		-  Devin: the one really annoying thing about course account is that
		stuff can get misleading because of old data.
	- shivab: why are departments running out of space and why are *we* taking
	 up the slack??
	- devin: runs web server for professor
		- this server has to do with his professional stuff.
		- also does class accounts.
		- this prof only teaches every other semester.

NOT DONE EDITING!

	other teachers come to talk

departments are vil because they charge a ton and give very little access

bureautcratic red tape up the wazoo

took a month to get permission

they have bugs in publishing server.  not a straight server.

they are migrating everyone to courseweb, which is unacceptable because they already have a full website.

why not have a professor do it and stick it under their own individual account?
b/c that would confuse other profs, students.

This will allow for a persistent place,
shared space on alternative space.

Jkit; this would score us points.

devin: wouldn't immediately get us more funding?

but would get us mad kudos?

and b/c we'd have professors relyuing upon us it would be huge.

Eleen: policy changes?  
jkit: would work the same as student gruops, with minor modifications as needed?

devin: definitely eligible uder curent account policy, aside from letters and numbers.

Don't create accounts for nonpersisten classes?

-----

Heller will be a social lounge.

geo motions to close
phlee seconds


DEVIN says: OCF can get money by helping to run ASUC elections!