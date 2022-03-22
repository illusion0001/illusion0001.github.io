---
layout: single
---

# Dark Souls III: The Fire Fades Edition

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## Framerate Patch

### 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.03 (Click to Expand)</summary>

{% highlight yml %}
- game: "Dark Souls III: The Fire Fades Edition"
  app_ver: "01.03"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "\nOnly useful for base console.\nYou must apply FPS Unlock patch to take effect on Base Console.\nPro owners do not need this patch."
  arch: generic_orbis
  enabled: False
  patch_list:
        # VFR
        - [ bytes, 0x180805D, "EB 0E" ]
        # Fliprate
        - [ bytes, 0x18081D6, "EB 0E" ]
{% endhighlight %}

</details>

### 30 FPS Limit (Proper Frame-Pacing)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.03 (Click to Expand)</summary>

{% highlight yml %}
- game: "Dark Souls III: The Fire Fades Edition"
  app_ver: "01.03"
  patch_ver: "1.0"
  name: "30 FPS Limit (Proper Frame-Pacing)"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        # Fliprate
        - [ bytes, 0x18081D6, "EB 0E" ]
        # sceVideoOutSetFlipRate 0x1
        - [ bytes, 0x21180C3, "BE 01 00 00 00 EB 03" ]
{% endhighlight %}

</details>

## 720p Resolution

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.03 (Click to Expand)</summary>

{% highlight none %}
# Replace all 3 occurrences.

80 07 00 00 38 04 00 00

00 05 00 00 D0 02 00 00
{% endhighlight %}

</details>
