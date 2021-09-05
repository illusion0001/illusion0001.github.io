# Days Gone

## 60 FPS Unlock (Work-in-Progress)

Everything double speed. Need to find a way to re enable dynamic timestep.

[Test video](https://media.discordapp.net/attachments/682331022498594881/883831024277143672/1_23.mp4).

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.61 (Click to Expand)</summary>

```
# sync interval
# aslr addr 0x620E3D0
0x5B2E3D0 01
```

</details>

## Resolution Patch

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.61 (Click to Expand)</summary>

```
# Base
# 1920x1080 -> 1280x720
0x495D438 00 05 00 00 D0 02 00 00

# Neo
# 3840x2160 -> 1920x1080 // untested
0x2314831 80 07 00 00 38 04 00 00
```

</details>
