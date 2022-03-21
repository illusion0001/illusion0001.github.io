---
layout: single
---

# Life is Strange: True Colors

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

Happy new year Deck Nine Developers!

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.05 (Click to Expand)</summary>

{% highlight yml %}
- game: "Life is Strange: True Colors"
  app_ver: "01.05"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x414B742, "EB 07" ]
{% endhighlight %}

</details>

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.05 (Click to Expand)</summary>

{% highlight yml %}
- game: "Life is Strange: True Colors"
  app_ver: "01.05"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x3A0540C, "48 E8 C1 84 5D 02" ]
        - [ bytes, 0x5FDD8D2, "00 41 C7 04 8E 00 00 86 42 C4 C1 7A 10 04 8E C3" ]
{% endhighlight %}

</details>
