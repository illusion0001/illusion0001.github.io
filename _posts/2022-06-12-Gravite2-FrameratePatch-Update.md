---
layout: post
title: "Gravity Rush 2 (Gravity Daze 2) Unofficial 60FPS Patch Now Playable on PS4/PS4 Pro"
excerpt: "Fight against the Nevis and protect towns at higher framerates."
header:
  teaser: https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2C-ep03.png
  overlay_image: https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2C-ep03.png
  overlay_filter: 0.5
  og_image: https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2C-ep03.png

categories: patches
tags: [ "ps4", "modded console" , "Gravity Rush 2", "Gravity Daze 2" ]
twitter: {card: "summary_large_image"}
toc: true
toc_sticky: true
---

{% include_relative _orbis_console_note.md %}

Featured on:

- [NoisyPixels](https://noisypixel.net/gravity-rush-2-fan-creates-60-fps-patch/)

## Improvements

Over the past few months I have been working on rewriting the Gravity Rush 2 (Gravity Daze 2) patch from scratch and there has been some ~~small~~ big improvements.

- The game now runs at correct speed at any framerate.
- Video stuttering has been fixed.
- Implemented button combination for easy testing.

What's the first one about? Well, if you have read my [previous post](/patches/2021/12/19/Gravite2-FrameratePatch/) on the matter, you will have notice that timestep was fixed to 60FPS, meaning if the game were to drop any frames, the game would slow down as well, with this update, this has been resolved.

<div align="center">
<video width="100%" controls muted>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2-FrameComp.mp4" type="video/mp4">
</video>
</div>

Notice how Kat is running slower on the middle.

Second update is that the videos no longer slows down and stutters anymore, check out these two videos and you'll see what I mean.

<div align="center">
<video width="100%" controls muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2-Video-Before.mp4" type="video/mp4">
</video>
</div>

<div align="center">
<video width="100%" controls muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2-Video-After.mp4" type="video/mp4">
</video>
</div>

The first video runs noticeably slower and the sound is out of sync. However, the second video plays just fine.

I have completed the game and added the necessary level checks for the game to be playable with this patch.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2-Credits1.png" %}

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2-Credits0.png" %}

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2-Credits2.png" %}

Just a reminder that the level checks here is to prevent the game from softlocks and will fall back to the default 30FPS mode. But Episode 23 is a special case. In this episode, you are required to solve puzzles and along the way, there are these sequences.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GR2-EP23b.png" %}

Which of course, have their scripting tied to the timestep and will never play unless it is 33ms.

To overcome this (or any other softlocks you may find) I have implemented a button combination. these can be pressed at anytime.

| Button | Action                             |
|--------|------------------------------------|
| L3 + X | Switch between 30 and 60FPS Modes. |

What does it do exactly?

Pressing this combination will cycle through the framerate target between 30 and 60FPS. It can be used during Episode 23 dialogue sequences since the puzzle sections plays out just fine at 60FPS.

Raven's Story is also playable. Softlock protection are also implemented here and will fallback to 30FPS in sections that are required.

<div align="center">
<video width="100%" autoplay controls muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/Gravite2-FrameratePatch-Update1/GravityDazeOverture-PatchMeme0.mp4" type="video/mp4">
</video>
</div>

<div align=center>
<em> <a href="https://youtu.be/tFeXtu-3u78?t=561">Gravity Rush: The Animation - Overture | Parts A & B</a> </em>
</div>

As they say, being a hero doesn't pay the bills.

Oh, you might want to check your calendar to see what day it is. That's right, today (June 12th) marks the day Gravity Rush for the PS Vita was released in North America! <i class="twa-2x MayruAnimationKit02Dance"></i> Animation made by [MayruAnimations](https://twitter.com/MayruAnimation/)

Want to see the patch in action? Checkout the video below and you can find the links to support me on GitHub, Patreon and other platforms.

## Showcase

Base PS4/Slim

<iframe width="560" height="315" src="https://www.youtube.com/embed/VPkU-jb7DHc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

PS4 Pro

<iframe width="560" height="315" src="https://www.youtube.com/embed/4xaZPn55RkU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Patch

- <a href="/_patch/GravityDaze2-Orbis/" class="button" role="button"><i class='fas fa-download'></i> Patch Source Code</a>
- <a href="/install-instructions/" class="button" role="button"><i class='fas fa-download'></i> Patch Installation Instructions</a>

{% include_relative _supporters.md %}
