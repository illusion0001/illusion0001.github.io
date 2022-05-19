---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/orbis/GravityDaze2-Orbis.yml"
title: "Gravity Rush 2 (Gravity Daze 2)"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

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
