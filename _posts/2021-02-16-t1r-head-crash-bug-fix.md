---
layout: post
title: "Solving the Infected's Severed Head Crash Bug in The Last of Us (PlayStation 4)"
subtitle: "Is it a Head? Is it a bottle? No! It's a game bug. Part 2."
excerpt: "Is it a Head? Is it a bottle? No! It's a game bug. Part 2."
categories: Patches
tags: tlou ps4 patches bugfix
banner: /assets/images/t1r-ps4-head-crash/t1r-head-banner.png
---

Your move. Naughty Dog.

***

## Intro

Usually, when an NPC, actor, or Player's buddies does an action where they would cut Infected's Head off, they leave behind a severed head. 

If a Player decided to throw an object, let's say a brick or bottle. The game would crash. Why's that?

Affected Consoles:

- ~~PlayStation 3~~ [Unofficially Patched](https://illusion0001.github.io/patches/2021/02/15/t1-head-crash-bug-fix.html)

- ~~PlayStation 4~~ [Unofficially Patched](https://illusion0001.github.io/patches/2021/02/16/t1r-head-crash-bug-fix.html) ([Video](https://youtu.be/KCnMwV-jOoU))

- PlayStation 5 [Video](https://youtu.be/HQ7oOmx4mmg?t=127)

- PS4/PS5 versions issue still persists on latest patch 1.11

<video controls muted width="640" height="360">
  <source src="\assets\images\t1r-ps4-head-crash\t1r-head-crash-before.mp4" type="video/mp4">
</video>

## Cut to the Chase

Most of the explaination was already covered in our PS3 version, see that post for more details.

[Solving the Infected's Severed Head Crash Bug in The Last of Us (PlayStation 3)](https://illusion0001.github.io/patches/2021/02/15/t1-head-crash-bug-fix.html)

We were only able to get the debugger [PS4 Reaper](https://www.psxhax.com/threads/ps4reaper-ps4-rte-debugger-and-trainer-maker-by-shiningami.6077/) working once due to connection and attaching issues but that was enough for what we needed.

![](\assets\images\t1r-ps4-head-crash\ps4r-register.png)

Guessing from PS3 registers, It could be RBX that is holding collision data.

## Solution

We can do a check if RBX isn't 0 we can skip and run normally.

```
006bc849 e8 d0 53        CALL       SUB_00c21c1e // jump to code cave
         56 00
~~~
00c21c1e 48 89 85        MOV        qword ptr [RBP + -0xc20],RAX // pervious instruction overwritten by Call
         e0 f3 ff ff
00c21c25 48 83 fb 00     CMP        RBX,0x0 // check if rbx isn't 0
00c21c29 0f 84 04        JZ         LAB_00c21c33 // skip
         00 00 00
00c21c2f 48 8b 43 40     MOV        RAX,qword ptr [RBX + 0x40] // load as normal
                     LAB_00c21c33
00c21c33 c3              RET // return
```

Let's implement this fix and see the results.

<iframe width="640" height="360" src="https://www.youtube.com/embed/a5QEZGT7HOU?start=10" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Success! Doesn't crash now when throwing an object.

## Patch

To apply patch and for use on a exploitable PlayStation 4 console, you'll need to dump the game, modiify the executable with a hex editor and install the fake patch back onto the console.

In Eboot.bin, Find and Replace

```

1.00

48 8B 43 40 48 89 85 D0 F3 FF FF 4C 89 EF

to

E8 10 46 50 00 90 90 90 90 90 90 4C 89 EF

~~~

89 4C 24 34 C5 FA 2A C1 C5 FA 11 44 24 68 C5 FA 2A C8 C5 DA 5A E4 48 8D 15 70 AB 6E 00

to

48 89 85 D0 F3 FF FF 48 83 FB 00 0F 84 04 00 00 00 48 8B 43 40 C3 48 8D 15 70 AB 6E 00

####

1.10

48 8B 43 40 48 89 85 E0 F3 FF FF

to

E8 D0 53 56 00 90 90 90 90 90 90

~~~

BE A0 A0 00 FF 4C 89 EF C5 E2 5E DE 8B 48 3C 44 8B 70 48 48 8D 05

to

48 89 85 E0 F3 FF FF 48 83 FB 00 0F 84 04 00 00 00 48 8B 43 40 C3

```

## Credits

Thank you to [ZEROx](https://www.youtube.com/user/ZEROx2085) for improving over my inital patch. and for believing in x86!
