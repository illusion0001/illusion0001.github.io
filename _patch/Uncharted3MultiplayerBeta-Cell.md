---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/cell/Uncharted3MultiplayerBeta-Cell.yml"
title: "Uncharted 3: Multiplayer Beta"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Article: Uncharted 3 Multiplayer Beta Now Playable Without PSN (PS3)](/patches/2022/03/09/Big3-MPBeta-Lan/)

## Patches

{% include_relative patch_header.md %}

Patch file: `{{ page.patch_file }}`

File to be patched: `EBOOT.ELF` (decrypted `EBOOT.BIN`)

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>
