---
layout: single
---

# Fry Cry 6

[Game Index](/patch/#patches)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

Notes: CPU+GPU Limited. For use with 9th generation of game consoles.

Preview: ![](https://storage.googleapis.com/assets-illusion0001/images/patches/preview/FC6-FPS/FC6-FPS-0.png)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Fry Cry 6"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x9F7471, "EB 0E" ]
        - [ bytes, 0x9F7481, "31 F6" ]
{% endhighlight %}

</details>

<!--

## Resolution Patch

CPU+GPU Limited. For use with 9th generation of game consoles.

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight none %}
# Base
#0x9EF8A9 # int32
#0x9EF8AF # int32
# Neo
#0x9EF932 # int32
#0x9EF938 # int32
{% endhighlight %}

</details>

-->
