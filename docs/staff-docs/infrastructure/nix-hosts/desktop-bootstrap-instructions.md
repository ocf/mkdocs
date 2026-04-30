# Desktop Bootstrap Instructions

# Installing NixOS

* From UEFI settings, set `Boot > Launch PXE OpROM Policy` to `UEFI Only`.
* Determine the device you wish to install Nix on (i.e. /dev/nvme0n1), desired hostname, and the last octet of its IP.
* Follow instructions at [ocf/nix](https://github.com/ocf/nix) for setting up a PXE boot server and running the bootstrap script.
* Follow bootstrap script prompts to install NixOS.

# Applying Nix Configs

Update [ocf/nix](https://github.com/ocf/nix) repo to have a new hosts/desktops entry for the machine being added.

Run `colmena apply --on [hostname]` to apply configs.

# Add to DNS 

* ldap-add-host <hostname> <octet> desktop
* ldapvi cn=<hostname>
  * add the macAddress field

Rebuild [ocf/dns](https://github.com/ocf/nix) repo with `make`, then commit.


\