---
layout: single
---

# Assetto Corsa Competizione

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## Resolution Patch (720p)

[Video](https://youtu.be/XnRTDuLJBig)

CPU Limited in Races.

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: Assetto Corsa Competizione
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "Resolution Patch (720p)"
  author: "illusion"
  note: "CPU Limited in Races."
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x34BA740, "E9 CB E3 38 FE 41 C7 04 8E 00 00 86 42 C4 C1 7A 10 04 8E C3" ]
        - [ bytes, 0x2E93FA8, "48 E9" ]
        - [ bytes, 0x2E96E32, "48 E8 0D 39 62 00" ]
{% endhighlight %}

</details>