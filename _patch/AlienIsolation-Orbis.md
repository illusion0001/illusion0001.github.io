---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/orbis/AlienIsolation-Orbis.yml"
title: "Alien: Isolation"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Article](https://illusion0001.github.io/patches/2021/09/09/AlienIsolation-Patches/)

## Patches

{% include_relative patch_header.md %}

Patch file: `{{ page.patch_file }}`

File to be patched: `eboot.bin`

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>
