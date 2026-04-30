We sometimes need to send email in mass for things like opstaff hiring. This is how we do it.

## Getting emails from ldap
You need admin privilege to complete this step:

`kinit []/admin && ldapsearch "(creationTime>=20240815000000-00)" mail | grep mail >> emails.txt`

Here I set creationTime filter to the start of the Fall 2024 semester. You can change it to whenever that suits your needs. 
The idea here is that we are filtering for freshman and sophomore.

## Importing emails to Google Sheets
There are many ways to export the .txt file into CSV. I (vibe) wrote a python script to do that.
Once you have the emails in CSV, import it to a Google Sheet under OCF google drive.

## Sending emails
You can either use ocflib.misc.mail.send_mail or Gapps script. I used Gapps.
I stole and modified the script from the DecalVM mailing list. You should copy paste the following code into Your Sheet -> Extensions -> App Script:
```
function sendHiringEmails() {
  // --- Please update this ---
  var sheetName = "Sheet1"; 
  // -------------------------

  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  if (!sheet) {
    Logger.log("Error: Sheet not found. Please check the 'sheetName' variable.");
    return;
  }
  
  var data = sheet.getDataRange().getValues();
  var alias = "storce@ocf.berkeley.edu";
  
  // --- Email Content ---
  var subject = "Waddles says hi!";
  var message = `
    Waddles is the best!
  `;
  // ---------------------
  total = 0
  for (var i = 0; i < data.length; i++) {
    var email = data[i][0]; // Get email from the first (and only) column

    // Basic validation to skip empty rows or invalid-looking emails
    if (email && email.includes("@")) {
      try {
        GmailApp.sendEmail(email, subject, "", {
          from: alias,
          htmlBody: message
        });
        Logger.log("Email sent to: " + email);
        total += 1
      } catch (e) {
        Logger.log("Error sending email to: " + email + " - Error: " + e.message);
      }
    } else {
      Logger.log("Skipping row " + (i + 1) + ": Invalid or empty email.");
    }
  }
  Logger.log("Email sent to " + total + " students.")
}
```
Of course, change the message, alias, sheetname etc.
Make sure that when you run it you have the permission to send as the alias address.
