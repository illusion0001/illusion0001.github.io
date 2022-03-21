---
layout: single
---

# Need for Speed: Rivals

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock (Proof of Concept)

https://www.pcgamingwiki.com/wiki/Need_for_Speed_Rivals#High_frame_rate

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

{% highlight yml %}
- game: "Need for Speed: Rivals"
  app_ver: "01.04"
  patch_ver: "1.0"
  name: "60 FPS Unlock (Proof of Concept)"
  author: "illusion"
  note: "\nGame can now be run at any FPS without slow down or speedups, although logics are still borked."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x494B83, "48 B2 01" ]
        - [ bytes, 0x5F6906, "48 E8 94 0D 91 01" ]
        - [ bytes, 0x1F076A0, "41 C7 46 28 00 00 70 42 C4 81 7A 10 46 28 C3" ]
{% endhighlight %}

</details>

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

{% highlight yml %}
- game: "Need for Speed: Rivals"
  app_ver: "01.04"
  patch_ver: "1.0"
  name: "Resolution Patch"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        # Render.ResolutionScale
        - [ lef32, 0x5CF1CD, 0.67 ]
{% endhighlight %}

</details>
