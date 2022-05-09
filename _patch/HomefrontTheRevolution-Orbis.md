---
layout: single
excerpt: "Game Patch"
title: "Homefront: The Revolution"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

CPU+GPU Limited. For use with 9th generation of game consoles.

In file `eboot.bin`

<details>
<summary>Code 1.12 (Click to Expand)</summary>

{% highlight none %}
41 3B B7 D4 00 00 00 74 10 41 89 B7 D4 00 00 00

41 3B B7 D4 00 00 00 75 10 41 89 B7 D4 00 00 00
{% endhighlight %}

</details>
