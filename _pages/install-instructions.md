---
layout: single
title: Install Instructions
excerpt: Step-by-step instructions for installing patches to executable files.
permalink: /install-instructions/

toc: true
toc_sticky: true
---

These instructions are general and apply to most patch from this website.
Games used for the presentation does not have any relevance for the steps.

**This guide does not cover how to build the update package itself.** It only covers how to install patches into the binary file.

# Installing Patch Using Automated Program

1) Download the program: [py-patch](https://github.com/illusion0001/py-patcher-bin/releases/latest)

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/setup/launcher0.png" %}

2) Extract the program archive to a folder somewhere on your computer.

3) Double click on the program and follow the on-screen instructions.

4) Install the patched executable back on to the console.

- **(PS4 Only)** Build the update package with the newly patched executable file and install it on the console.
- (If there is a malware detection when runnning the program, it is a false positive.)
- (Patch files can be updated by using `-dl` flag)
- (An internet connection is required to download/update [patch](/_patch/patch.zip) files.)

Video Guide:

<div align="center">
<video width="100%" controls muted>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/setup/launcher-vidya.mp4" type="video/mp4">
</video>
</div>

# Legacy methods

## Installing Patch using Direct File Address method

<p align="center">
<img src="https://img-assets.illusion0001.workers.dev/assets/images/setup/addr-setup0.png">
</p>

<p align="center">
<em>Open Goto.</em>
</p>

<p align="center">
<img src="https://img-assets.illusion0001.workers.dev/assets/images/setup/addr-setup1.png">
</p>

<p align="center">
<em>Paste address from file.</em>
</p>

<p align="center">
<img src="https://img-assets.illusion0001.workers.dev/assets/images/setup/addr-setup2.png">
<em>Paste Write value from file.</em>
</p>

- Save your changes.

## Installing Patch using Array of Bytes method

<p align="center">
<img src="https://img-assets.illusion0001.workers.dev/assets/images/setup/hxd0.png">
</p>

<p align="center">
<em>Open Search.</em>
</p>

<p align="center">
<img src="https://img-assets.illusion0001.workers.dev/assets/images/setup/hxd1.png">
<em>Paste copied first line into search field and change search to Hex Value as well as change direction to all and click 'Search All'.</em>
</p>

<p align="center">
<img src="https://img-assets.illusion0001.workers.dev/assets/images/setup/hxd2.png">
<em>Copy second line from patch file and Paste Write.</em>
</p>

Save your changes.

***

*Updated on: 2022-03-07*
