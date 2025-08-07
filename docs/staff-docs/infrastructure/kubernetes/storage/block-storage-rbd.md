# Block Storage (RBD)

[Rados Block Devices](https://docs.ceph.com/en/quincy/rbd/index.html) (RBD) are the [block device](https://en.wikipedia.org/wiki/Device_file#BLOCKDEV) abstraction provided by Ceph. They can be mounted by any arbitrary Linux machine, but we have not built infrastructure to do this. Instead, we use them exclusively for performant `ReadWriteOnce` volumes in Kubernetes.

## Storage Pools

There is currently only one RBD pool called `rbd-nvme`. It stores all its data on NVMe drives replicated across 3 unique hosts. It is our highest performance storage class, and is suitable for databases and other latency and throughput sensitive workloads.

## Usage

Create a `PersistentVolumeClaim` (PVC) with `storageClass` set to `rbd-nvme`.

```python
{
    "apiVersion": "v1",
    "kind": "PersistentVolumeClaim",
    "metadata": {
        "name": "ocfdocs-example",
    },
    "spec": {
        "accessModes": ["ReadWriteOnce"],
        "resources": {"requests": {"storage": "8Gi"}},
        "storageClassName": "rbd-nvme",
    },
}
```

## Performance Tuning

If you're using `rbd-nvme` you probably want to go fast. For databases, make sure the block size of the volume matches the page size the database uses (e.x. PostgreSQL defaults to 8K). You may also want to increase the page size of the database (16K is a good value to start at).

## Data Durability

All Persistent Volumes are backed up to the OCF backup server unless they have the label `velero.io/exclude-from-backup: true`. These backups are then periodically replicated offsite in Fremont, CA. For more details on the backup strategy, see [Backups (Velero)](/doc/backups-velero-xVMmUZgO2s).