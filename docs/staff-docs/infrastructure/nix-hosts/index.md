---
title: Nix Hosts
---

[NixOS](https://nixos.org) is the Linux distribution created from the [nixpkgs](https://github.com/NixOS/nixpkgs) package repository, which is written in the [Nix](https://nixos.wiki/wiki/Overview_of_the_Nix_Language) language. Although our services are based on Kubernetes, there still needs to be some component actually installing packages on servers, and NixOS fulfills this role.

For a good introduction on NixOS and Nix, see the excellent third-party documentation available at <https://zero-to-nix.com>.

## Benefits

* **Declarative configuration management**
* **Very little manual configuration drift**
* **Easy rollbacks if things break**
* **Side-by-side versions of packages**

## A Quick non-technical rundown of NixOS

Normally, when you're running an Operating System, say, Windows (eww), you have to go into a bunch of settings and windows to make your computer do what you want it to do. These settings are stored in files, which live on your computer's hard drive. NixOS lets you *start* with those files, and build the OS second. In addition, every package you install has its own directory, with its own dependencies, that are **immutable**, or unchangeable by users. All this together lets you do some cool things:

* **Declarative configuration management** - I can share my Operating System configuration, the apps I use, any custom scripts I might have, etc. really easy
* **Very little manual configuration drift** - Since you control the files you use, you can reproduce your exact configuration really easily. Removing a package will *completely* remove it, since you are literally rebuilding your OS without it.
* **Easy rollbacks** - Made a change that breaks things? Just roll your configuration files back to before that change and you're good to go! Think about how hard this might be on a Windows machine…

NixOS is built for 1 core function: ***reproducibility****.* A certain config file will build NixOS a certain way, and that assurance is why we use NixOS.

## Development

You might want to use Nix on your computer to easily get a development environment for various OCF systems. If the repository has a file called flake.nix in it, you can get a development environment for it as simply as nix shell github.com:ocf/<reponame>. For example, to get transpire, you can do nix shell github.com:ocf/transpire.

`nix shell` is really cool because you can use it install and work with any packages you want in a new shell. You can use `nix shell -p pkg1 pkg2` to open a new shell with those packages installed.

To install Nix, follow the instructions at https://zero-to-nix.com/start/install

## Old Linux Systems (Puppet)

We used to use [Puppet](/doc/puppet-4chWqU6Eqx). Actually we still do use puppet, and most of our legacy infrastructure is on it. See the link in the first sentence for more information!
