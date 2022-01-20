# Resident Evil: HD

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Demo](https://youtu.be/MSVD1Gmm4P8)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.00 (Click to Expand)</summary>

```
0xB894B 00 00 70 42 00 00 70 42

# this is a note for other patch devs
# first bit is game tick
# second bit is target fps
# cc implemented game speed/frametime calc based on tickrate (absolute hacks :p) for win32 ver
# code path still exist which is why this is possible
```

</details>

As part of Resident Evil Origins Collection

In file `BH1HD\bh1hd.elf`

<details>
<summary>Code 1.01 (Click to Expand)</summary>

```
0xB9B1B 00 00 70 42 00 00 70 42
# disc ver has notes
```

</details>
