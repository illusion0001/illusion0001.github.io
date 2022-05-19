---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/orbis/ResidentEvilHD-Orbis.yml"
title: "Resident Evil: HD"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Demo](https://youtu.be/MSVD1Gmm4P8)

## Patches

{% include_relative patch_header.md %}

Patch file: `{{ page.patch_file }}`

File to be patched: `BH1HD\bh1hd.elf`

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>
