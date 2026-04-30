# How to Learn Nix

This document contains many of the resources that `~njha` used to learn Nix and NixOS.

## Step 1. The Language

**Time Estimate**: 1 hour, less if you're familiar with functional languages

**Required Reading**: <https://nixos.org/guides/nix-language.html>

To check if you understood this guide, go to the worked examples at the end but **don't scroll so far you can see the explanation**. For each one of these examples, look at only the nix source code, and explain the syntax (i.e. this is a function that takes x, y, z args and returns ...). If you can easily come up with everything in the explanation below each example, you're ready to move on. If not, study this page until it makes sense!

## Step 2. The OS

**Time Estimate**: 1-2 hours, less if you're familiar with DIY Linux installs e.x. Arch Linux

**Manual**: <https://nixos.org/manual/nixos/stable/>

Next you should install a copy of the OS. If you have spare hardware lying around you can use that (I find this more fun), or you can create a virtual machine to play around inside. To do this, grab the ISO from nixos.org, and install it following the `Installation` section of the guide linked above. You should get familiar with how to find out what options and packages are. Consider reading the package definitions for a few packages you're installing.

* NixOS Options: <https://search.nixos.org/options>
* NixOS Packages: [https://search.nixos.org/packages](https://search.nixos.org/packages?)

It's a good idea to either install Nix locally (see [Nix on your Computer](/doc/nix-on-your-computer-r7pLkYWNML) for installation instructions) or use your NixOS install to play around with Nix more.

## Step 3. Nix Course

**Time Estimate**: ??? it's been a while

**Course**: <https://zero-to-nix.com>

Now that you have *some* background, you're very ready to jump into an introductory course in Nix. I find that having some operational understanding on how to use Nix before your first read through of this course really helps, which is why I put the course third in this list. You should work through this course as it tells you!

This course will also introduce you to flakes. If you're confused (and you will be, since the design of flakes seems intended to be maximally confusing), feel free to read some of the resources linked in Step 4 out of order.

## Step 4. Flakes

**Time Estimate**: ??? either you get it immediately or it's super confusing

**Required Reading**: <https://zero-to-nix.com/concepts/flakes>

**Required Reading**: <https://serokell.io/blog/practical-nix-flakes>

**Optional Reading**: <https://www.tweag.io/blog/2020-05-25-flakes/> (a little outdated)

Flakes are a permanently-in-beta-but-everyone-uses-them feature of Nix. The way it works is, at any supported entrypoint to a Nix expression (for example, `configuration.nix` in NixOS) you can put a `flake.nix` instead. The structure of the flake is some set of inputs, which the runtime will grab, and then an outputs function which takes those inputs as arguments. The output of that outputs function is the output of your nix flake expression. Confusingly, this isn't the same as a regular `configuration.nix` -- the runtime expects a differently layout of keys in the object :(

## Step 5. Contribute to OCF

**Time Estimate**: as long as you want to spend

Okay! You know everything you need to know now (seriously! it's not that much). Ask an SM for some task that needs to be done in our Nix setup and figure out how to do it. You'll be a pro in no time.
