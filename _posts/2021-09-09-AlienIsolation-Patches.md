---
layout: single
title: "Patches and Enhancements for Alien: Isolation (PS4)"
excerpt: "Removing save comfirm message and bringing a PC exclusive feature to console."
header:
  teaser: "https://gs2-sec.ww.prod.dl.playstation.net/gs2-sec/appkgo/prod/CUSA00363_00/3/i_b2589b00f5519f8e53bf65225b78d3ab58efac7de467e2f5297cec8fc4f94c65/i/pic0.png"
  overlay_image: "https://gs2-sec.ww.prod.dl.playstation.net/gs2-sec/appkgo/prod/CUSA00363_00/3/i_b2589b00f5519f8e53bf65225b78d3ab58efac7de467e2f5297cec8fc4f94c65/i/pic0.png"
  overlay_filter: 0.5
  og_image: "https://gs2-sec.ww.prod.dl.playstation.net/gs2-sec/appkgo/prod/CUSA00363_00/3/i_b2589b00f5519f8e53bf65225b78d3ab58efac7de467e2f5297cec8fc4f94c65/i/pic0.png"
categories: patches
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---



**Update - 9/27/2021
I just found out it is possible to remove the save dialog on the PC version of AI thanks to ThirteenAG's [SkipSaveConfirmationDialog](https://github.com/ThirteenAG/AlienIsolation.SkipSaveConfirmationDialog).**

***

# Intro

I recently got a copy of [Alien Isolation](https://www.alienisolation.com/) for the PlayStation 4, a sci-fi survival horror game developed by [Creative Assembly](https://www.creative-assembly.com/) and I was bothered by the save confirmation dialog box and the narrow Field of View. neither can be changed or tweaked on the console version but this is a multi-plat release and of course there's the PC version which allowed for changing the FOV and graphical settings that is considered optional on that platform.

But there's no way to remove the save confirmation screen, let's see what can be done about it.

## Part 1 - Researching Save Prompt

Let's start with the save confirmation screen, when us, the player goes to save our progress at the emergency station, will be prompted with the dialogbox mentioned earlier.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-save.png" %}

Assuming the dialog is a boolean, it can either be a `00` or a `01`, let's start by searching for 1 when the prompt is shown and when it is not.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-search0.png" %}

That's a lot of results.. Let's rinse and repeat until the result list becomes manageable.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-search1.png" %}

Ah, 11 results. That's more like it, let's set a breakpoint on each of these until it breaks when the dialog pops up.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-search2.png" %}

2 Results. First one is a write so we can discard that as it is not important, the second one however is more interesting.

```
01197e01 41 80 bc        CMP        byte ptr [R12 + 0x12e1],0x0
         24 e1 12 
         00 00 00
01197e0a 74 0d           JZ         LAB_01197e19
01197e0c 4c 89 e7        MOV        RDI,R12
01197e0f be 1b 00        MOV        ESI,0x1b
         00 00
01197e14 e9 93 05        JMP        LAB_011983ac
         00 00
                     LAB_01197e19                                    XREF[1]:     01197e0a(j)  
01197e19 4d 8d b4        LEA        R14,[R12 + 0x1040]
         24 40 10 
         00 00
01197e21 41 0f b6        MOVZX      ECX,byte ptr [R12 + 0x1473]
         8c 24 73 
         14 00 00
01197e2a 41 0f b6        MOVZX      EDX,byte ptr [R12 + 0x1471]
         94 24 71 
         14 00 00
01197e33 41 8b bc        MOV        EDI,dword ptr [R12 + 0x48ec]
         24 ec 48 
         00 00
01197e3b 41 8b b4        MOV        ESI,dword ptr [R12 + 0x48f0]
         24 f0 48 
         00 00
...
011983ac e8 bf 0e        CALL       FUN_01199270
         00 00
...
01199319 48 8d 35        LEA        RSI,[s_AI_UI_DLG_BTN_DONT_SAVE_01f03ab1]         = "AI_UI_DLG_BTN_DONT_SAVE"
         91 a7 d6 00
01199343 48 8d 35        LEA        RSI,[s_AI_UI_DLG_BTN_RETRY_01ef8510]             = "AI_UI_DLG_BTN_RETRY"
         c6 f1 d5 00
01199371 48 8d 35        LEA        RSI,[s_AI_UI_DLG_WSETUP_CONFIRM_NODEVIC_01f03a   = "AI_UI_DLG_WSETUP_CONFIRM_NODE
         17 a7 d6 00
01199378 48 8d 15        LEA        RDX,[s_AI_UI_DLG_WSETUP_CONFIRM_NODEVIC_01f03a   = "AI_UI_DLG_WSETUP_CONFIRM_NODE
         e8 a6 d6 00
```

A compare, jump to function, and that function has what seems to be dialog save variables. how about we skip this jump and run the rest of the code?

```
01197e0a eb 0d           JMP        LAB_01197e19 ; skip save confirm code
```

<div align="center">
<video width="100%" controls >
  <source src="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-skip.mp4" type="video/mp4">
</video>
<em>It automatically saved and skipped the dialog!</em>
</div>

## Part 2 - Researching FOV

On the PC there's an option to adjust the FOV from 47 to 75. The default seems to be 47 and is a float.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-FOV0.png" %}

Searching for 47 and adjusting the value back and forth, a lot of them is locked but there's only one that can be manually adjusted.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-FOV1.png" %}

I manually set `0x05B0AC00` to 100, but this value is not static so let's have a look in memory and see if we can find it in the console version.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-FOV2.png" %}

Highlighted in red at the top left is the address and value we just found, the values with red squares indicated that it has changed and is not relevant to us. let's remember the row of address next to our float value and see if we can find it on the console.

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-Console-FOV-0a.png" %}

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-Console-FOV-0b.png" %}

I decided to check the first one and sure enough, it was the one we were looking for.

```
0115b8c6 e8 3a 84        CALL       MyFOVSubroutine ; call
         1d 00
                     MyFOVSubroutine                                 XREF[1]:     FUN_0115b770:0115b8c6(c)
01333d05 c7 84 21        MOV        dword ptr [RCX + 0x38],0x42c80000 ; 100 degrees as example
         38 00 00 
         00 00 00 
01333d10 c5 fa 10        VMOVSS     XMM0,dword ptr [RCX + 0x38] ; move 100.0f into xmm0
         41 38
01333d15 c3              RET ; return
```

{% include img1 image_path="https://storage.googleapis.com/assets-illusion0001/images/AlienIsolation-Patches/AI-Console-FOV-3.png" %}

<div align=center>
<em>Left = 47, Right = 70, Bottom Middle = 100</em>
</div>

Just for fun, here is a comparison between the different FOV angles.

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/r7hd-VvBy80" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

<a href="https://github.com/illusion0001/illusion0001.github.io/blob/main/_patches/AI-Moon-Orbis.md" class="button" role="button"><i class='fas fa-download'></i> Patch Code</a>

{% include_relative _supporters.md %}
