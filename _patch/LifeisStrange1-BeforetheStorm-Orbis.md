---
layout: single
excerpt: "Game Patch"
title: "Life is Strange: Before the Storm"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/05/11/wif-dawn-60fps/)

CUSA08487, may work for other versions too.

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
40 0F 95 C6 E8 DD CF 1B 00

40 0F 94 C6 E8 DD CF 1B 00
{% endhighlight %}

</details>
