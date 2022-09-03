---
layout: single
title: "Graphics Patches for God of War 3 and Ascension for RPCS3"
excerpt: "Experience God of War PlayStation 3 titles in Glorius 4K Resolution and Beyond."
header:
  teaser: "https://drive.google.com/uc?id=1uRhY-luQzBmKUX_HmVSW1GQ3nzdbbQ1z"
  overlay_image: "https://drive.google.com/uc?id=1uRhY-luQzBmKUX_HmVSW1GQ3nzdbbQ1z"
  overlay_filter: 0.5
  og_image: "https://drive.google.com/uc?id=1TpEzZ6icwuoYA23YDmVw3HS3XIr-ImvZ"
categories: patches
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---


# Intro

Another blast from the past, This time we will be looking into the improving the graphics of the God of War titles on PlayStation 3.

Specifically the things you would find when playing a PC game like running at any resolution and optional motion blur and depth of field to name a few.

## Part 1 - Brightness Options Came To The Rescue

Starting with God of War 3, I went into the game display options to look for clues.

{% include img1 image_path="https://drive.google.com/uc?id=1UnK-6MbeLlhP1UmsqXgkuT6JaSKxfOyI" %}

<div align=center>
<em>In-Game Brightness Menu</em>
</div>

Moving this silder around and searching for values I narrowed it down to 4 byte int.

{% include img1 image_path="https://drive.google.com/uc?id=1r_4Sla1XltcLzmsSHDOXwV31jRLVdC3E" %}

<div align=center>
<em>In-Game Brightness Menu</em>
</div>

Max of `100` and Min of `0`.

Peeking into memory reveals something interesting.

{% include img1 image_path="https://drive.google.com/uc?id=1v-Aisz8Z4Xc3oZ8jjHHlI3ej6n3USDqN" %}

<div align=center>
<em>Highlighted is Brightness Value</em>
</div>

There is a toggle, in 4 byte int. `0x52BF2C`

Setting it to 0 gives us this.

{% include img1 image_path="https://drive.google.com/uc?id=1c_Jl5xcqVFDKdkIOAvTB7HiO6VDTPYGk" %}

<div align=center>
<em>Strange colors.</em>
</div>

Hmm, it gives strange results. Let's try patching this to 0 at startup.

`- [ byte, 0x52BF2F, 0 ]`

{% include img1 image_path="https://drive.google.com/uc?id=1kK6bYz8HJBlE34V4OXqDE5lS9_mc1sOv" %}

<div align=center>
<em>2560x1440 Internal Resolution</em>
</div>

Woah, a crisp clean image. How about in-game?

{% include_relative _image_note.md %}

{% include img1 image_path="https://drive.google.com/uc?id=1N9acgckMznUSeb8De6o5s8eLChvQl1Zv" %}

<div align=center>
<em>Absolutely Stunning!</em>
</div>

How about God of War Ascension?

{% include img1 image_path="https://drive.google.com/uc?id=1_81N1rI3WxuKdSSUHR3NXD5t5-m4ASqb" %}

<div align=center>
<em>In-Game Settings Menu</em>
</div>

Oh, a value number next to the brightness setting, how curious.

{% include img1 image_path="https://drive.google.com/uc?id=1e4JT8qxcZBBirfgghVxABUQIT6Y5KsgD" %}

<div align=center>
<em>GOWA Memory View</em>
</div>

No toggle next to brightness, there is some toggle at the bottom.

{% include img1 image_path="https://drive.google.com/uc?id=1v_zxb8OiFNRe45ZQ-Q72VvuHYaovZWu-" %}

<div align=center>
<em>GOWA Mysterious toggle disabled</em>
</div>

Another one with strange graphical issues.

`- [ byte, 0x83ce77, 0 ]`

Let's try the same method I used for God of War 3.

{% include_relative _image_note.md %}

{% include img1 image_path="https://drive.google.com/uc?id=1fJbk3vTNCU5ILsKOs4sND-_TD86Ftlzp" %}

<div align=center>
<em>2560x1440 Internal Resolution</em>
</div>

This seem to be MLAA as well, job done right?

## Part 2 - More Graphics Improvemnts

After a few weeks of letting my friend [ZEROx](https://www.youtube.com/user/ZEROx2085/) know about my findings, he decided to look into the more of the game internal Grahpics Options.

First was that he was able to improve more of the game performance by looking at the code.

```
00390724 4b ff fc b5     bl         FUN_003903d8
00390728 3c 60 00 9b     lis        param_1,0x9b
...
00390750 38 c0 00 00     li         param_4,0x0
00390754 4b ff fc 85     bl         FUN_003903d8
00390758 3c 60 00 84     lis        param_1,0x84
0039075c 80 63 ce 74     lwz        param_1,-0x318c(param_1)=>DAT_0083ce74
```

Nop on `branch link` to call the functions skipped it.

```yml
- [ be32, 0x00390724, 0x60000000 ]
- [ be32, 0x00390754, 0x60000000 ]
```

Searching for the text `DepthOfField` leads us here.

```
00433ef8 93 fd 00 08     stw        r31=>s_DepthOfField_0067b638,0x8(r29)
...
00434080 41 82 01 98     beq        LAB_00434218
...
00434250 41 82 00 50     beq        LAB_004342a0
...
                     LAB_004342a0 XREF[1]:     00434250(j)  
004342a0 3b c0 00 01     li         r30,0x1
004342a4 30 7f 00 10     addic      r3,r31,0x10
004342a8 78 63 00 20     rldicl     r3,r3,0x0,0x20
004342ac 4b f7 b6 dd     bl         FUN_003af988
004342b0 60 00 00 00     ori        r0,r0,0x0
004342b4 80 9f 00 1c     lwz        r4,0x1c(r31)
004342b8 38 60 00 00     li         r3,0x0
004342bc 80 bf 00 20     lwz        r5,0x20(r31)
```

Following the branching leads to the last one in the list.

A few testing with `li` and register of `0` comes down to `lwz r5,0x20(r31)`

{% include img1 image_path="https://drive.google.com/uc?id=1PS5As5ff_dy1iMocjQqsM9VyBXtjmNSs" %}

<div align=center>
<em>Depth of Field: Enabled</em>
</div>

{% include img1 image_path="https://drive.google.com/uc?id=18ag_hpR6sGj0jfCYG7epmvSk_ayiI6PC" %}

<div align=center>
<em>Depth of Field: Disabled</em>
</div>

Same can be done for Motion Blur.

## Part 3 - Backporting to God of War 3

MLAA Patch Performance Improvement

```
0023128c 80 1e 00 00     lwz        r0,0x0(r30)=>DAT_0052bf2c
002312b4 4b ff f9 99     bl         FUN_00230c4c
002312c8 4b ff f9 85     bl         FUN_00230c4c
...
0023137c 4b ff f8 d1     bl         FUN_00230c4c
```

A few nop to the call `0x230c4c` narrowed down to  `0x0023137c`.

However, Graphics Options is a little more involed.

{% include img1 image_path="https://drive.google.com/uc?id=13YE3v-va2dXUCdm4ZxBl4QndAgy5diM5" %}

String refernce and a reverse branch. Hmm.

{% include img1 image_path="https://drive.google.com/uc?id=1Sjq7HEChNzxw25-LS8m3KasFsEbfEicC" %}

Setting a breakpoint on `001c65b8 bl FUN_001b61e0` lead us somewhere.

{% include img1 image_path="https://drive.google.com/uc?id=1KcaLhqmX7cxskk827CXi_QADK5g_zw_o" %}

<div align=center>
<em>Take notice of Register 3</em>
</div>

{% include img1 image_path="https://drive.google.com/uc?id=1e1mD-P8hIXUP-YKGp8RyRU3WEXhB5RnD" %}

Setting byte `0x321ACA6B` to 0 disables motion blur.

This method can also be used for Depth of field.

{% include img1 image_path="https://drive.google.com/uc?id=1EGexTBMmZSeoAvGrqMU53ndlamzVhY6x" %}

# Results

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/J-rf0FcXpLw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/p_gvO2jBWwI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

Patch was made available back in August 2020. You can download through the emulator built-in Patch Manager.

{% include img1 image_path="https://drive.google.com/uc?id=15E5MSUoxwPjo-X0-sq8M8BLEfMXe5Ba5" %}

{% include_relative _supporters.md %}
