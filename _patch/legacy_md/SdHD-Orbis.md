---
layout: single
---

# Sleeping Dogs: Definitive Edition

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.07 (Click to Expand)</summary>

{% highlight yml %}
- game: "Sleeping Dogs: Definitive Edition"
  app_ver: "01.07"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "CPU/GPU Limited. For use with 9th generation of game consoles."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x70B88B, "00 00 00 00" ]
{% endhighlight %}

</details>
