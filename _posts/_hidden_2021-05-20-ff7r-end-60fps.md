---
layout: post
title: "60FPS Patch for Final Fantasy 7: Remake"
excerpt: "
PS4 Owners gets the patch first before PS5? Unofficially of course."
categories: patches
header:
  teaser: "https://img-assets.illusion0001.workers.dev/assets/images/ff7r-end-60fps/banner2.png"
  overlay_image: "https://img-assets.illusion0001.workers.dev/assets/images/ff7r-end-60fps/banner.png"
  overlay_filter: 0.5
  og_image: "https://img-assets.illusion0001.workers.dev/assets/images/ff7r-end-60fps/banner.png"
tags: ff7r ps4 patches
tags: [Articles, Releases]
# twitter: {card: "summary_large_image"}

toc: true
toc_sticky: true
---

{% include_relative _orbis_console_note.md %}

This patch was tested on a Base PlayStation 4. Users with a PS4 Pro will be able to run at a higher resolution than what's seen here. See [**Patch Section**](#patch) for more info.

# Intro

This post will be a short one! Sorry to those who expected a long and in-depth post.

## File Editing

Let's cut to the chase. Looking through the game files [Resolution Scale](https://docs.unrealengine.com/en-US/RenderingAndGraphics/DynamicResolution/index.html) and vsync interval caught my interest. Of course these are not set in the executable due to it's flexiblty. It's set from file instead. There are defaults in the executable but they are ignored as it later gets replaced by value loaded from settings file.

In file: `pakchunk0-ps4.pak` is where graphics settings is stored.

```
; The ini comments are my own.
rhi.SyncInterval=2 ; 30hz
r.DynamicRes.MinScreenPercentage=83.3333333 ; 83% of target ir
r.DynamicRes.MaxScreenPercentage=100 ; 100 % of target ir (1080p for base not sure for Neo)
```

I'll be changing these to 

```
rhi.SyncInterval=1 ; 60hz
r.DynamicRes.MinScreenPercentage=50.0000000 ; 50 % of target ir (540p for base)
r.DynamicRes.MaxScreenPercentage=63 ; 63 % of target ir (720p for base)
```

# Result

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/ync0bSVoX-0?start=325" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<div align="center" class="responsive-video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/JeKoRI4ZVUM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

# Patch

Base Console owners will be able to run the game at 720p 60FPS.

Pro Console owners will be able to choose between 900p and 1080p for 60FPS.

Dynamic Resolution threshold can always be customized.

Both Consoles must have framerate patch applied to take effect.

<a href="/_patch/FinalFantasyVIIRemake-Orbis" class="button" role="button">{{ site.theme_settings.download_icon }} Patch Code</a>

{% include_relative _supporters.md %}
