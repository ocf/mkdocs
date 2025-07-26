---
title: Keycloak
---

At the time of writing, we have two instances of Keycloak running, one of the old k8s cluster and one on the new one. The old one is decommissioned, as we are trying to migrate everything to the new one.

To access keycloak, login through the page https://idm.ocf.berkeley.edu/admin/ocf/console

To add a new application to keycloak, you need to add a client, either through github/ocf/kubernetes/apps/keycloak, or directly in the web interface. Again, at the time of writing, the CI/CD pipeline is broken for keycloak specifically, so the easier way is to do so in the web interface.

(OCF moment)
