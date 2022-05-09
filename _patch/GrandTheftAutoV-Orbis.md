---
layout: single
excerpt: "Game Patch"
patch_file: "_patch0/orbis/GrandTheftAutoV-Orbis.yml"
title: "Grand Theft Auto V"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

## Patches

For use with [py-patch tool](https://github.com/illusion0001/py-patcher-bin/releases/latest).

[Video](https://youtu.be/FqTg3Sij3MQ)

Author: [illusion](https://twitter.com/illusion0002)

Ported Author: [GraFfiX_221211](https://twitter.com/GraFfiX_221211)

Patch file: `{{ page.patch_file }}`

File to be patched: `eboot.bin`

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>
