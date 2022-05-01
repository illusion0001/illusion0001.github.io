---
layout: single
title: "Framerate Patch and Intro Skip for God Of War 3/Ascension (RPCS3)"
excerpt: "Experince God of War 3 and Ascension with its addicting hack and slash action at 120FPS and beyond."
header:
  teaser: "https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Screen_thumbnail0.png"
  overlay_image: "https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Screen_thumbnail0.png"
  overlay_filter: 0.5
  og_image: "https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Screen_thumbnail0.png"

categories: patches
tags: [ rpcs3, "God of War", "GOW3", "GOWA" ]
twitter: {card: "summary_large_image"}
toc: true
toc_sticky: true
---

The Motorstorm post has been postponed! ~~(Admittedly I haven't even start writing it)~~

With the recent PC release of [God of War (2018)](https://store.steampowered.com/app/1593500/God_of_War) patches for the series are becoming more relevant than ever. This post will be a little on the longer side because there's a lot to elaborate on. Let's get into it!

## Intros or No Intros

The PS3 God of War games has two stages of its intro section. One being the Sony logo and the Santa Monica videos.

### Simple Text

Let's start with the simplest. The background with text. The game spawns `IntroLoaderThread` PPU thread for this and the solution here is to skip this process.

### Harder Videos

It took me a while to figure this one out. At first I thought the game referenced the filenames found within the executable, the files being `SMLogo` and `openingCredits` but removing these references in the executable still plays it, so I gotta come up with a solution.

It turns out the solution was right in front of me. You see, once you start a new game or save it, on subsequent runs, the game enables a boolean on the second intro video, allowing the users to skip the video with the press of the X button. I have a genius idea. What if we always enable this boolean and send the X button input?

<div align="center">
<video width="100%" controls loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Game_SkipDemo.mp4" type="video/mp4">
</video>
</div>

The game boots up and there's no intro, but there's one problem, since this code will always run when there's a video playing, meaning it will skip every video that plays, so that's not very desirable. I passed my working code to [ZEROx](https://www.youtube.com/user/ZEROx2085) and we came up with a solution:

```cpp
    int controller_button = cellPadGetData();
    int frame_count = 0;
    bool UserPressedSkipButton  = false;
    bool VideoIsFinshed         = false;
    char[] video_name = m2v_files;
    if (video_name == "SMLogo" || video_name == "openingCredits" )
    {
      skipAlways();
    }
    else {
    skipOnbuttonPress();
  }

void skipAlways() {
  bool UserPressedSkipButton = true;
  bool VideoIsFinshed        = true;
  return;
}

void skipOnbuttonPress() {
  if (controller_button == DEFINE_ACTION_BUTTON /* 64 */ ) {
    bool UserPressedSkipButton = true;
    bool VideoIsFinshed        = true;
  }
  return;
}
```

What this code does is it checks if the video filenames match. If they do, we call into the always skip video subroutine. The benefit of this being that it will only skip the intro videos and not the rest of the game, which is handy for those who do not want to watch intros every time they want to play.

## Static and Dynamic Framerates

In all God of War games, they have deltatime. It calculates the difference between the amount of time it takes to push a frame onto the display and writes that delta between the frames to game logic and other things. But since this is code from the PS2 era, things are weird. They have a specific range the game runs at: 15 to 60FPS. Going below 15FPS will snap to the maximum frametime of 66.67ms, going above 60 will snap to 16.67ms. meaning if you wanted to run the games at 120FPS, you'll get double speed.

But of course, if there is a will, there is a way, at least for the PS3 titles.

The code is very similar between them so we won't explain it for both games, but here's how it goes:

In memory, the game keeps track of a lot of things during gameplay. The area of interest is `0x006406f0`.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Screen_memarea3.png" %}

This area holds: framerate (int32) and frametimes (float32). Setting a breakpoint on the constantly writing floats gives us a few clues, one is it leads to this rather complicated sub at `0x0026b674`, I have not analyzed this one myself but I can tell that it has very important key information which helped us solve the puzzle.

```cpp
MinFPS = target_FPS / ( 400 / 100 );
```

This snippet of code divides the maximum framerate by 4 times a 100. Which adds up to 60/4 = 15. Simple. And changing this to 5000 gives us a minimum framerate of 2. Looking just a little closer, there's -1.0 on this load float instruction. 

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Screen_Ghidra0.png" %}

That looks interesting, let's check it out in memory, and..

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Screen_FPSConst1.png" %}

A constant of 59.94. How interesting.

And the code that gives us this value is even more interesting:

```cpp
  if (frame_height == 576) {
    SetMaxFPS(50.00); // PAL
  }
  else {
    SetMaxFPS(59.94); // NTSC
  }
```

It compares if scanline height is 576 for PAL users, and if so sets the max FPS to 50.0, else (usually 480 lines) 59.94.

How about we change this to 120?

<div align="center">
<video width="100%" controls autoplay muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Game_120FPSDemo4.mp4" type="video/mp4">
</video>
</div>

Is that God of War 3 at up to 120FPS?

Yes, it is.

But the game is currently broken. There are two problems,

<div align="center">
<video width="100%" autoplay muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Game_ChainBugDemo.mp4" type="video/mp4">
</video>
</div>

<div align="center">
<video width="100%" autoplay muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/GOW-PS3-FPS-Patches/Game_WaterBugDemo.mp4" type="video/mp4">
</video>
</div>

One with the super slow chain swing and two when kratos dives into the water, causing the game to freak out and be stuck in a loop. The solution? Set the reading float to a static 60.

During our testing, we discovered that this patch (accidentally) fixed a very annoying bug: out-of-sync in-game cinematics.

<iframe width="560" height="315" src="https://www.youtube.com/embed/r1sGjetEHz0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

That's an unexpected bug fix! <i class="twa twa-party-popper"></i> The best kind.

## Closing words

If there are more bugs that you have found with our patch, please post them in the comments and a save file so we can investigate.

Join in next time where we actually get to see mud tracks and big trucks! Stay tuned!

## Patch

{% include_relative _generic_rpcs3_patch_note.md %}

{% include_relative _supporters.md %}
