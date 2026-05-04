---
date: 2014-04-10
---

# CVE-2014-0160 ("Heartbleed") openssl vulnerability update
On Monday, an extremely serious bug in openssl was announced. The bug affected all recent versions of openssl, including the version in use on all OCF servers.<div>
<br /></div>
<div>
Every OCF server was patched against the bug within an hour of Debian releasing a fix. However, because the bug was present in openssl for multiple years, there is no guarantee that private keys or other sensitive information (like user passwords) were not leaked.</div>
<div>
<br /></div>
<div>
As a precaution, we have revoked all SSL certificates in use by OCF (~9 of them), discarded old private keys, and installed new certs and keys in their place.</div>
<div>
<br /></div>
<div>
Some estimates suggest that over 66% of all HTTPS websites were vulnerable to this bug, and it is known that many high-profile sites were. We encourage you to update your OCF password, as well as your passwords on every website you use.</div>

