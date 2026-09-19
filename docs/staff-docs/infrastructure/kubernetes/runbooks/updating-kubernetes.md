# Updating Kubernetes

It is *generally* safe to update the cluster many minor versions at once, but you should make sure all the software in the cluster is up to date first. Kubernetes minor versions usually have breaking changes, some of which much be addressed prior to upgrade. Make sure to read the "urgent upgrade notes" in the changelog of every minor version in your upgrade path.

Read the Kubernetes docs for [kubeadm upgrade](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/) and [version skew policy](https://kubernetes.io/releases/version-skew-policy/) before upgrading, and if you encounter any issues. The following is a rough series of steps that should accomplish a version upgrade in line with the two documents.

1. Update the git ref in the ocf/nix Kubernetes module to point to the new version.
    - Build once with an empty hash to get the correct hash before you commit.
2. SSH into a control plane node and use kubeadm to upgrade the cluster.
    - You'll likely need to use a nix shell to get a newer kubeadm version without also updating the kubelet.
    - For example: `nix shell github:NixOS/nixpkgs/nixos-unstable#kubernetes`.
    - Run `kubeadm upgrade plan [version]` to ensure you can upgrade to the intended version.
    - Once this looks good, run `kubeadm upgrade apply [version]`.
3. Repeat for the other control plane nodes, but with `kubeadm upgrade node` instead.
4. Get kubectl access via SSH to a node you *aren't* upgrading.
5. Upgrade kubelet on a control plane node.
    - Drain the node with `kubectl drain cytosine --ignore-daemonsets --delete-emptydir-data`/
    - FIXME: If pod eviction budgets are poorly configured, you may need to add `--disable-eviction`.
    - Deploy to the node with `colmena apply boot` (NOT switch).
    - Reboot the node.
    - Make sure all systemd services (especially cri-o and kubelet) are running.
6. Uncordon the node and repeat for the other control plane nodes.
7. Repeat the steps 3-6 for worker nodes.
8. If all nodes are Ready and report the new version, you're all done.
