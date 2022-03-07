---
layout: single
---

# Horizon Zero Dawn

[Game Index](/patch/#patches)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.52 (Click to Expand)</summary>

{% highlight yml %}
- game: "Horizon Zero Dawn"
  app_ver: "01.52"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x125AFB, "84" ]
{% endhighlight %}

</details>

## Resolution Patch

Much like other Decima based titles, resolution doesn't make much of a different in performance.

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.52 (Click to Expand)</summary>

{% highlight yml %}
- game: "Horizon Zero Dawn"
  app_ver: "01.52"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        # base
        # 1920x1080 -> 1280x720
        - [ bytes, 0x1C74E20, "00 05 00 00 D0 02 00 00" ]
        # neo
        # 3840x2160 -> 1920x1080 // untested
        - [ bytes, 0x1C74E48, "80 07 00 00 38 04 00 00" ]
{% endhighlight %}

</details>
