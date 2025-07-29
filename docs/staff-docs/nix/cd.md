---
title: Deploy
---

TODO: make this fancy with generators (see https://github.com/oddlama/agenix-rekey), privkey goes into secrets dir, pubkey automatically generated and placed on host by nix.

we need the runner(s) to have permission to place files & make changes on the host which will run the service!

## if SSH is necessary for deploy:

### client (workflow) to server (amethyst)

1. generate SSH keypair

```
[jaysa@shadow:~]$ ssh-keygen
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/j/ja/jaysa/.ssh/id_ed25519): ./bestdocs-deploy-key
Enter passphrase for "./bestdocs-deploy-key" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in ./bestdocs-deploy-key
Your public key has been saved in ./bestdocs-deploy-key.pub
The key fingerprint is:
SHA256:6k8WOSLlFO+gyQcYaAZlhcZ0LaMmLY086A8bim+uZ28 jaysa@shadow
The key's randomart image is:
+--[ED25519 256]--+
|o==oo..          |
|.+++o .o         |
|==...o+ .        |
|=o=. B o .       |
|.+. = + S        |
| +   o o o       |
|o =   . o        |
|o.+.E. o         |
|.Boo. ...        |
+----[SHA256]-----+
```

2. upload SSH_PRIV_KEY of workflow to github
- repo -> settings -> security: secrets and variables -> actions -> new repository secret
- Name: bestdocs_deploy_privkey
- Secret: output of `cat bestdocs-deploy-key`

3. upload SSH_PUBLIC_KEY of workflow to host
- in /nix/hosts/.../hostname.nix:
```
  users.users = {
    "deploy-bestdocs" = {
      group = "nginx";
      openssh.authorizedKeys.keys = [
        "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPFUy5jvotIFajdAbwnqYAcMZMlwAxTZ3wPq44fmZ4v2"
      ];
    };
  };
```

### server (amethyst) to client (workflow)

1. setup ssh keys in project's github workflow file
1. get host pubkey by running `ssh-keyscan amethyst.ocf.berkeley.edu | grep ssh-ed25519`

`amethyst.ocf.berkeley.edu ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIlmVSSUC4PTOzfMvsHbUVr1e+7GLXvIPx1tX+W3CIU1`

1. paste this into the github workflow file of the project

```
steps:

      ...

      - name: Setup SSH keys
        run: |
          mkdir -p ~/.ssh
          echo '${{ secrets.BESTDOCS_DEPLOY_PRIVKEY }}' > ~/.ssh/id_ed25519
          chmod 400 ~/.ssh/id_ed25519
          echo "amethyst.ocf.berkeley.edu ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIlmVSSUC4PTOzfMvsHbUVr1e+7GLXvIPx1tX+W3CIU1"
```

- if public key of amethyst ever changes, must also change it here

## deploy dependencies

1. in project's flake.nix, add new devShell with necessary packages for build/deploy 
   - `mkdocs/flake.nix` for example, only needs rsync on the github actions runner!

5. in project's repo, write deploy step in build.yml workflow file. make sure to use the devShell in its commands! 
   - if it fails, check github actions and keep debugging...

## finale
5. check github actions tab of project repo and hopefully it all works!
