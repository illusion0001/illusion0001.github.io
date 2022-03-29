---
layout: single
---

# Elden Ring: Network Test

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## Patch Preview

Patch applied: Resolution Patch (Neo) + 30 FPS Fix

![](https://img-assets.illusion0001.workers.dev/assets/images/patches/preview/EldenRingPatches/EldenRingNeoPreview.png)

## Framerate Patch

### 60 FPS Unlock (For Base)

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: "Elden Ring: Network Test"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "60 FPS Unlock (For Base)"
  author: "illusion"
  arch: generic_orbis
  enabled: False
  patch_list:
        # Flipmode
        - [ bytes, 0x1BF6627, "95" ]
        # VFR
        - [ bytes, 0x1BF6795, "48 E9 5B 00 00 00" ]
{% endhighlight %}

</details>

### 30 FPS Fix (Proper Frame Pacing)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: "Elden Ring: Network Test"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "30 FPS Fix (Proper Frame Pacing)"
  author: "illusion"
  note: "Locks FPS to 30 with Proper Frame Pacing."
  arch: generic_orbis
  enabled: False
  patch_list:
        # Flipmode (Base Only)
        - [ bytes, 0x1BF6627, "95" ]
        # Call
        - [ bytes, 0x2D42FF0, "E8 0F D5 39 00" ]
        # Main code
        - [ bytes, 0x30E0503, "00 BF 00 01 11 4E BE 01 00 00 00 E8 ED F8 D8 FF C3" ]
{% endhighlight %}

</details>

## Resolution Patch (720p for Base, 1080p for Pro)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: "Elden Ring: Network Test"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "Resolution Patch (720p for Base, 1080p for Pro)"
  author: "illusion"
  arch: generic_orbis
  enabled: False
  patch_list:
        # Base
        - [ bytes, 0x3C68B8C, "00 05 00 00 D0 02 00 00" ]
        # Neo
        - [ bytes, 0x1BE505F, "80 07 00 00" ]
        - [ bytes, 0x1BE5069, "38 04 00 00" ]
{% endhighlight %}

</details>

## Bypass Network Check

Author: [Whitehawkx](https://twitter.com/Whitehawkx)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: "Elden Ring: Network Test"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "Bypass Network Check"
  author: "Whitehawkx"
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x015724A0, "E9 00 01" ]
{% endhighlight %}

</details>

## Disable Fog Wall

Author: Pav

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: "Elden Ring: Network Test"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "Disable Fog Wall"
  author: "Pav"
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x013BBC33, "90 90 90 90 90" ]
{% endhighlight %}

</details>

## Enable Video Recording and Screenshots

Re-enables built-in video recording and screenshots (Share button)

Author: [Whitehawkx](https://twitter.com/Whitehawkx)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight yml %}
- game: "Elden Ring: Network Test"
  app_ver: "01.00"
  patch_ver: "1.0"
  name: "Enable Video Recording and Screenshots"
  author: "Whitehawkx"
  note: "Re-enables built-in video recording and screenshots (Share button)"
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x01BFF799, "00" ]
{% endhighlight %}

</details>
