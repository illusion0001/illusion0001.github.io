---
layout: single
title: Install Instructions
excerpt: Step-by-step instructions for installing patches to executable files.
permalink: /install-instructions/

toc: true
toc_sticky: true
---

# Updated Guide (PS4)

To setup custom game patches on your PS4, you will need to have a jailbreakable console, that is on firmware 9.00 or lower.

- 1) Start by loading GoldHEN 2.3 or newer on your PS4. (See excellent guide by [Wololo](https://wololo.net/2021/12/14/ps4-how-to-run-the-ps4-9-00-jailbreak-full-guide-with-goldhen-payload/).
- 2) Download the app GoldHEN Cheats Manager, link can be found [here](https://github.com/GoldHEN/GoldHEN_Cheat_Manager/releases/latest).
- 3) Copy it to the root of your USB drive and install it from the PS4 Package Installer.
{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/setup/new/vsh-pkginstaller.png" %}
- 4) Once installed, download the plugins from the GoldHEN Plugins Repository [Releases Page](https://github.com/GoldHEN/GoldHEN_Plugins_Repository/releases/latest).
- 5) Using a FTP client, copy the plugin files to `/data/GoldHEN/plugins`
- 6) Make a text file called `plugins.ini` if it does not exist, add the following to the file, if the line `[default]` already exist, just add `/data/GoldHEN/plugins/game_patch.prx` to the line below it.

  - Example:

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/setup/new/win32-plugins-text.png" %}

  - The folders should look like this:

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/setup/new/filezilla_plugins-folder.png" %}

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/setup/new/filezilla_plugins-cfg.png" %}

- 7) Update the database using the GoldHEN Cheats Manager app and you can now start using Custom Game Patches without needing a computer after the setup! 

***

**The guide below is outdated and should not be used!.**

***

# Legacy guide

These instructions are general and apply to most patch from this website.
Games used for the presentation does not have any relevance for the steps.

**This guide does not cover how to build the update package itself.** It only covers how to install patches into the binary file.

## Installing Patch Using Automated Program

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

## Legacy Guide

### Installing Patch using Direct File Address method

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

### Installing Patch using Array of Bytes method

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
