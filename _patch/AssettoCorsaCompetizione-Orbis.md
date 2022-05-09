---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/orbis/AssettoCorsaCompetizione-Orbis.yml"
title: "Assetto Corsa Competizione"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

## Patches

{% include_relative patch_header.md %}

Author: [illusion](https://twitter.com/illusion0002)

Patch file: `{{ page.patch_file }}`

File to be patched:`eboot.bin`

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>
