---
layout: single
---

# Resident Evil 3

[Game Index](/patch/#ps4)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.05 (Click to Expand)</summary>

{% highlight yml %}
- game: "Resident Evil 3"
  app_ver: "01.05"
  patch_ver: "1.0"
  name: "Resolution Patch"
  author: "illusion"
  note: "720p for Base, 1080p for Pro."
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x30A09FC, "1F 85 2B 3F" ]
# 67% of 1920x1080 or 2880x1620
# 1920x1080 => 1280x720
# 2880x1620 => 1920x1080
# 00 00 80 3F = 1.00f (default)
# 1F 85 2B 3F = 0.67f
{% endhighlight %}

</details>
