---
title: Kubernetes Engine (OKE)
---

[Kubernetes](https://kubernetes.io) (abbreviated k8s) is a container orchestration system originally developed by Google. It provides an interface for running software that abstracts away the fact that the software runs on multiple machines. It also allows you do this completely declaratively, which means that instead of describing a list of actions to it (like a computer program), you instead tell it what you want the end goal to be (e.x. there should always be 3 copies of this software running). We think these properties make it a good level of abstraction to build an application platform on top of.

Our current Kubernetes deployment was originally envisioned by `~njha` and `~fydai`, who were frustrated with the state of the existing Kubernetes cluster (which was on a single machine, and had no benefit over running a container runtime like Podman directly). Over time `~etw` and `~oliverni` joined the project (and `~fydai` graduated). A number of others also briefly helped along the way! Finally in late 2022 - early 2023 we had something we were pretty happy with.

## Tech Stack

* **Container Runtime (CRI)**: [CRI-O](https://cri-o.io)
  * Well-supported and stable for pretty much everything that runs on Kubernetes.
  * Version is tied to Kubernetes version, so we're actually incentivised to keep this up to date.
  * `containerd` has weird bugs in the default installation, so much so that other people still (as of Kube 1.21) run dockershim in production (update 2022: containerd + rook is broken on NixOS)
* **Container Networking (CNI)**: [Cilium](https://docs.ocf.berkeley.edu/doc/networking-cilium-DgA0LO5klN)
  * This is responsible for the underlying transport between all containers, and between containers and the internet.
  * Cilium is the most advanced CNI plugin available as of now. (eBPF, HTTP Filtering, etc)
* **Cluster DNS**: [CoreDNS](https://coredns.io/)
  * This provides DNS that understands Kubernetes, allowing you to do things like `GET http://pod-a.namespace` from other pods.
* **LoadBalancer**: [MetalLB](https://metallb.universe.tf/)
  * A LoadBalancer allows Kubernetes services to directly bind themselves to Public IPs.
  * See the [IP Address Allocation sheet](https://docs.google.com/spreadsheets/d/1S3BbwsuRKAT_rwEl1BSJBVns6OVDLq3D7ez843Q2GEY/edit?usp=drive_web&ouid=115545330206286749428) to see what IPs we have allocated for cluster use.
  * MetalLB is one of two LoadBalancer solutions (the other being kube-vip, which we use for HA control plane) for bare metal, and it's worked without any hassle so far.
* **Ingress**: [Cilium](https://docs.ocf.berkeley.edu/doc/networking-cilium-DgA0LO5klN)
  * An Ingress allows assigning domains to Services, and routes traffic sent to those domains to the appropriate pods.
  * We originally considered Traefik, but Traefik is very difficult to debug. After breaking Traefik for the third time, we gave up and went with Contour. Then we took so long to build up the cluster that Cilium launched an Ingress controller. It was very broken so njha made some PRs and now it works okay.
* **TLS Certificates**: [cert-manager](https://cert-manager.io/)
  * Just an ACME client for Let's Encrypt.
  * It retrieves and constantly updates the TLS certificates that the Ingress needs.
* **Storage**: [Ceph](https://docs.ocf.berkeley.edu/doc/storage-ceph-VFJNU8C3Q2)
  * Rook runs a Ceph cluster inside Kubernetes. Right now it has OSDs on `jaws` and `lockdown`.
  * Rook also provides PersistentVolumeClaims to Kubernetes, so Pods can store things.
  * There are also plans to expose an S3-compatible API to consume by e.x. Argo Workflows to store outputs of CI runs, or Mastodon to store images, etc.
* **Secrets**: [Vault](https://www.vaultproject.io/), [vault-secrets-operator](https://github.com/ricoberger/vault-secrets-operator)
  * Vault stores secrets (hopefully securely) in a key-value store.
  * vault-secrets-operator listens for VaultSecret objects, which sync the data inside Vault into regular Kubernetes secrets. The content of these secrets can then be used inside ConfigMaps, or templated into files to be used inside pods.
* **CI**: TODO
* **CD**: [Argo CD](https://argoproj.github.io/argo-cd/)
  * This is a tool that keeps the state of the cluster up to date with the current state of git.
  * Everything should be deployed via ArgoCD, see the Usage section for more information.
* **Backups**: TODO

## Old Kubernetes

There was an old deployment of Kubernetes before the current one. It suffered from a number of problems that resulted in us deciding to scrap it and start over rather than try and fix it.

* Deployed through Puppet w/o good upgrade story
* Deployed on a single physical machine, with 3 VMs as control-plane nodes
* Secret management via hostPath puppet shares (requires `puppet-trigger` on all workers to update secrets)
* Git-ops via Jenkins and `ocf-kubernetes-deploy` (Shopify krane)
* No support for Service type = LoadBalancer (based on the erroneous belief that MetalLB requires additional network configuration)
* Older, less performant choice of container networking
* Storage via NFS on a single server instead of distributed via Ceph
* No centralized metrics/logs, no support for otel tracing, nothing is instrumented
* Using Docker as the container runtime
* Control plane not highly available (all traffic goes to a single control plane node)
