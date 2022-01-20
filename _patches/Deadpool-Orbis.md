# Deadpool

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Default flip setting is double buffer, optionally can be changed to adaptive sync at the cost of screen tearing.

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

```
# Fliprate
0x745AA1 00

# Screenflip type
# 01 Double buffer
# 02 Adaptive sync
# 03 triple buffering?
# default: 01
0x745FDE
```

</details>
