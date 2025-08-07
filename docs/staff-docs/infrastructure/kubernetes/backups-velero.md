# Backups (Velero)

All the Kubernetes objects and persistent volumes in the cluster are backed up using [Velero](https://velero.io). To do this, we use [Velero's CSI Snapshot support](https://velero.io/docs/main/csi/) along with the [Snapshot Controller](https://github.com/kubernetes-csi/external-snapshotter) and [Rook's support for CSI Snapshotting](https://rook.io/docs/rook/latest-release/Storage-Configuration/Ceph-CSI/ceph-csi-snapshot/).

## Backup Design

`hal` runs a very simple `minio` instance which exposes an S3-compatible API. This instance is only intended for use as a backup target. Do not use it for anything else. Velero uses this S3-compatible API as its backup target.

Snapshotting inside the `minio` target directory on hal is turned off. This means that Velero is fully in charge of retention in terms of what is stored on `hal`. Replication to `rsync.net` stores the last two months of backups. Restoring backups end-to-end all the way from `rsync.net` has never been tested(!!), but we have tested backups for other things on `rsync.net` that also come from the backups zfs dataset on hal, so it should work? Untested backups aren't real though, so someone should test this eventually.