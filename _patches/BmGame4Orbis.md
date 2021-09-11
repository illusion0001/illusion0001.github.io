# Batman: Arkham Knight

## 60 FPS Unlock

[Video](https://youtu.be/v4AvZ-LjTmc)

CPU Limited. For use with Prospero.

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code for 1.14 (Click to Expand)</summary>

```
# 60fps
0x616ABF 00

# prevent game from speedup above 30fps
0x617F22 85

# triple buffering
0x617CA8 04

# sync modes
# 00 no output
# 01 untested
# 02 full adaptive sync // when usevsync is off
# 03 double buffer adaptive sync // default
# 04 triple buffering
```

</details>

## Resolution Patch

[Video](https://youtu.be/v4AvZ-LjTmc)

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code for 1.14 (Click to Expand)</summary>

```
0x276C034 00 05 00 00 D0 02 00 00 00
```

</details>
