---
title: Managing OCF Chat
---

config on host stored in `/etc/ergo.yaml`. should pull from github

`/server add ocf irc.ocf.io`
`/connect ocf`

## IRC

### account creation
https://github.com/ergochat/ergo/blob/stable/docs/USERGUIDE.md#account-registration
connect to ocf, have the nickname you want
`/msg NickServ register mySecretPassword validEmailAddress@example.com`

### SASL
this section of [libera.chat SASL](https://libera.chat/guides/weechat):

- `/set irc.server.ocf.sasl_mechanism plain`
- `/set irc.server.ocf.sasl_username USERNAME`
- `/set irc.server.ocf.sasl_password PASSWORD`

### IRC admin login (server operator)
(NEEDS ROOT)
connect to irc.ocf.io as your normal user

this oper named "admin" is defined in ergo.yaml. the only op on the server, with the password only accessible to root users.
`/oper admin ADMINPASSWORD`

### IRC Channel OP
connect to irc.ocf.io
channel already exists

`/msg ChanServ OP #channelname`


### Channel creation
`/join #channelname`
`/msg ChanServ REGISTER #channelname`

NOTE: need to find way to declaratively create and register channels when server starts

If you restart anything, you better set aside time to debug the bridges.....

## Matrix
to create a new channel, you must be a Matrix admin
TODO document how to do this with SQL to your user. it is not set with nix

also, don't forget postgres needs to be manually updated between postgres versions lol

## I'm not in one of the rooms on matrix! How do I join?
go to matrix, add a room, remove the 'public room' or other search filter, `#_discord_735620315111096391_1288710167633985536:ocf.io`

## accessing matrix database
- proxmox ssh into scootaloo, the host for matrix and irc.
- `sudo -u matrix-synapse psql`
- `SELECT name, admin FROM user WHERE name='@jaysa:ocf.io'` to check if the user exists
