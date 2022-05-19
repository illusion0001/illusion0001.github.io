---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/orbis/ResidentEvil2-Orbis.yml"
title: "Resident Evil: 2"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Demo](https://youtu.be/Qf3BCH8-ZPM)

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
