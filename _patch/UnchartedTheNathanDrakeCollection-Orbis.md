---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/orbis/UnchartedTheNathanDrakeCollection-Orbis.yml"
title: "Uncharted: The Nathan Drake Collection"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

## Patches

{% include_relative patch_header.md %}

Patch file: `{{ page.patch_file }}`

File to be patched: `eboot.bin/big2-shipping.elf/big3-shipping.elf`

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>
