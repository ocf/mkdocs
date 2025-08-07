# JupyterLab on Slurm

Below are the steps needed to run a [JupyterLab](https://jupyter.org/try) instance on our HPC infrastructure. Note that this method is provided as a best effort, so things may break.

# 1. Set up Miniconda and Jupyter

First off, we need to install Jupyter on segfault, the HPC logon server. This will allow us to create a JupyterLab instance on corruption the actual compute node. To install Jupyter, we first need to install Miniconda, which will make package management much easier.


```bash
ssh <user>@segfault.ocf.berkeley.edu
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```


Accept the license agreement and install into the default location (which should be the same as `$HOME`, e.g. `/home/e/et/ethanhs` ). Make sure to install the conda activation code into your `.bashrc`. Since this is a server, you will want to copy that into your `.bash_profile`, so run the following:\n

```bash
cat .bashrc >> .bash_profile
```


Log out of segfault


```bash
exit
```


Then, ssh back in. You should see `(base)` at the start of your prompt once you ssh in.


```bash
ssh <your OCF username>@segfault.ocf.berkeley.edu
```


Next, we will want to install Miniconda locally. On Windows it is recommended to use the WSL,


Follow the [official installation instructions for your platform](https://docs.conda.io/en/latest/miniconda.html).

# 2. Install slurm-jupyter

On your local machine you will want to install slurm-jupyter in a conda environment. First make sure you are in a conda prompt (the prompt should start with `(base)` like above.


Let's make a conda environment to install slurm-jupyter into *locally* (on your machine)

```bash
conda create -n hpcctl python=3.10
conda activate hpcctl
pip install git+https://github.com/ocf/slurm-jupyter.git
```


We also need to install slurm-jupyter and set it up on segfault/hpcctl. First, let's make a conda environment for us to install into. Note that you will be using this conda environment to install any additional packages (e.g. numpy, pytorch, etc), so we suggest making an environment per-project. Also the version of Python can be changed to 3.6 or above, we just use 3.10 for our example here.

```bash
conda create -n my-cool-project-name-here python=3.10
```


Next we will activate this environment to install slurm-jupyter into our environment:

```bash
conda activate my-cool-project-name-here
pip install git+https://github.com/ocf/slurm-jupyter.git
```


Finally, we will want to run the `slurm-jupyter` setup script. This creates a certificate for your jupyterlab instance.

```bash
config-slurm-jupyter.sh
```

This script will ask you several questions, answer them as follows:

```bash
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:California
Locality Name (eg, city) []:Berkeley
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Open Computing Facility
Organizational Unit Name (eg, section) []:OCF HPC
Common Name (e.g. server FQDN or YOUR name) []:hpcctl.ocf.io
Email Address []: <your OCF username>@ocf.berkeley.edu
```


Finally, you will need to set up ssh-key based login to segfault/hpcctl. This is so that `slurm-jupyter` can issue slurm commands without prompting for a password. Locally on your machine create an ssh-key if you don't have one already:\n

```bash
# Accept all the defaults
ssh-keygen -t ed25519 -C "<your OCF username>@ocf.berkeley.edu"
ssh-copy-id -i ~/.ssh/id_ed25519.pub <your OCF username>@hpcctl.ocf.io
```

You will need to log in once more to copy the key, but after this you should not need a password to log into hpcctl.

# 3. Run your jupyterlab instance!

Finally, back on your local machine, you can run `slurm-jupyter`to create a new slurm job running jupyterlab.

Here are a few examples of how one could run this command:\n

```bash
# Run in the conda environment "falcon-finetune" using 1 GPU, 32G of RAM on corruption.
python -m slurm_jupyter -e falcon-finetune -f hpcctl.ocf.io -g 1 -m 32G

# Run a CPU-only job, using 16 cores
python -m slurm_jupyter -e my-cpu-env -f hpcctl.ocf.io -c 16 -m 32G
```

For the full list of options, run

```bash
python -m slurm_jupyter -h
```

Note that some values are unsupported, such as requesting more than 4 GPUs.