---
layout: single
---

# Uncharted: The Nathan Drake Collection

[Game Index](/patch/#ps4)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## Uncharted: 1

### Intro Skip

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2022/02/05/uncharted-tlou-introskips/)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "Uncharted: 1"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Intro Skip"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x960A17, "01" ]
{% endhighlight %}

</details>

## Uncharted: 2

### Intro Skip

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2022/02/05/uncharted-tlou-introskips/)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "Uncharted: 2"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Intro Skip"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x1061E94, "01" ]
{% endhighlight %}

</details>

### Quit to Menu Crash Bug Fix

Author: [illusion](https://twitter.com/illusion0002), [ZEROx](https://github.com/Xcedf)

[Article](https://illusion0001.github.io/patches/2021/02/18/uc2-quit-menu-bug-fix/)

<details>
<summary>Code PS3 (Click to Expand)</summary>

{% highlight none %}
PS3 Version

1.00

80 4B 00 04 4E 80 04 21 E8 41 00 28 78 7C 00 20 A0 1C 04 B4

to

80 4B 00 04 4E 80 04 21 E8 41 00 28 78 7C 00 20 48 50 E8 E9

38 A0 FF FF 80 DE 81 A0 C0 3E 82 68 78 A5 00 20 C0 5E 81 98 4B FC 04 B5 60 00 00 00 FC 00 98 90

to

2F 9C 00 00 40 9E 00 0C 38 00 00 01 48 00 00 08 A0 1C 04 B4 4E 80 00 20 60 00 00 00 FC 00 98 90

1.09

80 4B 00 04 4E 80 04 21 E8 41 00 28 78 7C 00 20 A0 1C 04 B4

to

80 4B 00 04 4E 80 04 21 E8 41 00 28 78 7C 00 20 48 8C E3 01

2C 42 2C 25 73 2C 20 30 30 30 2C 20 25 73 0A 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

to

2C 42 2C 25 73 2C 20 30 30 30 2C 20 25 73 0A 00 2F 9C 00 00 40 9E 00 0C 38 00 00 01 48 00 00 08 A0 1C 04 B4 4E 80 00 20 00 00 00 00
{% endhighlight %}

</details>

<details>
<summary>Code PS4 (Click to Expand)</summary>

{% highlight none %}
1.00

from

66 41 83 BF 20 06 00 00 00 7E 5A

to

E8 87 CC 61 00 90 90 90 90 7E 5A

from

48 89 E5 41 56 53 49 89 F6 48 89 FB 48 8B 4B 08 48 8B 43 10 48 29 C1 48 C1 E9 02 83 F9 02 77

to

49 83 FF 00 0F 85 09 00 00 00 48 C7 C7 01 00 00 00 EB 07 49 8D BF 20 06 00 00 48 83 FF 00 C3

1.02

Needs porting!
{% endhighlight %}

</details>

## Uncharted: 3

### Intro Skip

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2022/02/05/uncharted-tlou-introskips/)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "Uncharted: 3"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Intro Skip"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False # Todo: move this to a separate file
  patch_list:
        - [ bytes, 0x5691D6, "00" ]
{% endhighlight %}

</details>
