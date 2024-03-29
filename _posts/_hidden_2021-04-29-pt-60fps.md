---
layout: post
title: "60FPS in Silent Hills: P.T. (Playable Teaser)"
excerpt: "Now you can get spooked at 60FPS.. with some visual issues.."
categories: patches
tags: pt ps4 patches
header:
  teaser: "https://img-assets.illusion0001.workers.dev/assets/images/pt-60fps/banner.png"
  overlay_image: "https://img-assets.illusion0001.workers.dev/assets/images/pt-60fps/banner.png"
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---

{% include_relative _orbis_console_note.md %}

# Cursitory

Would it be possible to run P.T. The scariest game of the genaration on the PS4?

Frame rate unlocking may not be the only piece of the puzzle. Resolution comes into play and perhaps other graphical settings as well because Metal Gear Solid V: Ground Zeros can render a huge open level at 60FPS at 1080p but P.T. can't maintain a stable framerate rendering just a hallway at 1080p.

## Framerate Limit Research

From my experince looking at other games on the PS3 and Xbox 360, frame rate limit is usually set by a interval setting. For example 1 for 60Hz and 2 for 30Hz. I'll refer to it as vsync flip rate from now on.

Let's do a search for function fliprate within the P.T. executable.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/pt-60fps/pt-ghdra0.png" %}

```
**************************************************************
*                          FUNCTION                          *
**************************************************************
FUN_0103f910                                    XREF[3]:     FUN_00d8a670:00d8a718(c), 
                                                               019b7a8c(*), 01a29438  
0103f910 55              PUSH       RBP
0103f911 48 89 e5        MOV        RBP,RSP
0103f914 41 56           PUSH       R14
0103f916 53              PUSH       RBX
0103f917 41 89 f6        MOV        R14D,param_2 // move param 2 into register 14
---
0103f95b 44 89 f6        MOV        param_2,R14D
0103f95e e8 2d 0a        CALL       sceVideoOutSetFlipRate // call flip rate function
         37 00
```

You may have already noticed that there is a couple of refernces to this function (XREF)

`FUN_00d8a670:00d8a718(c)` this call looks interesting, let's see what's going on here.

```
00d8a713 be 01 00        MOV        param_2,0x1 // move 1 into param 2
         00 00
00d8a718 e8 f3 51        CALL       FUN_0103f910 // calls function we saw earlier with param 2 loaded with 1
         2b 00

```

Pretty self explanatory here. Just moves 1 into param 2 and then 2 gets loaded in R14 inside of the function we saw earlier. Could this be the framerate limit we have been looking for?

<div align="center">
<video width="100%" controls >
  <source src=https://img-assets.illusion0001.workers.dev/assets/images/pt-60fps/PT-1080-fps0-demo.mp4" type="video/mp4">
</video>
<em>Footage provided by Patreon Supporter: smasher248.</em>
</div>

Turns out it is! Although performance is too unstable and bounces around from 30 to 60FPS wildly. It may also be using double buffered vsync as well.

## Resolution Hacking

Resolution values are also stored in 4 bytes.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/pt-60fps/pt-ghdra1.png" %}

```
006381be 48 b8 80        MOV        RAX,0x43800000780
         07 00 00 
         38 04 00 00
```

Simply changing this to 1280x720 will allow the game to boot but has some visual issues.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/pt-60fps/pt-res-b.png" %}

<div align=center>
<em>Native 1080p</em>
</div>
{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/pt-60fps/pt-res-a.png" %}

<div align=center>
<em>Upscaled 720p</em>
</div>

If anyone would like to help out and Improve on this inital release of the resolution patch, Pull Requests are very much welcome! Or we can just run it on the PS5 in the future with no compermises to the resolution.

## Results

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/WhRceDucjfQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

<a href="/_patch/SilentHillsPT-Orbis" class="button" role="button">{{ site.theme_settings.download_icon }} Patch Codes</a>

{% include_relative _supporters.md %}
