---
layout: post
title: "Solving the Infected's Severed Head Crash Bug in The Last of Us (PlayStation 3)"
subtitles: "Is it a Head? Is it a bottle? No! It's a game bug. Solved by 2 bedroom coders. Part 1."
categories: Patches
tags: tlou ps3 rpcs3 patches
banner: /assets/images/t1r-ps4-head-crash/t1r-head-banner.png
---

Is it a Head? Is it a bottle? No! It's a game bug.

Solved by 2 bedroom coders. Part 1.

Your move. Naughty Dog.

## Intro

Usually, when an NPC, actor, or Player's buddies does an action where they would cut Infected's Head off, they leave behind a severed head. 

If a Player decided to throw an object, let's say a brick or bottle. The game would crash. Why's that?

Affected Consoles:

- ~~PlayStation 3~~ [Unofficially Patched](https://illusion0001.github.io/patches/2021/02/15/t1-head-crash-bug-fix.html)

- ~~PlayStation 4~~ [Unofficially Patched](https://illusion0001.github.io/patches/2021/02/16/t1r-head-crash-bug-fix.html)

- PlayStation 5 [Video](https://youtu.be/HQ7oOmx4mmg?t=127)

- PS4/PS5 versions issue still persists on latest patch 1.11

<video controls autoplay muted width="640" height="360">
  <source src="\assets\images\t1-ps3-head-crash\t1-head-crash-before.mp4" type="video/mp4">
</video>

## Finding what caused the crash

When the game crashed, using an emulator we can see that it gives an access violation as well as the address it stopped.

![](\assets\images\t1-ps3-head-crash\t1-head-acess-violation.png)

Going to this location in Ghidra gives us some clues.

![](\assets\images\t1-ps3-head-crash\ghidra-head-crash-hint.png)

```c
if (dVar30 < (double)*(float *)(puVar8 + 0x28))
```

The game does checks if: 

- Object is throwable

- Object collided with is enemy

We can check using a Debugger with a breakpoint set on the crash address.

Hit on the Head.

![](\assets\images\t1-ps3-head-crash\t1-head-debug0.png)

Hit on an Enemy.

![](\assets\images\t1-ps3-head-crash\t1-head-debug-spu-data.png)

In Register 29, there's some data here. It seems to be collision data.

Our best guess is that the game thinks the object collied is an enemy and no data generated.

## Solution

We can add some data into Register 10 and additional check to prevent crashing.

```yml
 - [ be32, 0x006d9368, 0x483aa7ed ] #Branch
 - [ be32, 0x00a83b54, 0x3d400001 ] #r10 = 0x10000
 - [ be32, 0x00a83b58, 0x7f9d5000 ] #r29 vs r10
 - [ be32, 0x00a83b5c, 0x409d0008 ] #Skip if r29<=r10 // If r29 less or equal to r10 then do nothing
 - [ be32, 0x00a83b60, 0x813d0040 ] #lwz r9,0x40(r29) // load as normal
 - [ be32, 0x00a83b64, 0x4e800020 ] #Return
```

Let's implement this fix and see the results!

<iframe width="640" height="360" src="https://www.youtube.com/embed/yDHUPHUYr1w?start=17" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Success!

## Patch

To use patch on the RPCS3 Emulator, simply download and enable through Patch Manager.

To apply patch and for use on a real PlayStation 3 console, you'll need to decrypt the executable, apply the patch, save and resign the executable. There's plenty of resources online already, We won't be covering it here.

In Eboot.bin, Find and Replace

```
1.00

from

81 3D 00 40 7B E3 00 20 90 01 09 A0

to

48 3A 4B 95 7B E3 00 20 90 01 09 A0

from

FA E1 00 E0 FB 01 00 E8 FB 21 00 F0 FB 41 00 F8 FB 81 01 08 81 3E 80 18

to

3D 40 00 01 7F 9D 50 00 40 9D 00 08 81 3D 00 40 4E 80 00 20 81 3E 80 18

1.11

from

81 3D 00 40 7B E3 00 20 90 01 0A 60

to

48 3A A7 ED 7B E3 00 20 90 01 0A 60

from

FA E1 00 E0 FB 01 00 E8 FB 21 00 F0 FB 41 00 F8 FB 81 01 08 81 3E 80 18


to

3D 40 00 01 7F 9D 50 00 40 9D 00 08 81 3D 00 40 4E 80 00 20 81 3E 80 18

```

## Credits

Thank you to [ZEROx](https://www.youtube.com/user/ZEROx2085) for improving over my inital patch.

And [Aphelion](https://www.youtube.com/c/AphelionGamingTV/) for allowing me to use his footage in the post.
