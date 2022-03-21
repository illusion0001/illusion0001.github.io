---
layout: single
---

# Deadpool

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Default flip setting is double buffer, optionally can be changed to adaptive sync at the cost of screen tearing.

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: "Deadpool"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x745AA1, "00" ]
        # Screenflip type
        # 01 Double buffer
        # 02 Adaptive sync
        # 03 triple buffering?
        # default: 01
        # 0x745FDE
{% endhighlight %}

</details>
