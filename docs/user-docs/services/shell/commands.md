---
title: Commands
---

This is a brief guide to commands that can be run to manage your account, edit a website, or work on our server. To use them, access our login server via [SSH](index.md), either locally or on our [web terminal](https://ssh.ocf.berkeley.edu). Simply type in a command and hit enter to run it. To log out, run the command `exit`.

In the tables below, `ARGUMENT` is a required argument and `[optional]` is an
optional one. For more information on a specific command, run `man COMMAND`.

## OCF commands

These commands help you manage your OCF account.

| Command | Description |
|---------|-------------|
| `how SCRIPT` | Shows the source code for a script |
| [`makehttp`](../web/index.md#via-ssh) | Puts a shortcut to your web directory in your home folder |
| [`makemysql`](../mysql.md#creating-a-mysql-database) | Generates a new random password for your database, creating the database if it does not exist |
| `paper` | Shows how many pages you can currently print |
| `update-email` | Prompts you to set a contact email address for your OCF account |

## File commands

For convenience, here is a very basic listing of commands to manage files. For
a more complete listing, see for example
[Wikipedia](https://en.wikipedia.org/wiki/List_of_Unix_commands).

| Command | Description |
|---------|-------------|
| `cd DIRECTORY` | Changes the current directory to a new one |
| `cp [-r] SOURCE DEST` | Copies a file. The `-r` option allows for copying directories. |
| `less FILE` | Lets you view the contents of a text file |
| `ls [FILE]` | Lists information about files and directories |
| `mkdir DIRECTORY` | Creates a new directory |
| `micro FILE` | Lets you edit a text file with a basic interface |
| `mv SOURCE DEST` | Moves or renames a file or folder |
| `rm [-r] FILE` | Deletes a file. The `-r` option allows for deleting non-empty directories. |
| `rmdir DIRECTORY` | Deletes an empty directory. Safer than `rm -r`. |
