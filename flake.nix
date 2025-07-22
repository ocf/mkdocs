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
      packages = forAllSystems (pkgs: {
        default = pkgs.callPackage ./. { };
      });

      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          inputsFrom = [ self.packages.${pkgs.system}.default ];
          shellHook = "mkdocs serve";
        };
      });

      formatter = forAllSystems (pkgs: pkgs.nixpkgs-fmt);
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs.python313Packages; [
	  mkdocs-material
	  mkdocs-rss-plugin
	  mkdocs-git-revision-date-localized-plugin
	  mkdocs-awesome-nav
        ];
	shellHook = "mkdocs serve";
      };
      formatter.${system} = pkgs.nixpkgs-fmt;
    };
}
