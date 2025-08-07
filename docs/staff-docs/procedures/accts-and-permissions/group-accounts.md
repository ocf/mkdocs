# Group Accounts

## Change group account password


1. Have RSO's signatory come in for staff hours, and verify that person is a signatory.

   
   1. SSH into supernova, run:

```bash
check $GROUP_NAME
```

The bottom of the output should show a list of signatories. You can also check the organization's CalLink page. You should ask for their Cal ID and make sure it matches the signatory name.


2. Next, change their password. Run:

```bash
chpass $GROUP_NAME
```

They may be afraid that nothing appears as they type. Gently reassure them, noting that they will get to verify their password by typing it a second time.