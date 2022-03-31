---
layout: single
patch_file: "_patch0/orbis/AC2-Orbis-Shipping.yml"
game_title: "Assetto Corsa Competizione"
---

# {{ page.game_title }}

[Game Index](/patch/#ps4)

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
