---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/orbis/ResidentEvilZero-Orbis.yml"
title: "Resident Evil: Zero"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Demo](https://youtu.be/TP2MTZ6gC7s)

## Patches

{% include_relative patch_header.md %}

Patch file: `{{ page.patch_file }}`

File to be patched: `BH0HD\bh0hd.elf`

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>
