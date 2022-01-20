# The Sinking City

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock + Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

```
0x2204E3A 48 E8 31 14 6D 00
0x2204706 E8 76 1B 6D 00
0x28D6270 CC 41 C7 04 8E 00 00 86 42 C4 C1 7A 10 04 8E EB 0D C7 44 21 04 55 55 85 41 C5 FA 10 61 04 C3

# Need to hardcode frametime to 16.67ms otherwise
# Dynamic res will lock to 33.33ms
# 00 00 86 42 # 67.0f
# 55 55 85 41 # 16.67f
```

</details>
