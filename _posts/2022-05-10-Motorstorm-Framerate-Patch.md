---
layout: post
title: "Patches and Improvements for MotorStorm Titles (RPCS3)"
excerpt: "PS3 racing exclusives at 60FPS. No motion blur and Dynamic Resolution Scaling."
header:
  teaser: "https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/cover-thumbnail-ms3.png"
  overlay_image: "https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/cover-thumbnail-ms3.png"
  overlay_filter: 0.5
  og_image: "https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/cover-thumbnail-ms3.png"

categories: patches
tags: [ rpcs3, "Motorstorm", "PS3 Motorstorm", "Evolution Studios" ]
twitter: {card: "summary_large_image"}
toc: true
toc_sticky: true
---

A beloved classic franchise from Evolution Studios. Where we race against AI and online opponents in muddy race tracks with big trucks, sounds exciting? Because it is!

## Original Experience

Motorstorm Titles on PS3 ran at a wobbly 30FPS, 720p with dynamic resolution scaling, that's right the game has DRS, all the way back in 2006.

Low sample motion blur, although it looks fine at it's original resolution and framerate but it does not hold up particularly well at high resolution and framerates and at first sight, fixed timestep. <i class="twa-2x kat-angry"></i>

## Hidden Gems - Part 1 (Framerate Modes)

Running the game on the RPCS3 emulator with increased vblank shows disappointing results. sped up gameplay.

<div align="center">
<video width="100%" controls muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/video-ms1-no-delta-30fps-target.mp4" type="video/mp4">
</video>
</div>

<div align=center>
<em> Look at it go! The game is so fast it might hurt. </em>
</div>

The hidden gem here is game speed. When you crash your vehicle, the game slows down to 0.125f. And normal gameplay it's 1.00f. peeking at this area shows some curious values.

`3F 80 00 00 00 00 00 02 00 00 00 00 01`

Setting the byte 2 to 1 gives us..

<div align="center">
<video width="100%" controls muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/video-ms1-no-delta-60fps-target.mp4" type="video/mp4">
</video>
</div>

60FPS Gameplay? Alright, that's cool but it's still fixed timestep and double speed at 120FPS.

Not shippable if you ask me.

Let's pay a little more attention to what's *down below*, what happens if I set this next int32 to 1... <i class="twa-2x kat-smug"></i>

<div align="center">
<video width="100%" controls muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/video-ms1-delta-120fps.mp4" type="video/mp4">
</video>
</div>

<div align=center>
<em> Is that Deltatime? </em>
</div>

I apologize if that clip made you all jelly. It did for me seeing it for the first time as well.

The same memory pattern exists in other games all the way to Motorstorm RC.

As for the names, the files were left bare within MotorStorm: Pacific Rift.

```lua
-- globalparams.lua: auto-generated by GoStorm2 at 17/07/2007 14:28:25
FrameRateMode("30Hz Lock")
-- Possible values:
-- See game_config.xml for more info.
-- 30Hz Lock    -- 30 FPS    (No Havok Deltatime) -- Default for all games.
-- 60Hz Lock    -- 60 FPS    (No Havok Deltatime)
-- Compensation -- Deltatime (Use Havok Deltatime)
```

## Blur, Blurryness Everywhere - Part 2 (Dynamic Resolution Scaling)

Two things stood out to me when I played this with the unlocked framerate, the image can become blurry out of nowhere and the motion blur doesn't look as good.

Let's start with the most obvious image quality flaw, dynamic resolution scaling. The game scales the resolution based on frametime targets, if it is below its threshold of 33.3ms, the game drops its resolution to 360p at it's lowest, to find it? 720p during the clearest moments and `Decreased Values` when things get blurry.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/Screen_MS1-3.png" %}

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/Screen_MS1-4.png" %}

I narrowed it down to this subroutine (`0x002634c8`) with a compare float statement and all I have to do is to skip this operation, simple.

## Blur, Blurryness Everywhere - Part 3 (Motion Blur)

Peeking at the game executable and searching for Blur, I got a few results. `WorldMotionBlurBase` `BlurAccel` and `BlurDecel`. This smells like some sort of configuration key. Let's try memory.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/Screen_MS1-5.png" %}

<div align=center>
<em> Oh, what's that? Game settings? </em>
</div>

<details>
<summary>advancedsettings.lua (Click to Expand)</summary>

{% highlight lua %}
-- Taken from NPEA90006/NPEA80017 1.01 at address 0x300767ba

-- Begin original file:
-- advancedsettings.lua: auto-generated by GoStorm2 at 28/02/2007 10:28 am
WorldMotionBlurBase(0.55)
CarMotionBlurBase(0.43)
BoostBlurEnabled(true)
BlurAccel(0.01)
BlurDecel(0.01)
WorldBlurMax(1)
CarBlurMax(1)
ParticleEmissionRate(1)
VehicleDamageRate(0.81)
{% endhighlight %}

</details>

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/Screen_MS1-6.png" %}

Setting these to 0.0f gets rid of the motion blur and it looks good!

<div align="center">
<video width="100%" controls muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/video-ms1-no-blur.mp4" type="video/mp4">
</video>
</div>

## Blur, Blurryness Everywhere - Part 4 (Porting to Newer Games)

Get ready because the things we learned in the past two sections of this post is going to be thrown out the window, Starting with Motorstorm Pacific Rift, they changed the settings to use the XML format and the code being much easier to read.

```cpp
// Motorstorm RC for demonstration, similar code is used in Pacific Rift and Apocalypse.
// at 0x001a8050 for NPUA80678 01.02
ParseFile("scripts/viewportquality.xml");
// -- snip --
GetSectionKeyName       = ParseSectionKey("General");
bool GetBoolValFromFile = ParseValueKey("enableMotionBlur");
// <General enableMotionBlur="true"/>
enableMotionBlur = GetValFromFile;
```

Take `enableMotionBlur` for example, the game code looks for this key in a file named `viewportquality.xml` within the `scripts` folder and reads this value, and since this may change depending on user tweaks, let's always load this variable using the load intermediate instruction.

The same can be done for `variableScaling` (Dynamic Resolution Scaling)

Comparison Images:

<div align=center>
<em> Before: </em>
</div>

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/Screen-MS2-0.png" %}

<div align=center>
<em> After: </em>
</div>

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/Motorstorm-Framerate-Patch/Screen-MS2-1.png" %}

<div align=center>
<em> Checkout how crisp that image looks! Very clear and clean of blur. </em>
</div>

<div align="center">
<video width="100%" controls autoplay muted loop>
  <source src="https://img-assets.illusion0001.workers.dev/assets/misc/youtube/GravityDazeOverture-Kat-Happy.mp4" type="video/mp4">
</video>
</div>

<div align=center>
<em> <a href="https://youtu.be/tFeXtu-3u78?t=70">Gravity Rush: The Animation - Overture | Parts A & B</a> </em>
</div>

I won't lie, this is actually me when I figured out that hidden deltatime feature in these games.

I have already covered MLAA in a [previous post](/patches/2021/02/11/ms3-mlaa/) of mine for Motorstorm Apocalypse so if you are interested, check it out!

## Closing Words

That's going to be it for this post, if you like it be sure to share this with others and let them know that if they have a powerful PC, high framerate Motorstorm is a reality, enjoy your enhanced video games!

Oh and one more thing, I wished we got a remaster for these games on the current platform, would be interesting to see how that plays out. Yes, including Driveclub and my beloved Gravity Rush (Gravity Daze) 2

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/memes/capture/screen-console-ports-meme.png" %}

<div align=center>
<em> <a href="https://youtu.be/tFeXtu-3u78?t=485">Gravity Rush: The Animation - Overture | Parts A & B</a> </em>
</div>

Ah well, I guess emulation will do just fine on our computers.

## Showcase

<iframe width="560" height="315" src="https://www.youtube.com/embed/-AszzQQ7RI0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Patch

{% include_relative _generic_rpcs3_patch_note.md %}

{% include_relative _supporters.md %}
