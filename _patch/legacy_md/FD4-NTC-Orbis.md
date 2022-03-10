---
layout: single
---

# Sekiro: Shadows Die Twice

[Game Index](/patch/#ps4)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Demo](https://youtu.be/d8VtX2635-Q)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Sekiro: Shadows Die Twice"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "Only needed for Base console, enhanced consoles already have framerate unlocked."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        # FlipMode
        - [ bytes, 0x1F6AF27, "95" ]
        # VFR
        - [ bytes, 0x1F6B0C3, "48 E9 6B 00 00 00" ]
{% endhighlight %}

</details>

## Resolution Patch (720p Base, 1080p Pro)

[Demo](https://youtu.be/d8VtX2635-Q)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Sekiro: Shadows Die Twice"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: Resolution Patch (720p Base, 1080p Pro)
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        # Base
        # 1920x1080 -> 1280x720
        - [ bytes, 0x3E2DD44, "00 05 00 00 D0 02 00 00 " ]
        # Neo
        # 3200x1800 -> 1920x1080
        - [ bytes, 0x1F643FF, "80 07 00 00" ]
        - [ bytes, 0x1F64409, "38 04 00 00" ]
{% endhighlight %}

</details>
