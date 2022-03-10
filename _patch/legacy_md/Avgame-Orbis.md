---
layout: single
---

# Vampyr

[Game Index](/patch/#ps4)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

Next Gen got a patch, why not old gen too? https://twitter.com/VampyrGame/status/1450779093868371968

Remember Me: Remastered when? :)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.07 (Click to Expand)</summary>

{% highlight yml %}
- game: "Vampyr"
  app_ver: "01.07"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x32C3726, "EB 69" ]
{% endhighlight %}

</details>

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.07 (Click to Expand)</summary>

{% highlight yml %}
- game: "Vampyr"
  app_ver: "01.07"
  patch_ver: "1.0"
  name: "Resolution Patch"
  author: "illusion"
  note: "720p for Base PS4."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x3129259, "48 E8 C6 1D 1B 00 90 90" ]
        - [ bytes, 0x32DB020, "E9 89 50 05 00 C7 00 00 00 86 42 C5 F0 57 C9 C5 FA 10 00 C3" ]
# 67.0f of 1920x1080 for base.
{% endhighlight %}

</details>
