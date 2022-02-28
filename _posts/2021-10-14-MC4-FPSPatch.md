---
layout: single
title: "Dynamic FPS Patch for Midnight Club: Los Angeles"
excerpt: "Fast and Furious Racing at up-to 60 FPS!"
thumbnail: "https://storage.googleapis.com/assets-illusion0001/images/MC4-FPSPatch/MC4-Thumbnail-0.jpg"
header:
  overlay_image: "https://storage.googleapis.com/assets-illusion0001/images/MC4-FPSPatch/MC4-Thumbnail-0.jpg"
  overlay_filter: 0.5
  og_image: "https://storage.googleapis.com/assets-illusion0001/images/MC4-FPSPatch/MC4-Thumbnail.jpg"
categories: patches
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---


# Intro

Did you know that Midnight Club: Los Angeles on last generation of consoles run with a fixed timestep?

Turns out that it does. When this game started running on emulators, people quickly discovered that it ran with a fixed timestep, which means it either meets its target framerate, in this case 30 Frames Per Second or else it will either slow down or speed up. Let's patch this so we can see what the game could look like when performance bottlenecks are eliminated in future versions of emulators.

## Part 1 - Research

Common fixed timestep values usually are `1/30` or `1/60`, `0.03333333`, `0.01666667` for 30 and 60FPS targets. Now why is this important? Some games may used fixed timestep due to not having dynamic timestep implemented or there may be cases where logics are broken when it is not synced with the rest of the hardcoded game logics, i.e Timers, Animation timings, etc.

We will be searching for `0.03333333` as that is what its used in MCLA. which in hex is `3D088889` Big Endian format.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/MC4-FPSPatch/MC4-Screen0.png" %}

A lot of results, let's try changing one of these to our current frametime which is about `0.077` from `77/1000`.

It turns out it is the first result that our change has effect, which is `0x827D7520`.

Neat thing about the xenia emulator is that it is super easy to get executable address.

`emit_source_annotations # Add extra movs and nops to make disassembly easier to read.`

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/MC4-FPSPatch/MC4-Screen0a.png" %}

<div align=center>
<em>Piece of cake!</em>
</div>

## Part 2 - Patching

```cpp
  *(float *)(param_2 + 0x68) = fVar1;
  *(float *)(param_2 + 8) = fVar1;
  if (*(char *)(param_2 + 0x38) == '\0') {
    dVar8 = (double)*(float *)(param_2 + 0x14);
...
      // LAB_821bdb90
      fVar1 = (float)((double)*(float *)(param_2 + 0x20) * dVar9);
      dVar7 = (double)fVar1;
...
      if (param_4 != '\0') {
        *(float *)(param_2 + 0x18) = (float)(dVar7 + (double)*(float *)(param_2 + 0x18));
      }
    }
  }
  else {
    fVar1 = *(float *)(param_2 + 0x20);
```

There is a bunch of code below the if statement and I snipped most of it out, the line of interest are `fVar1 = (float)(min_frametime);` as that is where our breakpoint stopped.

`821bdbb4  beq  cr6,LAB_821bdc34`

This is where `if (param_4 != '\0')` goes to.

```
LAB_821bdc34 XREF[6]:     821bdb08(j), 821bdb68(j),
                          821bdb7c(j), 821bdb8c(j),
                          821bdbb4(j), 821bdbc4(j)
```

Looks like a lot is branching to here. If you may have noticed there is an `if` in the first code block I have already shown.

`if (*(char *)(param_2 + 0x38) == '\0')` this also uses branching to jump to places in the code, let's reuse that branch instruction and make it always jump with the `b` instruction. that stands for unconditional **b**ranch. 

`0x821bdb08 b Label_821bdc34`

Let's port this to the PS3 version.

`3D 08 88 89 3D CC CC CD 38 D1 B7 17` This is the constants from the 360 version, this will become useful later on.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/MC4-FPSPatch/MC4-Screen1.png" %}

<div align=center>
<em>Oh no, no results</em>
</div>

It turns out the mininum frametime is just slightly different. searching for just `3D CC CC CD 38 D1 B7 17` yielded one result.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/MC4-FPSPatch/MC4-Screen0b.png" %}

<div align=center>
<em>Wait, this looks like a different constant</em>
</div>

`3D 08 AB 86`? that looks *strange*. seems to be a calcuaction error of some sort. `1/29.7` and not `1/30` it could be `29.97` but that is unlikely though, thanks to [Whatcookie](https://github.com/Whatcookie) for pointing that out!

```
004c50c0 beq cr7,Label_004c5218
LAB_004c50c4 XREF[1]:     004c5220(j)
004c50c4 lfs f0,0x1c(r3)  // breakpoint
004c5220 bne cr7,Label_004c50c4
```

The breakpoint stopped at `4c50c4` the PS3 code is a little weird, it first branches to `4c5218` then to back to after doing a compare,

but anyways, similar patching method can be used here. first we want to stop it from jumping all over the place by nopping out `bne cr7,Label_004c50c4` then jumping to `4c52c4`. `4c5240 b Label_004c52c4` I replaced branch at 240 because there is some code that runs after `bne`. The end result is the same.

Enjoy!

# Results

Note that the video below is recorded in slow motion to show the patch at its best.

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/4vjIctNwu8A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

<a href="https://wiki.rpcs3.net/index.php?title=Midnight_Club:_Los_Angeles#Patches" class="button" role="button"><i class='fas fa-download'></i> Patch Code: RPCS3</a>

<a href="https://github.com/xenia-canary/game-patches/blob/main/patches/545407F8%20-%20Midnight%20Club%20Los%20Angeles.patch" class="button" role="button"><i class='fas fa-download'></i> Patch Code: Xenia</a>

{% include_relative _supporters.md %}
