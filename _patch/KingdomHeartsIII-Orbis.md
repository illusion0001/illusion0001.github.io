---
layout: single
excerpt: "Game Patch"
title: "Kingdom Hearts III"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 720p Resolution

Author: [illusion](https://twitter.com/illusion0002)

Only useful for base console.

You may modifiy this to 50% for Pro console for (almost) 60FPS in 4k output mode, otherwise set output to 1080p and disable supersampling.

In file `eboot.bin`

<details>
<summary>Code 1.01 (Click to Expand)</summary>

{% highlight none %}
48 8B 05 59 9E CF 05 C5 F0 57 C9 C5 FA 10 00 

C5 F0 57 C9 C7 04 20 0A 57 85 42 C5 FA 10 00
{% endhighlight %}

</details>

<details>
<summary>Code 1.10 (Click to Expand)</summary>

{% highlight none %}
48 8B 05 49 B1 3E 06 C5 F0 57 C9 C5 FA 10 00

C5 F0 57 C9 C7 04 20 0A 57 85 42 C5 FA 10 00
{% endhighlight %}

</details>
