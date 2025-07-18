{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs.python313Packages; [
	  mkdocs-material
	  mkdocs-rss-plugin
	  mkdocs-git-revision-date-localized-plugin
        ];
	shellHook = "mkdocs serve";
      };
      formatter.${system} = pkgs.nixpkgs-fmt;
    };
}

# nix flake init, then 
# nix fmt
# nix develop
