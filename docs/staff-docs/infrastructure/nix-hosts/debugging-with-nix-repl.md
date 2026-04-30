If you'd like to evaluate something to test it before you push (as you should), you can use `:lf`in a nix repl to load the outputs of the flake, and then you can inspect any of them just by typing their name. Nix is a lazily evaluated language, so you can look at things by trying to evaluate them in the repl.

```none
$ cd /path/to/nix/flake
$ nix repl
>> :lf .#
>> nixosConfigurations.adenine
{ _module = { ... }; config = { ... }; extendModules = «lambda @ /nix/store/gmdhl9qfaic5765lxw2wj6hb2ifjmhjd-source/lib/modules.nix:329:23»; extraArgs = { ... }; options = { ... }; pkgs = { ... }; type = { ... }; }
```
