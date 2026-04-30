# Class Accounts

Procedures for accounts created for use by classes utilizing the OCF lab's computers for teaching  (e.g. ATDP, SWE++)


---

# Info

We provide group accounts to use as shared accounts for classes. All students log in to the same account (or they are logged into before class by the instructor). Since OCF's desktops put home directories on tmpfs, this means that each student gets their own home directory. The home directory is wiped the next time the computer goes to sleep (see [puppet://ocf_desktop/suspend/ocf-suspend](https://github.com/ocf/puppet/blob/master/modules/ocf_desktop/files/suspend/ocf-suspend)).

# Account setup

* Create a group account (run `approve`, with `callinkOid` set to `0`)
* Desktop session customization (`.desktoprc`):
  * Skeleton for the current (2022) KDE desktop

    ```bash
    # remove existing icons
    rm -f ~/Desktop/libreoffice.desktop
    rm -f ~/Desktop/print-queue.desktop
    rm -f ~/Desktop/remote-terminal.desktop
    rm -f ~/Desktop/sftp.desktop
    rm -f ~/Desktop/terminal.desktop
    rm ~/Desktop/writer.desktop
    
    # KDE config modifications:
    #  hide paper indicator
    #  remove terminal shortcut on applications bar
    sed -i \
      -e 's/paper-genmon/true/g' \
      -e 's/,applications:org\.kde\.konsole\.desktop//g' \
      ~/.config/plasma-org.kde.plasma.desktop-appletsrc
    
    # ADDITIONAL CONFIG GOES HERE
    
    # prevent students from messing with shared data
    umount -l ~/remote
    ```
  * Any additional files/config should be stored in the NFS home directory (mounted as `~/remote` on the desktops themselves) and copied over in the `.desktoprc`, e.g.

    ```bash
    # copy over some desktop icons
    cp ~/remote/atom.desktop ~/Desktop
    
    # GitHub desktop "installation"
    export PATH="$HOME/.local/bin:$PATH"
    mkdir -p ~/.local/bin
    if [ ! -x ~/.local/bin/github-desktop ]; then
      cp ~/remote/apps/GitHubDesktop-linux-3.0.1-linux1.AppImage ~/.local/bin/github-desktop
    fi
    cp -r ~/remote/apps/github-desktop/* ~/.local/
    install -m755 ~/.local/share/applications/github-desktop.desktop ~/Desktop/
    ```
* The account should be sorried when class is not in session

# Lab setup

## Puppet

TODO

## For Opstaff

* To wake up all computers in the lab, run `lab-wakeup -f`
* To check if all computers are online: run `ssh-list desktop true` (or `ssh-list desktop -t 5 true`  - `-t <n>` is a timeout in seconds, so offline machines don't take as long to error)
  * (2023Sp) Expected failures (not actually lab machines): `newton`, `hozer-71`