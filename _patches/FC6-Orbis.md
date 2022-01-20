# Fry Cry 6

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

Notes: CPU+GPU Limited. For use with 9th generation of game consoles.

Preview: ![](https://storage.googleapis.com/assets-illusion0001/images/patches/preview/FC6-FPS/FC6-FPS-0.png)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

```
0x9F7471 EB 0E
0x9F7481 31 F6
```

</details>

<!--

## Resolution Patch

CPU+GPU Limited. For use with 9th generation of game consoles.

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

```
# Base
#0x9EF8A9 # int32
#0x9EF8AF # int32
# Neo
#0x9EF932 # int32
#0x9EF938 # int32
```

</details>

-->
