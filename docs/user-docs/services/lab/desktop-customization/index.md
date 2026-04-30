---
title: Desktop Customization
---



## .desktoprc

To begin customizing your desktop, you need to create a file named `.desktoprc`
in your remote directory. This is a bash script which will be sourced each time
you log into any OCF desktop.

Lines that start with `$` are commands to enter into a terminal emulator such as `kitty` or `Konsole`.

>`~/remote` is an sshfs mount from `carp`, the OCF's public login server

To create a `.desktoprc` file, open a text editor of your choice and create a new file at `~/remote/.desktoprc`.

For example, here's how to do it with the Konsole terminal and Kate text editor:

1. Press Ctrl+Alt+T
2. Run `$ kate ~/remote/.desktoprc` in a terminal such as `kitty`.
3. Paste the following line: `nix run home-manager -- switch --flake ~/remote/home-manager`
4. Ctrl+S to save

Now, after logging in, the computer will switch to the flake within that directory.

## Home Manager Flake

We will first create a directory on `~/remote` that will set up NixOS
Home Manager via a Nix Flake. Run these commands in a terminal such as `kitty`.

`$ mkdir ~/remote/home-manager`

Now, we will generate basic `flake.nix` and `home.nix` files in that directory we just made with the next command.

`$ nix run home-manager/master -- init ~/remote/home-manager`

## Plasma Manager

The default desktop environment on the OCF desktops is KDE Plasma. To make configuration management easier on KDE, we will use a home manager module called [plasma-manager](https://github.com/nix-community/plasma-manager).

First, you'll want to add `plasma-manager` to your `flake.nix` file like so:

``` nix title="flake.nix" hl_lines="7-11 15 26-29"
inputs = {
  nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  home-manager = {
    url = "github:nix-community/home-manager";
    inputs.nixpkgs.follows = "nixpkgs";
  };
  plasma-manager = {
    url = "github:nix-community/plasma-manager";
    inputs.nixpkgs.follows = "nixpkgs";
    inputs.home-manager.follows = "home-manager";
  };
};

outputs =
  inputs@{ nixpkgs, home-manager, plasma-manager, ... }:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in
  {
    homeConfigurations."YOURUSERNAME" = home-manager.lib.homeManagerConfiguration {
      inherit pkgs;

      # Specify your home configuration modules here, for example,
      # the path to your home.nix.
      modules = [ 
        plasma-manager.homeModules.plasma-manager
        ./home.nix 
      ];

      # Optionally use extraSpecialArgs
      # to pass through arguments to home.nix
    };
  };
}
```

Then, re-apply the flake with `nix run home-manager -- switch --flake ~/remote/home-manager`. You should see some terminal output, with some lines about the new inputs getting successfully added! You can now begin customizing your desktop. Be sure to save the files you've changed and run that command each time you want to refresh your configuration.

If you're having trouble understanding Nix syntax, check out the Nix documentation on [Names and Values](https://nix.dev/tutorials/nix-language.html#names-and-values).

### System light/dark mode

Insert the following in your `home.nix` file to change the system theme to dark:

``` nix title="home.nix"
  programs.plasma.workspace = {
    lookAndFeel = "org.kde.breezedark.desktop";
    iconTheme = "Papirus-Dark";
  };
```

### Desktop Themes

1. Find a theme you want. Here are some from the official `nixpkgs` repository:
    - [kde-gruvbox](https://github.com/printesoi/kde-gruvbox)
    - [catppuccin-kde](https://github.com/catppuccin/kde)
    - [nordic](https://github.com/EliverLara/Nordic)
    - [twilight-kde](https://github.com/yeyushengfan258/Twilight-kde)
    - [plasma-overdose-kde-theme](https://github.com/Notify-ctrl/Plasma-Overdose)
    - [sweet-nova](https://github.com/EliverLara/Sweet)
    - [whitesur-kde](https://github.com/vinceliuice/WhiteSur-kde)

2. Add a line with the nix package name, such as `pkgs.kde-gruvbox`, to the `home.packages` list in the `home.nix` file.

3. Re-apply the flake (`$ nix run home-manager -- switch --flake ~/remote/home-manager`), then run `$ plasma-apply-desktoptheme --list-themes` to check that it was installed.

4. A

### Setting the wallpaper

### Additional Customization!

See [Plasma-Manager Options](https://nix-community.github.io/plasma-manager/options.xhtml)

### Custom KDE cursor

## Terminal Customization

1. https://home-manager-options.extranix.com/
2. Look at the options
3. Set it (ex. programs.kitty.themeFile)

## Debugging and Monitoring

You can look at the logs and outputs from your desktoprc by running `$ systemctl —user status desktoprc.service` or `$ journalctl —user desktoprc.service`.

## Tracking with Git & Github

## Sample Configs from OCF Staff
- laksith: [.desktoprc](https://github.com/laksith19/ocf-desktoprc/), [home manager flake](https://github.com/laksith19/ocf-home-manager)

- jaysa: [.desktoprc](), [home manager flake]()

## Resources

Searches:

- [Nixpkgs Search](https://search.nixos.org/packages)
- [NixOS Options Search](https://search.nixos.org/options?)
- [Home Manager Option Search](https://home-manager-options.extranix.com/)

Wikis:

- [wiki.nixos.org](https://wiki.nixos.org/wiki/NixOS_Wiki)
- [nixos.wiki](https://nixos.wiki/wiki/Main_Page)

Relevant Reading:

- [Home Manager Manual - Nix Flakes](https://nix-community.github.io/home-manager/index.xhtml#ch-nix-flakes)
