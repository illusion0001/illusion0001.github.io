---
layout: single
title: "Bug Fix: The Last of Us Part 2 Broken Aim After Using The Bow"
excerpt: "Shaky aiming camera after using the bow is now fixed!"
header:
  teaser: https://drive.google.com/uc?id=1a-euvDHvVRPHkEETIs5Snm4UKGgEWttm
  overlay_image: https://drive.google.com/uc?id=1a-euvDHvVRPHkEETIs5Snm4UKGgEWttm
  overlay_filter: 0.5
  og_image: https://img-assets.illusion0001.workers.dev/assets/images/t2-bow-charge-bugfix/t2-thumbnail-video-no-text1.png

categories: patches
tags: [ "ps4", "modded console" , "The Last of Us Part 2", "Bug Fixes" ]
twitter: {card: "summary_large_image"}
toc: true
toc_sticky: true
---

# Introduction

Hello! <i class="twa-2x twa-waving-hand"></i>

It has been a while since my last post, why's that?

I had worked on a few things.

- Plugin system in collabration with [Sistro](https://github.com/SiSTR0), [OSM](https://github.com/OSM-Made), [jocover](https://github.com/jocover) and a few other [developers](https://github.com/GoldHEN/GoldHEN_Plugins_Repository#coded-by). A [video](https://youtu.be/gt_H45SpaAE) by [Modded Warfare](https://www.youtube.com/@MODDEDWARFARE) covered this quite well.
- This post you are reading right now! That's right, new year new bugfix!

I have been working on this bug for the past few months on and off and I'm happy to say that it is fixed!

## Part 1 - Problem at hand

This bug sounds even more strange than my previous bug fix post about the [Infected Severed Head Crash Bug](/patches/2021/02/15/t1-head-crash-bug-fix/) for the PS3/PS4 games.

Good thing is, it was officially fixed by the developers in the Re-Remaster on PS5!

<div align="center">
<video width="100%" controls loop muted>
  <source src="https://drive.google.com/uc?id=1L3C1rkZMLTeapMJrTesPLy42GFWYHj0h" type="video/mp4">
</video>
</div>

Thanks to [The Kempy](https://twitter.com/Kempy161) for testing!

Now what exactly is this broken aim bug?

in The Last of Us Part 2, Naughty Dog developers implemented a tiredness feature, where the player charges the bow after a certain amount of time, the aim will become shaky.

<div align="center">
<video width="100%" controls loop muted>
  <source src="https://drive.google.com/uc?id=1WwLgpxsf8itsRlhSomuS7NM9ADgh4H52" type="video/mp4">
</video>
</div>

But here comes the weird part, they do not reset this factor correctly, leaving the player's aim shaky even after a few minutes.

The only way to get out of this bugged aiming mode is to Restart to Checkpoint or Quit and reload your save.

## Part 2 - Looking into the Bug

Some observations I noticed when I first investigated the bug back in September of 2022 when it was brought to my attention thanks to the speedrunner [Anthony Caliber](https://www.youtube.com/@AnthonyCaliber).

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Kl4PrVXVBEk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- The charge time is always 20 seconds.
- The camera becomes shaky quite fast after charging the bow for 15 seconds.
- It can be partially fixed by charging or firing the bow but aiming is still quite shaky, so not entirely fixed.

Let's search for some values.

I'll tackle the charge time first, since it is the only constant variable so far.

20 seconds.. timers is usually a float, for example most game delta time calculations, it is a float. `0.03333` is 33 milliseconds. and `1.0000` is 1000 milliseconds which in turn is 1 second.

After searching for a while and modifiying every `20.0f` floats, memory location `0x110F559E14` is the address the game reads for the charge time.

Let's try setting this one to 4 seconds.

<div align="center">
<video width="100%" controls loop muted>
  <source src="https://drive.google.com/uc?id=1IkrMxWjVbtHx4LFeiiakbwJYxk2DA85O" type="video/mp4">
</video>
</div>

Check that out, the player can only charge the bow for 4 seconds now.

A breakpoint leads to this instruction.

```
01555a6d VMOVSS XMM0,dword ptr [RAX + RCX*0x4]
```

{% include img1 image_path="https://drive.google.com/uc?id=1RwiWFQDgKG9mkrtIwWnUZKssnIPiz7OK" %}

Hmm, two vector floating reads. What if I step there?

{% include img1 image_path="https://drive.google.com/uc?id=1P1c1HPLTtndT0Vo-amZHHSnRD_puHLiA" %}

Aha! `xmm1` seems to contain our current time.

Let's write some small code to display these.

{% include img1 image_path="https://drive.google.com/uc?id=1RqIKyjVQ6li7uLTAjIT7lIc0lAw4M0sJ" %}

Yep, this is it. Now we have the max charge time and the current charge time.

Now the multiplier. We know that it increases over time and decreases when we charge the bow.

This took a while to find but luckliy, I found it!

Here I changed the value to `10.0f` and aiming a shotgun does this:

<div align="center">
<video width="100%" controls loop muted>
  <source src="https://drive.google.com/uc?id=1Ca1nMESfTOiILYXk7JvE5x1bvmou7yEj" type="video/mp4">
</video>
</div>

Woah, Ellie needs to take a break from fighting all day huh.

I can't give any memory location for this one since it is not static (I learned this the hard way). So I set some breakpoints and these two instructions stood out to me.

```
015550b7 VMOVSS dword ptr [R14 + 0x4a0],XMM0 ; this one writes when aiming
0155577d VMOVSS dword ptr [R14 + 0x4a0],XMM0 ; this one writes when charging bow
015c9011 VMOVSS XMM3,dword ptr [RAX + 0x4a0] ; this one always reads when bow is eqiup
```

The write instruction is in the same area as the charge timers, if I stub this function `015547a0`, the bow no longer works.

Let's give it a name.. How about `BowController`? that sounds pretty good.

{% include img1 image_path="https://drive.google.com/uc?id=1RZnrdmbsh6GP7dl8aEWYlIY3FfCjKucJ" %}

Alright, we have found all three key piece of the puzzle.

- 1) Max Charge Time
- 2) Current Charge Time
- 3) Sway multiplier

## Part 3 - Fixing the Bug

But how will we fix it? I have some ideas.

- Always resetting the multiplier to `1.0f`.
- Implementing a cooldown timer after using the bow.

I will go with the latter, because I think the developers wanted a tiredness effect after using the bow for some time but this bug goes unnoticed, let's fix it for them.

```c
// Pusedo code for the patch, may not be 100% accurate, see sources at
// `https://github.com/GoldHEN/GoldHEN_Patch_Repository/blob/a92199c51bf86ffe10e4413928f6a6872928269f/patches/json/TheLastOfUs2-Orbis.json#L547`
// for more info.

#include "ndlib/process/clock.h" // GetProcessDeltaTime

extern bool is_using_bow;
extern float bow_charge_time;
extern float bow_max_charge_time;
extern float weapon_sway_mul;
float cooldown_timer = 0.0f;

void bow_charge_fix(void)
{
    if (weapon_sway_mul == 1.0f) // the default is 1
        return;
    float max_cooldown_timer = 15.f;
    float current_timer = GetProcessDeltaTime();
    if (is_using_bow)
    {
      cooldown_timer = 0.f;
      return;
    }
    if (cooldown_timer > max_cooldown_timer)
    {
        weapon_sway_mul = 1.f;
        cooldown_timer = 0.f;
        return;
    }
    // Count timer up
    cooldown_timer = cooldown_timer + current_timer;
    return;
}
```

Let's test this change in-game.

<div align="center">
<video width="100%" controls loop muted>
  <source src="https://drive.google.com/uc?id=1cF3z2lLy3MxkfGtYiZw9HuiNkNMmCYaz" type="video/mp4">
</video>
</div>

The timer counts up after using the bow, resets after 15 seconds and most importantly, resets the sway multiplier!

By the way, for those who want to see the stats for themselves can do so. I have included all the patches shown in this post in the patch file.

{% include img1 image_path="https://drive.google.com/uc?id=16AjsWBmGZz1Y0RUQZtiV_cC11JSwl57R" %}

You will need to enable the following patches:

- Enable Dev Menu
- Bug Fix: Broken Aim After Using The Bow

And in the debug menu, `Dev Menu|Weapons|Bow and Arrow|Show Bow Charging` option. The menu can be opened by pressing `L3+Touchpad Right`

# No Fix for Newer Platforms?

You may have noticed that I did not fix the bug in the recently released The Last of Us Part 1 on PS5, that is because the system have not been fully exploited yet.

Though when the PC version comes out, I will fix it if the developers have not fixed it by then.

# Official Fix is Possible

If someone can get me in touch with the right people, this fix can be done officially! Both for the PS4 and PS5 games.

My contact info:

- [Twitter](https://twitter.com/illusion0002) @ `illusion0002`
- Email: illusion3185@gmail.com

# Showcase

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/gV7gX8GvfCQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Patch

I have updated the instructions for use with the new GoldHEN Plugins system.

- <a href="/install-instructions/" class="button" role="button"><i class='fas fa-download'></i> Patch Installation Instructions</a>

Below is the source code for the patch.

- <a href="https://github.com/GoldHEN/GoldHEN_Patch_Repository/blob/a92199c51bf86ffe10e4413928f6a6872928269f/patches/json/TheLastOfUs2-Orbis.json#L547" class="button" role="button"><i class='fas fa-download'></i> Patch Source Code</a>

{% include_relative _supporters.md %}
