---
date: 2019-01-04
---

# Introducing OCF PGP Keyserver Service
The OCF is happy to announce the public release of our PGP keyserver service, available at <a href="https://pgp.ocf.berkeley.edu/">pgp.ocf.berkeley.edu</a>. We are proud to be a part of the community supporting reliable public key infrastructure!<br />
<br />
At present, we are providing HKP and sks-recon on IPv4 and IPv6, as well as HTTP and HTTPS access. We are building out support for HKPS and keyserver pool membership. The following domains are supported, at the accompanying ports.<br />
<ul>
<li>ppg.ocf.berkeley.edu (80, 443, 11370, 11371)</li>
<li>keyserver.ocf.berkeley.edu (80, 443, 11370, 11371)</li>
<li>pgp.ocf.io (443: HSTS)</li>
<li>keyserver.ocf.io (443: HSTS)</li>
</ul>
We will soon be providing service at pgp.berkeley.edu and keyserver.berkeley.edu as well.<br />
<br />
If you would like to peer your SKS server instance with ours, please feel free to submit a pull request against our <a href="https://github.com/ocf/puppet/blob/master/modules/ocf_keyserver/files/membership">membership file</a>!
