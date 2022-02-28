---
layout: single
title: "Initial Framerate Patch Release (Work-In-Progress) for Gravity Rush 2"
excerpt: "A fast paced game means fast framerate, right?"
thumbnail: "https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-feature-img.png"
header:
  overlay_image: "https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-feature-img2.png"
  overlay_filter: 0.5
  og_image: "https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-feature-img.png"
categories: patches
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---


# Intro

When I got into framerate patching 8 months ago, I looked at the exclusives on the [PlayStation website](https://web.archive.org/web/20211217080552/https://www.playstation.com/en-us/ps4/ps4-games/) and saw 1 title that seem rather interesting and it does not have a PS5 Patch back then and even now. Not even a framerate unlock on Pro hardware. Yes, I'm talking about Gravity Rush 2 or Gravity Daze 2 if you are in Japan.

## Part 1 - Went out Looking

What's so special about this title that took me so long to breakthrough? First is that there are barely any string references, second is they have their own frame limiter for video playback which also clamps down during gameplay.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-FPS2a.png" %}

<div align=center>
<em>32-33 FPS <i class="twa galciv"></i></em>
</div>

So where do we start? Fliprate to 0 for 60hz output got us that. 32 to 33 framerate limit. And I went on for months, on and off looking for what this is about. And I even managed to break the framebuffer.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-Framebuffer0.png" %}

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-Framebuffer1.png" %}

<div align=center>
<em>Nice looking Jigsaw puzzle</em>
</div>

So I gave up. For a while at least. A few months went by, I decided to take a break and then validate the dozen projects I have, I realized that this game still hadn't gotten a patch from anyone after I put out my findings over on my git page. So I went looking, after a couple of days, I found it.

Looking at the framerate graph, it averages about 33 fps. Why is this important? Because 33fps is 30 milliseconds per frame! You know what that means.

`1000 / 33` equals to 30.. ish. But wait, what happens if we plug this number into the executable?

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-30msSearch.png" %}

A couple results, seems boring. Or so I thought..

```cpp
  lVar3 = sceKernelGetProcessTime();
  uVar4 = lVar3 - (param_1);
  if (uVar4 < 30000) {
    sceKernelUsleep(30000 - (int)uVar4);
  }
  scePthreadMutexLock();
  sceGnmSubmitDone();
```

What's this? It sleeps draw thread for 30ms?

Another case of Japanese developers reinventing the wheel. <i class="twa twa-purple-heart"></i> <i class="twa twa-purple-heart"></i> Its wonderful.

But anyway, removing this code gives us, you guess it, unlocked framerate.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-FPS3.png" %}

<div align=center>
<em>First section of the demo, known to be cpu limited area</em>
</div>

Since I have last published my findings, I have determined that this game is subject to fixed timestep, which means if the game framerate goes above or below the target framerate, it will speed up or slow down. Which in this case is 30 frames a second. 

If you have seen my findings a few months back, you have seen that there's a byte for this particular setup that will purposely set everything to 16.7ms for locked 60 fps gameplay but the thing is, this isn't perfect.

Some sections will softlock the game because the game tick is running twice as fast; so we must implement a check that will set the game back to 30 fps for those problematic sections, otherwise run freely at up to 60 fps, with slowdown in hardware limited areas because we are still using fixed rate.

## Part 2 - Finding Level Names

Saving between two points, the start of epiosde 1 and the end of the epoiode and comparing the results can easily give us the level name we are looking for.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-savedata-compare.png" %}

<div align=center>
<em>Thanks to our Patreon Supporter <a href="https://github.com/ac2pic">ac2pic</a> for their knowledge about Gravity Rush save structure.</em>
</div>

## Part 3 - Coding Kat

For level names we can search for this in memory then save the string into somewhere in the executable for easier access.

```cpp
  if (in_R12 == "ep" /* story episodes */ || in_R12 == "ft" /* free roam */ || in_R12 == "sm" /*side missions*/ ) {
    level_text = in_R12;
  }
  return;
```

The code I'm using here write asset strings into upper portions of memory, so I have to filter out most level prefix names found in the save file. Like `ep` for episodes or `sm` for side missions.

```cpp
  lVar3 = sceKernelGetProcessTime();
  uVar4 = lVar3 - (param_1);
  // if (uVar4 < 30000) {
  //   sceKernelUsleep(30000 - (int)uVar4);
  // }
  scePthreadMutexLock();
  sceGnmSubmitDone();
```

Few commented lines of code, what does this do?

We skipped the code to stall the rendering thread and well it does nothing as you may expect. But there are caveats to this.

Most notable being that if there is nothing to stall the thread, the video playback thread can't keep up and lags behind as a result, if anyone wants to take the challenge of improving on my initial semi working code, feel free to do so. [Patch file](https://github.com/illusion0001/illusion0001.github.io/blob/main/_patches/Gravity_Daze_2_Orbis.md#semi-functional-video-stutter-fix-for-patch-develeopers-only)

```cpp
  int game_flag = 2; // default

if (game_flag == 1) { // 60hz
  const float frametime = 0.01666667;
  const int32 fliprate  = 0;
  sceVideoOutSetFlipRate(handle, fliprate);
  return;
}

if (game_flag == 2) { // dangerous if failed on startup or loading levels
 return;              // But this shouldn't fail because flag is initialized with mode 2
}

if (game_flag == 3) { // 30hz, only use when softlock mode is true
  const float frametime = 0.03333334;
  const int32 fliprate  = 1;
  sceVideoOutSetFlipRate(handle, fliprate);
  return;
}
```

Alright, what does all this do exactly? Let's go one by one.

The variable game flag is something I created, this is to keep track of what state the game is currently in. 

When it is `1` set the constant for the fixed timestep to 16.7ms and set the fliprate to 0 for 60hz output. As a reminder, we have already skipped the code to sleep the render thread so this should work.

When it is `2` it does nothing, the function gets called and it just exits. This is to prevent any render thread hard lock during the game initialization period.

And `3` as you guess, swaps to 30 fps and timestep to 33.3 milliseconds.

```cpp
string level_name = ep_xxx; // default

if (   level_name == ep00_c /* regression, todo: is this caused by our code? */ 
    || level_name == ep01_com
    || level_name == ep01_d 
    || level_name == ep02_a ) {
        game_flag = 3; // 30hz
} else {
        game_flag = 1; // 60hz
    return;
  }
```

This one checks during level changes, if any of the levels matched, set the game back to 30 fps, then 60 once we leave that particular area or level of the game. The example being the end of the intro, first episode and the tutorial of episode 2. Note that the intro having a softlock is a regression potentially in my code? I'll look into it at a later date but it should not be a big deal.

## Showcase

**A minor correction to the video, the resolution showed in the video was 1920x1080 (1080p) not 1280x720 (720p). A blur has been added to avoid confusion.**

This patch is best experinced on PS4 Pro with 1080p output and supersampling disabled.

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/-vlwychcrx0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

{% include_relative _orbis_install_note.md %}

<a href="https://github.com/illusion0001/illusion0001.github.io/blob/main/_patches/Gravity_Daze_2_Orbis.md" class="button" role="button"><i class='fas fa-download'></i> Patch Code</a>

{% include_relative _supporters.md %}
