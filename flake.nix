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
        deploy = pkgs.mkShell {
	  packages = with pkgs; [
	    rsync
	    openssh
	  ];
        };
      });
      formatter = forAllSystems (pkgs: pkgs.nixpkgs-fmt);
    };
}
