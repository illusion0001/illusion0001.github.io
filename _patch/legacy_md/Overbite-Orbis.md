---
layout: single
---

# MediEvil

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## Resolution Patch (720p)

[Article](https://illusion0001.github.io/patches/2021/10/02/Overbite-FPSFixes/)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "MediEvil"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Resolution Patch (720p)"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x21B3801, "E8 2C 00 00 00" ]
        - [ bytes, 0x21B3832, "C7 04 8B 00 00 86 42 C5 FA 10 04 8B C3" ]
        # 00 00 86 42 # 67.0f
        # 83% should be enough for neo 60fps
{% endhighlight %}

</details>

## Framerate Patch

[Article](https://illusion0001.github.io/patches/2021/10/02/Overbite-FPSFixes/)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "MediEvil"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Resolution Patch (720p)"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        # Call
        - [ bytes, 0x275C719, "E8 C7 90 FE FF" ]
        - [ bytes, 0x275C746, "1B" ]
        # FPS Function
        - [ bytes, 0x27457E0, "E9 96 F4 01 01 C5 F8 2E 0C 8B 4C 8D 14 8B 81 3C 8B 00 00 F0 41 74 0D 41 C7 82 04 D6 00 00 00 00 00 00 EB 0B 41 C7 82 04 D6 00 00 02 00 00 00 C3" ]
{% endhighlight %}

</details>