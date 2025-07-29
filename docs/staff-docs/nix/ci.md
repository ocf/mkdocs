---
title: OCF CI
---

hostname: spike

## adding a runner

1. edit `spike.nix` in `hosts/servers`, add new entry in `runners`. pattern match, look at `options.nix` for github-actions module
2. generate github personal access token, as per description in `options.nix` of github-actions for OCF org
[TODO insert docs for github personal access token here]
3. in the repo of the service, create the `github/workflows/build.yml` file
