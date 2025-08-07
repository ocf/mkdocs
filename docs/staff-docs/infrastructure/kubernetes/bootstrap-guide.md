# Bootstrap Guide

In normal cluster operation, you shouldn't need to re-deploy everything from scratch. However, the bootstrap process might be useful for pedagogical reasons or catastrophic events. This document contains \~njha's notes as they brought up the cluster for the first time, written in the form of a guide.

## Netboot + Install

Boot into any version of the NixOS installer, either via netboot or an install disc. If netboot isn't configured, a [netboot.xyz](https://netboot.xyz) image might help. The easiest way to do this is via Samba + Supermicro IPMI. If you need a quick Samba server, the [impacket library](https://github.com/fortra/impacket/blob/master/examples/smbserver.py) for Python has an SMB server example that appears to work with Supermicro IPMI.

There are 3 steps to installing NixOS. If things have changed, the [NixOS install guide](https://nixos.org/manual/nixos/stable/index.html#sec-installation) may help.


1. Partition and mount
2. Generate hardware configuration
3. Build and reboot

First, you want to partition your disks. You want two partitions: a 512MB EFI boot partition (minimum-- I've been considering 1GB), and an ext4 partition filling the rest of the disk. Kubernetes doesn't support swap anyway, so there's no point making a swap partition. We considered fancier filesystems like btrfs or ZFS as well, but \~etw says there are some performance issues with btrfs (quotas don't scale with large numbers of subvols), so we decided against it. To partition your disks, use a tool like `sgdisk(8)`. Then, format the boot partition as FAT and the ext4 partition as ext4 via `mkfs.fat -F 32 -n boot` and `mkfs.ext4 -L nixos` respectively. Then, mount the root partition to `/mnt` and the boot partition to `/mnt/boot` (`mkdir /mnt/boot` first).

You can now proceed to generating the hardware configuration. To do this, simply run `nixos-generate-config --root /mnt` and grab `/mnt/etc/nixos/hardware-configuration.nix`. Commit this file to `ocf/nix` on GitHub, along with whatever other machine level configuration you need. There are examples of this at that repository. Be sure to also reference your machine's root config in the `flake.nix`. Then, delete all the files in `/mnt/etc/nixos`, and `git clone https://github.com/ocf/nix.git .` while inside `/mnt/etc/nixos`.

Last, you just need to install! Run `nixos-install --flake .#hostname` from `/mnt/etc/nixos`, replacing hostname with the hostname of the machine you're deploying. This should install successfully. You'll be prompted to set a root password, so set the OCF's one at that step. If all went well, reboot! If not, time to debug!

## Configure Teleport

If the cluster is already running, you might want to setup teleport first. Doing this is as easy as creating a teleport auth token in the file `/var/lib/ocfteleport/authtoken` and then restarting the teleport systemd service. You can get the token via: `tctl nodes add --ttl=10m --roles=node`. Put only the token with no other information in the file. A newline is fine.

## Installing Kubernetes

If the cluster is not already running, you'll need to log in as `ocfemergency` to complete initial setup. Then, you can initialize a new cluster.

```bash
kubeadm init --config /etc/kubernetes/kubeadm.yaml
```

If the cluster is already running, you should upload certs and create a token on a control plane machine already in the cluster.

```bash
kubeadm init phase upload-certs --upload-certs # only needed if you're adding a control plane machine
kubeadm token create --print-join-command # needed for control plane and workers
```

To join a worker node, just copy paste the command that `token create --print-join-command` gave you. To join a control plane node, append `--control-plane --certificate-key <key_from_upload-certs>` to that command, and then run it.

If you're joining a node to an existing cluster, you are done! Stop reading this guide.

## Deploy Cilium

> Note: The rest of this guide makes use of `transpire object apply`. This command is not implemented at the time of writing. If it still isn't implemented by the time you're reading this, use `kubectl ns <ns> && transpire object print cilium | kubectl apply -f -`. Do not use `-n` with `kubectl apply` because if the transpire objects are deployed to multiple namespaces this will break. `kubectl ns` comes from a `krew` plugin of the same name. It's just a convenient way of setting the default namespace in your `$KUBECONFIG`.

`transpire object apply cilium`

Make sure there are no failed pods. TODO: I had to manually edit the Cilium Ingress service to be IPv4 and IPv6 and PreferDualStack

## Deploy CoreDNS

Make sure there are no failed pods. Note that coredns deploys to kube-system, because cilium assumes it lives there.

## Validate networking

To validate, start `cilium hubble port-forward` in one terminal, and then run `cilium -n cilium connectivity test` in another. This should fully pass, and if it doesn't then you will get some information from hubble to help you debug.

Note: When we set this up, some http tests failed with 503. IDK if this is an actual issue or not.

## Deploy metallb

Make sure there are no failed pods.

## Deploy cert-manager


:::warning
TODO: We never put the TSIG key in Vault.

:::

Manually deploy the tsig key for now. Later when vault is up you can put it in vault.

TODO: update ingresses in ocfkube to use new tls

## Deploy argocd

There should be no errors, and you should be able to see the argocd dashboard online.

Get the client secret from keycloak, do echo -n "..." | base64 and `k edit secret argocd-secret` and add your base64 value under the key oidc.keycloak.clientSecret. You should now be able to log in from online :sparkles:

## Deploy rook

Make sure there are no failed pods. Run ceph status via the kubectl plugin. Make sure it's health_ok (NOT HEALTH_WARN. WARN IS NOT OK. DO NOT CONTINUE UNTIL HEALTH_OK OR YOU WILL HAVE A BAD TIME.)

## Validate rook

Create a test pvc and make sure it gets bound. If it doesn't, debug.

## Deploy vault

port-forward to vault-0, click through menus, make keys

k port-forward vault-0 8200

create kv v2 store called kvv2

create a policy called vault-secrets-operator

```hcl
path "kvv2/data/*" {
  capabilities = ["read"]
}
```

exec into vault-0 with /bin/sh, run this...


:::warning
You might actually not want to exec into the Vault pod… try giving it the API Server endpoint from outside the Vault pod (dna.ocf.io). That is the right way to do it.

:::

```sh
export VAULT_TOKEN=<root token>
export VAULT_ADDR=http://127.0.0.1:8200

vault auth enable kubernetes

vault write auth/kubernetes/config \
  kubernetes_host=https://${KUBERNETES_PORT_443_TCP_ADDR}:443

export VAULT_SECRETS_OPERATOR_NAMESPACE="vault-secrets-operator"
vault write auth/kubernetes/role/vault-secrets-operator \
  bound_service_account_names="vault-secrets-operator" \
  bound_service_account_namespaces="$VAULT_SECRETS_OPERATOR_NAMESPACE" \
  policies=vault-secrets-operator \
  ttl=24h

exit
```

Don't forget to exec in again and `rm ~/.ash_history` (yes it uses ash...)

Also enable metrics in the top right menu of Vault.

Go to the other vaults, for the raft config, give them the IP address of vault 0 and leave everything else blank

e.x. <http://10.0.1.242:8200>

also unseal them

setup oidc: <https://www.spicyomelet.com/sso-with-keycloak-and-hashicorp-vault/>
<https://ocf.berkeley.edu/gh/terraform> there's a branch, just terraform apply this lol

## Deploy vault-secrets-operator

As usual, should just work.

## Deploy teleport

Deploy the helm chart, go around to nodes and give them a token