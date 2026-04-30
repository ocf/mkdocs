---
title: Login Servers
---

## Public login server (carp)

## Staff login server (koi)

When contributing to the OCF codebase, you will need some way of running and
testing your code. Most of our applications cannot be run on a personal
machine--they need to be run on OCF infrastructure. For most projects we
recommend doing all development from `koi`, a server available to all
staff. Our [Kubernetes server](../infrastructure/kubernetes/index.md) is also
accessible from `koi`.

## Before you begin
You need to be on staff to log into the server. If you're not sure whether or
not you're on staff, try logging in. If this doesn't work, talk to a staff
member and we can add you! All are welcome and encouraged to join.

## Logging in
To log in, open a terminal window and type in:

```bash
ssh username@koi.ocf.berkeley.edu
```

For more instructions, see the [SSH docs](../../user-docs/services/shell/index.md). You should
replace `ssh.ocf.berkeley.edu` with `koi.ocf.berkeley.edu`.

## Setting up SSH Keys

You can log in to `koi` like normal (`ssh $USER@koi.ocf.berkeley.edu`) with your username and password, but should seriously consider creating and uploading an SSH key so that you don't need to type a password when logging in anymore.

First, check if you have an SSH key. You can do this by checking `~/.ssh` on your laptop. If you see files named `id_rsa` or `id_ed25519` (these are private keys and should never leave your computer, the public keys are in `id_rsa.pub` or `id_ed25519.pub`), then you already have an SSH key! If not, create an SSH key like…

```bash
# Accept all default values when prompted. You can set a password on the key if you want.
ssh-keygen -t ed25519 -C "$USER@ocf.berkeley.edu"
```

Then, to upload your public key to a server (e.x. koi), do…

```bash
ssh-copy-id koi.ocf.berkeley.edu
```

## Configuring your SSH Config

Paste this into `~/.ssh/config`, and you'll be able to ssh into any OCF host with just `ssh $HOSTNAME.ocf`.

```bash
Host koi.ocf
  ProxyJump none
  Port 22
  # This will allow koi to sign things with your *private* key!
  # Only uncomment this if you understand the risks and/or have an SSH agent 
  # that will interactively prompt you about when your key is being used.
  # ForwardAgent yes

Host *.ocf
    Hostname %h.berkeley.edu
    ProxyJump koi.ocf
```

## Things you can do on `koi`

### Administration scripts

Some scripts, such as ones used to create group accounts and refund printing
quotas, are available on `koi`. Learn more about these in the scripts
section of [staff documentation](../index.md).

### Development and Testing
You can `git clone` OCF repositories and run them on `koi`. An example
for `ocfweb`:

```bash
git clone https://github.com/ocf/ocfweb # clone the repository
cd ocfweb # change directory into the repository

... make changes ...

make test # run tests to make sure everything is working
make dev # start a development server and see your changes live
```

### Kubernetes
To access Kubernetes, simply run `kubectl` commands. See the [Kubernetes
documentation][kubernetes-basics] for more information.

Note that staff only have viewing permissions for the cluster. Interested
stafferse can request write access to a development namespace by talking to a
root staffer.

[kubernetes-basics]: https://kubernetes.io/docs/tutorials/kubernetes-basics/

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

