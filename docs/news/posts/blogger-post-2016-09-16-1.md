---
date: 2016-09-16
---

# Weak user passwords have been reset recently
We're always looking for ways to make sure our users' accounts remain secure. It's important to have strong passwords because OCF accounts aren't just used for lab access or printing, but also for web hosting and <a href="https://www.ocf.berkeley.edu/docs/services/">many other services</a>. These services are accessible via the internet, which means anybody (including those with no relation to UC Berkeley) could try to guess the passwords.<br />
<br />
Recently, we attempted to guess the passwords of our users in an attempt to find users with exceptionally weak passwords and have them upgrade to a stronger password. To do this, we used both lists of passwords from online password dumps (including passwords used by real people on other services), lists of the most common passwords, and other methods such as trying different variations of each character of a password.<br />
<br />
This is the same thing an attacker would do to try to break into a user's account. It's important to keep in mind that we <i>cannot read users' passwords</i>. We store them in a non-reversible manner as password hashes. Passwords are hashed using a one-way function that can be computed at login and compared to the stored hash. At no time are OCF staff able to find out the passwords of our users, except in the way above (by trying hundreds of thousands of passwords until one matches).<br />
<br />
The guessing method only works on the weakest of passwords; it also explains why <a href="https://xkcd.com/936/">the best way to make a password strong is to make it<i> </i>long</a>, rather than trying to make it more complicated by adding numbers or special characters.<br />
<br />
We have removed the passwords from the accounts we were able to guess passwords for. These users should either <a href="https://ocf.io/password">reset their password online</a> (if they have a CalNet account linked to their OCF account, as most current and recent students do), or <a href="https://www.ocf.berkeley.edu/docs/services/account/#manual-reset">use the manual verification process otherwise</a>.
