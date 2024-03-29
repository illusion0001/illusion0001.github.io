---
layout: post
title: "Custom Resolution in Uncharted 4"
excerpt: "60FPS is possible.. With a few compromises."
categories: patches
tags: uncharted ps4 patches
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---

{% include_relative _orbis_console_note.md %}

# Intro

This will be a short one due to how easy it was to patch. For those who expected a long in-depth post, sorry!

I have always wonder if the resolution can be tone down in Uncharted 4, would 60FPS be possible? Short answer is No. But in the future on the PS5, very much of a possiblity.

## Research

For starters, resolution numbers is stored as 4 bytes. At least in Naught Dog games. A quick search for `1600` and `900` in one row shows one result . Why 900p? The multiplayer modes switches to 900p during gameplay.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/uc4-60fps-dream/ghidra-900p-search.png" %}

```
012cf1f2 48 ba 40        MOV        RDX,0x38400000640 // 1600x900
         06 00 00 
         84 03 00 00
012cf207 48 b8 c0        MOV        RAX,0x438000003c0 // 1920x540
         03 00 00 
         38 04 00 00
012cf21c 48 8d 88        LEA        RCX,[RAX + 0x3c0] // add 540
         c0 03 00 00
012cf22a 48 b9 00        MOV        RCX,0x21c00000500 // 1280x540 for split screen
         05 00 00 
         1c 02 00 00
012cf234 48 89 93        MOV        qword ptr [RBX + 0x7d78]=>DAT_02bde528,RDX // load from rdx into memory
         78 7d 00 00
012cf23b 48 89 83        MOV        qword ptr [RBX + 0x7d80]=>DAT_02bde530,RAX // load from rax into memory
         80 7d 00 00
012cf242 48 89 8b        MOV        qword ptr [RBX + 0x7d88]=>DAT_02bde538,RCX // load from rcx into memory
         88 7d 00 00
```

`012cf1f2` is what we are interested in.

`40 06 00 00` 1600 in 4 bytes.

`84 03 00 00` 900 in 4 bytes.

Patching this to 960x540 is as simple as swapping out the existing numbers with our own.

`C0 03 00 00` 960 in 4 bytes.

`1C 02 00 00` 540 in 4 bytes.

That's it!

```
012cf1f2 48 ba c0        MOV        RDX,0x21c000003c0 // 960x540
         03 00 00 
         1c 02 00 00
```

## Results

{% include_relative _image_note.md %}

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/uc4-60fps-dream/u4-patch0.png" %}

<div align=center>
<em>Native 1080p</em>
</div>
{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/uc4-60fps-dream/u4-patch1.png" %}

<div align=center>
<em>Upscaled 900p</em>
</div>
{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/uc4-60fps-dream/u4-patch2.png" %}

<div align=center>
<em>Upscaled 540p</em>
</div>
<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/k1t4NtmV68M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

<a href="/_patch/Uncharted4AThiefsEnd-Orbis/" class="button" role="button">{{ site.theme_settings.download_icon }} Patch Codes</a>

{% include_relative _supporters.md %}
