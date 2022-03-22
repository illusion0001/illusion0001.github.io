---
layout: single
---

# Skyrim

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.17 (Click to Expand)</summary>

{% highlight yml %}
- game: "Skyrim"
  app_ver: "01.17"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0xFA7A55, "01 00 00 00" ]
{% endhighlight %}

</details>

## Resolution Patch (720p for Base)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.17 (Click to Expand)</summary>

{% highlight yml %}
- game: "Skyrim"
  app_ver: "01.17"
  patch_ver: "1.0"
  name: "Resolution Patch (720p for Base)"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        # Base
        # 1920x1080 -> 1280x720
        - [ bytes, 0x126D5AB, "00 05 00 00 D0 02 00 00" ]
        # Neo // untested!
        # 3840x2160
        # 0x6A6A78
        # 0x6A6A82
        # 3520x1980
        # 0x6A6A7D
        # 0x6A6A8B
{% endhighlight %}

</details>