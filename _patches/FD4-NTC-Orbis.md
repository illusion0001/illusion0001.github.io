# Sekiro: Shadows Die Twice

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Demo](https://youtu.be/d8VtX2635-Q)

Author: [illusion](https://twitter.com/illusion0002)

Only needed for Base console, enhanced consoles already have framerate unlocked.

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

```
# FlipMode
0x1F6AF27 95

# VFR
# Not applying this will result in double speed.
0x1F6B0C3 48 E9 6B 00 00 00
```

</details>

## Resolution Patch

[Demo](https://youtu.be/d8VtX2635-Q)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

```
# Base
# 1920x1080 -> 1280x720
0x3E2DD44 00 05 00 00 D0 02 00 00 

# Neo
# 3200x1800 -> 1920x1080
0x1F643FF 80 07 00 00
0x1F64409 38 04 00 00
```

</details>
