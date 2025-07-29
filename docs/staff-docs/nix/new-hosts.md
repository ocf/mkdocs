---
title: Creating New Nix Hosts
---

## Overview

1. create a new branch on ocf/nix
2. set up the nix configs for that specific host
3. finally, deploy the VM (be sure to run install script command on that branch)!
4. grab final SSH public key of VM (secrets.md), add to the branch as `secrets/host-keys/hostname.pub`
5. run `agenix rekey`, push changes, `colmena apply --on HOSTNAME` from trusted user (SSH key is in profile/base.nix) (for now)
6. add, commit, make PR
7. eventually merge into main after seeing that spike successfully builds on Github Actions

## 1. Writing the New Host Config

under `nix/hosts`

copy config for most similar existing host, then make changes.

when writing, go to nix options search, thoroughly look over all options available and see which are relevant to your host

### Testing

`nix develop -c colmena build --on HOSTNAME` will check if the config builds correctly. if you don't specify host, Nix will see if the config can build correctly on all hosts.

`nix fmt .` from root dir for formatting

`nix build .#colmenaHive.nodes.HOSTNAME.config.system.build.vmWithDisko` will try to build out entire config, and give a script to test locally on a VM



## 2. New VM on Proxmox
### General

- click create virtual machine
- choose VM name from my little pony (check LDAP and run dig to ensure host doesnt already exist!) (TODO link LDAP docs)
- select start at boot

### OS

- select nix ISO image

### System

- graphic card: SPICE
- machine: q35
- SCSI Controller: VirtIO SCSI single
- enable QEMU agent
- BIOS: OVMF (UEFI)
- EFI Storage: primary-zfs
- de-select Pre-Enroll keys

### Disks
- enable SSD emulation
- storage: primary-zfs

### Other Hardware
- give at least 32GB mem!
- TODO (@laksith19): figure out prebaking custom nixos install iso with all configs prebuilt

- note: bootstrap process may require much more memory than actual service. set to 32GB, then change later

- bridge: vmbr0
- model: VirtIO (paravirtualized)

- device: /dev/sda
- hostname is same as VM name
- get new ip from google drive (TODO write doc for getting new host ip)

- start the VM!

## 3. NixOS Install

run the install script. disk partitioning, installs NixOS, puts our config from github for `hostname` on there

`sudo nix run --extra-experimental-features "nix-command flakes"
'github:nix-community/disko/latest#disko-install' -- --write-efi-boot-entries
--flake 'github:ocf/nix/BRANCHNAME#HOSTNAME' --disk main /dev/DISKNAME`

run `lsblk` on host and replace DISKNAME with the primary drive (sda, nvme0n1, etc)

if command does not initially succeed, nix-collect-garbage before trying to run again (something something cache).

## Resizing hosts

run the install script again lol

TODO (@laksith19): play around with disko for resizing

