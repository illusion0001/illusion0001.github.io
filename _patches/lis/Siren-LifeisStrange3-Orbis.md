# Life is Strange: True Colors

[Game Index](../README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

Happy new year Deck Nine Developers!

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.05 (Click to Expand)</summary>

```
0x414B742 EB 07
```

</details>

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.05 (Click to Expand)</summary>

```
0x3A0540C 48 E8 C1 84 5D 02

# 67% of internal resolution
0x5FDD8D2 00 41 C7 04 8E 00 00 86 42 C4 C1 7A 10 04 8E C3
```

</details>
