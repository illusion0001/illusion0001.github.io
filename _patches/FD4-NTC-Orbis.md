# Sekiro: Shadows Die Twice

## 60 FPS Unlock

[Demo](https://youtu.be/d8VtX2635-Q)

Author: [illusion](https://github.com/illusion0001)

Only needed for Base console, enhanced consoles already have framerate unlocked.

In file `eboot.bin`

<details>
<summary>Code 1.05 (Click to Expand)</summary>

```
# FlipMode
0x1F6A8D7 95

# VFR
# Not applying this will result in double speed.
0x1F6AA73 48 E9 6B 00 00 00
```

</details>

## Resolution Patch

[Demo](https://youtu.be/d8VtX2635-Q)

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.05 (Click to Expand)</summary>

```
# Base
# 1920x1080 -> 1280x720
0x3E2DD44 00 05 00 00 D0 02 00 00 

# Neo
# 3200x1800 -> 1920x1080
0x1F63DAF 80 07 00 00
0x1F63DB9 38 04 00 00
```

</details>
