---
title: TODO
---

Things we probably should get to at some point. If you're adding things to this
list and especially the starter tasks try to link to the relevant host config
and maybe some general direction if you know what needs to be done (at least in principle).

## Starter Tasks
Good first steps to get learn your way around the repo and pick up the nix language.

### Fix / Improve OCF TV
[Tornado](https://github.com/ocf/nix/tree/main/hosts/misc/tornado.nix) is the host that keeps the labmap up on the TV. It runs [sway](https://swaywm.org/)
a tiling window manager and allows staff to control it via a VNC connection
by running `ocf-tv` on any of the lab desktops.

#### Server
WayVNC is started as a command at the end of the sway config at the moment and this
sometimes causes the VNC server to die if a client disconnects uncleanly, needing sway
to be reloaded. The only way to do this when the VNC server is down is a reboot which really
isn't ideal. We use a module system in Nix that allows us to reuse code across hosts and 

We have (had)

### Make Print Queue Real
This might be more of a physical plug shit in and check if it works task but it's a task nonetheless.
The monitor is no longer there and it could be because it wasn't working and someone decided to remove
it. The system in question is [overheat](https://github.com/ocf/nix/tree/main/hosts/overheat.nix) a 
raspberry pi 4 that you should be able to find near / behind papercut.

## Not so Starter Tasks

### Docs
yup...

### CD

