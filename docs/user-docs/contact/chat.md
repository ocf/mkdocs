---
title: OCF Chat
---

OCF staff often use our bridged chat server to communicate. If you have questions, feel free to
drop by &mdash; it's often faster than emailing us, especially for
discussion-type questions.

We normally chat in the `#rebuild` channel. For historical reasons, `#ocf` is
mostly for non-OCF-related discussion.

Use whichever chat service you prefer, but keep in mind that IRC and Matrix are the coolest.

## 1. Matrix

With an OCF account, you'll be able to join our server!

1. Go to [chat.ocf.io](https://chat.ocf.io).

2. Click "Sign In"

3. Click "Continue with OCF"

4. Enter your OCF username and password. Do not use your Berkeley email. 

5. Enjoy!

You can set your username and profile picture in the settings of OCF Chat. 

## 2. Internet Relay Chat (IRC)

You have a couple of options for chatting over IRC:

### Option 1: Using your own client

You can connect using any IRC client. If you do not already have an IRC client,
we recommend using [Hexchat][hexchat] because it is free, open source, and
generally easy to use. Our server settings are listed below:

* **Server:** `irc.ocf.berkeley.edu`
* **Port:** `6697` (requires SSL/TLS)
* **Channels:** `#rebuild` (best to reach staff), `#ocf` (best for off-topic)

### Option 2: Over SSH

If you're logged in to the OCF login server via [[SSH|doc services/shell]], you
can use the pyrc script to easily connect to IRC. It will automatically launch
a tmux session to contain your IRC session, so that you aren't disconnected
when you close the terminal.

To do so, just type `pyrc` and hit enter. irssi will launch; press alt +
left/right to switch which channel you're viewing.

### Option 3: Over XMPP

If you have an XMPP account, you can join IRC channels with room name
`#channelname` and server name `irc.ocf.berkeley.edu` (alternatively,
`#channelname@irc.ocf.berkeley.edu` depending on your client).

## Authenticating with NickServ

To make sure that you can keep the same username, even after being disconnected
and reconnecting again, you can register with NickServ.

### Registering with NickServ

To register with NickServ, choose a password and enter the command `/msg
NickServ register [password] [email]` into your IRC client. NickServ should
reply after you run the registration command that you have been registered with
your email. To see if you are registered properly, try running `/msg NickServ
info`. You should see your email address, and where you are logged in from,
among other results.

## 3. Discord

If you want to NOT use open source software, you can use Discord :/

The url is: [ocf.io/discord](https://ocf.io/discord)

## Other important info

### Everything is public

When chatting, please keep in mind that the channels are open to the whole world. 

Anyone could be keeping a log of what is said, so please don't say anything that you wouldn't
want to be public!

### I can't log in!

When logging in to Matrix or IRC, use your OCF username. Do not use your `@berkeley.edu` email. 

If you're still having trouble, you can always reset your password.

### List of Major OCF Channels

*#announcements*: Low volume announcements channel. Turn on notifications for
messages in this channel!

*#rebuild*: Technical discussion

*#administrivia*: Administrative discussion

*#henlo*: Memes and off-topic social chat with current staff

*#ocf*: General alumni/staff off-topic hangout channel and non-OCF tech
discussion

*#rebuild-spam*: Information on Github changes/PRs (spammy)

*#test*: Actual spam

### List of Minor OCF channels

*#decal-general*: DeCal student chat

_#\*-comm_: Channels for committee discussion

*#cs162-fa19*, *cs170-fa19*, and others: Per-class discussions

*#xcf*: XCF discussion
