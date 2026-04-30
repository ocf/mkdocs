# Nix on your Computer

You might want to use Nix on your computer to easily get a development environment for various OCF systems. If the repository has a file called `flake.nix` in it, you can get a development environment for it as simply as `nix shell github.com:ocf/<reponame>`. For example, to get [transpire](/doc/configuration-transpire-uJ5GHrW9cg), you can do `nix shell github.com:ocf/transpire`.



:::info
`nix shell` is really cool because you can use it install and work with any packages you want in a new shell. You can use `nix shell -p pkg1 pkg2` to open a new shell with those packages installed.

:::

To install Nix, follow the instructions at <https://zero-to-nix.com/start/install>