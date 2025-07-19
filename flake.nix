{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    systems.url = "github:nix-systems/default";
  };

  outputs = { self, nixpkgs, systems }:
    let
      pkgsFor = system: nixpkgs.legacyPackages.${system};
      forAllSystems = fn: nixpkgs.lib.genAttrs (import systems) (system: fn (pkgsFor system));
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = with pkgs.python313Packages; [
            mkdocs-material
            mkdocs-rss-plugin
            mkdocs-git-revision-date-localized-plugin
          ];
          shellHook = "mkdocs serve";
        };
      });

      formatter = forAllSystems (pkgs: pkgs.nixpkgs-fmt);
    };
}

# nix flake init, then
# nix fmt
# nix develop
