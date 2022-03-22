---
layout: single
---

# Tekken 7

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## Disable Post Processing

Preview:
<p align="center">
<img src="https://img-assets.illusion0001.workers.dev/assets/images/patches/preview/TekkenGame/TekkenGame_PostProcess.png">
</p>

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 4.00 (Click to Expand)</summary>

{% highlight yml %}
- game: "Tekken 7"
  app_ver: "04.00"
  patch_ver: "1.0"
  name: "Disable Post Processing"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x1B01EDC, "48 E9" ]
{% endhighlight %}

</details>
