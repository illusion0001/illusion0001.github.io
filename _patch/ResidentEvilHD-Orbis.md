---
layout: single
patch_file: "_patch0/orbis/ResidentEvilHD-Orbis.yml"
game_title: "Resident Evil: HD"
---

# {{ page.game_title }}

{% include_relative index.md %}

[Demo](https://youtu.be/MSVD1Gmm4P8)

## Patches

{% include_relative patch_header.md %}

Patch file: `{{ page.patch_file }}`

File to be patched: `BH1HD\bh1hd.elf`

Author: [illusion](https://twitter.com/illusion0002)

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>
