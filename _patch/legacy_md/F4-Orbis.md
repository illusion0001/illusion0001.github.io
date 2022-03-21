---
layout: single
---

# Fallout 4

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.34 (Click to Expand)</summary>

{% highlight yml %}
- game: "Fallout 4"
  app_ver: "01.34"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x10B8FB7, "00 00 00 00" ]
{% endhighlight %}

</details>

## Resolution Patch (720p for Base)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.34 (Click to Expand)</summary>

{% highlight yml %}
- game: "Fallout 4"
  app_ver: "01.34"
  patch_ver: "1.0"
  name: "Resolution Patch (720p for Base)"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        # Base
        # 1920x1080 -> 1280x720
        - [ bytes, 0x10B8A98, "00 05 00 00" ]
        - [ bytes, 0x10B8B3C, "D0 02 00 00" ]
        # Neo // untested!
        # 2560x1440
        # 0x9A0AFB
        # 0x9A0B21
{% endhighlight %}

</details>
