---
layout: single
---

# Batman: Arkham Knight

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

[Video](https://youtu.be/v4AvZ-LjTmc)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.14 (Click to Expand)</summary>

{% highlight yml %}
- game: "Batman: Arkham Knight"
  app_ver: "01.14"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "CPU Limited. For use with 9th generation of game consoles."
  arch: generic_orbis
  enabled: False
  patch_list:
        # 60fps
        - [ bytes, 0x616ABF, "00" ]
        # prevent game from speedup above 30fps
        - [ bytes, 0x617F22, "85" ]
        # triple buffering
        - [ bytes, 0x617CA8, "04" ]
        # sync modes
        # 00 no output
        # 01 untested
        # 02 full adaptive sync // when usevsync is off
        # 03 double buffer adaptive sync // default
        # 04 triple buffering
{% endhighlight %}

</details>

## Resolution Patch (720p)

[Video](https://youtu.be/v4AvZ-LjTmc)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.14 (Click to Expand)</summary>

{% highlight yml %}
- game: "Batman: Arkham Knight"
  app_ver: "01.14"
  patch_ver: "1.0"
  name: "Resolution Patch (720p)"
  author: "illusion"
  note: 
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x276C034, "00 05 00 00 D0 02 00 00 00" ]
{% endhighlight %}

</details>
