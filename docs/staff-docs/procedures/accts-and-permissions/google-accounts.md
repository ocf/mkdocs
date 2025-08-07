# Google Accounts

The OCF has its own Google Apps deployment, which we mainly use for GDrive and GMail. While it's possible to use `@berkeley.edu` Google accounts for these (`@ocf.berkeley.edu` emails redirect to Berkeley Google accounts by default), most active staffers choose to have a dedicated account because:

* It allows for nicer integration with our Google Drive folders.
* It makes it easier to send emails from the `ocf.berkeley.edu` domain, which is good if you want to send an email while representing the OCF.
* It can be useful to have a separation between OCF and Berkeley accounts.

## Making an account

Google Apps accounts are available upon request for OCF staff members, and are granted at SM discretion. Upon getting one, staffers should be aware that OCF emails will be sent to the new account instead of the Berkeley account that they're used to.

Making a new account requires Google Admin privileges.


1. Go to [admin.google.com](http://admin.google.com), click on the "Users" section of the Admin panel, and press the '+' button.
2. Fill in the first and last name of the user, and make sure their email address matches their OCF username.
3. Update the user's `mail` attribute in LDAP to use Google Apps (`kinit YOUR_USER/admin ldapvi uid=THEIR_USER`) and change it to `usernamehere@g.ocf.berkeley.edu`. 

   
   1. **The** `g.` **in the domain is critical; omitting it can cause email delivery loops in our system!**
4. Add the user to the appropriate Google groups, and (if needed) add them as members on the OCF Staff shared drive.