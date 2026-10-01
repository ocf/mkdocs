---
title: Test configs in a VM
---

```
nix build .\#colmenaHive.nodes.HOSTNAME.config.system.build.vm
./result/bin/run-HOSTNAME-vm -smp CORES -m RAM
# suggested: -smp 6 -m 12G
```
