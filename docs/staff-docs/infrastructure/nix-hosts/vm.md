---
title: Test configs in a VM
---

```
nix build .\#colmenaHive.nodes.HOSTNAME.config.system.build.vm
./result/bin/run-HOSTNAME-vm -vga virtio -display gtk,gl=on -smp CORES -m RAM
# suggested: -smp 6 -m 12G
```
