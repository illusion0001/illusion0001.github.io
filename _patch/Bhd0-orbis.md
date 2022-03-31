---
layout: single
patch_file: "_patch0/orbis/Bhd0-orbis.yml"
game_title: "Resident Evil: Zero"
---

# {{ page.game_title }}

[Game Index](/patch/#ps4)

[Demo](https://youtu.be/TP2MTZ6gC7s)

## Patches

{% include_relative patch_header.md %}

Patch file: `{{ page.patch_file }}`

File to be patched: `BH0HD\bh0hd.elf`

Author: [illusion](https://twitter.com/illusion0002)

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>