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

**This guide does not cover how to build the update itself.** It only covers how to install the patches.

# Installing Patch Using Automated Tool

[Download Program](https://github.com/illusion0001/py-patcher/releases)

1) Download the program linked above.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/setup/launcher0.png" %}

2) Download the [patch](/_patch/patch.zip) zip file.

3) Extract both archive to a folder somewhere on your computer.

4) Open a `.yml` patch file you want to patch, change `enabled: False` to `enabled: True`, save the file.

5) Open PowerShell 

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/setup/launcher1.png" %}

6) Type `.\launcher.exe -f (file to be patched) -c (patch file)`

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/setup/launcher2.png" %}

7) Hit Enter and if your executable is valid, it should apply all the patches, your patched executable file is saved to `filename-patched` in the same folder that the program is in.

Video Guide:

<div align="center">
<video width="100%" controls muted>
  <source src="https://storage.googleapis.com/assets-illusion0001/images/setup/launcher-vidya.mp4" type="video/mp4">
</video>
</div>

# Legacy methods

## Installing Patch using Direct File Address method

<p align="center">
<img src="https://storage.googleapis.com/assets-illusion0001/images/setup/addr-setup0.png">
</p>

<p align="center">
<em>Open Goto.</em>
</p>

<p align="center">
<img src="https://storage.googleapis.com/assets-illusion0001/images/setup/addr-setup1.png">
</p>

<p align="center">
<em>Paste address from file.</em>
</p>

<p align="center">
<img src="https://storage.googleapis.com/assets-illusion0001/images/setup/addr-setup2.png">
<em>Paste Write value from file.</em>
</p>

- Save your changes.

## Installing Patch using Array of Bytes method

<p align="center">
<img src="https://storage.googleapis.com/assets-illusion0001/images/setup/hxd0.png">
</p>

<p align="center">
<em>Open Search.</em>
</p>

<p align="center">
<img src="https://storage.googleapis.com/assets-illusion0001/images/setup/hxd1.png">
<em>Paste copied first line into search field and change search to Hex Value as well as change direction to all and click 'Search All'.</em>
</p>

<p align="center">
<img src="https://storage.googleapis.com/assets-illusion0001/images/setup/hxd2.png">
<em>Copy second line from patch file and Paste Write.</em>
</p>

Save your changes.

***

*Updated on: 2022-03-07*
