---
layout: single
title: "Framerate Unlock Patches for Ratchet and Clank PS3 titles (RPCS3)"
excerpt: "PS5 does not yet have a remaster, but the PC does, through an emulator."
thumbnail: "https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/RC_Feature.png"
header:
  overlay_image: "https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/RC_Feature.png"
  overlay_filter: 0.5
  og_image: "https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/RC_Feature.png"
categories: patches
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---


# Intro

Time for some more framerate PlayStation 3 patches, or to be more specific, RPCS3 patches. You know, an emulator. With the knowledge gained with the previous post, I decided to tackle a series of titles, that is the Ratchet and Clank HD era games. Ranging from Tools of Destruction all the way to the Nexus.

## Research and Patching

When I first boot up one of their games with the frame limit set to off, I saw this.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_rc_sc0.png" %}

<div align=center>
<em>82 FPS? Weird limit but alright</em>
</div>

What about the newer games?

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_rc_sc4.png" %}

<div align=center>
<em>Another strange arbitrary cap</em>
</div>

Alright, let's fire up the debugger and see what we can find.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_rc_dbgsc0.png" %}

<div align=center>
<em>Is that current frametime?</em>
</div>

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_rc_dbgsc2.png" %}

<div align=center>
<em>Seems like it is</em>
</div>

These look like a group of frametime values and after a little bit of trial and error it turns out that `E67B04` is the minimum frametime. Take note of the hex value `3C 5A 74 0E` or `0.01333` in float. let's try changing this to 0.005.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_rc_sc1.png" %}

<div align=center>
<em>Oh look, framerate cap increased</em>
</div>

Is it really increased though? Introducing the tried and true method of... Looking at the ground<i class="twa twa-trade-mark"></i>.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_rc_sc2.png" %}

<div align=center>
<em>Yes, yes it is increased</em>
</div>

Doing a search for this value in the executable shows that this is a base value for the min frametime value.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/ghidra_rc_ft0.png" %}

But wait, 13ms? wasn't the cap we see in the game is 12ms?

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_rc_sc3.png" %}

<div align=center>
<em>Wha? <i class="twa twa-thinking-face"></i></em>
</div>

[Juhn <i class="twa twa-cat-face"></i>](https://github.com/isJuhn/) the developer behind the [KAMI, Kot(Cat) and Mouse Injector](https://github.com/isJuhn/KAMI) did some investigation and found out that this number is multiplied by 0.9

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_rc_dbgsc3.png" %}

A little bit of code explanation,

`lfs` which loads float from offset to `f13` that has the 0.9 value, then loads into `f1` with 0.013333 and reads the value.

Then it gets multiplied by the `fmuls` instruction and thus get us the 12ms we saw earlier.

That would be it for the rest of the games, right?

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rc_dev_value_meme.png" %}

Starting with A Crack in Time, a later entry in the series, things changed. changing the value we previously discoverd works but has a side effect.

{% include_relative _incompatible_video_note.md %}

<div align="center">
<video width="100%" controls >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rc_rpcs3_fps_before_demo.mp4" type="video/mp4">
</video>
<em>Oh no, Game Patching worse nightmare, double speed.</em>
</div>

In this case if it exceeds the minimum frametime set by the game it will speed up, it **does not** slow down below the target frametime but it speeds up, if above.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_rc_dbgsc4.png" %}

16.67ms is here to save our day, searching for `3c 88 88 89` and changing some values around resolved the issue.

<div align="center">
<video width="100%" controls >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rc_rpcs3_fps_after_demo.mp4" type="video/mp4">
</video>
<em>Correct game speed, nice.</em>
</div>

Thought the headache was over? Far from it. Repeating the same method works in memory but there is no such value as `3C 5A 74 0E` in the executable.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/ghidra_rc_ft1.png" %}

However, setting a breakpoint on that value got us here.

```
0072c1e4 lfd  f1,0x8(param_1)=>DOUBLE_0072c140 = 0.013333333 // 3f 8b 4e 81 c0 00 00 00
0072c1e8 fsub f2,f3,f1
0072c1ec frsp f2,f2
0072c1f0 fsel f1,f2,f3,f1
0072c1f4 frsp 1,f1
0072c1f8 stfs f1,0x4(r31) // <-- breakpoint
```

Wait a minute, a double? They set the value initally in double, which is twice the bits as float for more accurate decimals and then converts it to float again.

<div align="center">
<video width="100%" autoplay loop >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/memes/tenor/we_do_a_little_trolling_meme.mp4" type="video/mp4">
</video>
</div>

The end results is the same as the rest of the games, unlocked framerate with no speedups.

{% include_relative _shilling.md %}

# Credit(s)

[Juhn <i class="twa twa-cat-face"></i>](https://github.com/isJuhn/) for explanation on framerate limits.

# Results

Note that the video below is recorded in slow motion to show the patch at its best.

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/azrU00bZuIc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

For those looking to use the patch on the emulator, you can head over to the patch manager, click on the "Download Latest Patches" and find the patch you wanted to use with your game Title ID and version, click on the checkbox to enable the patch and save changes.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_patch_example.png" %}

<a href="https://wiki.rpcs3.net/index.php?title=Help:Game_Patches/Main#Ratchet_.26_Clank_Future:_A_Crack_in_Time" class="button" role="button"><i class='fas fa-download'></i> Patch Source Codes</a>

{% include_relative _supporters.md %}
