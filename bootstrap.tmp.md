# bootstrap yay yippee

do the new nix host funny things yay

if ur starting from scratch kubelet will probably fail bc u need to:
```
kubeadm init --config /etc/kubernetes/kubeadm.yaml
```

make sure to add the apiserver ip to the host manually at first, until kubevip is working!

or for adding a new node:
```
# control-plane
kubeadm init phase upload-certs --upload-certs
kubeadm token create --print-join-command --certificate-key [key from upload-certs]

# worker
kubeadm token create --print-join-command
```

Run the printed command on the node that you're adding.

# Setup Git Repo

Make sure to make adjustments to the flux repo to accomodate for a new cluster if necessary.

# Get container networking working

You'll need to install cilium through helm. Make sure to get the values from the HelmRelease.

```
kubectl create ns cilium # if it doesn't exist
helm install cilium oci://quay.io/cilium/charts/cilium -n cilium --values cilium-values.yaml
```

# Bootstrap Flux

You'll need to add the SSH key that it outputs as a deploy key to the ocf/flux repo. Add it with the write access and the name `temp` initially. After the bootstrap finishes, delete it and add it back read-only with the name `flux [cluster] deploy key`.

```
flux bootstrap git \
    --url=ssh://git@github.com/ocf/flux.git \
    --branch=main \
    --path=./bootstrap/[cluster] \
    --components-extra=image-reflector-controller,image-automation-controller
```

Flux should magically handle everything here as long as you've set up the repo correctly.
