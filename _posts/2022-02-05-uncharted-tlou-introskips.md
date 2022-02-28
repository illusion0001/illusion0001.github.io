---
layout: single
title: "Intro Skip Patches for Uncharted and The Last of Us"
excerpt: "Introduction logos are no more."
header:
  teaser: "https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/intro_noicon_thumbnail.png"
  overlay_image: "https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/intro_noicon_thumbnail.png"
  overlay_filter: 0.5
  og_image: "https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/intro_cut_thumbnail.png"
categories: patches
tags: uncharted tlou ps4 patches
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---

{% include_relative _orbis_console_note.md %}

# Intro

With the recent release of the Uncharted Collection on the PS5 I thought it would be fun to try to skip the intro and understand a little more how the bootflow works.

## Part 1 - Task ID differences

If you remember from a [previous post](/patches/2021/12/04/t1-nailbomb-softlock-patch/) where I discussed on finding task ID, the layout goes something like this.

String (ASCII)

Address pointer (32 or 64 Bit depending on the platform)

Task ID (usually 32 but 64 Bit in The Last of Us: Part 2 with the change to entirely 64 bit hashes).

32 Bit Pointer and Hashes (PS3, Big Endian, Uncharted 3)

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/ND_task_ID_e00.png" %}

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/ND_task_ID_e01.png" %}

64 Bit Pointer and Hashes (PS4, Litle Endian, The Last of Us: Part 2)

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/ND_task_ID_e02.png" %}

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/ND_task_ID_e03.png" %}

## Part 2 - Intros or No Intros

HD era naughty dog games have this task called `ndi` which stands for **N**aughty **D**og **I**ntro. Simple enough. The ID associated with this task has not changed since Uncharted 1, which is `0xed857351` and `menu` with its ID being `0xd006e7b5`.

Now why is this important? Because the game's code looks up these id on what to load. For instance here is a snippet of code from Uncharted 3.

```cpp
      // taken from uc3 ps3 code
      // language-selection is exclusive to uncharted 3
      if (skip_ndi) {
        task = 0x66b93942; // language-selection
       // bootflow goes like this: 
       // t1, uc4, and uc-tll
       // ndi -> menu
       // uc3
       // language-selection -> ndi (handled by language-selection flow) -> menu
       // uc1 and uc2
       // autosave-warning -> ndi -> menu
      } else {
        task = 0xd006e7b5; // menu
      }
```

Code is simple enough, in this case, if this condition is true, it will skip over `language_selection` and `ndi`.
The very same process can be repeated for the following games.

```
Uncharted 1: Drake's Fortune   (PS4 only)
Uncharted 2: Among Thieves     (PS3/PS4)
Uncharted 3: Drake's Deception (PS3/PS4)
The Last of Us                 (PS3/PS4)
Uncharted 4: A Thief's End
Uncharted: The Lost Legacy
The Last of Us: Part 2         (not yet possible)
```

As to why Uncharted 1 intro skip is not yet possible on the PS3?

Because the compiled script file on that version is not the easiest thing to read. Well same for Uncharted 2 but in that case searching for the menu task ID and always booting into that does the trick but not for the first game.

As for The Last of Us Part 2, the intro is baked directly into the `menu` task. Which also explains why there are no `ndi` task to be found in the task list. 

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/t2_task_menu.png" %}

I think it is still possible if I look hard enough into the game's code or it could simply be a case of...

<div align="center">
<video width="100%" autoplay loop >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/memes/tenor/skill_issue_meme.mp4" type="video/mp4">
</video>
</div>

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/u1_ps3_taskbin.png" %}

<div align=center>
<em>Uncharted 1 task script file</em>
</div>

Yeah.. I wouldn't touch this script file with a ten foot pole.

## Part 3 - Porting to newer system

Let's see if the PS4 version is any difficult for the PS3 era titles. Thankfully, Bluepoint did all of the hard work for us on the trilogy collection and we can simply enable Boolean to skip over the video that plays during the `ndi` task and call it a day.

`bp_skipintromovies` this is a command line parameter, it only exists in Uncharted 1 and 2 but it shows that they probably got bored watching the intro so they implemented this cvar. :p

This Boolean is used when the user switches games from the option menu.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/u3_appchooser.png" %}

However, things are not as cut and dry as I would have thought.

In Uncharted 3, this string cannot be found. Another solution must have existed. And there is a solution to this. A while ago back in 2021..? When I was looking for a way to optimize the developer menu enable code I came across this magnificent piece of code.

```cpp
  if (0x027b9d22 != 0) { // is game launched from app chooser?
    0x027baf7e =  true;
    0x027baf6a =  true;
    0x027baf67 =  true;
    0x027baf69 =  true;
    0x027baf64 = false; // dev menu bool
    0x027b9d21 =  true;
    0x027b9d6c =  true; // skip ndi bool
  }
```

The last one happens to be the same one that skips the intro in the public beta version of the original game. I can simply turn this Boolean off and there we go. Uncharted 3 on the PS4 intro is skipped. Nothing to be worried about as there are no multiplayer components to this one.

I got the motivation to do intro skips was from fixing a bug where Uncharted 3 Public Beta on the PS3 would crash upon entering the Lan menu, which will be an upcoming post for those curious about it.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/uncharted-t1-introskips/u3_ps3_public_beta_tease.png" %}

<div align=center>
<em><i class="twa-2x twa-eyes"></i></em>
</div>

## Closing Words

Well that's all for this post, below are the showcase video, where you can find the patch and support me as a independent patch creator.

Have a good rest of your day! I'll catch you next time.

# Credits

[ZEROx](https://www.youtube.com/user/ZEROx2085) for porting to the PS3 version.

[Freako](https://www.youtube.com/c/Freako/) and [HereisMe](https://www.youtube.com/user/HdHereidme) for publishing their knowledge about reversing Naughty Dog Titles.

## Showcase

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Ord-myNMg2E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

This patch is available for PS3 (RPCS3), and PS4.

For those looking to use the patch on the RPCS3 emulator, you can head over to the patch manager, click on the "**Download Latest Patches**" button and find the patch you wanted to use with your game Title ID and version, click on the checkbox to enable the patch and save changes.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/RatchetPS3-FPSUnlock/rpcs3_patch_example.png" %}

<a href="https://wiki.rpcs3.net/index.php?title=Uncharted_2:_Among_Thieves#Patches" class="button" role="button"><i class='fas fa-download'></i> Patch Source Code: Uncharted 2 (RPCS3)</a>

<a href="https://wiki.rpcs3.net/index.php?title=Uncharted_3:_Drake%27s_Deception#Patches" class="button" role="button"><i class='fas fa-download'></i> Patch Source Code: Uncharted 3 (RPCS3)</a>

<a href="https://wiki.rpcs3.net/index.php?title=The_Last_of_Us#Patches" class="button" role="button"><i class='fas fa-download'></i> Patch Source Code: The Last of Us (RPCS3)</a>

PlayStation 4 users, can follow this guide on how to install the patch [here](/install-instructions). (the following tutorial **does not** cover how to build the update package. only to install the patch into the binary.)

<a href="https://github.com/illusion0001/illusion0001.github.io/blob/main/_patches/uncharted-collection.md#intro-skip" class="button" role="button"><i class='fas fa-download'></i> Patch: Uncharted: The Nathan Drake Collection (PS4)</a>

<a href="https://github.com/illusion0001/illusion0001.github.io/blob/main/_patches/tlou1.md#intro-skip" class="button" role="button"><i class='fas fa-download'></i> Patch: The Last of Us Remastered (PS4)</a>

<a href="https://github.com/illusion0001/illusion0001.github.io/blob/main/_patches/uncharted4.md#intro-skip" class="button" role="button"><i class='fas fa-download'></i> Patch: Uncharted 4 (PS4)</a>

<a href="https://github.com/illusion0001/illusion0001.github.io/blob/main/_patches/uncharted-tll.md#intro-skip" class="button" role="button"><i class='fas fa-download'></i> Patch: Uncharted: The Lost Legacy (PS4)</a>

{% include_relative _supporters.md %}
