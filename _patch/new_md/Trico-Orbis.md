---
layout: single
patch_file: "_patch0/orbis/trico-orbis.yml"
---

# The Last Guardian

[Game Index](/patch/#ps4)

## Patches

For use with [py-patch tool](https://github.com/illusion0001/py-patcher/releases/).

[Installation Guide](/install-instructions/)

Download all [patch](/_patch/patch.zip) files.

Patch file: `{{ page.patch_file }}`

File to be patched: `eboot.bin`

Author: [illusion](https://twitter.com/illusion0002)

<details>
<summary>Contents of patch file (Click to Expand)</summary>

{% highlight yml %}
{% flexible_include {{ page.patch_file }} %}
{% endhighlight %}

</details>
