# SSHing into Supernova

As an OCF staff member, a lot of what you may need to do may need to happen on an OCF machine. The machine set aside for this is `supernova`. You can login to it like normal `ssh $USER@supernova.ocf.berkeley.edu` with your username and password, but should seriously consider creating and uploading an SSH key so that you don't need to type a password when logging in anymore.

## Setting up SSH Keys

First, check if you have an SSH key. You can do this by checking `~/.ssh` on your laptop. If you see files named `id_rsa` or `id_ed25519` (these are private keys and should never leave your computer, the public keys are in `id_rsa.pub` or `id_ed25519.pub`), then you already have an SSH key! If not, create an SSH key like…

```bash
# Accept all default values when prompted. You can set a password on the key if you want.
ssh-keygen -t ed25519 -C "$USER@ocf.berkeley.edu"
```

Then, to upload your public key to a server (e.x. supernova), do…

```bash
ssh-copy-id supernova.ocf.berkeley.edu
```

## Configuring your SSH Config

Paste this into `~/.ssh/config`, and you'll be able to ssh into any OCF host with just `ssh $HOSTNAME.ocf`.

```bash
Host supernova.ocf
  ProxyJump none
  Port 22
  # This will allow supernova to sign things with your *private* key!
  # Only uncomment this if you understand the risks and/or have an SSH agent 
  # that will interactively prompt you about when your key is being used.
  # ForwardAgent yes

Host *.ocf
    Hostname %h.berkeley.edu
    ProxyJump supernova.ocf
```

## Troubleshooting

### Cannot delete characters or use keyboard shortcuts

This may occur if you're using a terminal emulator on the machine you're using to SSH that sets a custom `TERM` environment variable. If you're using something xterm-compatible (e.x. `kitty`, `alacritty`), then first check the value of `TERM` as follows…

```bash
❯ echo $TERM
xterm-kitty
```

And then add this to your `~/.bashrc` on the remote end (replacing `xterm-kitty` with the `TERM` variable you got in the first step)…

```bash
if [[ $TERM = "xterm-kitty" ]]; then export TERM=xterm-256color; fi
```

This will make the remote end treat your terminal as if it's xterm, which should make your keyboard shortcuts and backspace work again.

The proper fix for this is to find the package on the remote end that provides support for your terminal emulator, and install it. For example, the `kitty-terminfo` package on Debian is installed on all OCF machines so that if you use kitty over SSH, your terminal will work. If you'd like to fix your terminal just for your user, find the appropriate terminfo file and place it in `~/.local/share/terminfo/`.