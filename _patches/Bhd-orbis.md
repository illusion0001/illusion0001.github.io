# Resident Evil: HD

## 60 FPS Unlock

[Demo](https://youtu.be/MSVD1Gmm4P8)

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.00 (Click to Expand)</summary>

```
0xB894B 00 00 70 42

# end users ignore!!
# this is a note for other patch devs
# setting only the first bit to 60.0f is needed
# second bit doesn't seem to do anything
# cc implemented game speed/frametime calc based on tickrate (absolute hacks :p) for win32 ver
# code path still exist which is why this is possible
```

</details>

As part of Resident Evil Origins Collection

In file `BH1HD\bh1hd.elf`

<details>
<summary>Code 1.01 (Click to Expand)</summary>

```
0xB9B1B 00 00 70 42
# disc ver has notes
```

</details>
