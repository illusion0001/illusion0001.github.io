# Days Gone

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Video](https://youtu.be/JufzJFXRlLQ)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.70 (Click to Expand)</summary>

```
0x5BAE3D0 01 00 00 00
0x386B4DB 89 05 ef 2e 5a 03
```

</details>

## Resolution Patch

[Video](https://youtu.be/JufzJFXRlLQ)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.70 (Click to Expand)</summary>

```
# Base
# 1920x1080 -> 1280x720
0x49CD818 00 05 00 00 D0 02 00 00
```

</details>
