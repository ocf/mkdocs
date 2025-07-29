---
title: Getting Involved
---

## How can I get involved in the OCF?

Glad you asked! Students from all backgrounds are welcome to join staff. We
don’t interview or have a selection process for joining—you simply have to
learn, participate, and contribute. We don't impose a specific
time commitment; some volunteers work many hours per week, while others only contribute
occasionally.

However, the most effective way to get started is to come to the lab during weekly meetings and after-hours to talk to staff members. We can help you figure out your interests at the OCF and provide more direction.

If you have no prior experience with coding, Linux, working with servers, etc. but would like to learn how to contribute to the OCF technically, we have several resources to help you get acquainted.

### Join the OCF Chat

Staff often communicate on our bridged [OCF Chat](../../user-docs/contact/chat.md) via their preferred chat platform. Some important channels:

- `#announcements`: events and important information
- `#rebuild` - technical discussion
- `#administrivia` - general discussion
- `#ocf` - off-topic discussion

These channels are typically very active, and you shouldn’t feel the need to
read every line to stay updated. You also aren’t required to understand all the
technical jargon that’s used in `#rebuild`. Feel free to introduce yourself in
any of these channels if you’re new, and don’t be afraid to ask questions!

### In-person meetings

We hold two meetings each week during the fall and spring semesters. If you're
new to the OCF, we recommend you attend our [General
Meetings](staff-meetings.md). If you're curious about the larger technical and
administrative decisions we make, you can also listen in on our [Board of
Directors](../bod) meetings.

### Linux SysAdmin DeCal

If you'd like to learn about many of the tools we use around the OCF in a more traditional course setting, we regularly offer the [Linux SysAdmin DeCal][decal]. All lectures and lab assignments are [open source][decal-web] and available for free on the website, and you are more than welcome to use them even if you aren't officially enrolled in the course.

### Hang out in the lab

OCF staff members usually like to socialize in the lab. We’re a friendly bunch,
so feel free to talk to us! You can also come into the lab after-hours—just
say you’re interested in joining staff and we’ll let you in.

### Starter Tasks

The [Starter Tasks](startertasks.md) page in our documentation contains a variety of intermediate-difficulty exercises that are another great way to get some practice working with OCF infrastructure.

### Contribute

We know that contributing to the OCF can feel daunting, but we
don’t want you to be discouraged. Don’t worry about finding the best way to
contribute, just start by doing something that gets you excited.

#### GitHub

All of our code is on GitHub ([github.com/ocf][ocf-github]). Our Github issues are a bit out-of-date, and you're currently better off checking the README of any given repository or diving straight into its code.

If you’re feeling particularly adventurous, you could also [search for the string
“TODO” across our entire codebase][sourcegraph-todo].

#### Help Tickets

During the semester, our [help@ocf.berkeley.edu mailing list](../../user-docs/contact)
gets around 14 emails per week from the UC Berkeley community. Volunteers like
you respond to these emails. Most requests are about requesting virtual hosting
and helping users debug or fix their websites. If you’re interested in seeing
how this process works, ask a staffer to add you to the RT mailing list. Since
this is high-volume, we recommend filtering these to a different folder so you
don’t get notified all the time.

Joining this list doesn’t obligate you to respond to help requests. It’s
perfectly acceptable to only read tickets as a way to learn more about what we
do.

If you’re on staff, you can view the ticket archive at [rt.ocf.berkeley.edu][rt].

#### Your idea here

As a volunteer organization, the OCF’s direction is driven by the interests of
our members. If you have a new idea for the OCF, we want to help you build it.
You can use our chat channels or talk to a veteran staffer in person to get a
starting point and roadmap.

### Staff Hours

During the week, veteran staffers host “staff hours”
([ocf.io/staffhours][staffhours]), where we provide support to users of our
services. Newbies are encouraged to attend staff hours too. For a newbie,
attending staff hours can serve multiple purposes:

   * Learn by shadowing veteran staffers as they help people out
   * Talk about your interests so we can help you find stuff to work on
   * Get one-on-one mentoring so you can learn about the vast, complex world of
     OCF infrastructure
   * Get context and more information on a particular area you’re interested
     in contributing in

## FAQ

**I wasn’t able to make the first/second/nth meeting of the semester, can I
still join?**

Yes! You can join at any meeting at any time. If you’re worried about what you’ve missed, you can ask a veteran staffer to bring you up to speed or review the [BoD minutes](../bod) for that week.

**What if I can’t physically be present at weekly meetings?**

You can still be part of OCF staff! Classes, work, and other conflicting commitments have come up for most staff members in the past. Even if you can't make meetings, the
suggestions on this page are useful for getting started. You can always stay active in the OCF chat and hang out in the lab outside of official meetings.


[account-chpass]: https://github.com/ocf/ocfweb/blob/master/ocfweb/account/chpass.py
[account-register]: https://github.com/ocf/ocfweb/blob/master/ocfweb/account/register.py
[account]: https://github.com/ocf/ocfweb/tree/master/ocfweb/account
[announce]: https://ocf.io/announce
[api-hours]: https://github.com/ocf/ocfweb/blob/master/ocfweb/api/hours.py
[decal]: https://decal.ocf.berkeley.edu/
[decal-web]: https://github.com/ocf/decal-web
[docs-src]: https://github.com/ocf/ocfweb/tree/master/ocfweb/docs/docs
[getinvolved-src]: https://github.com/ocf/ocfweb/blob/master/ocfweb/docs/docs/staff/getinvolved.md
[ircbot/issues]: https://github.com/ocf/ircbot/issues
[ircbot]: https://github.com/ocf/ircbot
[mirror-healthcheck-puppet]: ️https://github.com/ocf/puppet/blob/master/modules/ocf_mirrors/manifests/monitoring.pp
[mirror-healthcheck]: https://github.com/ocf/puppet/blob/master/modules/ocf_mirrors/files/healthcheck
[ocf-github]: https://github.com/ocf
[ocf-github-issues]: https://github.com/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+archived%3Afalse+user%3Aocf+
[ocf-github-issues-starter]: https://github.com/issues?q=is%3Aopen+is%3Aissue+archived%3Afalse+user%3Aocf+label%3A%22good+first+issue%22
[ocflib-account]: https://github.com/ocf/ocflib/tree/master/ocflib/account
[ocflib-mail]: https://github.com/ocf/ocflib/blob/master/ocflib/misc/mail.py
[ocflib-mysql]: https://github.com/ocf/ocflib/blob/master/ocflib/infra/mysql.py
[ocflib-printing]: https://github.com/ocf/ocflib/tree/master/ocflib/printing
[ocflib/issues]: https://github.com/ocf/ocflib/issues
[ocflib]: https://github.com/ocf/ocflib
[ocfweb-vhost]: https://github.com/ocf/ocfweb/blob/master/ocfweb/account/vhost.py
[ocfweb-stats]: https://github.com/ocf/ocfweb/tree/master/ocfweb/stats
[ocfweb/issues]: https://github.com/ocf/ocfweb/issues
[ocfweb]: https://github.com/ocf/ocfweb
[projects]: https://ocf.io/projects
[prometheus-mirror]: https://github.com/ocf/puppet/blob/master/modules/ocf_prometheus/files/rules.d/mirror.rules.yaml
[prometheus-printer]: https://github.com/ocf/puppet/blob/master/modules/ocf_prometheus/files/rules.d/printer.rules.yaml
[puppet-321]: https://github.com/ocf/puppet/pull/321
[puppet-373]: https://github.com/ocf/puppet/pull/373
[puppet-aliases]: https://github.com/ocf/puppet/blob/master/modules/ocf_mail/files/site_ocf/aliases
[puppet-desktop-packages]: https://github.com/ocf/puppet/blob/master/modules/ocf_desktop/manifests/packages.pp
[puppet-dhcp]: https://github.com/ocf/puppet/blob/master/modules/ocf_dhcp/manifests/init.pp
[puppet-firewall]: https://github.com/ocf/puppet/tree/master/modules/ocf/manifests/firewall
[puppet-www]: https://github.com/ocf/puppet/blob/master/modules/ocf_www/manifests/site/www.pp
[puppet/issues]: https://github.com/ocf/puppet/issues
[puppet]: https://github.com/ocf/puppet
[rt]: https://rt.ocf.berkeley.edu/
[slack]: https://ocf.io/slack
[slackbridge/issues]: https://github.com/ocf/slackbridge/issues
[slackbridge]: https://github.com/ocf/slackbridge
[sourcegraph-todo]: https://sourcegraph.ocf.berkeley.edu/search?q=TODO+case:yes
[staffhours]: https://ocf.io/staffhours
[utils-acct]: https://github.com/ocf/utils/tree/master/acct
[utils-lab-wakeup]: https://github.com/ocf/utils/blob/master/staff/lab/lab-wakeup
[utils-makehttp]: https://github.com/ocf/utils/blob/master/makeservices/makehttp
[utils-makemysql-real]: https://github.com/ocf/utils/blob/master/makeservices/makemysql-real
[utils-makevm]: https://github.com/ocf/utils/blob/master/staff/sys/makevm
[utils-paper]: https://github.com/ocf/utils/blob/master/printing/paper
