---
date: 2018-11-07
---

# Upgrading user-facing servers to Debian stretch
In the past year and a half we've upgraded our entire infrastructure to Debian stretch, with the notable exception of any user-facing machines.<br />
<br />
<b>Edit (2018-11-25)</b>: We've now upgraded all of the servers listed below! Please contact <a href="mailto:help@ocf.berkeley.edu">help@ocf.berkeley.edu</a> if you have any questions about the upgrade or notice anything broken.<br />
<br />
The time to upgrade them is now! We've prepared upgraded versions of each of these servers and will swap them out on <strike style="font-weight: bold;">Sunday, November 18th, 2018</strike> the evening of <b>Sunday, November 25th, 2018</b>. This has been postponed from the 18th since some apphosting groups did not have their applications ready on the new server to make the migration possible.<br />
<br />
The servers that will be upgraded are:<br />
<ul>
<li><b>tsunami</b>, the public login server</li>
<li><b>werewolves</b>, the apphosting server (we've reached out to groups using this server and will be replacing with a new server named <b>vampires</b>)</li>
<li><b>death</b>, the web server</li>
</ul>
Most users won't notice the update, except that most software will have newer versions. The one main exception is users who have dynamically-linked binaries somewhere in their home directories.<br />
<br />
Because many libraries will be upgrading, most of these kinds of programs will fail to run after the upgrade. The best solution is to recompile the binaries (or find newer, pre-compiled versions).<br />
<br />
One specific case is with environment managers like Python's virtualenv, Ruby's rbenv/rvm, and Node's nodeenv/nvm. These often put fully-compiled versions of the interpreter in your home directory, and in most cases, these will fail to work once the server is upgraded. After the upgrade, you'll need to rebuild these to get them to work again. Here are some major versions of programs that will be upgrading:<br />
<br />
- Ruby 2.1.5 -> Ruby 2.3.3<br />
- Python 3.4.2 -> Python 3.5.3<br />
- Python 2.7.9 -> Python 2.7.13<br />
- NodeJS 0.10.29 -> NodeJS 4.8.2<br />
- PHP 5.6.36 -> PHP 7.0.30<br />
- Perl 5.20.2 -> Perl 5.24.1<br />
<br />
For upgrading any apps using our application hosting, you can find more detailed instructions on our website: <a href="https://www.ocf.berkeley.edu/docs/services/webapps/">https://www.ocf.berkeley.edu/docs/services/webapps/</a><br />
<br />
During the server swap, you should expect a small amount of downtime (about 5-10 minutes) as the new servers are swapped into place of the old servers.<br />
<br />
If you have any questions or need assistance feel free to reach out to <a href="mailto:help@ocf.berkeley.edu">help@ocf.berkeley.edu</a>.<br />
<br />
Thanks for flying OCF!
