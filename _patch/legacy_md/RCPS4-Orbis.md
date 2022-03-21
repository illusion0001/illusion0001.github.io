---
layout: single
---

# Ratchet and Clank

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.09 (Click to Expand)</summary>

{% highlight yml %}
- game: "Ratchet and Clank"
  app_ver: "01.09"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "GPU Limited. For use with 9th generation of game consoles."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x31F834, "90 90" ]
{% endhighlight %}

</details>
