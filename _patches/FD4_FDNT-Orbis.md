# Dark Souls III: Network Stress Test

**This page has been moved to the [website](https://illusion0001.github.io/patch).**

<!--


[Installation Guide](https://illusion0001.github.io/install-instructions/)

## Framerate Patch

### 60 FPS Unlock (With Delta Time)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

```
0x2390407 C7 43 08 05 00 00 00 EB 07
0x239050C 41 B6 01
```

</details>

<!--

### 30 FPS Limit (Proper Frame-Pacing)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

```
# Fliprate

# sceVideoOutSetFlipRate 0x1
```

</details>

-->

## 720p Resolution

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

```
0x5926D84 00 05 00 00 D0 02 00 00
```

</details>
