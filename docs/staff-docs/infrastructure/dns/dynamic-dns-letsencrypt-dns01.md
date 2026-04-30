# Dynamic DNS / LetsEncrypt DNS01

Most of OCF's certificate issuance (basically, everything that isn't user vhosts) happens through DNS01 challenges going through the nameserver on `pestilence` and its dynamic update mechanism. If certs for OCF domains aren't getting renewed, check here!

## Detailed Background

The OCF runs BIND9 `named` as an authoritative nameserver for `ocf.io`, and as shadow-authoritative for `ocf.berkeley.edu`. To handle DNS01 challenges for Let's Encrypt certificate issuance, the challenge subdomains are all `CNAME`[d to the ](https://github.com/ocf/dns/blob/b87d263d9e9eafa2f16da2e5b471fd6de0bb867b/build-zones#L32-L33)`letsencrypt.ocf.io`[ zone](https://github.com/ocf/dns/blob/b87d263d9e9eafa2f16da2e5b471fd6de0bb867b/build-zones#L32-L33). This zone is managed through named's support for [Dynamic Update](https://github.com/ocf/dns/blob/b87d263d9e9eafa2f16da2e5b471fd6de0bb867b/build-zones#L32-L33) with a fixed TSIG key managed in puppet ([named ](https://github.com/ocf/puppet/blob/d35b1647cd2d0b19c38d97e1150487b05759cdf0/modules/ocf_ns/templates/named.conf.options.erb#L63-L66)`letsencrypt.ocf.io`). On each host requesting certificates, puppet [populates the TSIG key](https://github.com/ocf/puppet/blob/d35b1647cd2d0b19c38d97e1150487b05759cdf0/modules/ocf/manifests/ssl/setup.pp#L40-L44) and [runs ](https://github.com/ocf/puppet/blob/d35b1647cd2d0b19c38d97e1150487b05759cdf0/modules/ocf/manifests/ssl/lets_encrypt/dns.pp#L27-L32)`dehydrated` to refresh certificates. `dehydrated` checks the certs it manages, and, for each cert that doesn't exist or is close to expiration, performs a request to `named` on `pestilence` to set the `TXT` record (on the `letsencrypt.ocf.io` zone), and completes the ACME request.

## `named` Journal Corruption

Occasionally `named`'s journal for the `letsencrypt.ocf.io` zone falls out of sync, and it fails to load the zone:

```none
zone letsencrypt.ocf.io/IN (unsigned): journal rollforward failed: journal out of sync with zone
zone letsencrypt.ocf.io/IN (unsigned): not loaded due to errors.
```

TODO: investigate why (maybe it doesn't like git touching the files?)

This causes updates to the `letsencrypt.ocf.io` zone to fail (since the zone no longer exists) with the following error from `named`:

```none
client @0x7fdff40170e0 169.229.226.23#34119/key letsencrypt.ocf.io: update failed: www.letsencrypt.ocf.io: not authoritative for update zone (NOTAUTH)
```

When this happens, all journals can be synced and purged by running `rndc sync -clean` as root (on pestilence). After reloading `named` (`systemctl reload named`), BIND9 should pick up the zone again and start responding to update requests as normal.