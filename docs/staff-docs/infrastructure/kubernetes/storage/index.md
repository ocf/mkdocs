# Storage (Ceph)

[Ceph](https://ceph.io/en/) is a distributed storage platform built to allow massive storage volumes with very high reliability. Ceph internals are outside the scope of OCF documentation. A good video introduction to the basic mental model behind Ceph can be found [here](https://www.youtube.com/watch?v=7I9uxoEhUdY).

## Deployment

At the OCF, Ceph is deployed via [Rook](https://rook.io) on Kubernetes. Rook is a [Ceph Orchestrator](https://docs.ceph.com/en/quincy/mgr/orchestrator/), which means that it deploys and monitors all the different Ceph components. You can find our configuration for Rook at [ocf/kubernetes/apps/rook.py](https://github.com/ocf/kubernetes/blob/main/apps/rook.py).

## Usage

Ceph is currently configured to provide three types of storage: [block storage](https://docs.ocf.berkeley.edu/doc/block-storage-rbd-EucTOnsYgo), [object storage](https://docs.ocf.berkeley.edu/doc/object-ocean-o3-wXmmY5Vgko), and [filesystems](https://docs.ocf.berkeley.edu/doc/filesystems-cephfs-mt7KdqJEqU). Click the links for a guide to using each of them, and explanations on when you should use each one.