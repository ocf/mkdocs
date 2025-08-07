# Granting Staff Privileges

# ocfstaff


1. Run this command on any OCF machine, which will open your `$EDITOR`.

```bash
kinit $USER/admin ldapvi cn=ocfstaff
```


2. Add or remove the line `memberUid: staffusername` within the file (your placement doesn't matter, the list sorts itself alphabetically later).

   
   1. Be VERY VERY careful to not hit `dG` or something like that in vim, which will delete the whole file. We have backups (and have had to do this in the past), but don't rely on them -- be careful!
   2. Make sure there are no empty lines in the entry, and that the first line with the object DN (something like `0 cn=ocfstaff,ou=Groups,dc=OCF,dc=Berkeley,dc=EDU`) isn't changed - otherwise ldapvi gets confused, and might clear the object.
3. (Optional) Their groups won't update on all of the servers until the daily cronjob runs. If they need the `ocfstaff` role on a specific server immediately, then [SSH](/doc/ssh-iQbr9ALK7Z) into that server and run the following commands.

   ```bash
   sudo nss_updatedb ldap
   # may fail, but probably okay if it does fail
   sudo systemctl restart unscd
   ```

# ocfroot

Instructions and considerations for adding someone as a new root staffer are in the secret documentation. If you are root you should know where that is, or whoever added you to root didn't follow procedure and needs to be (nicely) yelled at.