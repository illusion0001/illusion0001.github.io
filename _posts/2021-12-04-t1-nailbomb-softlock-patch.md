---
layout: single
title: "University Nailbomb Softlock Fix for The Last of Us (PS3, PS4)"
excerpt: "A nailbomb, and a door, equals a softlock."
thumbnail: "https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-nailbomb-feature-image.png"
header:
  overlay_image: "https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-nailbomb-feature-image.png"
  overlay_filter: 0.5
  og_image: "https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-nailbomb-image.png"
categories: patches
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---

<i class="twa twa-warning"></i> <i class="twa twa-warning"></i> **Warning: This post contains spoilers for the video game, The Last of Us. If you have not yet completed the game, you should do so or if you simply don't care, you can read through. You have been warned.** <i class="twa twa-warning"></i> <i class="twa twa-warning"></i>

***

# Intro

A few weeks back I was browsing through [AnthonyCaliber](https://www.youtube.com/channel/UC4PlYBhe8mzGFW4lmIkIQsg) videos. Showcasing various glitches in The Last of Us Remastered. Most of the glitches in the video are out of bounds and does not prevent progressing through the game but there is one glitch that caught my eye.

<div align="center">
<video width="100%" controls >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/T1-AC-nailbomb-section-trimmed.mp4" type="video/mp4">
</video>
<em>(Credit: <a href="https://www.youtube.com/channel/UC4PlYBhe8mzGFW4lmIkIQsg">AnthonyCaliber</a>) <a href="https://youtu.be/L_JrpN96uBg?t=6482">Original Video (Timestamped 01:48:02)</a></em>
</div>

Once I saw this, a great idea popped into my head. Either to give the player infinite health during this section or making the nailbomb ineffective. I went with the latter option as the former caused issues. As you might’ve seen from the video, if the two hunters die then the camera will freeze but the player can still move so that is a no go. My plan is to research into the weapons, which in this case the nailbomb and how the game knows what task or level it's currently on.

## Part 1 - Research

Let's start by seeing how the game keeps track of what level or task we are on. Thanks to the work of Freako and HereisMe. Some of this has already been worked out and is published. 
In the [Naughty Dog Modding](https://discord.com/invite/VWEbKZsTNb) server, Freako has kindly provided all the info that he knows about the game in an archive which will become very useful as this post goes on. So let's have a look at it.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/nd-task-research-folder.png" %}

<div align=center>
<em>TLOU Research folder</em>
</div>

A few folders, the ones we're interested in are `tasks` and `weapon-loadout`.
Inside the task folder is a text file and some example files. This text file list where things are, what's been discovered, etc.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-task-struct-2.png" %}

<div align=center>
<em>Basic Task.bin data structure. (Credit: <a href="https://www.youtube.com/c/Freako/">Freako</a>)</em>
</div>

The image is barebones but enough for us to understand. From the text file on how to find a given task is as follows: get string address, find string offset as address. The identifier is found right next to the string. Obviously this is for the ps3 version soo, give me a moment while I extract the PS4 version. Alright here's the list of task we'll need to keep track and to later patch.

```
uni-4-lab-rebar-ambush
uni-4-lab-rebar-aiming
uni-4-lab-help-off-rebar
uni-4-lab-injured-escape-start
uni-4-lab-injured-escape-vault
```

Since we're on x86_amd64 (PlayStation4), the CPU architecture is little funny. You see there's this thing called a little or big endian and it gets confusing if you're new, like me. Say you have a value, `09 87 65 43 21 00 00 00` this is how it would be represented on big endian, which is what the PlayStation 3 uses. But on x86, it's little endian which means, these bytes are swapped. Now it is `43 65 87 09 00 00 00 21`. Wrap your head around that when you have to keep track of things, worse of all, hexadecimal data displayed via printf is byte swapped! So what's the point?

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/Jackie-Chan-confused-be-le-meme.png" %}

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-taskid-0.png" %}

<div align=center>
<em>Real thinking hours. <i class="twa thinkhappy"></i></em>
</div>

Anyways, here's the task ids

```
uni-4-lab-rebar-ambush          // F0 8E BC 40
uni-4-lab-rebar-aiming          // CF F0 66 A4
uni-4-lab-help-off-rebar        // 6A 60 B6 9A
uni-4-lab-injured-escape-start  // 5C 5D 81 11
uni-4-lab-injured-escape-vault  // C8 5F D3 4A
```

Alright, now for the weapons, fortunately, there's only one we need to know what the ID is and that is the nailbomb, already figured out by the legend that is HereisMe. 

```
0x18A76844 == WeaponIdNailBomb()
```

Reverse that and that's what our id is on ps4.

## Part 2 - Reproducing the issue

Now to the reproduction steps. Following what Anthony did, got us the same result, the hunter dies and the camera is stuck. Or the nailbomb explodes and the player is put into an indefinite loop. A softlock.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-camera-stuck-1.png" %}
{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-camera-stuck-1a.png" %}

<div align=center>
<em>This camera is not moving</em>
</div>

<div align="center">
<video width="100%" controls >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-nailbomb-softlock-demo1.mp4" type="video/mp4">
</video>
<em>Indefinite respawns and nailbomb exploding.</em>
</div>

***InCase** anyone is wondering, yes I do know that you can restart encounters to "resolve" these issues but it should not even happen in the first place.* <i class="twa twa-eyes"></i>

## Part 3 - Patching

I made the decision to get rid of the explosion but left the nailbomb intact. The player can shoot and it will do absolutely nothing.

Searching for the string of nailbomb, nada. what about bomb?

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-ghidra-smokeb-search-4.png" %}

<div align=center>
<em>...a smoke bomb string reference</em>
</div>

Welp, that was a disappointment alright.

Hey, what about that weapon ID earlier? This yielded some results. I will now introduce you, to the method of lazy reversing. Look for a branch and skip it or put a return from subroutine at the beginning of the function.

Alright, let's have a look at some of these references.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-ghidra-weaponid-search-3.png" %}

<div align=center>
<em>That's a lotta results</em>
</div>

Most of these don't do anything interesting and there's only one reference that did do something. 

This reference disables the damage output.

<div align="center">
<video width="100%" controls >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-nailbomb-damage-demo-0.mp4" type="video/mp4">
</video>
<em>That does something.</em>
</div>

Okay, now what? if we use this code for our fix, it could work but the explosions particles would still go off. Looks a little distracting, don't you think?

Oh look, there's an error message that I missed. `Explosion Missing Parameters` these unfortunately doesn't print anything on to the screen but it gives us a clue. the word explosion can be used to find other references.

```cpp
  if (local_2b0 == 0) {
    FUN_01c84620(6);
    FUN_01c84a80("Explosion Missing Parameters");
  }
// ...
    if ((bool)uVar31) {
      uVar30 = uVar2 < 0x18a76844;
```

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-ghidra-explode-strings-7.png" %}

<div align=center>
<em>That is a lot of results</em>
</div>

The refernce that disables the particles is around `SpawnExplosionEffects - no explosion settings` string.

Let's give it a try.

<div align="center">
<video width="100%" controls >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-nailbomb-oneline-demo-2.mp4" type="video/mp4">
</video>
</div>

Hmm, it still blows up. even if there is no particles. that's distracting if you ask me.

Wait a minute, there's two `SpawnExplosion` strings.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-ghidra-spawnexplode-search-5.png" %}

`SpawnExplosion - can't find explosion settings` sounds interesting.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-ghidra-explode-calls-6.png" %}

<div align=center>
<em>Related function calls</em>
</div>

Hmm, let's have a look at the call references to this function. Alright time to bisect what does what. Some of these did what we saw before and some even crashed the game outright, so that's not good. How do I test this you may ask?

Removing the call. using the no operation instruction.

There is one call that stood out. `0x016a299a`

```cpp
  if ((param_1 + 0x40) == 0) {
    // ...
    FUN_01a7f5c0(param_1);
  }
  return;
```

Close to a return.. hmm, what could that mean?

There's a branch up here, let's skip it.

<div align="center">
<video width="100%" controls >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-nailbomb-processing-demo-3.mp4" type="video/mp4">
</video>
<em>Ahh-yes!</em>
</div>

Not only does this not blow-up, it does absolutely nothing when an npc goes near it!

Time for the patch.

Keep in mind that this is my interpretation of the code I wrote in assembly but the pseudocode should be readable enough to your average amateur programmers.

```cpp
  if (task == 0x40bc8ef0 || 0xa466f0cf || 0x9ab6606a || 0x11815d5c || 0x4ad35fc8 )
  {
    // uni-4-lab-rebar-ambush         40bc8ef0
    // uni-4-lab-rebar-aiming         a466f0cf
    // uni-4-lab-help-off-rebar       9ab6066a
    // uni-4-lab-injured-escape-start 11815d5c
    // uni-4-lab-injured-vault        4ad35fc8
            // 
    return; // disable nailbomb explosion output
  }
  // enable nailbomb explosion, normal path
  SpawnExplosion();
  SpawnExplosionEffects();
```

Looks good! time to try it out.

<div align="center">
<video width="100%" controls >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/TLOU-Nailbomb-Softlock/t1-nailbomb-typo.mp4" type="video/mp4">
</video>
</div>

Oh no, what happened? 

As it turns out, I made a minor typo. I was comparing against 0x9ab6**60**6a and not the supposed 0x9ab6**06**6a. A simple fix solved this.

{% include_relative _shilling.md %}

Enjoy your one-less bug video game!

# Result

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/wDJmLgw2oF4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Credits

Special thanks to:

[ZEROx](https://www.youtube.com/user/ZEROx2085) for porting to the PS3 version.

[Freako](https://www.youtube.com/c/Freako/) and [HereisMe](https://www.youtube.com/user/HdHereidme) for publishing their knowledge about reversing Naughty Dog Titles.

# Patch

This patch is available for PS3 (RPCS3), and PS4.

For those looking to use the patch on the RPCS3 emulator, you can head over to the patch manager, click on the "**Download Latest Patches**" button and find the patch you wanted to use with your game Title ID and version, click on the checkbox to enable the patch and save changes.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_patch_example.png" %}

<a href="https://wiki.rpcs3.net/index.php?title=The_Last_of_Us#Patches" class="button" role="button"><i class='fas fa-download'></i> Patch Source Code (RPCS3)</a>

<a href="https://github.com/illusion0001/illusion0001.github.io/blob/main/_patches/tlou1.md#University-Nailbomb-Softlock-Fix" class="button" role="button"><i class='fas fa-download'></i> Patch (PS4)</a>

PlayStation 4 users, can follow this guide on how to install the patch [here](/install-instructions). (the following tutorial **does not** cover how to build the update package. only to install the patch into the binary.)

{% include_relative _supporters.md %}
