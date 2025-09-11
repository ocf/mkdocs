---
title: Desktop Customization
---



## .desktoprc

To begin customizing your desktop, you need to create a file named `.desktoprc`
in your remote directory. This is a bash script which will be sourced each time
you log into any OCF desktop.

>`~/remote` is an sshfs mount from `tsunami`, the OCF's public login server

To create a `.desktoprc` file, open a text editor of your choice and create a new file at `~/remote/.desktoprc`.

For example, here's how to do it with the Konsole terminal and Kate text editor:

1. Press Ctrl+Alt+T
2. Run `$ kate ~/remote/.desktoprc`
3. 
4. Ctrl+S to save

## Home Manager Flake

Now, we're going to create a directory on `~/remote` that will set up NixOS
Home Manager via a Nix Flake.

`mkdir ~/remote/home-manager`

`kate ~/remote/home-manager/flake.nix`

Paste the following default configuration into the empty `flake.nix` file, replacing `USER` with your ocf username:

```
{
  description = "Default OCF Home Manager Configuration"

  inputs = {
    # Specify the source of Home Manager and Nixpkgs.
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    home-manager = {
      url = "github:nix-community/home-manager";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { nixpkgs, home-manager, ...}:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in
  {
    homeConfigurations."USER" = home-manager.lib.homeManagerConfiguration {
      inherit pkgs;

      # Specify your home configuration modules here, for example,
      # the path to your home.nix.
      modules = [ ./home.nix ];

      # Optionally use extraSpecialArgs
      # to pass through arguments to home.nix
    };
    formatter.${system} = pkgs.nixpkgs-fmt;
  };
}
```

Now, we're going to create a basic `home.nix` file, where the majority of our customization will later take place.

More resources:

[Home Manager Manual - Nix Flakes](https://nix-community.github.io/home-manager/index.xhtml#ch-nix-flakes)

## Debugging and monitoring:

You can look at the logs and outputs from your desktoprc by running `$ systemctl —user status desktoprc.service` or `$ journalctl —user desktoprc.service`.

## Tracking with Git & Github

## Sample Configs from OCF Staff
- laksith: [.desktoprc](https://github.com/laksith19/ocf-desktoprc/), [home manager flake](https://github.com/laksith19/ocf-home-manager)

- jaysa: [.desktoprc](), [home manager flake]()
