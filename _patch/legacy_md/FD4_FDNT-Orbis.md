---
layout: single
---

# Dark Souls III: Network Stress Test

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## Framerate Patch

### 60 FPS Unlock (With Delta Time)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: "Dark Souls III: Network Stress Test"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "60 FPS Unlock (With Delta Time)"
  author: "illusion"
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x2390407, "C7 43 08 05 00 00 00 EB 07" ]
        - [ bytes, 0x239050C, "41 B6 01" ]
{% endhighlight %}

</details>

## 720p Resolution

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: "Dark Souls III: Network Stress Test"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "720p Resolution"
  author: "illusion"
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x5926D84, "00 05 00 00 D0 02 00 00" ]
{% endhighlight %}

</details>

<!--

### 30 FPS Limit (Proper Frame-Pacing)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
# Fliprate

# sceVideoOutSetFlipRate 0x1
{% endhighlight %}

</details>

-->
