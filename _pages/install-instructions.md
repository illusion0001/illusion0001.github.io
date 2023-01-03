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
{% include img1 image_path="https://drive.google.com/uc?id=1GhBGlGvW25ipLACwSdpRGq7YLMR4VZq_" %}
- 4) Once installed, download the plugins from the GoldHEN Plugins Repository [Releases Page](https://github.com/GoldHEN/GoldHEN_Plugins_Repository/releases/latest).
- 5) Using a FTP client, copy the plugin files to `/data/GoldHEN/plugins`
- 6) Make a text file called `plugins.ini` if it does not exist, add the following to the file, if the line `[default]` already exist, just add `/data/GoldHEN/plugins/game_patch.prx` to the line below it.

  - Example:

{% include img1 image_path="https://drive.google.com/uc?id=1icMnzbp87m1g6wuwM3J2Cz2ry4a8j5Xm" %}

  - The folders should look like this:

{% include img1 image_path="https://drive.google.com/uc?id=1cvusAH-6Q-98qX6ZDZ1EDdda9ZRbEA66" %}

{% include img1 image_path="https://drive.google.com/uc?id=1op5rkaQ9L9GZ2TBw02UxIPIYyv18g8zH" %}

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

{% include img1 image_path="https://drive.google.com/uc?id=1mL9ibo-NNC4B5NJyrw1TnkGuwCbSf_6n" %}

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
  <source src="https://drive.google.com/uc?id=1WLGOa8a25UNIysvoIo-_qhIGysjjbCzA" type="video/mp4">
</video>
</div>

## Legacy Guide

### Installing Patch using Direct File Address method

<p align="center">
<img src="https://drive.google.com/uc?id=1SkEVVbBU4u-ayJJlNYZla6-LrX-7m8sS">
</p>

<p align="center">
<em>Open Goto.</em>
</p>

<p align="center">
<img src="https://drive.google.com/uc?id=10crSOcTZ3YiwlU9vAl-yaj7Ke9A0ps7W">
</p>

<p align="center">
<em>Paste address from file.</em>
</p>

<p align="center">
<img src="https://drive.google.com/uc?id=16yx8ofuBuavUh0VBp2S3co2TuSJbDUNZ">
<em>Paste Write value from file.</em>
</p>

- Save your changes.

### Installing Patch using Array of Bytes method

<p align="center">
<img src="https://drive.google.com/uc?id=18Z0g3FRaUbtnhiU2r0r5IsLGNBGmTdJz">
</p>

<p align="center">
<em>Open Search.</em>
</p>

<p align="center">
<img src="https://drive.google.com/uc?id=1W7m3x3mmsyEwG6_GG5EnztJ44wC0cXUx">
<em>Paste copied first line into search field and change search to Hex Value as well as change direction to all and click 'Search All'.</em>
</p>

<p align="center">
<img src="https://drive.google.com/uc?id=1zzg3Ya7PN5k4NMmU1BA6PyySpj2rtTBQ">
<em>Copy second line from patch file and Paste Write.</em>
</p>

Save your changes.

***
