# Updating Kubernetes

These are some rough notes I'm (`njha`) typing as I update the cluster from 1.25 → 1.28. It is *generally* safe to update the cluster many major versions at once, but you should make sure all the software in the cluster is up to date first. Kubernetes says you should go one major version at a time, so you should read the release notes and think about what could go wrong before you update too far in one go.

* Push the change to the Nix repository
* edit kube-system cm/kubeadm-config to include the new version (e.x. 1.28.4)
* for each node
  * get kubectl access without teleport, either via emergency SSH on a **different** node, or a temporary credential
    * use this access to drain a node
  * nixos-rebuild boot
  * reboot
  * make sure kubelet came back up (`systemctl status kubelet`)
    * for this update, an option was deprecated (it became the default option) so I just removed it and kubelet started up
  * in root shell, `kubeadm upgrade node`
* That should be it! Ensure all nodes are Ready (for 1.28 there were no issues).