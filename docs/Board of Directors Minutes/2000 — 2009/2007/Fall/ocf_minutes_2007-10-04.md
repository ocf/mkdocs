10/5/07
OCF informal meeting

* indicates person is currently on BoD

akit*
wjm*
sahnn*
dmchan*
geo*
cardi*
sluo*
thanos
stevklaw

Quorum is not met; a BoD meeting cannot be called to order.
This will just be an informal meeting for discussion.

GM AGENDA

Microsoft Licenses
- We got approved for discounted Microsoft licenses
- $20 each for professional license
- will buy 15 Office 03's

Maintenance Day is this Saturday, 1 pm
- please come!

Transformers movie at Wheeler, 10/19


SM AGENDA

Billy is resigning from the SM position
- wjm: I've been really busy and don't have time to do anything these days
	- other people are already doing all the work for me
	- I can't in good conscience keep the SM position

Discussion: Why is the SM position undesirable?
- sluo: for everyone who has done it, we've all felt it's been too large a job
	- we need to split it up, delegate the work or something
- catbert: can I be evil head of HR?
- akit: can we set up teams and then just have heads of committees?
- sluo: if we delegate and nothing gets done, either SM has to do it all anyway, or nothing gets done
- cardi: can we get freshmen?
- sluo: it's hard to get freshmen who know enough, though
- wjm: i do know linux pretty well, but it's still so complicated that it's pretty overwhelming
- wjm: if we kept it all uniform, e.g. all debian, it'd be a lot easier
- sluo: we don't gain enough from doing that though, and it would look bad on our part since we have stuff from Sun
- steven law: sooner or later something will have to go, though
- cardi: eventually there will be no one to pass on sun skills
	- one way or another, if we don't do something now to promote solaris and pass on those skills it'll just get lost
	- even in the Beg Sysadmin deal, their Sun experieicne is limited to what they see on the cs lab machines and doesn't even get into the actual OCF lab setup

Insert here a lot of technical detail I know nothing about.

- cardi: i feel like our systems are so intertwined that it's hard to delegate specific things
	- in order to do anything you have to go through so many systems
	- if we want to start delegation, we have to start isolating services
	- don't rely on people already knowing how ocf works
	- seems like everything we have so far we've been barely holding togethe
- sluo: it boils down to two things: user accounts and storage
	- we need a central place for user accounts and a central storage
- wjm: right now if something breaks we have nowhere to go but dwc
- sluo: insert graphic illustration about how doing away with dwc, sluo, sle and yury would be the end of the ocf
	- involving assassinations and a padded room
- cardi: isolated solutions would help
	- things we can move off of solaris, let's move off
	- if we can isolate services perfectly, like web servies and mail
		- you could run on two different machines with different operating systems
		- if you could manage that it would be easier to recruit more people who know one or the other
- sluo: you can't really separate the services any more than they are now
	- e.g. I haven't touched web in a long time now, usually it's sle that fixes it
	- if we wanted to turn mail over to someone, the biggest obstacle would be getting someone who knows sendmail
	- the problem here is not that it's intertwined but that sendmail just sucks
	- so, I don't see that delegating by services would necessarily be an improvement
- cardi: so what can we do to better administrate the ocf?
	- the problem with storage is NIS+
	- looks like our next step is to go to LDAP and Kerberos
- sluo: i dunno if LDAP reduces the level of complexity
	- only real uposide is that no one will withdraw support any time soon
	- I don't know that anyone has a good solution
- cardi: if we could modernize though, maybe it will open up solutions
	- is there a way to have LDAP and NIS+ coexist?
	- could it be a slow migration?
- sluo: not really, but we could run them side by side while the migration finishes
	- we don't gain anything by not migrating everyone at once
	- we do gain ability to keep using the existing tools that depend on NIS+
- cardi: only other thing i could think of is attempt to create a map of OCF
	- services to servers, etc
	- see what we can cut off / have running standalone
- cardi: maybe we can stop certain services for a while
	- so we can focus on one problem at a time
	- e.g. take down user accounts temporarily
- sluo: but every service people want basically depends on the user accounts
	- except hosting our own website, which isn't very helpful to users
- sluo: NFS 2 and 3 have interesting implementation issues
	- insert technical jargon here
- cardi: if someone were to restart the ocf from scratch, we'd still end up with NFS problems?
- sluo: right,we'd probably still use nfs and have the same inherent problems
	- still have problems of user acounts and storage
	- and we'd probably have an all linux lab
- cardi: how do the big coporations do it?
	- in terms of how they organize their infrastructure?
- sluo: most large installations have an LDAP server doing the accoutns
	- and some large storage
	- either that, or they don't have central storage at all, just stuff lying all around, which is not good
	- and they have Active Directory, or Redhat directory, or fill-in-the-blank directory

- akit: So how would we make the SM position bearable?
- wjm: we'd have to break it down, the position shouldn't exist at all
- sluo: we all agree we need to break it down, but there's no real way of doing that
- sluo: what happens when you have more than like 2 people, people just keep saying someone else will take care of it
	- in the end, nothing will happen
- sluo: It's more than just how to break down the post:
	- we need to think about how to motivate people to want to learn and do this stuff
- sluo: even in the advanced decal, we taught a lot of stuff but...
	- you've learned the principles, but now you need to learn about how the OCF is put together
	- and all the intricacies that come with any specific system
	- there's no template for creating a large site
	- unless we were to start from scratch
	- # of quirks OCF has is probably partially due to ancient stuff and lack of maintenance
	- but any system will have its own quirks and you just need to have a local guru to know everything
- cardi: is there any way we could interface with other departments?
	- see how they're doing things
	- e.g. the EECS instructional labs
	- from what it sounds like they are the ones who have a huge number of users and a large variety of systems
	- they have more money and more people, but their setup is similar
	- printers, acounts that log into solaris, windows and linux machines
	- any way we could see how they run things?
- sluo: I think we have a pretty good picture of what their setup looks like
	- I don't know what their directory is but I heard they use NIS
	- they defintely use NFS
	- it's basically a standard large lab setup
	- they have money and people
	- operationally their setup is probably cleaner than ours
	- how would we switch our setup though?
- cardi: doesn't seem like there's any feasible short term solution
	- but what if we just start trying to create a map of the ocf?
	- if we could do that, it would help people figure out how to reorganize
	- no major changes for now that aren't necessary
	- we could delegate this, start mapping it out
	- figure out the machines and services
	- draw lines between critical machines e.g. sandstorm and war
 
More technical jargon here.

- wjm: i'll hit up the milennium people and ask if we could get any hardware
- sluo: it'd probably be x86
- wjm: yeah.

- cardi: i think mapping would be the only way anyone could have an idea of what to do.
	- we have a core problem but don't know where to start fixing it
- wjm: we don't even have a core problem, but just symptoms of problems
	- a real map would be helpful, not just knowledge "in our heads"
- cardi: an actual documentation would be helpful
	- even if it's just on paper, not on the wiki

- akit: anyone want to be SM?
- akit: sluo, do you want to be it for this week?
- sluo: fine... i'll be caretaker SM
- akit: okay, let's try to make the SM job more reasonable

- sahnn: what if we stop taking new accounts temporarily?
- sluo: that won't help our core problem
	- people would still be askin for a lot of help in the lab
- wjm: it'd be helpful if anyone had access to the lab after hours instead of the few people with keys
- sluo: there are a couple of people (like aaron) who like to stay in lab after horus a lot
	- but these people are really rare
	- it's kind of a nightmare to have to do it

How's the Eshelman move going?
- sluo: we could move our servers without moving the lab
	- we're still waiting on it
	- nobody knows what's going on-- we don't know, they dont' know
	- there's no power, no ventilation, no progress
	- and also Publications doesn't want to move
- wjm: what's the holdup?
	- cutting the cables would invovle taking down the whole network
	- we'd lose our services for a week
	- it would take an entire vacation period for people to stay and get the work done
	- power isn't that big a problem, but...
	- ventilation: where can you stick a ventilation shaft?
	- you'd have to change the infrastructure of the building
	- you might as well wait until the building is torn down
- cardi: right now it seems like we can't do anything in the way of moving
	- there was no indication of a timeline, except that when they kick us out, they'd give us an extra semester
	- maybe we should have gotten a timeframe established for preparation with the MOU
	- the MOU guarantees only the space and the extra semester
	- we don't have control over this situation, we're just waiting
- sluo: (unless we have like 500,000 bucks to do it ourself)
- cardi: it's unlikely we'll be as successful as devin was

Mapping
- wjm: if i had a list of all the machines and could ask what each mahine was running and what they do it'd be okay
- sluo and cardi: the hard part would be reading it all and putting it together

- wjm: this BoD did not happen.
- sluo: nothing was produced and nothing was decided
- dmchan: pics or it didn't happen

Excerpt from IRC	
20:05 <+sle> we could move to more standard ways of doing things, rather than 
             hacking together stuff
20:05 <+sle> because what happens is that the person who made the hack in the 
             first place graduates or drops off active staff
20:06 <+sle> and the new staffers have to pick up the pieces and figure out how 
             they fit