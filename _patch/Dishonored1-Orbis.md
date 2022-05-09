---
layout: single
excerpt: "Game Patch"
title: "Dishonored: Definitive Edition"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock (CUSA02218)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.01 (Click to Expand)</summary>

{% highlight none %}
BE 01 00 00 00 E8 CE E3 22 01

BE 00 00 00 00 E8 CE E3 22 01
{% endhighlight %}

</details>
