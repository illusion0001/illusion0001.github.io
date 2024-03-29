---
layout: post
title: "60FPS Patch for Life is Strange and Before the Storm"
excerpt: "The upgrade PS4 owners never got. Until now."
categories: patches
tags: lis bts ps4 patches
header:
  teaser: "https://img-assets.illusion0001.workers.dev/assets/images/wif-dawn-60fps/dawn-banner.png"
  overlay_image: "https://img-assets.illusion0001.workers.dev/assets/images/wif-dawn-60fps/dawn-banner.png"
  overlay_filter: 0.5
  og_image: "https://img-assets.illusion0001.workers.dev/assets/images/wif-dawn-60fps/banner2.png"
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---

{% include_relative _orbis_console_note.md %}

# Cursitory

I have been experimenting with unlocking framerate with success in [Silent Hills: P.T.](/patches/2021/04/29/pt-60fps/) and I always wondered if the Base PlayStation 4 Hardware could achieve 60FPS on two of my most beloved titles. Life is Strange and it's prequel Before the Storm.

As of the writing of this post, Xbox Users now gets a 'patch' from the Xbox Team allowing for higher framerate on Series X and S Consoles!

> Life is Strange (@LifeIsStrange) on Twitter:
> 
> We can’t wait for fans to experience #LifeisStrange and #LifeisStrange2 now with FPS boost on Xbox Series X & S!

[Tweet](https://twitter.com/lifeisstrange/status/1390694180549283849)

## Lifting 30FPS Limit in Unreal Engine 3

In my [previous](/patches/2021/04/29/pt-60fps/) post we have already established that vsync flip rate or interval is most likely responsible for controlling the target. It can be called `SceVideoOutFlipRate` or `SceVideoOutSubmitFlip`.

I'll use the same method of finding function responsible for controlling the target framerate mode here and it may end up being easier than I initally thought!


For the first game and that is Life is Strange, searching for just `flip` yields some results. 

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/wif-dawn-60fps/ghidra_flip_search.png" %}

<div align=center>
<em>SubmitFlip but no fliprate? Let's search for more</em>
</div>

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/wif-dawn-60fps/ghidra_vsync_search.png" %}

<div align=center>
<em>Vsync in Unicode string came up with more interesting results</em>
</div>

```
012bb916 48 8d 35        LEA        param_2,[u_togglevsync_02fd8598]
         7b cc d1 01
012bb938 48 8d 05        LEA        RAX,[DAT_03875828]
         e9 9e 5b 02
012bb94c 89 88 60        MOV        dword ptr [RAX + 0x360]=>DAT_03875b88,ECX
         03 00 00
```

togglevsync catched my interests and it points to a memory location, let's see what happens when its set to 1.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/wif-dawn-60fps/wif_screentear.png" %}

<div align=center>
<em>Unlocked Framerate! But it has no limits and introduce a lot of screen tearing</em>
</div>

```
018a2dfc 83 b9 60        CMP        dword ptr [RCX + 0x360]=>DAT_03875b88,0x0
018a2e16 0f 84 8c        JZ         LAB_018a2ea8
         00 00 00
         03 00 00 00
018a2e77 b0 01           MOV        AL,0x1
018a2ea4 77 aa           JA         LAB_018a2e50
```

This looks interesting, it moves 1 into AL and there's JA which stands for Jump Above in x86 asm. I don't have much idea as to what's going on here but I tried setting this AL instruction to 0 and removing this Jump instruction seem to solve the issues I had with screen tearing and it now limits to 60FPS.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/wif-dawn-60fps/wif-60fps.png" %}

<div align=center>
<em>Aw yeah. That's more like it. 60FPS and no Screen Tearing</em>
</div>

## Lifting 30FPS Limit in Unity

How about Before the Storm?

This title runs on unity. Let's try to simply search for flip in function name and see what we get.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/wif-dawn-60fps/ghidra_flip_search2.png" %}

```
01e53d99 45 85 f6        TEST       R14D,R14D
01e53d9c 74 15           JZ         LAB_01e53db3
01e53d9e 8b bb a0        MOV        param_1,dword ptr [RBX + 0x2a0]
         02 00 00
01e53da4 31 f6           XOR        param_2,param_2
01e53da6 41 83 fe 01     CMP        R14D,0x1
01e53daa 40 0f 95 c6     SETNZ      param_2
01e53dae e8 dd cf        CALL       sceVideoOutSetFlipRate
         1b 00
```

Seems like this jump will not set a zero and skip calling this function entirely. But there's a Set Not Zero here. Which I think will set it to 1? How about Set Zero.

`01e53daa 40 0f 94 c6     SETZ      param_2`

Let's test this change in game.

<div align="center">
<video width="100%" controls >
  <source src=https://img-assets.illusion0001.workers.dev/assets/images/wif-dawn-60fps/dawn_60fps_preview.mp4" type="video/mp4">
</video>
<em>It worked!</em>
</div>

# Result

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Oy2CapKF3gE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

<a href="/_patch/LifeisStrange1-Orbis" class="button" role="button">{{ site.theme_settings.download_icon }} Patch Code: Life is Strange</a>

<a href="/_patch/LifeisStrange1-BeforetheStorm-Orbis" class="button" role="button">{{ site.theme_settings.download_icon }} Patch Code: Life is Strange Before the Storm</a>

{% include_relative _supporters.md %}
