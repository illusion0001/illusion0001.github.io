---
layout: single
---

# Rise of the Tomb Raider

[Game Index](/patch/#patches)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Video](https://youtu.be/xnPVxnp5NHw)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Rise of the Tomb Raider"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "CPU Limited in some areas."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x49226C, "31 F6" ]
{% endhighlight %}

</details>

## Resolution Patch

[Video](https://youtu.be/xnPVxnp5NHw)

Features some minor flickering at the bottom right is caused by the patch.

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Rise of the Tomb Raider"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "Resolution Patch"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        # Base
        # This game creates a separate container for resolution
        # Which means we can set this to whatever res we want.
        # At least it's true for tr3/tr11 anyway.
        - [ bytes, 0x4AC076, "00 05 00 00" ]
        - [ bytes, 0x4AC082, "D0 02 00 00" ]
{% endhighlight %}

</details>
