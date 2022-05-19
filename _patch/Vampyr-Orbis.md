---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/orbis/Vampyr-Orbis.yml"
title: "Vampyr"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

<!--

Next Gen got a patch, why not old gen too? https://twitter.com/VampyrGame/status/1450779093868371968

Remember Me: Remastered when?

-->

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
