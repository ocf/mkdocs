# Configuration (Transpire)

[Transpire](https://github.com/ocf/transpire) (/tɹænˈspaɪ̯ɚ/) is a Kubernetes config generation tool designed by and for the Open Computing Facility. If you're wondering why we wanted to build our own thing, check out the [History](/doc/history-wxYwTlBgfS) document.

## Design Goals

Here's what we wanted out of transpire.

* All non-secret configurations and values should live transparently in Git.
  * This includes Kubernetes resources, and configuration for our own apps.
  * People before us at the OCF opted to throw the entire configuration file into a secret store if it contained any secret values, which is a little annoying if you don't have access to secrets.
* Secrets are stored securely
  * Can create Kubernetes secrets, and template secrets into application configuration
  * Can automatically generate certain types of secrets (CA Certs, random strings)
* Minimize YAML
  * We don't like writing YAML very much.
  * Writing YAML tends to result in config being copied around from one project to the next - warts and (now-unnecessary) workarounds included - which makes it hard to change things across the whole organization at once
    * e.g. what to do when you want to change how secrets are injected, and every single project has copy-pasted (sometimes with modifications!) the old method into its own YAML file?
* Support Helm charts
  * We should be able to get any helm chart from a repository
  * We should be able to arbitrarily modify any Helm chart
* Support any reasonable method of distributing Kubernetes manifests
  * Also known as "HTTP(s) URLs and checksums"

## Installation

Although `transpire` is published on PyPi, it may be out of date. We therefore recommend you install it from the latest commit on `main` directly.

### via pip

```bash
pip install git+"https://github.com/ocf/transpire.git"
```

### via nix

This command will start a new shell with the `transpire` command available.

```bash
 nix shell github:ocf/transpire
```

### via poetry

This method is recommended if you are going to make changes to `transpire` itself, not just configuration built by `transpire`.

```bash
git clone https://github.com/ocf/transpire.git
cd transpire
poetry shell
poetry install # you now have a shell with transpire in it
# in the future just cd transpire && poetry shell to get here...
```

## Usage


:::warning
Transpire is still currently very unstable, and the API changes quite frequently, so we're holding off on documenting it too much until we're sure we like it. Talk to njha or etw for more information, or [read source code](https://github.com/ocf/transpire). 

:::

You'll need to clone the OCF's [transpire root repository](http://github.com/ocf/transpire/) and run transpire commands from there, even if you're making changes to another app (like docs). We're working on fixing this.