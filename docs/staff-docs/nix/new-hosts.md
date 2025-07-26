---
title: Creating New Nix Hosts
---

## General

click create virtual machine
choose name from my little pony (check LDAP to see if already exists)
select start at boot

## OS
select nix ISO image

## System
graphic card: SPICE
machine: q35
SCSI Controller: VirtIO SCSI single
enable QEMU agent
BIOS: OVMF (UEFI)
EFI Storage: primary-zfs
de-select Pre-Enroll keys

## Disks
enable SSD emulation
storage: primary-zfs

## Other Hardware
give at least 4GB mem!

bridge: vmbr0
model: VirtIO (paravirtualized)

start the VM

run the bootstrap script
`sudo nix run --extra-experimental-features "nix-command flakes" github:ocf/nix#bootstrap`

device: /dev/sda
hostname: same as VM name
get new ip from google drive (TODO write doc for getting new host ip)
