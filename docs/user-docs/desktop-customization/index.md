# Desktop Customization

:::info
This is still a work in progress - the KDE plasma docs aren't the best and most things here have been figured out through trial and error. You should be able to configure basic things with the instructions provided here but I'll eventually document the more interesting things you can do. If you want to just look at random cool things that I've discovered feel free to poke through my [current desktoprc](https://github.com/laksith19/ocf-desktoprc/)!

:::

When you login to an OCF desktop `~/remote/.desktoprc` is automatically [sourced](/doc/sourced-WqYnEn3HjV). As `~/remote` is an sshfs mount from tsunami. To get started with your own custom configuration you can run `$ kate ~/remote/.desktoprc`. This will open up a text editor with a new file, paste / type in a config that you want to use and save the file. This file will now be run every time you login to one of the desktops. 


## Sample Config:

Here's a template to get you started:

```bash
# Sample desktoprc for OCF desktops
echo "Starting desktop config..."

# Personally I like setting these flags in scripts as they avoid weird issues
# You can read more about these options here - http://redsymbol.net/articles/unofficial-bash-strict-mode/
# Feel free to comment it out, they don't really do much for this sample script
set -euo pipefail

# Uncomment this line if you want to print every command run to logs
# set -x

# open up a terminal type plasma- and press tab a couple times, the autocomplete should give you a list of different
# commands available to customize the desktop enviornment. You can then run those commands with --help to learn how to
# use them! Try running a command in the terminal, if you like what it did to your desktop copy paste it into your desktoprc!

# Set dark theme
plasma-apply-lookandfeel -a org.kde.breezedark.desktop

# Set wallpaper
plasma-apply-wallpaperimage ~/remote/.config/desktop/wallpaper.jpg

# Set cursor theme
plasma-apply-cursortheme "Adwaita"

# Remove all desktop icons :) - cause I personally hate them loll
rm -rf ~/Desktop/*

# Install custom packages - in this case lsd and intellij (just as an example).
# These packages are not limited to terminal utilities but can install full custom desktop applications for you!
# You can search the list of available packages at - https://search.nixos.org/packages?channel=unstable
# Note: You'll have to use the nixpkgs#<package> format for any package you find through the package search. 
nix profile install nixpkgs#lsd nixpkgs#jetbrains.idea-community-bin 

# Don't put much beyond this as it'll take a while to finish getting and installing custom packages 
# Unless you need package for some command you want to run.

echo "Completed, running desktoprc!"
```


## Debugging and monitoring:

You can look at the logs and outputs from your desktoprc by running `$ systemctl —user status desktoprc.service` or `$ journalctl —user desktoprc.service`.