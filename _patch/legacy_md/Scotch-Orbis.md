---
layout: single
---

# Mafia: Definitive Edition

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.03 (Click to Expand)</summary>

{% highlight yml %}
- game: "Mafia: Definitive Edition"
  app_ver: "01.03"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "CPU/GPU Limited. For use with 9th generation of game consoles."
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x2D2E2A1, "EB 05 90" ]
{% endhighlight %}

</details>