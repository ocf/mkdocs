---
title: Getting Started
---

OCF's kubernetes setup can be intimidating to newcomers, but it's important to learn because a good amount of our infra is on there!

OCF ArgoCD URL: [https://argo.ocf.io](https://argo.ocf.io)

## Accessing the k8s cluster:

1. SSH into the [staff login server (koi)](../../nix-hosts/login-servers/)
2. Run `tsh login --proxy tele.ocf.io:443 --bind-addr=127.0.0.1:4242 --browser=none --auth=ocfauth tele.ocf.io` on koi.
3. Then, run `ssh -L 4242:localhost:4242 -N koi` on your local host that can open a browser.
4. Open the URL which tsh login had outputted on `koi` in your local browser, which should log you into Teleport. You can now close the ssh tunnel on local host.
3. Now, back on koi from now on: `export KUBECONFIG=${HOME?}/teleport-kubeconfig.yaml`
4. `tsh kube login dna.ocf.io`
5. If running `kubectl get pods` shows `No resources found in default namespace.`, you're good to go!

There is a web dashboard available at [tele.ocf.io](https://tele.ocf.io) that also contains similar instructions. Be sure to use OCF OIDC to log in (at the bottom of the options).

## k9s

You can continue using kubectl to interact with the cluster, but k9s is also a nice tui option. Run `k9s` to open it.

`k9s` has vim-like keybinds:

- `:q` to quit
- `:ns` to view available [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
- scroll with `j` and `k` down to the `ocfweb` namespace (you can also scroll with your mouse). Press enter.
- You are now viewing the pods for `ocfweb`; press enter on one to see its containers. Press `esc` (maybe twice) to go back to the previous page.
- Press `l` to see the logs for that pod. Use `j` and `k` to scroll through them.
- Press `d` on the pod to get additional information about it.
- see more keybinds: [k9scli.io/topics/commands](https://k9scli.io/topics/commands/)

If you kill a pod, argocd **should** recreate it according to the cluster state defined in [ocf/kubernetes](https://github.com/ocf/kubernetes). Don't go around restarting or deleting pods unless you have time to fix them, in case it isn't restarted properly!!
