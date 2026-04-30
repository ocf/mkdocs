---
title: Puppet
---

The puppetmaster is [lightning][servers]. Instructions on
making, testing, and deploying changes to Puppet are located at the [Git
repository](https://github.com/ocf/puppet) on GitHub.

We only use puppet on our old debian hosts. We are trying to migrate many of these hosts to Nix or to our k8s cluster. Nix hosts handle deploying changes through [self-hosted github actions runners](../nix/ci-cd.md) rather than puppet.

[servers]: https://www.ocf.berkeley.edu/docs/staff/backend/servers/

