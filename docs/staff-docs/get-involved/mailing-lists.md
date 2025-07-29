---
title: Staff Mailing Lists
---

There are several mailing lists used internally by staff. Append
`@ocf.berkeley.edu` to the end of each mailing list.

All staffers are automatically added to the following two mailing lists:

 * `staff`: For staff announcements, such as meeting times and events.
 * `wheel`: For technical discussion among all staff

Staffers can also choose to be further added to the following mailing lists.
Technical Managers are required to join them:

 * `rt`: Emails sent to Request Tracker are copied to this mailing list. If
   you are on the `rt` mailing list, you can reply to RT tickets from your
   email. You are highly encouraged to join this mailing list even if you're
   not root staff.
 * `root`: Miscellaneous messages from system daemons are sent here:
    * Cron daemons send mail containing any stdout/stderr output from cronjobs
    * [Jenkins][jenkins] sends emails whenever a Jenkins build fails
    * ocflib sends emails whenever an uncaught exception is thrown in ocfweb,
      create, enforcer, and several other background tasks
    * Miscellaneous other emails are sent here
  * `alumni`: On graduation, if you would like to receive information such as alumni event invites, you can add your preferred non-ocf email here.

   The mailing lists below can get many emails per day.

 * `puppet`: Error messages from puppet runs go here. This list tends to be
   very noisy.
 * `mon`: Monitoring alerts are sent here:
    * [Rackspace Cloud Monitoring][rackspace] emails us alerts when our
      important services are inaccessible from outside the OCF network.
    * [Prometheus][prometheus] sends mail whenever some measurement (e.g. disk
      usage, RAM usage, etc.) is outside the normal range.
 * `extcomm`: A compilation of technical mailing lists for upstream projects
   and projects we mirror.

On the administrative side, the `officers` mailing list receives emails related
to OCF administrivia. Cabinet members are expected to be on this mailing list,
and any other staffer can audit it as well.

Operations Staff are added to the `opstaff` mailing list.

<!-- TODO: uncomment when this list becomes official -->
<!-- Alumni are able to join the `alums` mailing list. Announcements -->
<!-- about alumni events and the like are sent here. -->

There are also some special purpose mailing lists:

 * `ocf@lists.berkeley.edu` ([ocf.io/announce][announce]): we add emails from
   Calapalooza tabling to this mailing list, and send out announcements about
   staff meetings here. We use a Berkeley mailing list here to let non-OCF
   members sign up for it.

   This mailing list should be cleared every fall.

[announce]: https://ocf.io/announce
[jenkins]: https://jenkins.ocf.berkeley.edu/
[rackspace]: https://intelligence.rackspace.com/login
[prometheus]: https://prometheus.ocf.berkeley.edu/
