---
layout: single
game_title: "Dishonored: Definitive Edition"
---

# {{ page.game_title }}

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock (CUSA02218)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.01 (Click to Expand)</summary>

{% highlight none %}
BE 01 00 00 00 E8 CE E3 22 01

BE 00 00 00 00 E8 CE E3 22 01
{% endhighlight %}

</details>
