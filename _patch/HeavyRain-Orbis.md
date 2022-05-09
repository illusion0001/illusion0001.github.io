---
layout: single
excerpt: "Game Patch"
title: "Heavy Rain"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
E8 CF CE 78 00 BE 01 00 00 00

E8 CF CE 78 00 BE 00 00 00 00
{% endhighlight %}

</details>

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

{% highlight none %}
BE 80 07 00 00 48 8D 91 20 07 00 00 C7 00 00 00 00 00 48 89 48 08 C7 40 30 01 00 00 00 48 89 50 38 48 8D 91 40 0E 00 00 48 81 C1 60 15 00 00 C7 40 60 02 00 00 00 48 89 50 68 C7 80 90 00 00 00 03 00 00 00 48 89 88 98 00 00 00 BA 38 04 00 00

# 720p target

BE 00 05 00 00 48 8D 91 20 07 00 00 C7 00 00 00 00 00 48 89 48 08 C7 40 30 01 00 00 00 48 89 50 38 48 8D 91 40 0E 00 00 48 81 C1 60 15 00 00 C7 40 60 02 00 00 00 48 89 50 68 C7 80 90 00 00 00 03 00 00 00 48 89 88 98 00 00 00 BA D0 02 00 00
{% endhighlight %}

</details>
