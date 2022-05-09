---
layout: single
excerpt: "Game Patch"
title: "The Witcher 3"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

[Article](https://illusion0001.github.io/patches/2021/07/07/W3Witcher-ResPatch/)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.62 (Click to Expand)</summary>

{% highlight none %}
BE 01 00 00 00 E8 7A E2 BC 00

BE 00 00 00 00 E8 7A E2 BC 00
{% endhighlight %}

</details>

## Resolution Patch

Currently for Base Console, Pro Backbuffer is included but untested.

[Article](https://illusion0001.github.io/patches/2021/07/07/W3Witcher-ResPatch/)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.62 (Click to Expand)</summary>

{% highlight none %}
# Base
# targeting 1280x720
B9 80 07 00 00 41 B8 38 04 00 00

B9 00 05 00 00 41 B8 D0 02 00 00

# Neo
B9 80 07 00 00 41 B8 70 08 00 00

# targeting ??x??
{% endhighlight %}

</details>

## Display Framerate Stats

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/07/07/W3Witcher-ResPatch/)

In file `eboot.bin`

<details>
<summary>Code for 1.62 (Click to Expand)</summary>

{% highlight none %}
49 89 DC 0F 84 33 01 00 00 C4 C1 7A 10

49 89 DC 0F 85 33 01 00 00 C4 C1 7A 10
{% endhighlight %}

</details>
