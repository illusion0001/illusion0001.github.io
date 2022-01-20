# Mad Max

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Demo](https://youtu.be/Cr-fdcSJros)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

```
0xF2F900 BE 00 00 00 00 90 90 90
```

</details>

## Resolution Patch

[Demo](https://youtu.be/Cr-fdcSJros)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

```
# 1920x1080 -> 1280x720
0xA92F48 00 05 00 00 D0 02 00 00
```

</details>

## Disable Motion Blur

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

```
0xAA7F5A 00
```

</details>
