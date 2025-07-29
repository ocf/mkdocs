---
title: Database (MySQL)
---

The OCF provides each user with a MySQL database. Read the following sections
for information about performing common MySQL tasks, and our rules and policies
regarding MySQL.

The actual server runs [MariaDB](https://mariadb.org/), which is an
active community-driven fork of MySQL. In practice, you shouldn't notice any
important differences between the two, though MariaDB does contain [some
improvements](https://mariadb.com/kb/en/mariadb/mariadb-vs-mysql-features/).


## Policies

We limit users to 1 database, and this database has the same name as your
username. As a user of shared database server we ask you to respect the
community and refrain from any activities that will hurt the quality of service
for other users. We understand this policy is vague, so our suggested maximum
size for databases is 1GB, and for individual tables 256 MB. Storing large
amounts of data is not a problem unless the server has to perform complex
queries on this data.


## Web-based interface for editing

If you are looking for a familiar phpMyAdmin interface, visit
<https://pma.ocf.berkeley.edu>.

## Creating a MySQL database

Log into the OCF via [SSH](shell), at the terminal prompt enter
the command `makemysql`. Hit yes to confirm the operation. Note your password
in a safe place.

## Reset Password

To reset a MySQL password, simply follow the directions above for creating a
MySQL database. This program WILL NOT DELETE an existing database.


## Accessing MySQL

Assuming your database is set up, in order to access it (or allow a web
application to access it), you will need 4 pieces of information:

* Database Host: mysql
* Database Name: {your OCF username}
* Database User: {your OCF username}
* Database password: {your database password}

Note: Your database password is not the same as your OCF account password. It
is a randomly generated password that was created when your database was
created. To use your OCF MySQL database with a web application, enter the above
information during the application's installation process.

To connect to the OCF's MySQL server using the MySQL client on an OCF machine,
simply run the command: `mysql`

This command will prompt you for your MySQL database password.

## Backing up a MySQL database

To backup your database (which you should probably do regularly), the basic
command to use is

    mysqldump [username] > backup

where username denotes your OCF username and `backup` is the name of the file
you want to dump the contents of your database into. This command will prompt
you for your MySQL password.

To see more options, try running

    mysqldump --help


## Restoring a MySQL database from backup

If you need to restore your database from a backup (dump file) you made
previously, you simply need to connect to the database and run the SQL commands
in the dump file. To do this from the command line, use

    mysql -D [username] < backup

where backup is the name of the file that contains the dumped data. As usual,
this command will prompt you for your MySQL password.


## Using .my.cnf for passwordless access to MySQL

If you are using MySQL in a script or in another program, you will probably
want to set it up so that the `mysql` call does not prompt for your password.
While passing the -p option is the obvious way to achieve this, it is also
*very insecure* because anyone on OCF can see the password while the mysql
command is running. A better approach is to create a `~/.my.cnf` file with
proper permissions that contains your MySQL password. To do this, enter the
following commands: make sure you replace dbpasswd with the MySQL password
given to you when you ran makemysql.


    touch ~/.my.cnf
    cat >> ~/.my.cnf << EOF
    [client]
    password = dbpasswd
    EOF
    chmod 600 ~/.my.cnf

And make sure that your .my.cnf has correct permissions by running

    $ ls -l ~/.my.cnf
    -rw-------  1 staff ocf 64 2005-11-15 16:16 /home/s/st/staff/.my.cnf

Now the mysql command will automatically log you in, so you won't have to
memorize or write down your MySQL password.
