# Emergency login in case of OIDC failure

\[All steps bellow require root privileges\]

If for some reason other login methods for OIDC stop working, you use the unseal token to authenticate with it. To generate a new one, log into our cluster and follow the steps below:

```python
kubectl exec -it vault-0 -- /bin/sh

$ export VAULT_ADDR=http://127.0.0.1:8200

$ vault operator generate-root -init
Nonce  ...
OTP    ... # Save this for later!

$ vault operator generate-root
Unseal Key (will be hidden): <enter unseal key> # Key in 1pass
Encoded Token  ... # Save this too!

$ vault operator generate-root -decode="<encoded token>" -otp="<otp>"
```

Then use the generated token to access Vault through the option "token"