---
title: Staff VMs
---

just like look at other staff VMs on `doorplug` (the proxmox node), look at the general guide for creating nix hosts, vibe it out

## Troubleshooting

### No bootable option or device

When trying to provision a NixOS VM through ISO (after step 3.), we ran into an issue where no bootable option or device was found. The way to solve this was to attach the ISO first:

sudo virsh attach-disk [domain name] /var/lib/libvirt/images/latest-nixos-minimal-x86_64-linux.iso sda --driver qemu --type cdrom

Then disable secure boot in BIOs and add "console=ttys0" to the bootloader screen by pressing "e" and appending the parameter.

### Help! I locked myself out of my VM!

> Root permissions required for this section.

1. [Set up a SOCKS proxy to access the proxmox cluster remotely.](https://bestdocs.ocf.io/staff-docs/infrastructure/nix-hosts/proxmox/#proxmox)
2. Go to https://reef.ocf.berkeley.edu:8006
3. Find your VM on `yuu` or `reef` by hostname.
4. Do what you need to do depending on how you locked yourself out (open console to change things, reboot, etc).
