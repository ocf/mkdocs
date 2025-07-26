---
title: Proxmox Cluster
---

## IPMI
- more hardware-level control than regular ssh can provide
- emulating physical access to server but over network

on host doorplug
IP source of truth google sheet

assigning new host an ip
- check google sheet for unused IPs
- take previous host using that IP down, if it still exists
- assign IP on installation to new host

- ping/dig ip from OCF network
- dig -x to see if DNS entry exists
