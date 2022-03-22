---
layout: single
---

# The Evil Within

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "The Evil Within"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "\nGPU Limited. For use with 9th generation of game consoles.\nUses Triple buffering."
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x23BCE3, "00" ]
{% endhighlight %}

</details>
