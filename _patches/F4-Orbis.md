# Fallout 4

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.34 (Click to Expand)</summary>

```
0x10B8FB7 00 00 00 00
```

</details>

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code for 1.34 (Click to Expand)</summary>

```
# Base
# 1920x1080 -> 1280x720
0x10B8A98 00 05 00 00
0x10B8B3C D0 02 00 00

# Neo // untested!
# 2560x1440
0x9A0AFB
0x9A0B21
```

</details>
