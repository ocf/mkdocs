---
title: Self-hosted Debian Github Runner for ocflib
---

## Origin 
Why self-host a github runner if Github gives you free ones if your repo is public?

In a nutshell, repositories like ocflib has CI tests that depends on having access to OCF LDAP (only accessible from within OCF network) and OCF groups/users (UNIX groups). If we want to keep using github's free runner, we have to configure some kind of external LDAP access only for the runner, and also configure test UNIX groups info prior to running each CI/CD. 

Self-hosted github runner would run under ocf network, on our k8s cluster. We also have a lot more control over it.

[words from storce]
Why did I write a new runner on top of the Nix runner? For a few (personal) reasons:
1. There is a significant lack of documentation around how Nix runner actuall works.
2. I am a big believer of OCF k8s, and have the runner be centralized along with other applications on k8s makes me happy :D.
3. I am not entirely comfortable with Nix (yet). Spinning up a Debian runner based off the existing OCF Docker image (that has things like LDAP pre-configured) was very simple to do.

## User Manual
### How to add new repositories to the runner
This action can only be performed by a superuser (ocfroot/owner of the OCF github organization). In order to avoid creating security vulnerabilities, it is very important for you to follow ALL OF THE STEPS below when adding a new repository, :
1. Thoroughly audit the files under `.github/workflow/` of the target repository. Make sure that there are no malicious code. Ideally, set up branch protection for the repository.
2. Go the github.com/ocf -> Settings -> Actions -> Runner groups -> Default, select the new repository by clicking the gear icon next to "x selected repository"
3. Under the target repository's action files (`.github/workflow/*.yml`), make sure that there are fork PR protections under your desired job (the conditional `if: github.repository == 'ocf/repo_name'`).
4. Again, under your desired job, write `runs-on: self-hosted`
Like:
```
name: __name__

on:
  push:
    branches: [master]

jobs:
  __job_name__:
    if: github.repository == 'ocf/repo_name'
    name: __name__
    runs-on: self-hosted
    steps:
      ...
```


## Architecture
The runner can be found at github:ocf/github-runner

The runner runs on our kubernetes cluster under the namespace github-runner. It uses the transpire CI/CD pipeline.

The Dockerfile and the comments in it should be largely self-explatory. A lot of the set up steps are just copy-pasted from Github's documentation. Some points, however are worth noting:

1. `setup_user.sh` initializes the runner with some UNIX groups/users (like the basic ocfstaff/guser etc.) so that some tests that runs on it (like those from ocflib) wouldn't fail. I couldn't find a smarter way to import them. Yes, this means that if some tests were to require new groups and users, we would need to manually change the script.
2. `start.sh` starts the runner. It uses Github Personal Access Token (PAT). We use PAT since the default runner intialization token provided by Github is ephemeral, which makes it unsuitable for an environment like k8s. The PAT is an org-scoped github PAT called `self-hosted-runner` that allows users to read and write to self-hosted runners and org-level administration. The PAT is injected as an environmental variable into the container.

While the org-scoped github PAT gives us the flexibility of using the runner for all OCF repos, we can't just let any actions or repos run on it. For example, a malicious action can execute `echo $GITHUB_PAT` and leak the PAT in action logs. There are security concerns with runnners like this. Here is how they are addressed:

1. While the PAT is org-scoped, the runner is assigned to the Default runner group (see ocf org Github admin page). The runner is only allowed to pick up jobs from authorized repos under the group. So an org owner (ocfroot) would have to approve any new repo.
2. Another vulnerability comes from fork pull request action triggers. A malicious user can open a PR and trick the runner into executing malicious code. To prevent this, the github workflow configuration file must have `if: github.repository == 'ocf/repo_name'` so that actions can only be triggered from the main repository, not a fork.






