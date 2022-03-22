---
layout: single
---

# Crash Team Racing Nitro-Fueled

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.20 (Click to Expand)</summary>

{% highlight yml %}
- game: "Crash Team Racing Nitro-Fueled"
  app_ver: "01.20"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "\nCPU/GPU Limited. For use with 9th generation of game consoles.\nAlso uses double buffer vsync.\nNot useful at the moment."
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x13ADEDB, "31 F6 EB 0F" ]
{% endhighlight %}

</details>
