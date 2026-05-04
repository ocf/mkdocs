---
date: 2014-06-01
---

# Email discontinuation update: forward-only on June 14th
Back in November of last year, the OCF Board of Directors announced that <a href="http://status.ocf.berkeley.edu/2013/10/email-service-changes.html">email service was being discontinued</a>, with the first phase being transitioning into forward-only email service.<br />
<br />
The start date for the first phase, October 20th, has long passed, although we never actually enforced the change. We're now ready to move into forward-only mode, and will enter this phase on <b>Saturday, June 14th</b>.<br />
<br />
After this date, email will be forwarded to your registered email address. For most members, this is the email you provided when you created your account, but for old accounts, or for accounts with complicated <span style="font-family: Courier New, Courier, monospace;">.forward</span> or <span style="font-family: Courier New, Courier, monospace;">.procmailrc</span> files, this entry may be blank or incorrect.<br />
<br />
You are strongly advised to run <span style="font-family: Courier New, Courier, monospace;">update-email</span> over SSH in order to verify that you have registered an email with LDAP. If you don't have an SSH client handy, the easiest way to access SSH is by visiting <a href="https://ssh.ocf.berkeley.edu/">ssh.ocf.berkeley.edu</a> in your web browser.<br />
<br />
<b>Email will only be forwarded to your email in LDAP.</b> <span style="font-family: Courier New, Courier, monospace;">.forward</span> and <span style="font-family: Courier New, Courier, monospace;">.procmailrc</span> files will no longer be processed. If no email has been set after June 14th, incoming email will bounce.<br />
<br />
If you need assistance updating your email or accessing your OCF account, please <a href="https://wiki.ocf.berkeley.edu/contact/">get in touch</a> so we can help you sort it out.<br />
<br />
Happy summer!<br />
<br />
<b>Edit for clarification:</b> Email addresses set in LDAP via <span style="font-family: Courier New, Courier, monospace;">update-email</span> will only be used for forwarding after June 14th. There's unfortunately no good way to run the old system (<span style="font-family: Courier New, Courier, monospace;">.forward</span>/<span style="font-family: Courier New, Courier, monospace;">.procmailrc</span> files) alongside the new system, so setting an email will have no effect until the switch. Sorry for the confusion!
