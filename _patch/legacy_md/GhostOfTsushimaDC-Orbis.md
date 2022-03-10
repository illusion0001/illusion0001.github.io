---
layout: single
---

# Ghost of Tsushima: Director's Cut

[Game Index](/patch/#ps4)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 2.13 (Click to Expand)</summary>

{% highlight yml %}
- game: "Ghost of Tsushima: Director's Cut"
  app_ver: "02.13"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note: "Enable "Better Framerate Mode" in the game options menu on Neo. Not very useful for Base Console due to hardware limits."
  # Dev Notes: "60 FPS mode everywhere, yes even in IGCs (in game cinematics). which is an upgrade over Prospero ver."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x707B1A, "EB 12" ]
{% endhighlight %}

</details>

### 900p for Pro

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 2.13 (Click to Expand)</summary>

{% highlight yml %}
- game: "Ghost of Tsushima: Director's Cut"
  app_ver: "02.13"
  patch_ver: "1.0"
  name: "900p for Pro"
  author: "illusion"
  note: "Enable "Better Framerate Mode" in the game options menu on Neo."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x706BD1, "40 06 00 00" ]
        - [ bytes, 0x706BD5, "84 03 00 00" ]
{% endhighlight %}

</details>

### Disable Checkerboarding

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 2.13 (Click to Expand)</summary>

{% highlight yml %}
- game: "Ghost of Tsushima: Director's Cut"
  app_ver: "02.13"
  patch_ver: "1.0"
  name: "Disable Checkerboarding"
  author: "illusion"
  note: "Enable "Better Framerate Mode" in the game options menu on Neo."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x706BEA, "00" ]
{% endhighlight %}

</details>
