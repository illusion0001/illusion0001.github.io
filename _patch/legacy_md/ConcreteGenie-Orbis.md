---
layout: single
---

# Concrete Genie

[Game Index](/patch/#patches)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

Patch version: 1.2

- Added support for PS4 Pro.

- Optimize Code, separated res code into separate entry.

In file `eboot.bin`

<details>
<summary>Code for 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Concrete Genie"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: 
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x2F98C96, "74 69" ]
{% endhighlight %}

</details>

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Concrete Genie"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "Resolution Patch"
  author: "illusion"
  note: 
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x2D41546, "c7 40 00 0a 57 85 42" ]
        # 0a 57 85 42 = 66.67f
        # 7F AA A6 42 = 83.33f
{% endhighlight %}

</details>

## Disable Motion Blur

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.06 (Click to Expand)</summary>

{% highlight yml %}
- game: "Concrete Genie"
  app_ver: "01.06"
  patch_ver: "1.0"
  name: "Disable Motion Blur"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x1BB4219, "EB 58" ]
{% endhighlight %}

</details>
