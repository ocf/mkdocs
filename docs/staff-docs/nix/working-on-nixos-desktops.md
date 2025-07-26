# Working on NixOS Desktops

# Setup

you dont have to use staff VM for this. but i do



1. ssh into your staff VM. if you dont have a staff VM, request one
2. install nix: <https://nixos.org/download/#nix-install-linux>
3. fork the ocf nix repo: <https://github.com/ocf/nix/tree/main>
4. clone your fork and push your changes to it
5. `colmena apply --on hostname`


# Add new package

clone this repo: <https://github.com/ocf/nix>


`colmena apply --on hostname`