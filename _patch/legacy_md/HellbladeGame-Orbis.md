---
layout: single
---

# Hellblade: Senua's Sacrifice

[Game Index](/patch/#ps4)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

[Framerate analysis](https://youtu.be/DO8zPsX_ahE)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "Hellblade: Senua's Sacrifice"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Resolution Patch"
  author: "illusion"
  note: "\nThis game already runs with uncapped framerate.\nOnly useful for Base Console."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        # allow screenpercentage to be used
        - [ bytes, 0x252C934, "74 0D" ]
        # call
        - [ bytes, 0x2702C8D, "67 67 E8 7D 0A 22 00" ]
        # main code
        - [ bytes, 0x2923710, "C3 48 8B 05 C8 72 E1 02 C7 00 00 00 86 42 C3 89" ]
        # Presets:
        # 540p target
        # C7 00 00 00 48 42 C3 89
        # 720p target // default, search for this, then replace with others
        # C7 00 00 00 86 42 C3 89
        # 900p target
        # C7 00 F6 A8 A6 42 C3 89
        # 50.0f  = 00 00 48 42
        # 67.0f  = 00 00 86 42
        # 83.33f = F6 A8 A6 42
{% endhighlight %}

</details>

## Skip Startup Videos

Author: [illusion](https://twitter.com/illusion0002)

[Demo](https://cdn.discordapp.com/attachments/650395105479360514/858528041557557278/SkipMovieDemo.mp4)

Curiously enough, it makes no difference in loading times.

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "Hellblade: Senua's Sacrifice"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Skip Startup Videos"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x1E5C0C2, "48 E9 87 06 00 00" ]
{% endhighlight %}

</details>

## Disable Motion Blur

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "Hellblade: Senua's Sacrifice"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Disable Motion Blur"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x178EE71, "EB 40" ] 
{% endhighlight %}

</details>

## Disable Film Grain

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "Hellblade: Senua's Sacrifice"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Disable Film Grain"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x156032F, "EB" ]
{% endhighlight %}

</details>

## Disable Post Processing

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "Hellblade: Senua's Sacrifice"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Disable Post Processing"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x15602B5, "48 E9" ]
{% endhighlight %}

</details>
