---
layout: single
patch_file: "_patch0/orbis/RatchetandClankRemakeOrbis.yml"
game_title: "Ratchet and Clank (Remake)"
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
