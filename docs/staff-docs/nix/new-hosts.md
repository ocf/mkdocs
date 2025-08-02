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

- Click create virtual machine
- Make sure you have the Advanced box checked at the bottom to be able to see all the config options, when
provisioning a new VM.
- There is a very helpful "Help" button in the bottom left of the VM creation window that will take you to the
appropriate page in the Proxmox docs that can provide really helpful information / context.
- Things keep chaning and new tools and features are introduced fairly often, so if you think something in these
docs need to be updated talk to a root staffer (the current SMs will be a good place to start).

### General

- Select a Node that has capacity for the about of CPU and RAM resources you wish to allocate.
- Choose VM name from my little pony (check LDAP and run dig to ensure host doesnt already exist!) (TODO link LDAP docs)
- Leave the resource pool empty (TODO: reconsider using this feature as more guests are migrated to proxmox)
- Select start at boot (order, delay and timeout can be left as is)
- Add a Tag for the OS the VM is going to run (nix / debian) and the primary purpose of the VM (webhost, staffvm etc...)

### OS

- If you're going to be using a network PXE boot (TODO: set one up this would be real nice), select "Do not use any media".
Otherwise select the storage where you uploaded / downloaded the ISO and the ISO image you want to boot from.
- Leave the Type and Version as their default values (Linux / xxx Kernel)

### System
<!-- TODO @laksith19: Usually prefer SPICE / QXL but it seems like there's a bug in the Driver in the
current lts kerne (6.12.40) that cause the guest displays to freeze up randomly and prevent reboots without
using a hypervisor level reset (basically a power-cycle) which is not ideal. As we're probably never going to
have graphical VMs, the graphics performance is not important and it's probably best to just stick to default.
Leaving this TODO, in case it's worth re-visiting in the future. -->
- Graphic card: Default
- Machine: q35
- SCSI Controller: VirtIO SCSI single
- Enable QEMU agent
- BIOS: OVMF (UEFI)
- EFI Storage: vmdata
- Disable Pre-Enroll keys
- Disable Add TPM (Unless you really know you need it)

### Disks
Most of these options are the default values enumarated here for completion, **except for the ones in bold**.

- Bus/Device: SCSI 0
- SCSI Controller: VirtIO SCSI single
- Cache: Default (No cache) (This just means that the host page cache is not used and the performace will be similar
to the VM having direct access to the disks. If you know what you're doing and think for the use case of the VM there's
a better a option the [Performance Tweaks](https://pve.proxmox.com/wiki/Performance_Tweaks#Disk_Cache)
section of the Proxmox Wiki is a really helpful guide.)
- **Enable Discard**
- Enable IO Thread
- **Storage: vmdata**
- **Disk size: xxGiB**: This space is thinly provisioned (or sparse) in ZFS and will not be used or reserved for the VM unless
actually used by the VM. This allows us to be able to overprovision VM disks with additional capacity, but make sure you keep an
eye the actual usage of the underlying storage pool (vmdata in this case).
- Format: Raw disk image
- **Enable SSD emulation**
- Disable Read-only
- Enable Backup
- Disable Skip replication
- Async IO: Default (io_uring) (TODO: Probably worth changing this to native when we eventually 
migrate to CEPH - [context](https://forum.proxmox.com/threads/proxmox-ve-7-2-benchmark-aio-native-io_uring-and-iothreads.116755/))

### CPU
Ignore the advanced settings for this section the defaults are sufficient.

- Sockets: 1
- Cores: 2 (a generalized default suggestion that should work for most use cases).
- Type: x86-64-v2-AES (Select the lowest compatible virtual QEMU CPU type in the cluster, this is important for live
migrations to work. Technically setting this to host will give you maximum performance but you'll not be able to
live migrate the VM from one host to another.)

### Memory
- Memory (MiB): Give at least 2048 (2 GiB)
- TODO(@laksith19): The current bootstrap process seems to be a memory hog needing like 32GiB of memory but we can
drop this down after the bootstrap process completes. Will need to figure out a better bootstrap process this is not
ideal.
- Minimum Memory (MiB): Set it to the same as Memory unless you expect the memory requirement of this
VM to be be realtively low with occasional spikes.
- Enable Balooning Device (Even if not using the Minimum Memory feature as it allows the guest to report
actual memory usage vs allocated memory usage more accurately to the host)

### Network

- Bridge: vmbr0
- Model: VirtIO (paravirtualized)
- TODO: we can have different bridges for different VMs, use NAT, VLAN tagging etc... but for now we stick to the same
model we used with the debian hosts, all VMs are just bridged on with the default bridge.

### Confirm
- Check if all the settings are correct.
- Enable start after created on the lower left corner
- Click finish to provision and start the VM!

## 3. NixOS Install

run the install script. disk partitioning, installs NixOS, puts our config from github for `hostname` on there

`sudo nix run --extra-experimental-features "nix-command flakes"
'github:nix-community/disko/latest#disko-install' -- --write-efi-boot-entries
--flake 'github:ocf/nix/BRANCHNAME#HOSTNAME' --disk main /dev/DISKNAME`

- run `lsblk` on host and replace DISKNAME with the primary drive (sda, nvme0n1, etc)
- for the settings reccomended in this page it's always /dev/sda
- hostname is same as VM name

if command does not initially succeed, nix-collect-garbage before trying to run again (something something cache).

## Resizing hosts

run the install script again lol

TODO (@laksith19): play around with disko for resizing

