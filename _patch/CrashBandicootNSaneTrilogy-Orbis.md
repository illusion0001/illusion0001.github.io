---
layout: single
excerpt: "Game Patch"
title: "Crash Bandicoot N. Sane Trilogy"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

Uses double buffer vsync.

For use with 9th generation of game consoles.

In file `eboot.bin`

<details>
<summary>Code 1.07 (Click to Expand)</summary>

{% highlight none %}
# sceVideoOutSetFlipRate

E8 2D E3 D0 00

90 90 90 90 90
{% endhighlight %}

</details>
