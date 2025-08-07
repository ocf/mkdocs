# Object Ocean (O3)

OCF Object Ocean is an object storage system built on top of [Ceph Object Gateway](https://docs.ceph.com/en/quincy/radosgw/index.html) (RADOSGW). It's fully compatible with AWS Simple Storage Service (S3).

## Storage Pools

There is currently only one O3 pool called `rbd-nvme`. It stores all its data on HDDs replicated across 3 unique hosts, and stores its metadata on NVMe drives replicated across 3 unique hosts. It is intended for batch storage of large files and media.

## Usage


:::warning
We currently don't have a good usage story worked out. The one user of this is docs.ocf (probably where you're reading this now) and the bucket and account for it were manually created via the Ceph Dashboard.

:::

Once you've generated an account via the Ceph Dashboard, you can configure AWS CLI to point to OCF Object Ocean as follows…

```bash
$ aws configure --profile=ceph
AWS Access Key ID [None]: exAMpLe
AWS Secret Access Key [None]: BlaBlaBla
Default region name [None]:
Default output format [None]: json

$ aws --profile=ceph --endpoint=https://o3.ocf.io/ s3 ls
bucket1
bucket2
```

## Multitenancy

Ceph Object Gateway [supports multitenancy](https://docs.ceph.com/en/quincy/radosgw/multitenancy/), so we can issue accounts that are restricted to one tenant with a certain storage space restriction. It is therefore possible to offer O3 access to OCF end users at some point in the future.

## Data Durability

There is no backup policy in place for Object Ocean. Although the three replicas will likely protect against drive failures, more catastrophic events *will* result in data loss. You should come up with a replication plan if you're storing critical data in Object Ocean.