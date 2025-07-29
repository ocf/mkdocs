---
title: Nix Secrets
---

secrets directory in ocf/nix

## host-keys

ssh public keys

for hosts that we know

`ssh-keyscan hostname | grep ed25519` to see public key of an ocf host from supernova/ocf desktops
- run this cmd after re-installing / newly installing a host.
- then, place pubkey in this dir. `ssh-keyscan hostname | grep -o ssh-ed25519.* > spike.pub`

## master-identities

public keys for all root users (FIDO2 hardware token)
private keys are on the yubikeys themselves

users who can edit secrets

### adding new master identities

need assistance from an existing root user (that has a master identity on the repo)

make sure you have FIDO2 pin set up for yubikey [insert link here]

to add a new master identity for a root user,

clone nix repo on a nix host, create new branch, nix develop

`age-plugin-fido2-hmac -g > secrets/master-identities/rootuser-ocf-nix-primary.pub`

enter FIDO2 pin, touch token

```
[*] Please insert your token now...
Please enter your PIN: [*] Please touch your token...
[*] Do you want to require a PIN for decryption? [y/n]: y
[*] Please touch your token
[*] Are you fine with having a separate identity (better privacy)? [y/n]: y
```

git add the new file. commit and push if existing root user is not there with you IRL!

existing root user:

run `agenix update-masterkeys`

plug in hardware token, touch token and enter PIN to re-key each secret
(annoying limitation of hardware tokens lol)

git add updated files that are under `master-keyed`. commit and push!

## master-keyed

all secrets, but rekeyed (encrypted) with all master identities!!
any secret here can be decrypted with one master identity

agenix does secret management, with extension agenix-rekey bc we have many
hosts and many users

## rekeyed

to rekey a secret, you decrypt the secret with the master identity hardware token, re-encrypt it with host public key, then store that rekeyed secret under `rekeyed` in the host directory.

only secrets which that hosts needs are rekeyed. these are defined in the host's nix config.

## agenix

agenix looks at master-identities dir 

\*-tsgi-secret.age allows host to make changes to DNS (allowing us to have SSL on it!)

## adding/editing a secret

in nix repo, after `nix develop`,

run `agenix edit ./secrets/master-keyed/secret-name.age`
if secret doesnt already exist, a new one is created.

this decrypts the secret (with your hardware token), opens a text editor with the secret. after saving and closing, agenix will re-encrypt with all master identities and store it in `master-keyed`.

once you've added a secret, run `agenix rekey`. This goes through the config of each host, sees if there have been changes to any secrets that this host uses... if there are, you are prompted to decrypt the .age secret with your master identity, then encrypt with the hosts public key.

need ssh priv key of host to decrypt secret on that host
