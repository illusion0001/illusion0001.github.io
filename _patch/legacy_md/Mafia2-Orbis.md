---
layout: single
---

# Mafia 2: Definitive Edition

[Game Index](/patch/#patches)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "Mafia 2: Definitive Edition"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "CPU/GPU Limited. For use with 9th generation of game consoles."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0xA17D16, "94" ]
{% endhighlight %}

</details>
