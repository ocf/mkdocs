---
title: Desktop Customization
---

## .desktoprc

The file `~/remote/.desktoprc` is automatically sourced when you log into any
of the desktops. Since `~/remote` is actually `sshfs`'d to your home folder on
NFS, this means you can put your common config or preferences in it and have
them be shared across all desktops.

### Example uses

If you want to get a feel for what you can do with your `.desktoprc`, try out
some of these useful ideas.

#### Sync your dotfiles

If you want your application settings shared between the desktops and login
servers, you can just copy them over with a line like this:

    cp ~/remote/{.bashrc, .bash_aliases, .vimrc, ...} ~/

Alternatively, if you have a [dotfile repo](https://dotfiles.github.io/), you
can either clone it...

    git clone https://github.com/username/dotfiles.git ~/.dotfiles
    ~/.dotfiles/my-install-script

... or just link to it in your NFS homedir, if you have it there:

    ln -s ~/remote/.dotfiles ~/.dotfiles
    ~/.dotfiles/my-install-script
