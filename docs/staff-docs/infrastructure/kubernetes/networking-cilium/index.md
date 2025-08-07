# Networking (Cilium)

[Cilium](https://cilium.io) is an [eBPF](https://ebpf.io)-based [Container Network Interface](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) (CNI) plugin for Kubernetes. On its own, Kubernetes doesn't know how to route traffic between pods. Cilium is the component that does all the routing. Being largely based on eBPF, Cilium is extremely fast and has good observability capabilities.

## Deployment

The OCF deployment of Cilium is [configured to replace](https://docs.cilium.io/en/stable/gettingstarted/kubeproxy-free/) the default `kube-proxy` component with Cilium's implementation. We also use the [Cilium ingress provider](https://docs.cilium.io/en/stable/gettingstarted/servicemesh/ingress/#gs-ingress) wherever possible (although there's no harm in deploying other ingress controllers if needed). The full configuration is available at [ocf/kubernetes/apps/cilium.py](https://github.com/ocf/kubernetes/blob/main/apps/cilium.py).

## Future Work

There's a lot we can do to optimize Cilium's performance. So far, not a lot of it has been done, since everything is more than fast enough for the OCF's needs. If this changes, there's probably a decent amount of free performance to be had by evaluating the [Cilium tuning guide](https://docs.cilium.io/en/v1.12/operations/performance/tuning/#xdp-acceleration) and deciding to use some of those optimizations.