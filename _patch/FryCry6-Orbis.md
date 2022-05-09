---
layout: single
excerpt: "Game Patch"
title: "Fry Cry: 6"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

Notes: CPU+GPU Limited. For use with 9th generation of game consoles.

Preview: ![](https://img-assets.illusion0001.workers.dev/assets/images/patches/preview/FC6-FPS/FC6-FPS-0.png)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Fry Cry 6"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  arch: generic_orbis
  enabled: False
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
