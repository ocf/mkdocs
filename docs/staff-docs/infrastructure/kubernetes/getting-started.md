---
title: Getting Started
---

This is a guide on getting set up with the OCF's Kubernetes cluster. It will be updated as we develop a staging environment and more accessible workflows for staff.

## Accessing the Cluster:
1. Connect to an OCF machine (desktop or login server)
2. Run `kubectl auth whoami`
3. :D

By default this targets the staging cluster, but you can pass `--context=dna` to target production if you have access.

(Currently only ocfroot can interact with the cluster, but we're working on a staging environment)

If your command hangs, you likely need a Kerberos ticket (i.e. run `kinit`). Alternatively, you could copy the contents of the `$KUBECONFIG` file to your `~/.kube/config` and add the `--no-browser` flag. If you want to connect from your own device, just copy our configuration and it should work as is. For more information on configuring auth, please see the [kubelogin documentation](https://github.com/int128/kubelogin/).

## kubectl

`kubectl` is the primary tool for a user to call the Kubernetes API. It is fairly extensive, but here are some basic commands that may be useful:

- `kubectl get nodes` - List all nodes in the cluster, useful to see if any nodes are NotReady or SchedulingDisabled (cordoned).
- `kubectl get ns` - List namespaces. Almost all resources should be in a namespace, which needs to be specified with `-n [namespace]` when appropriate.
- `kubectl get [resource]` - List all of the given resource in a namespace. Some common resource types are `deploy`, `pod`, `svc`, `ing`, `cm`.
- `kubectl api-resources` - List all resource types. This will be very overwhelming due to the number of CRDs, and probably not helpful.
- `kubectl get [resource]/[name]` - Get information on the named resource. Specify output type with `-o`, such as `-o yaml` for the object's manifest.
- `kubectl describe [resource]/[name]` - Get details on the current state of the named resource.
- `kubectl logs [pod|deployment]/[name]` - Get logs for the container running in a pod. You can specify a container with `-c` and follow the logs with `-f`.

There are a lot of other commands and flags, which you can learn about in [the docs](https://kubernetes.io/docs/reference/kubectl/). Some useful flags are `-A` to list all namespaces, and `--watch` to watch for changes in output. Flux should manage almost all resources during normal cluster operation, so directly mutating state with `kubectl` should be reserved for when it is absolutely needed for debugging purposes.

## k9s

If you'd prefer a tui wrapper with `vim`-like keybinds, `k9s` is installed on our machines:

- `:q` to quit.
- `:ns` to view available [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).
- Scroll with `j` and `k` down to the `ocfweb` namespace (you can also scroll with your mouse). Press enter.
- You are now viewing the pods for `ocfweb`; press enter on one to see its containers. Press `esc` (maybe twice) to go back to the previous page.
- Press `l` to see the logs for that pod. Use `j` and `k` to scroll through them.
- Press `d` on the pod to get additional information about it.
- See more keybinds: [k9scli.io/topics/commands](https://k9scli.io/topics/commands/).
