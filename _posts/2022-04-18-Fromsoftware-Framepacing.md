---
layout: single
title: "Framepacing Fixes for Fromsoftware Titles (PS4)"
excerpt: "Players dealt with bad framepacing on consoles since 2015."
header:
  teaser: "https://drive.google.com/uc?id=1f1i-BAB5mb6CDoGOuk3TtKwzVGCp9SG_"
  overlay_image: "https://drive.google.com/uc?id=12_4ONkFLi3O52GcRj4f0ywEaTRBRRx8U"
  overlay_filter: 0.5
  og_image: "https://drive.google.com/uc?id=1f1i-BAB5mb6CDoGOuk3TtKwzVGCp9SG_"

categories: patches
tags: fromsoftware bloodborne darksouls eldenring sekiro patches
twitter: {card: "summary_large_image"}
toc: true
toc_sticky: true
---

<!--
If things went to plan, you're probably here from the digital foundry video.

Hi there! (Wave emoji)
-->

{% include_relative _orbis_console_note.md %}

# Intro

If you have ever played a recent fromsoftware games on console, be it Bloodborne, Dark Souls 3 or the recently released Elden Ring. You may have noticed something off about the presentation. One being that it feels more stuttery than other games with a 30 fps cap. And the other is inconsistent framerate on the enhanced consoles. With the framerate going up and down as it pleases depending on what is happening on screen.

Let's address the first issue. Improper frame pacing. It is an issue that started to occur on the 8th generation era with Bloodborne.

{% include img1 image_path="https://drive.google.com/uc?id=1shHX-kkp7223R1Pe3XMzOryqOl_tsUzW" %}

<div align=center>
<em>Yikes. <i class="twa twa-grimacing-face"></i></em>
</div>

Now let's go back to the previous generation, the PS3/Xbox 360 era.

{% include img1 image_path="https://drive.google.com/uc?id=1arDjcAAhD-TF3gmfIrBWqjnc18_FTh1g" %}

Dark Souls on Xbox 360, no issues here. A consistent 30 fps when it meets the framerate target.

How about Demon Souls?

{% include img1 image_path="https://drive.google.com/uc?id=1bUWo1k9p0LTiXHMW6zCjpoxcBT8RpApF" %}

Yep, no issues here either.

## What Went Wrong?

I could only speculate on the decision to implement their own framerate cap for multi plat games is portability. Not having to deal with API calls for each console is a definite win but they did not realize *if* their timer precision was off, it will cause inconsistency in frame delivery.

But there's something even more strange. Checkout this [video](https://youtu.be/BN_4-d1wPQw?t=162) from VG Tech where they showcase Dark Souls 1 in Backcompat Mode on Xbox One and..

<div align="center">
<video width="100%" controls loop>
  <source src="https://drive.google.com/uc?id=1oTFDTCpRoOhF7UK1rVHfbMtFuo_hP9zc" type="video/mp4">
</video>
</div>

Bad framepacing on the newer consoles but not original hardware? Very strange indeed. <i class="twa twa-thinking-face"></i>

## The Simple Fix

So what are the solutions? A very simple fix to this would be to call the relavent API function calls equivalent to the platform.

Here are some suggestions.

| Platform | API Calls |
|---|---|
| PS3 | cellGcmSetFlipMode |
| PS4/PS5 | SceVideoOutFlipRate |
| Xbox 360 | [D3D::PresentInterval](https://docs.microsoft.com/ja-jp/previous-versions/windows/desktop/bb322831(v=vs.85)) |
| Xbox One/Series S/X | [IDXGISwapChain::Present](https://docs.microsoft.com/ja-jp/windows/win32/api/dxgi/nf-dxgi-idxgiswapchain-present) |

But calling these functions and giving them appropriate device handle is not enough to fix the issue. We must also lift the game's broken framerate limiter as well.

Either by changing `Game.FlipMode` in the code to `60FPS_*` or changing minimum frame update time from 33.33ms to 16.67ms. Let's see the changes.

Here's bloodborne with the frame pacing issues resolved.

{% include img1 image_path="https://drive.google.com/uc?id=10HYbWayElGcMSVbRsl5NpuY3AOaQrcRa" %}

Volla! With just a few lines of code, we get proper and consistent 30 frames per second! Killing two bug reports with one stone.

The same fix also applies for the uncapped framerate on the enhanced consoles in Dark Souls 3 and later titles. though when implementing this in reality, the framerate cap **must** always be an option rather than forcing it on the user.

## Trivia

Here's a little bit of trivia for you, there's already deltatime calculated for the framerate counter among other things.

{% include img1 image_path="https://drive.google.com/uc?id=1FAi3Iy5MvVJlbIK8Ise1mMSrzdkAnVji" %}

But fromsoftware did not use this until the release of Dark Souls 3. Which is also how I ported the framerate patch for Bloodborne by [Lance McDonald](https://twitter.com/manfightdragon) to the [Network Test](/_patch/BloodborneNetworkTest-Orbis/) version.

## Closing words

That is all I have for you today, you can support me using the links below and thanks to the patrons and you for reading!

Catch you next time where we race against opponents in a sea of mud with big trucks?

## Showcase

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/gxsnY6l-iPI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Patches

- <a href="/_patch/Bloodborne-Orbis/" class="button" role="button"><i class='fas fa-download'></i> Patch for Bloodborne</a>
- <a href="/_patch/DarkSoulsIIITheFireFadesEdition-Orbis/" class="button" role="button"><i class='fas fa-download'></i> Patch for Dark Souls 3</a>
- <a href="/_patch/SekiroShadowsDieTwice-Orbis/" class="button" role="button"><i class='fas fa-download'></i> Patch for Sekiro</a>
- <a href="/_patch/EldenRingNetworkTest-Orbis/" class="button" role="button"><i class='fas fa-download'></i> Patch for Elden Ring: Network Test</a>

Need help with installing the patches?

Check out the [Installation Guide](/install-instructions/).

{% include_relative _supporters.md %}
