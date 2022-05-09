---
layout: single
excerpt: "Game Patch"
title: "Judgement"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock (CUSA13197)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

All version uses disc executable.

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
48 89 7C 24 18 74 2A 89 9F D8 01 00 00

48 89 7C 24 18 75 2A 89 9F D8 01 00 00
{% endhighlight %}

</details>

## 60 FPS Unlock (CUSA15953)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.08 (Click to Expand)</summary>

{% highlight none %}
39 B7 E8 01 00 00 74 2A 48 8B 44 24 48

39 B7 E8 01 00 00 75 2A 48 8B 44 24 48
{% endhighlight %}

</details>

## Resolution Patch (Experimental)

Author: [illusion](https://twitter.com/illusion0002)

All version uses disc executable.

This patch was made and tested on Base Hardware. PS4 Pro is untested.

Changing backbuffer will cause GPU to hang.

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
# base backbuffer
# be warned, this will cause gpu hang.
# perhaps there's more buffers that i missed.
# below this one is ui buffer,
# changing to a lower value will
# over fill the screen.
40 06 00 00 84 03 00 00 20 03

# targetting 540p
C0 03 00 00 1C 02 00 00 20 03

# Pro backbuffer
# todo
# DF reported 1920x1080 so 80 07 00 00 38 04 00 00 should be one of them.
{% endhighlight %}

</details>
