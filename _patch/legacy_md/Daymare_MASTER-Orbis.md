---
layout: single
---

# Daymare 1998

[Game Index](/patch/#ps4)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

<p align="center">
<img src="https://storage.googleapis.com/assets-illusion0001/images/patches/preview/Daymare1998/Daymare_FPS_Preview.png">
</p>

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.00 (Click to Expand)</summary>

{% highlight yml %}
- game: "Daymare 1998"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x258C177, "75" ]
        # Skips: bSmoothFrameRate
        # This patch disables all of it, see preview image for significant improvemnt.
{% endhighlight %}

</details>

## 30 FPS Fix (Proper Frame Pacing)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.00 (Click to Expand)</summary>

{% highlight yml %}
- game: "Daymare 1998"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
0x258C177 75

0xE85D82 67 E8 0F FB 6E 01 90 90

0x2575897 41 C7 04 8E 02 00 00 00 41 8B 1C 8E C5 EB 2A C3 C3
{% endhighlight %}

</details>

## Resolution Patch (720p)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.00 (Click to Expand)</summary>

{% highlight yml %}
- game: "Daymare 1998"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "Resolution Patch (720p)"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x1E95945, "E8 30 FF 6D 00" ]
        - [ bytes, 0x1E9607A, "48 E8 08 F8 6D 00" ]
        - [ bytes, 0x2575870, "48 E9 95 44 22 FE 47 ED E3 70 C7 41 04 55 55 85 41 C5 FA 10 61 04 EB 0E 41 C7 04 8E 00 00 86 42 C4 C1 7A 10 04 8E C3" ]
        # 80% seems stable enough, maybe it's not needed
        # 00 00 86 42 # 67.0f
        # 55 55 85 41 # 16.67f
{% endhighlight %}

</details>
