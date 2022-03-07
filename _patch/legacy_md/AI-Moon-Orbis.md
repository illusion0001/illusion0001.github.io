---
layout: single
---

# Alien: Isolation

[Game Index](/patch/#patches)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## Skip Save Confirm Screen

[Article](https://illusion0001.github.io/patches/2021/09/09/AlienIsolation-Patches/)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

{% highlight yml %}
- game: "Alien: Isolation"
  app_ver: "01.04"
  patch_ver: "1.0"
  name: "Skip Save Confirm Screen"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x19BE0A, "EB" ]
{% endhighlight %}

</details>

## Custom FOV

[Article](https://illusion0001.github.io/patches/2021/09/09/AlienIsolation-Patches/)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

{% highlight yml %}
- game: "Alien: Isolation"
  app_ver: "01.04"
  patch_ver: "1.0"
  name: "Custom FOV (100.0)"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x15F8C6, "E8 3A 84 1D 00" ]
        - [ bytes, 0x337D05, "C7 84 21 38 00 00 00 00 00 C8 42 C5 FA 10 41 38 C3" ]
# 00 00 C8 42 = 100.0f as example, tweak this to your liking.
# highlight 00 00 C8 42 for float value
{% endhighlight %}

</details>
