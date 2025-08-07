# Writing .transpire.py

\[under construction, especially later sections\]

# Write .transpire.py: 

`.transpire.py` tells the CD/CI processes about your deployment: network settings, image location, ingress, and others. You should add `.transpire.py` to your repo's root.

Use this base model:

```python
from pathlib import Path

from transpire.resources import Deployment, Ingress, Service
from transpire.types import Image
from transpire.utils import get_image_tag


def objects():
    dep = Deployment(
        name="app",
        image=get_image_tag("app"),
        ports=[15000],
    )

    svc = Service(
        name="app",
        selector=dep.get_selector(),
        port_on_pod=15000,
        port_on_svc=80,
    )
 
    ing = Ingress.from_svc(
        svc=svc,
        host="app.ocf.berkeley.edu",
        path_prefix="/",
    )

    sec = Secret(
        name="app",
        string_data={
            "OUTLINE_API_KEY": "",
        },
    )
    
    yield dep.build()
    yield svc.build()
    yield ing.build()


def images():
    yield Image(name="app", path=Path("/"), registry="ghcr")
```

## 1. Build your image

We first dive into `images()`

```python
def images():
    yield Image(name="app", path=Path("/"), registry="ghcr")
```

You can also yield several different images for each component of your application.

> How does it work?
>
> \
> The `Image()` object tells one of the two deployment stages: `module-ci.yml` in `ocf/transpire` to build the image/s. `path` is the base directory in which the image should be build, and `registry` should be either "harbor" or "ghcr". As of Feb 2025, we started using GHCR as our main container registry. (Storce: a bit confused about `target`, will look into it).

## 2. Writing deployment

(Storce: I haven't looked into all the arguments and details in objects(), will do so in the near future. For simple applications, just copy the above structure. Should be pretty intuitive)

> How does it work?
>
>  
>
> The `objects()` object is used by `cluster-ci.yml`, the second phase in our deployment. It builds k8s deployment configuration files from `objects()` and update `ocf/cluster`

By now, if everything is working correctly, you should be able to see your application's configuration at `ocf/cluster` and you image at GHCR (go to github.com/ocf, and click on `packages` to verify this!)

If your run is failing, be sure to look at the CI logs and debug from there.

### 2.1 Secrets

One tricky part is secret management. We manage secrets at [vault.ocf.berkeley.edu](https://vault.ocf.berkeley.edu).

In order to push secrets to Vault, you can either run `transpire secret push [app]` or go to [vault.ocf.berkeley.edu](https://vault.ocf.berkeley.edu) and add secret through dashboard GUI. **This step requires root access!**

Also make sure your `objects()` is yielding `Secret()`. YOU SHOULD NOT WRITE YOUR SECRETS HERE! Just leave an empty string.

```python
sec = Secret(
        name=secret_name,
        string_data={
            "some-secret": "",
        },
    )
    
 yield sec.build()
```

Secrets can be exposed to your app in two different ways, as environment variables or a volume mount.


To add the secrets as environment variables, you want to use the `with_secret_env()` function on your deployment.

```python
deployment.pod_spec().with_secret_env(secret_name)

yield deployment.build()
```

This will add each value within the secret to the environment, with the keys and values reflecting those in Vault.


Adding the secrets as a volume mount is slightly more complicated. You want to add entries to the deployment's `volumes` and the appropriate container's `volume_mounts` similar to below (replacing `secret_name` with the name you chose for the secret, and `/path/to/secret_name` with the path you with to mount the volume.

```python
dep.obj.spec.template.spec.volumes = [
    {"name": secret_name, "secret": {"secretName": secret_name}},
]

dep.obj.spec.template.spec.containers[0].volume_mounts = [
    {"name": secret_name, "mountPath": "/path/to/secret_name"},
]
```

This will mount a volume at `/path/to/secret_name`. This will contain a file for each value, with the filename set to the key, and the contents set to the value of the secret in Vault. Note: for binary files, you will need to base64 encode them before storing them in Vault, and then decode the mounted file.


### 2.2 Volumes

(needs fact-checking) Transpire supports all of the types of volumes as described in this article: <https://kubernetes.io/docs/concepts/storage/volumes/#volume-types>. Transpire expects these as Python dictionaries, but the form should be roughly the same as the examples shown in the article.


Some examples:

```python
dep.obj.spec.template.spec.volumes = [
    {"name": "example-emptydir", "emptyDir": {}},
    {"name": "example-secrets", "secret": {"secretName": secret_name}},
    {"name": "example-nfs", "nfs": {"path": "/nfs/exported/path", "server": nfs_server_url"}},
]

dep.obj.spec.template.spec.containers[0].volume_mounts = [
    {"name": "example-emptydir", "mountPath": "/path/to/example-emptydir"},
    {"name": "example-secrets", "mountPath": "/path/to/example-secrets"},
    {"name": "example-nfs", "mountPath": "/path/to/example-nfs"},
]
```


### 2.3 Environment(?)

some examples:

```python
dep.obj.spec.template.spec.containers[0].env = [
    {"name": "PUPPET_CERT_DIR", "value": "/etc/ocfweb"},
    {"name": "OCFWEB_TESTING", "value": "0"},
  {"name": "OCFWEB_PROD_VERSION", "value": get_revision()},
]

deploy_outline.pod_spec().with_configmap_env(name).with_secret_env(name)

# Configuration details for outline-- notice how these are injected
# as environment variables into the Deployment!
yield {
    "apiVersion": "v1",
    "kind": "ConfigMap",
    "metadata": {"name": name},
    "data": {
        "AWS_REGION": "rgw-hdd",
        "AWS_S3_ACL": "private",
        "AWS_S3_FORCE_PATH_STYLE": "true",
        "AWS_S3_UPLOAD_BUCKET_NAME": "ocf-outline",
        "AWS_S3_UPLOAD_BUCKET_URL": "https://o3.ocf.io",
        "AWS_S3_UPLOAD_MAX_SIZE": "26214400",
        "DEFAULT_LANGUAGE": "en_US",
        "ENABLE_UPDATES": "true",
        "FORCE_HTTPS": "true",
        "PGSSLMODE": "require",
        "PORT": "8080",
        "SLACK_MESSAGE_ACTIONS": "true",
        "URL": "https://docs.ocf.berkeley.edu",
        "OIDC_CLIENT_ID": "outline",
        "OIDC_AUTH_URI": "https://idm.ocf.berkeley.edu/realms/ocf/protocol/openid-connect/auth",
        "OIDC_TOKEN_URI": "https://idm.ocf.berkeley.edu/realms/ocf/protocol/openid-connect/token",
        "OIDC_USERINFO_URI": "https://idm.ocf.berkeley.edu/realms/ocf/protocol/openid-connect/userinfo",
        "OIDC_DISPLAY_NAME": "OCF",
    },
}
```


### 2.4 Ingress

some examples:

```python
svc_web = Service(
    name="ocfweb",
    selector=dep_web.get_selector(),
    port_on_pod=8000,
    port_on_svc=80,
)
yield svc_web.build()

ing_web = Ingress.from_svc(
    svc=svc_web,
    host="www.ocf.berkeley.edu",
    path_prefix="/",
)
ing_web.obj.metadata.annotations[
    "ingress.kubernetes.io/force-ssl-redirect"
] = "false"
yield ing_web.build()
```

### 2.5 Liveness / Readiness Probes(?)

some examples:

```python
# ocfweb (http)
dep.obj.spec.template.spec.containers[0].readiness_probe = {
    "httpGet": {
        "path": path,
        "port": 8000,
        "httpHeaders": [{"name": "Host", "value": "www.ocf.berkeley.edu"}],
    },
    "initialDelaySeconds": 5,
    "periodSeconds": 5,
}

dep.obj.spec.template.spec.containers[0].liveness_probe = {
    "httpGet": {
        "path": path,
        "port": 8000,
        "httpHeaders": [{"name": "Host", "value": "www.ocf.berkeley.edu"}],
    },
    "initialDelaySeconds": 10,
    "timeoutSeconds": 3,
    "failureThreshold": 6,
}

# create (exec)
dep.obj.spec.template.spec.containers[0].readiness_probe = {
    "exec": {
        "command": ["python", "-m", "create.healthcheck"],
    },
    "initialDelaySeconds": 15,
    "periodSeconds": 15,
}

dep.obj.spec.template.spec.containers[0].liveness_probe = {
    "exec": {
        "command": ["python", "-m", "create.healthcheck"],
    },
    "initialDelaySeconds": 15,
    "periodSeconds": 15,
}
```


\