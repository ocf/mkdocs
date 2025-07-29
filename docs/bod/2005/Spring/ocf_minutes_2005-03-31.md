OCF Board of Directors' Meeting
Thursday, 31 March 2005

Attendance:
------------------------------
hmogri
frank
grffin
elliot
mattfong
kaisenl
dima
yury
aoshi
bac
jkit

Agenda:
------------------------------
GM
    Printer
    jonguan
    ASUC Elections
    Xavie
SM
    Alumni EECS
    Disk Array
        Allocation

Opening:
------------------------------
Quorum not met!

GM:
------------------------------
Printer
    Printer is broken
    Fullmer did the paperwork
    mattfong: we have to schedule a pickup w/TSW

    jkit: put the duplexer back in the printer so it will be fixed at the same
        time.  Get the iMac fixed too.

    dima: the fuser's broken too

    mattfong: we're not going to have enough money authorized to fix all
        that stuff, we'll need to reauthorize with a higher limit.

        After they do a diagnosis they'll call us with the cost?

    A new printer costs ~$5000

jonguan
    For a job application, said he was OCF staff and did research for OCF
        from 2001 until now...and he has not.  He did apply for sudo, but
        was denied.

    jkit: why should we lie for this guy?
    aoshi: just say he joined staff in 2001 and his list of accomplishments
        is ... (silence)

    No one's seen him in forever.

    dwc said he's approved more accounts than jhs

    if he doesn't hold office hours, he's not technically on OCF staff.

ASUC Elections
    Morning hours: 5am until no later than 9am
    Afternoon hours: between 4-8pm?  Angel never told Frank.
    Evening Hours: until ~11pm

    Be reachable.  We'll probably end up sitting around ASUC.

SM:
------------------------------
Alumni.EECS
    Their mailserver went down, and we're supposedly their MX backup
    Backup mail--we only store it when they go down
    jjlin objects: it's a one way relationship, they don't back us up.    
    postmaster has to read all the spam
    we'll need a new postmaster.  new postmaster should decide?
    CSUA will back us up, dima needs to talk to them.
    alumni already removed us
    they didn't know we were backing them up
    if we get CSUA do we need alumni.eeecs?
    as of now, it's a non-issue unless someone brings it up

Disk array

    Mail spool's on disk array now.
        Dima + Akop did it

    Keep mail separate
        Dima: 100 mb for mail

    Who Decides?
        Aoshi: There's nothing in our official docs about who decides
            quotas. Up to SM discretion?

    Merging
        Merge home and service?
        there were objections to combine mail and home
    Current Situation:
        Currently users get 320mb total
        Right now:
            death is @ 172 gigs, using 60-something percent
            services @ 105 gigs, using 85%

    What are good quota sizes?
        Maildir size:
            Current usage is 7%
            limit on mail to cut down spam?
            Dima suggests 100mb
            yury: crontab to kill spam?
        1 Gigabyte for each user?
            Aoshi: There's no technical argument against 1 gig
            Need?
                Mattfong: There's no practical reason for having a gig
                Dima: Groups need a gig
                Frank: Why does it matter why they need it?
            jkit: a gig with a disclaimer?
            1 gig soft, 1.1gig hard?
        Hozing?
            Raising space will lead to hozing?
            How hard is it to monitor hozing?
                vague mention of bandwidth logs
            Aoshi: if anybody hozes, squish them.
            Trust users vs. distrust users?
            You can lower users' quotas if they violate.
            If your over quota time expires you get sorried.
            bac: you don't have to police it yourself, but if someone
                asks you to take illegal content down you have to take
                it down

    General agreement upon:
        1 gigabyte (done in base 2, so 1024 mb)
        Merge home and services

SMTP Auth Deadline
    May 1st

Eschleman OCF2
    The library person will load paper if we give them a printer

Old Printer
    Old printer has low memory and stalls.

Everything Else
    Tabeled

Meeting Closed
    (Never met quorum)
