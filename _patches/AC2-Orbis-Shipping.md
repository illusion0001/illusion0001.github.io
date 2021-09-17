# Assetto Corsa Competizione

## Resolution Patch

[Video](https://youtu.be/XnRTDuLJBig)

CPU Limited in Races.

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code (Click to Expand)</summary>

```
0x34BA740 E9 CB E3 38 FE 41 C7 04 8E 00 00 86 42 C4 C1 7A 10 04 8E C3 # main
0x2E93FA8 48 E9 # min frametime
0x2E96E32 48 E8 0D 39 62 00 # call

# 00 00 86 42 = 67.0f
```

</details>

## Framerate Patch

`todo(illusion) find where t.maxfps is, setting is not loaded on base hw. only on neo.`
