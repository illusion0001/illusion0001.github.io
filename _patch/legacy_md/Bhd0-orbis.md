---
layout: single
---

# Resident Evil: Zero

[Game Index](/patch/#ps4)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Demo](https://youtu.be/TP2MTZ6gC7s)

Author: [illusion](https://twitter.com/illusion0002)

In file `BH0HD\bh0hd.elf`

<details>
<summary>Code 1.01 (Click to Expand)</summary>

{% highlight yml %}
- game: "Resident Evil: Zero"
  app_ver: "01.01"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "As part of Resident Evil Origins Collection."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x329AED, "00 00 70 42" ]

# this is a note for other patch devs
# bhd0 is a little different than bhd1
# first array is game tick
# second array is simulated tick (what we are patching)
# setting both bits to 60.0f will result in double speed
# however, setting only the second bit to 60.0f result in 60fps and no speedup
# cc implemented game speed/frametime calc based on tickrate (absolute hacks :p) for win32 ver
# code path still exist which is why this is possible
{% endhighlight %}

</details>
