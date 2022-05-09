---
layout: single
excerpt: "Game Patch"
title: "inFAMOUS Second Son"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.07 (Click to Expand)</summary>

{% highlight none %}
# Base
C7 43 0C 80 07 00 00 C7 43 10 38 04 00 00

# Presets:

# 720p target
C7 43 0C 00 05 00 00 C7 43 10 D0 02 00 00

# 540p target
C7 43 0C C0 03 00 00 C7 43 10 1C 02 00 00
{% endhighlight %}

</details>
