# Resident Evil: Zero

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Demo](https://youtu.be/TP2MTZ6gC7s)

Author: [illusion](https://twitter.com/illusion0002)

As part of Resident Evil Origins Collection

In file `BH0HD\bh0hd.elf`

<details>
<summary>Code 1.01 (Click to Expand)</summary>

```
0x329AED 00 00 70 42

# end users ignore!!
# this is a note for other patch devs
# bhd0 is a little different than bhd1
# first array is game tick
# second array is simulated tick (what we are patching)
# setting both bits to 60.0f will result in double speed
# however, setting only the second bit to 60.0f result in 60fps and no speedup
# cc implemented game speed/frametime calc based on tickrate (absolute hacks :p) for win32 ver
# code path still exist which is why this is possible
```

</details>
