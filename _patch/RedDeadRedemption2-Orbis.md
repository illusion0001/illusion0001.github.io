---
layout: single
excerpt: "Game Patch"
title: "Red Dead Redemption 2"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

[Demo](https://youtu.be/r5aY2vHjB_8)

CPU Limited. For use with 9th generation of game consoles.

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.29 (Click to Expand)</summary>

{% highlight none %}
0x538EB57 BE 00 00 00 00
{% endhighlight %}

</details>

## Resolution Patch

[Demo](https://youtu.be/r5aY2vHjB_8)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
# Base
# Do not apply this on Neo as it will cause a blackscreen.
80 07 00 00 38 04 00 00 3C 00 00 00 01 00 00 00 00 0F 00 00 70 08 00 00 3C 00 00 00 01 00 00 00
# 1920x1080 -> 1280x720
00 05 00 00 D0 02 00 00 3C 00 00 00 01 00 00 00 00 0F 00 00 70 08 00 00 3C 00 00 00 01 00 00 00
{% endhighlight %}

</details>
