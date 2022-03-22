---
layout: single
---

# Resident Evil: HD

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

[Demo](https://youtu.be/MSVD1Gmm4P8)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.00 (Click to Expand)</summary>

{% highlight yml %}
- game: "Resident Evil: HD"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0xB894B, "00 00 70 42 00 00 70 42" ]
# this is a note for other patch devs
# first bit is game tick
# second bit is target fps
# cc implemented game speed/frametime calc based on tickrate (absolute hacks :p) for win32 ver
# code path still exist which is why this is possible
{% endhighlight %}

</details>

In file `BH1HD\bh1hd.elf`

<details>
<summary>Code 1.01 (Click to Expand)</summary>

{% highlight yml %}
- game: "Resident Evil: HD"
  app_ver: "01.01"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "As part of Resident Evil Origins Collection."
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0xB9B1B, "00 00 70 42 00 00 70 42" ]
# disc ver has notes
{% endhighlight %}

</details>
