# Driveclub

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock (Work-In-Progress!)

Author: [illusion](https://twitter.com/illusion0002)

Timer is currently double speed.

- [ ] Find dynamic timestep from Motorstorm PS3 or Driveclub VR titles. (requires brute forcing, how-to in patch comments, contact me on discord if you managed to get the game speed + sound pitch run at half speed globally.)

In file `eboot.bin`

<details>
<summary>Code 1.28 (Click to Expand)</summary>

```
# fliprate
44 89 F6 E8 C2 B0 FF FF

31 F6 90 E8 C2 B0 FF FF

# min timestep
EC 51 B8 1E 85 EB A1 3F 89 88 08 3D 89 88 08 3D 89 88 08 3D

EC 51 B8 1E 85 EB A1 3F 89 88 88 3C 89 88 88 3C 89 88 88 3C

# notes for anyone wanting to help solve dynamic timestep
#
# game speed is 1.0f or 00 00 80 3f, on PS3 titles, one of the float controlls game and sound speed.
1.0f = 00 00 80 3f
0.5f = 00 00 00 3f
# there's over 10k results and replacing all is not an option
# if anyone has a better solution for patching bin
# via a patch file would be greatly appreciated.
# hex edit suck for brute forcing like this.
# Motorstorm®: APOCALYPSE Singleplayer Demo [NPEA90090]
# PPU-afb6e2e47e170711041775e0280707e503469d85:
#  - [ bef32, 0x001d7238, 0.5 ] # game+sound pitch scale.
                                # byte that controls timestep + delta time
                                # is right next to this one in memory,
                                # hope it's the same here on driveclub.
                                # mem address on ps3 350E36C4 (CE: 0x3350E36C4)
# PS3 mem layout for gametime
# 3F 80 00 00 00 00 00 02 00 00 00 00 01 01 00 00 00 00 00 00 00 00 00 00
# ^                    ^            ^
# |                    |            |
# |                    |            |
# Game speed           |            |
#                      min timestep |
#                                   |
#                                   delta time (flip this to 1)
#                                                              
```

</details>
