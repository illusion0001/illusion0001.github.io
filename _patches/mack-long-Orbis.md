# Crash Bandicoot N. Sane Trilogy

**This page has been moved to the [website](https://illusion0001.github.io/patch).**

<!--


[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

Uses double buffer vsync.

For use with 9th generation of game consoles.

In file `eboot.bin`

<details>
<summary>Code 1.07 (Click to Expand)</summary>

```
# sceVideoOutSetFlipRate

E8 2D E3 D0 00

90 90 90 90 90
```

</details>
