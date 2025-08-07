# Secrets (Vault)

[Hashicorp Vault](https://www.vaultproject.io) is a secret-management tool. It's built around a collection of loosely coupled "secret engines" that store or manage secrets, "authentication engines" that allow clients to authenticate to these engines, and roles that provide authorization. At the OCF, it runs on top of Kubernetes.

## Usage

### Web Interface

If you have root, you can access the web interface at [https://vault.ocf.berkeley.edu/](https://vault.ocf.berkeley.edu/ui/vault/auth?with=oidc%2F). The web interface should NOT be used for configuration (see the configuration section below) -- only for manual modification / viewing of secrets.

### Vault Secrets Operator

[Vault Secrets Operator](https://github.com/ricoberger/vault-secrets-operator) (VSO) is one recommended way to consume secrets from Kubernetes. It will allow you to create a regular Kubernetes `V1Secret` from the contents of Vault. This secret can then be used to create environment variables or files in a `Pod`.

OCF's convention is to put the contents of the `V1Secret` in Vault at the path  `kvv2/{k8s_namespace}/{k8s_secret_name}`. Then, create a `VaultSecret` object, which will create the `Secret` object based on that path. For example…

```python
{ # You typically do NOT want to use this example, see later for a better one.
    "apiVersion": "ricoberger.de/v1alpha1",
    "kind": "VaultSecret",
    "metadata": {"name": name},
    "spec": {
        "keys": keys,
        "path": f"kvv2/{namespace}/{name}",
        "type": "Opaque",
    },
}
```

The easier way to do this is to create a `V1Secret`, and let [transpire](/doc/configuration-transpire-uJ5GHrW9cg) automatically transform it into a `VaultSecret`. If the secret can be automatically generated (i.e. it's a random string) you can write some Python to generate it, and then push the generated secret to Vault with `transpire secret push <module>`.

```python
from transpire.resources import Secret
from secrets import token_urlsafe

def objects():
  # push me with `transpire secret push`
  yield Secret(
    name="docs-example",
    string_data={"password": token_urlsafe(24)},
  ).build()
```

We designed secrets this way to ensure that Helm charts that properly generate random secrets do not require additional configuration.

### Vault Sidecar Injector

Vault Sidecar Injector is another way to consume secrets from [Kubernetes](). To use it, simply annotate a `Pod` (probably via the `template` field on a `Deployment` or `StatefulSet`) describing the path in Vault to put the secret from, and how to expose the secret to the container (probably a file path).

The annotations to use are [documented on the Hashicorp website](https://developer.hashicorp.com/vault/docs/platform/k8s/injector), and are not reproduced here. Note that the service annotation is always required when using the sidecar injector at the OCF, otherwise it will default to `localhost`. It's possible this default can be changed, so you might want to take a minute and do that if you're using the injector for a new service.

```python
{ "vault.hashicorp.com/service": "https://vault.ocf.berkeley.edu/" }
```

### Outside of Kubernetes

Vault may have an engine that specifically supports your use-case (e.x. databases). If this is the case, configure Vault via OCF Terraform to support your use case. Instructions are provided in the [Vault documentation](https://developer.hashicorp.com/vault).

Generic secret provisioning to non-Kubernetes infrastructure is currently out of scope, and is explicitly not recommended for anything that sits underneath Kubernetes because it will create dependency loops. For example, [NixOS](/doc/nixos-linux-systems-Mh8Ugu5kdY) should use a different secret management solution.

## Configuration

As mentioned earlier, the only thing you should be doing from the Vault web interface is managing secrets. To configure Vault itself, you should write Terraform.