---
title: SSHing into Koi
---

When contributing to the OCF codebase, you will need some way of running and
testing your code. Most of our applications cannot be run on a personal
machine--they need to be run on OCF infrastructure. For most projects we
recommend doing all development from `koi`, a server available to all
staff. Our [Kubernetes server](../infrastructure/kubernetes/index.md) is also
accessible from `koi`.

## Before you begin
You need to be on staff to log into the server. If you're not sure whether or
not you're on staff, try logging in. If this doesn't work, talk to a staff
member and we can add you! All are welcome and encouraged to join.

## Logging in
To log in, open a terminal window and type in:

```bash
ssh username@koi.ocf.berkeley.edu
```

For more instructions, see the [SSH docs](../../user-docs/services/shell/index.md). You should
replace `ssh.ocf.berkeley.edu` with `koi.ocf.berkeley.edu`.

## Things you can do on `koi`

### Administration scripts

Some scripts, such as ones used to create group accounts and refund printing
quotas, are available on `koi`. Learn more about these in the scripts
section of [staff documentation](../index.md).

### Development and Testing
You can `git clone` OCF repositories and run them on `koi`. An example
for `ocfweb`:

```bash
git clone https://github.com/ocf/ocfweb # clone the repository
cd ocfweb # change directory into the repository

... make changes ...

make test # run tests to make sure everything is working
make dev # start a development server and see your changes live
```

### Kubernetes
To access Kubernetes, simply run `kubectl` commands. See the [Kubernetes
documentation][kubernetes-basics] for more information.

Note that staff only have viewing permissions for the cluster. Interested
stafferse can request write access to a development namespace by talking to a
root staffer.

[kubernetes-basics]: https://kubernetes.io/docs/tutorials/kubernetes-basics/
