---
date: 2016-02-06
---

# Upgrading user-facing servers to jessie
In the past year we've upgraded our entire infrastructure to Debian jessie, with the exception of user-facing machines.<br />
<br />
The time to upgrade them is now. We've prepared upgraded versions of each of these servers and will swap them out early morning on <b>Wednesday, Feb. 10th</b>.<br />
<br />
The servers that will be upgraded are:<br />
<br />
<ul>
<li><b>tsunami</b>, the public login server</li>
<li><b>biohazard</b>, the app-hosting server</li>
<li><b>death</b>, the web server</li>
</ul>
<br />
Most users won't notice the update, except that most software will be a newer versions. The one exception is users who have dynamically-linked binaries somewhere in their home directories.<br />
<br />
Because many libraries will be upgrading, most of these programs will fail to run after the upgrade. The best solution is to recompile the binaries (or find newer, pre-compiled versions).<br />
<br />
One specific case is with environment managers like Python's virtualenv, Ruby's rbenv or rvm, and Node's nodeenv or nvm. These often put fully-compiled versions of the interpreter in your home directory, and in most cases, this will fail to work. After the upgrade, you'll need to rebuild these.<br />
<br />
For application hosting, you can find instructions on our website:<br />
https://www.ocf.berkeley.edu/docs/services/webapps/<br />
<br />
During the server swap, you should expect a small amount of downtime (about 5 minutes).<br />
<br />
If you have any questions or need assistance feel free to reach out to help@ocf.berkeley.edu.<br />
<br />
<b>Update Feb 07: </b>We're going to push this back until early morning Wednesday (originally it was Monday) to give us a little more time to ensure a smooth upgrade.<br />
<br />
<b>Update Feb 09:</b> For biohazard (app hosting), we'll be reaching out to individual groups using the server to coordinate a smooth upgrade. biohazard will continue to be available (and unupgraded); we'll be moving groups one-by-one to the new server (named werewolves).
