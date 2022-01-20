# Beyond: Two Souls

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/07/01/QDR.Infraworld-Res-Letterbox-Patch/)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

```
BE 01 00 00 00 E8 98 DD A7 00

BE 00 00 00 00 E8 98 DD A7 00
```

</details>

## Letterbox Remover

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/07/01/QDR.Infraworld-Res-Letterbox-Patch/)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

```
0F B6 F7 39 F1 74 1B

0F B6 F7 39 F1 75 1B
```

</details>

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/07/01/QDR.Infraworld-Res-Letterbox-Patch/)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

```
BE 80 07 00 00 BA 38 04 00 00

BE 40 06 00 00 BA 84 03 00 00
```

</details>
