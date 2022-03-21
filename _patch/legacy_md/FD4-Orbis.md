---
layout: single
---

# Bloodborne

[Game Index](/patch/#patches)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 30 FPS Limit (Proper Frame-Pacing)

[Video](https://youtu.be/seKQOQy5Ab4)

Author: [illusion](https://twitter.com/illusion0002), [manfightdragon](https://twitter.com/manfightdragon)

In file `eboot.bin`

<details>
<summary>Code 1.09 (Click to Expand)</summary>

{% highlight none %}
# both code must be applied to take effect!!

# lift engine 30 fps cap
# set min timestep to 0.166667
# from manfightdragon
# https://www.patreon.com/posts/47314774
41 C7 44 24 18 89 88 08 3D 48 B9 00 00 00 00 1E

41 C7 44 24 18 89 88 88 3C 48 B9 00 00 00 00 1E

# sceVideoOutSetFlipRate to 0x1
# this works because it is now relying on the kernel function to cap
# the framerate rather than the engine
85 C0 49 89 DC 0F 88 2F 01 00 00 31 F6 89 C7 E8 85 93 4E 00

BE 01 00 00 00 49 89 DC 90 90 90 90 90 89 C7 E8 85 93 4E 00

## notes:
# Kernel function will provide fixed rate of update time.
# 0x0 16.67ms -- 60hz
# 0x1 33.33ms -- 30hz fix bad frame pacing.
# 0x2 50.00ms -- 20hz
##
{% endhighlight %}

</details>

## Disable Chromatic Aberration

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.09 (Click to Expand)</summary>

{% highlight yml %}
- game: "Bloodborne"
  app_ver: "01.09"
  patch_ver: "1.0"
  name: "Disable Chromatic Aberration"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x22A3AA8, "C7 83 AC 00 00 00 00 00 00 00 90 90" ]
{% endhighlight %}

</details>

## Disable Motion Blur

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.09 (Click to Expand)</summary>

{% highlight yml %}
- game: "Bloodborne"
  app_ver: "01.09"
  patch_ver: "1.0"
  name: "Disable Motion Blur"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x22A457B, "EB 16" ]
{% endhighlight %}

</details>
