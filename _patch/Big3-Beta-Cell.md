---
layout: single
patch_file: "_patch0/cell/big3-beta.yml"
game_title: "Uncharted 3: Multiplayer Beta"
---

# {{ page.game_title }}

[Game Index](/patch/#ps3)

[Article: Uncharted 3 Multiplayer Beta Now Playable Without PSN (PS3)](/patches/2022/03/09/Big3-MPBeta-Lan/)

## Patches

{% include_relative patch_header.md %}

Patch file: `{{ page.patch_file }}`

File to be patched: `EBOOT.ELF` (decrypted `EBOOT.BIN`)

Author: [illusion](https://twitter.com/illusion0002), [ZEROx](https://github.com/Xcedf)

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>