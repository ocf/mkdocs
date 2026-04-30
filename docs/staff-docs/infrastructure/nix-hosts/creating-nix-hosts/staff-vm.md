---
title: Staff VMs
---

just like look at other staff VMs on `doorplug` (the proxmox node), look at the general guide for creating nix hosts, vibe it out

## Troubleshooting

When trying to provision a NixOS VM through ISO (after step 3.), we ran into an issue where no bootable option or device was found. The way to solve this was to attach the ISO first:

sudo virsh attach-disk [domain name] /var/lib/libvirt/images/latest-nixos-minimal-x86_64-linux.iso sda --driver qemu --type cdrom

Then disable secure boot in BIOs and add "console=ttys0" to the bootloader screen by pressing "e" and appending the parameter.
