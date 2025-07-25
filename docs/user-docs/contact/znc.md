---
title: ZNC
---

[ZNC][znc] is an IRC network bouncer. It permanently connects to the IRC
server, so users connecting through it can preserve their chat session. Most
users don't need this, but IRC regulars may appreciate the extended chat
history and the absence of join/leave messages.

ZNC also integrates with NickServ, automatically authenticating for you with
a nickserv module if you save a password with ZNC.

### Creating a ZNC account

Ask a root staffer (or ping #rebuild) to create a ZNC username / password.

### Configuring ZNC

Configuration is most easily done through the [ZNC web interface][webznc]. It
requires you to login using your staff-created ZNC account.

Once you've logged in, under `Your Settings` you should set the following
fields:
* **Nickname**: your nickname
* **Alt. Nickname**: your alternate nickname, if your primary is taken
* **Ident**: should be same as nickname, used to uniquely identify you from
  everyone else using IRC
* **Networks**: add a network with server `irc.ocf.berkeley.edu +6697`,
  **space included**.

Click save at the bottom, and your ZNC account should be setup to connect to
the main IRC server.

### Connecting to ZNC

The OCF ZNC server settings are:

* **Server:** `irc.ocf.berkeley.edu`
* **Port:** `4095` (requires SSL/TLS)

You should also set your IRC client login settings:
* **Use SSL [...]**: True
* **Login method**: `Server password (/PASS password)`
* **Password**: your ZNC `password`, or `user:password`

Once you have setup both ZNC and your IRC client, you should be able to
connect to IRC normally.

### Setting up NickServ to work with ZNC

If you are [[using ZNC|doc staff/tips/staffvm/znc]], load the [NickServ
module][nickserv] by running `/znc LoadMod nickserv` while connected to your
ZNC server. Then, in your ZNC web admin interface, log in and go to `Your
Settings` under either the global or user modules links. Under the Networks
section, click on the `Edit` link next to the OCF network and scroll down to
the Modules section. Enable the `nickserv` module and type the password you
used to register with NickServ into the arguments box. Then save your changes
using the button at the bottom of the page and ZNC should automatically
authenticate with NickServ if you get disconnected from ZNC.

[znc]: https://wiki.znc.in/ZNC
[webznc]: https://irc.ocf.berkeley.edu:4095
[webirc]: https://irc.ocf.berkeley.edu
[thelounge]: https://thelounge.github.io
[hexchat]: https://hexchat.github.io
[nickserv]: https://wiki.znc.in/Nickserv
