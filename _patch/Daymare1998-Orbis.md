---
layout: single
patch_file: "_patch0/orbis/Daymare_MASTER-Orbis.yml"
game_title: "Daymare 1998"
---

# {{ page.game_title }}

{% include_relative index.md %}

## Patches

{% include_relative patch_header.md %}

Patch file: `{{ page.patch_file }}`

File to be patched: `eboot.bin`

Author: [illusion](https://twitter.com/illusion0002)

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>