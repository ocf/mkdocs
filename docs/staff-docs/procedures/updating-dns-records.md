# Updating DNS Records

The repo at <https://github.com/ocf/dns> holds the DNS configurations of the OCF, but the authoritative server is LDAP. Once `ocf/dns` is updated, the next puppet run updates OCF Name Server at ns.ocf.berkeley.edu with the new configuration.


## Updating DNS Records

### 1. Add entry to LDAP

Before adding an entry, make sure that your IP octet isn't currently being used by the OCF Network!! This step can only be performed by an OCF administrator or root user.

Use `ldap-add-host` from `ocf/utils` to add your new host. Ex:

```python
ldap-add-host <hostname> <octet> <type>
```

The main `type` categories are `server`, `desktop`, `staffvm`. Some others are `ipmi`, `printer` and `dhcp`

> `ldap-add-host` essentially just generates the new entry to LDAP based on an existing template, and use `ldapadd` to add the new entry

### 2. Build `ocf/dns`

Pull `ocf/dns` <https://github.com/ocf/dns>, and run `make`. You should also run `make test` to make sure everything is okay. 

> When you run `make`, the updated LDAP entries are pulled to generate new configuration for the name server. For example, look at `ocf/dns/etc/db.ocf`

### 3. Push `ocf/dns`

Now, commit your changes! The next puppet run will pull the changes you made and apply to our name server! (see `ocf/puppet/modules/ocf_ns/manifests/init.pp`)