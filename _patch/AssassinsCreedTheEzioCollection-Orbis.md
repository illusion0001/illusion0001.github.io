---
layout: single
excerpt: "Game Patch"
title: "Assassin's Creed: The Ezio Collection"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `ScimitarAC2.elf` `ScimitarACB.elf` `ScimitarACR.elf`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight none %}
# ScimitarAC2.elf 

BE 01 00 00 00 E8 B8 D5 50 01

BE 00 00 00 00 E8 B8 D5 50 01

# ScimitarACB.elf

BE 01 00 00 00 E8 70 30 61 01

BE 00 00 00 00 E8 70 30 61 01

# ScimitarACR.elf

BE 01 00 00 00 E8 61 CE 72 01

BE 00 00 00 00 E8 61 CE 72 01

{% endhighlight %}

</details>
