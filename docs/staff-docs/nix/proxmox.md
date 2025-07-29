---
title: Proxmox Cluster
---

TODO: integrate with LDAP, access control

## installation
proxmox on usb, graphical installer in server room
on host doorplug

- select smaller driver for OS
- set ip statically
- timezone America/Los Angeles

- put login info in OCF onepass

- go to ip of host in web browser on OCF network

- put nix ISO image on datacenter -> doorplug -> local

### set up ZFS
do this on the larger disk(s) on host (whichever the VMs will reside on)
- raid level: mirror

## SSL setup for proxmox instance

- after installation, go to datacenter, click ACME submenu, add ACME account
- user: root, email: root@obe, letsencrypt

add challenge plugin
- plugin ID: default
- DNS API: nsupdate (RFC 2136)
NSUPDATE_KEY=/etc/acme/nsupdate.key

put file at /etc/acme/nsupdate.key with this content:
```
key "letsencrypt.ocf.io" {
	algorithm hmac-sha512;
	secret "TODO lol";
};
```

secret is in nix repo, must have masterkey(yubikey) added
TODO: doc for how to access nix repo secrets

NSUPDATE_SERVER=169.229.226.22
NSUPDATE_ZONE=letsencrypt.ocf.io

set config of /etc/pve/nodes/doorplug/config with these commands:

`pvenode config set -acmedomain0 doorplug.ocf.berkeley.edu,plugin=default,alias=doorplug.letsencrypt.ocf.io`

`pvenode config set -acmedomain1 doorplug.ocf.io,plugin=default,alias=doorplug.letsencrypt.ocf.io`

go get that cert!

`pvenode acme cert order`

https://pve.proxmox.com/wiki/Certificate_Management#sysadmin_certs_acme_dns_challenge

## repos
disable enterprise repos for ceph and proxmox, move to no-subscription repo

## the end

go to doorplug.ocf.berkeley.edu:8006

## IPMI
- more hardware-level control than regular ssh can provide
- emulating physical access to server but over network

IP source of truth google sheet

assigning new host an ip
- check google sheet for unused IPs
- take previous host using that IP down, if it still exists
- assign IP on installation to new host

- ping/dig ip from OCF network
- dig -x to see if DNS entry exists
