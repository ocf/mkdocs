# Transpire: History

:::tip
Read this before you accuse us of [NIH syndrome](https://en.wikipedia.org/wiki/Not_invented_here)!

:::

## Old Kubernetes Era

In the old Kubernetes era we wrote Kubernetes YAML and processed them through Ruby templates to put secrets inside of them. This means a lot of people created secrets inside environment variables defined inline, which our CI promptly leaked to the entire public internet. Helm charts were unsupported, so if we wanted to use those we'd have to render the helm chart into a flat YAML file and commit it to git. Overall, it was not a fun time.

## The Pre-Python Era

The first third-party tool we tried was [Helm](https://helm.sh). Helm is the de-facto standard Kubernetes config generation framework, and pretty much any software intended to be deployed onto Kubernetes has a published Helm chart somewhere. Git-ops is a sane way to do infrastructure (citation needed), so we hooked up Helm to ArgoCD by feeding existing charts configuration values. This works in 80% of cases. In the other 20%, the chart doesn't have the configuration option you need, or there is no chart.

A chart not existing is unavoidable, so that was acceptable to us. However, we do need a way to make certain changes not available in the chart, without forking the chart! We don't want to maintain a bunch of different helm charts. Luckily, there is a solution to this too, and it's called kustomize-helm. What this does is it takes the output of Helm, and runs it through [Kustomize](https://kustomize.io) (the config generation tool built into kubectl) to edit the manifests. This solves maybe 80% of problems, with the remaining 20% being particularly complex edits. Try chopping off a particular annotation from 100+ objects using Kustomize. It's horrible.

## Infrastructure as Code

Luckily, configs are just data, and we have a tool to elegantly make changes to data. It's called a programming language. The third thing we tried is called [Pulumi](https://www.pulumi.com), which lets you generate Helm charts and edit them from Python or Typescript. It's actually pretty much exactly what we want, except it's very corporate and unless you pay them it's difficult to ship Pulumi's internal state around.

So instead we decided to have a git repository with a bunch of python files that just print out YAML when executed. We wrote a little script that lived inside ArgoCD that would execute the Python files to get the YAML out. We had some little utilities for building Helm charts and whatnot, and this was pretty good. There were some security concerns with running arbitrary code, but we figured that if you can write to the cluster YAML you own the cluster anyway, because you can now modify any image in the cluster (like the ArgoCD one) with a malicious one.

A nice bonus to this was we could now have global processing actions. For example, in the current deployment of transpire, when a Helm chart emits a Secret it automatically gets turned into a VaultSecret, which pulls its values from Hashicorp Vault. This way, no secret ever touches git, and we can automate secret rotation from elsewhere. We also have some level of validation and typechecking that happens at the YAML compilation stage, which prevents a number of issues.

## Transpire is Born

The little script inside ArgoCD kept breaking, and we figured it was a bit of a hack anyway, so we made a CI system that pushed the manifests as YAML to a separate git repository for ArgoCD to pick up and deploy. A nice thing about this is that we have a history of the actual (intended) state of the cluster over time.

Eventually, the utilities folder grew quite large, and so we moved it into its own project. That project is transpire!