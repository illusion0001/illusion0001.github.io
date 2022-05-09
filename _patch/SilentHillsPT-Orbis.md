---
layout: single
excerpt: "Game Patch"
title: "Silent Hills: P.T"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## Task Lists

- [x] Framerate Unlock
- [x] 720p Internal Resolution (Currently borked)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/04/29/pt-60fps/)

Not very useful without resolution hack on PS4, Might be useful in the future for PS5 Hardware.

This game uses double buffer vsync! If rendering budget does not meet target, will drop to half refresh rate.

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
BE 01 00 00 00 E8 F3 51 2B 00

BE 00 00 00 00 E8 F3 51 2B 00
{% endhighlight %}

</details>

## Resolution Hack (Borked)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
48 B8 80 07 00 00 38 04 00 00

48 B8 00 05 00 00 D0 02 00 00
{% endhighlight %}

</details>

## Graphics Patches

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

### Disable Lens Flare

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
4D 85 F6 0F 84 AF 0C 00 00 49 8B 5D

4D 85 F6 0F 85 AF 0C 00 00 49 8B 5D
{% endhighlight %}

</details>

### Disable Camera Blur

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
0F 84 BD 0A 00 00 48 8B 15 09 28 0B 01

0F 85 BD 0A 00 00 48 8B 15 09 28 0B 01
{% endhighlight %}

</details>

### Disable Screen Space Reflections

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
55 48 89 E5 41 57 41 56 41 55 41 54 53 48 81 EC 68 01 00 00 49 89 F4 48 89 BD E8 FE FF FF 48 8B 05 53 50 E3 00

C3 48 89 E5 41 57 41 56 41 55 41 54 53 48 81 EC 68 01 00 00 49 89 F4 48 89 BD E8 FE FF FF 48 8B 05 53 50 E3 00
{% endhighlight %}

</details>

### Disable Film Grain

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
75 1F BF 40 00 00 00

74 1F BF 40 00 00 00
{% endhighlight %}

</details>

### Partial lightprobe fix

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
# Partial lightprobe fix
48 85 DB 0F 84 83 07 00 00 45 0F B7 75 10

48 85 DB 48 E9 83 07 00 00 45 0F B7 75 10

# partial mirror fix // combine with lightprobe
C5 FA 59 05 C8 BC 8F 00 C5 FA 2C C0 C5 FA 2A C8 C5 FA 5C C1 C5 FA 59 05 B8 BC 8F 00 C4 E1 FA 2C C8 4C 8D 05 28 2E 31 01

C3 FA 59 05 C8 BC 8F 00 C5 FA 2C C0 C5 FA 2A C8 C5 FA 5C C1 C5 FA 59 05 B8 BC 8F 00 C4 E1 FA 2C C8 4C 8D 05 28 2E 31 01
{% endhighlight %}

</details>
