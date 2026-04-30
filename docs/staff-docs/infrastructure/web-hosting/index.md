---
title: Web Hosting
---

Currently, we host `bestdocs.ocf.io` and `decal.ocf.io` on `amethyst`, a NixOS host for static websites. See the OCF's [nix webhost module](https://github.com/ocf/nix/blob/main/modules/webhost.nix) for more information on its setup, as well as [`amethyst`'s host file](https://github.com/ocf/nix/blob/main/hosts/servers/amethyst.nix)

`vampires` is for dynamic websites, and `death` is for static web hosting. Both of these are debian hosts. `death` also hosts Wordpress websites for some reason.
