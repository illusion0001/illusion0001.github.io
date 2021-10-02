# Dark Souls III: The Fire Fades Edition

## Framerate Patch

### 60 FPS Unlock

Author: [illusion](https://github.com/illusion0001)

Only useful for base console.

You must apply FPS Unlock patch to take effect on Base Console.

Pro owners do not need this patch.

In file `eboot.bin`

<details>
<summary>Code 1.03 (Click to Expand)</summary>

```
# VFR
0x180805D EB 0E

# Fliprate
0x18081D6 EB 0E
```

</details>

### 30 FPS Limit (Proper Frame-Pacing)

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.03 (Click to Expand)</summary>

```
# Fliprate
0x18081D6 EB 0E

# sceVideoOutSetFlipRate 0x1
0x21180C3 BE 01 00 00 00 EB 03
```

</details>

## 720p Resolution

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.03 (Click to Expand)</summary>

```
# Replace all 3 occurrences.

80 07 00 00 38 04 00 00

00 05 00 00 D0 02 00 00
```

</details>
