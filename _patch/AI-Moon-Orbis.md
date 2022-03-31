---
layout: single
patch_file: "_patch0/orbis/AI-Moon-Orbis.yml"
game_title: "Alien: Isolation"
---

# {{ page.game_title }}

[Game Index](/patch/#ps4)

[Article](https://illusion0001.github.io/patches/2021/09/09/AlienIsolation-Patches/)

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
