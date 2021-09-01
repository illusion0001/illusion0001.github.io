# Horizon Zero Dawn

## 60 FPS Unlock

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.52 (Click to Expand)</summary>

```
0x125AFB 84
```

</details>

## Resolution Patch

Much like other Decima based titles, resolution doesn't make much of a different in performance.

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.52 (Click to Expand)</summary>

```
# base
# 1920x1080 -> 1280x720
0x1C74E20 00 05 00 00 D0 02 00 00

# neo
# 3840x2160 -> 1920x1080 // untested
0x1C74E48 80 07 00 00 38 04 00 00

```

</details>
