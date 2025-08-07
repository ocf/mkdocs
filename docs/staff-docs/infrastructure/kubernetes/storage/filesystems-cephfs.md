# Filesystems (CephFS)

[CephFS](https://docs.ceph.com/en/quincy/cephfs/index.html) is the filesystem abstraction provided by Ceph. A CephFS volume can be simultaneously mounted by any arbitrary number of Linux machines. We will likely need to do something like this to store user homes in Ceph. Right now, they can only be used in `ReadWriteOnce` or `ReadWriteMany` volumes in Kubernetes.

## Storage Pools

There are two pools, a fast pool (`cephfs-nvme`) and a slow pool (`cephfs-hdd`), which replicate across 3 hosts on NVMes and HDDs respectively. Both pools store metadata (filenames, sizes, directory structure) on NVMes so that operations like `stat` and `ls` are fast no matter which pool you pick.

## Usage

Create a `PersistentVolumeClaim` (PVC) with `storageClass` set to `cephfs-{nvme, hdd}`.

```python
{
    "apiVersion": "v1",
    "kind": "PersistentVolumeClaim",
    "metadata": {
        "name": "ocfdocs-example",
    },
    "spec": {
        "accessModes": ["ReadWriteMany"],
        "resources": {"requests": {"storage": "8Gi"}},
        "storageClassName": "cephfs-hdd",
    },
}
```

## Performance Tuning

We have not tried to optimize CephFS for performance. There is likely a lot of headroom to tweak things.

## Data Durability

All Persistent Volumes are backed up to the OCF backup server unless they have the label `velero.io/exclude-from-backup: true`. These backups are then periodically replicated offsite in Fremont, CA. For more details on the backup strategy, see [Backups (Velero)](/doc/backups-velero-xVMmUZgO2s).