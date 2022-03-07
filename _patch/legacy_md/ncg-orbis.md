---
layout: single
---

# Wreckfest

[Game Index](/patch/#patches)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.31 (Click to Expand)</summary>

{% highlight yml %}
- game: "Wreckfest"
  app_ver: "01.31"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "\n60FPS 99% of the time. No need for resolution patch.\nUses adapative sync."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x14460B, "95" ]
{% endhighlight %}

</details>
