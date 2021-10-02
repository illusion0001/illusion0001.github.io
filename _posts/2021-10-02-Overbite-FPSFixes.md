---
layout: post
title: "Patches for MediEvil (PS4 Remake)"
excerpt: "Resolving bad frame-pacing and patching the resolution."
thumbnail: "https://assets.illusion0001.workers.dev/0:/assets/images/Overbite-FPSFixes/overbite-thumbnail.png"
feature-img: "https://assets.illusion0001.workers.dev/0:/assets/images/Overbite-FPSFixes/overbite-feature.png"
image: "https://image.api.playstation.com/cdn/UP9000/CUSA11227_00/BJZksSXNxOU0vmTCa79nr7ULJM3F6a6B.png"
categories: patches
tags: [Articles, Releases]
twitter: {card: "summary_large_image"}
---

* TOC
{:toc}

# Intro

Another classic gets a complete overhaul in Graphics, Gameplay and the works but of course not all things are perfect and this game is no exception. When I first boot up the game for the first time, went into the options menu and it got me curious.

<p align="center">
<img src="https://assets.illusion0001.workers.dev/0:/assets/images/Overbite-FPSFixes/overbite-settings.png">
</p>

A 30FPS Cap option in the menu, but is it any good?

<p align="center">
<img src="https://assets.illusion0001.workers.dev/0:/assets/images/Overbite-FPSFixes/overbite-fps-borked.png">
<em>No, it is not.. :(</em>
</p>

Time for a fix and a good ol' resolution patch for 60FPS in some cases.

## Part 1 - Patching Resolution

Patching resolution in Unreal Engine 4 games has become easier than ever, usually you can guess 100.0(float) as the target and find the correct one in memory.

```cpp

MyResOverride(); // call
                 // vars renamed for easier reading

void MyResOverride(void)

{
  var.ResScale = 0x42860000; // write to memory 67.00f
  vmovss_avx(var.ResScale);  // read to xmm0, original instruction
  return;
}

```

Easy as that.

I heard that the PS4 Pro version does not have support for 4K displays, meaning if you run the game on a 4K TV Set, it will still output at 1080p.

## Part 2 - Fixing Frame-Pacing

In Unreal Engine, there is two ways at least that I know of to cap the framerate.

There is Sync Interval, which will cap to frametime.

And there is Max FPS, which instead will cap to framerate but very loosely as we saw earlier.

Toggling the option in the menu on and off lands on a float, when on it is set to 30.0(float) and when off it's set to 60.0(float), pretty simple.

A way to fix this is to completely ignore Max FPS and instead use the sync interval variable instead. it provides much better frametime stability and no stutters.

```cpp

  FpsFunction(); // call
                 // vars renamed for easier reading

void FpsFunction(void)

{
  vucomiss_avx(var.MaxFPS);   // original memory address
  if (var.MaxFPS) == 30.00) { // 0x41f00000
    var.SyncInterval = 2;     // 30.0hz (33.3ms)
  }
  else {
    var.SyncInterval = 0;     // 60.0hz (16.6ms)
                              // (unlimited with vsync off)
  }
  return;
}

```

What this code does is it checks if the value in memory is `30.00` or not, if it is, set `var.SyncInterval` to 2 for 30FPS or else, set it 0 which is the default.

To the developers, can we get this fix in a official patch? and even better, 4K support.

# Results

See the video below for a comparison between the patched versions.

<div align="center" class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/_FyHCSwze_8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

<a href="https://github.com/illusion0001/illusion0001.github.io/blob/main/_patches/Overbite-Orbis.md" class="button" role="button"><i class='fas fa-download'></i> Patch Code</a>

{% include_relative _supporters.md %}
