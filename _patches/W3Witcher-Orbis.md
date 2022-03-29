# The Witcher 3

**This page has been moved to the [website](https://illusion0001.github.io/patch).**

<!--


[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Article](https://illusion0001.github.io/patches/2021/07/07/W3Witcher-ResPatch/)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.62 (Click to Expand)</summary>

```
BE 01 00 00 00 E8 7A E2 BC 00

BE 00 00 00 00 E8 7A E2 BC 00
```

</details>

## Resolution Patch

Currently for Base Console, Pro Backbuffer is included but untested.

[Article](https://illusion0001.github.io/patches/2021/07/07/W3Witcher-ResPatch/)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.62 (Click to Expand)</summary>

```
# Base
# targeting 1280x720
B9 80 07 00 00 41 B8 38 04 00 00

B9 00 05 00 00 41 B8 D0 02 00 00

# Neo
B9 80 07 00 00 41 B8 70 08 00 00

# targeting ??x??
```

</details>

## Display Framerate Stats

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/07/07/W3Witcher-ResPatch/)

In file `eboot.bin`

<details>
<summary>Code for 1.62 (Click to Expand)</summary>

```
49 89 DC 0F 84 33 01 00 00 C4 C1 7A 10

49 89 DC 0F 85 33 01 00 00 C4 C1 7A 10
```

</details>
