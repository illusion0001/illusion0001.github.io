---
layout: single
---

# Mad Max

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

[Demo](https://youtu.be/Cr-fdcSJros)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Mad Max"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0xF2F900, "BE 00 00 00 00 90 90 90" ]
{% endhighlight %}

</details>

## Resolution Patch (720p)

[Demo](https://youtu.be/Cr-fdcSJros)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Mad Max"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "Resolution Patch (720p)"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        # 1920x1080 -> 1280x720
        - [ bytes, 0xA92F48, "00 05 00 00 D0 02 00 00" ]
{% endhighlight %}

</details>

## Disable Motion Blur

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Mad Max"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "Disable Motion Blur"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0xAA7F5A, "00" ]
{% endhighlight %}

</details>
