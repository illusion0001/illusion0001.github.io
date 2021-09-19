# Need for Speed: Rivals

## Framerate Patch 

Mostly a PoC, broken in so many ways it's unplayable.

https://www.pcgamingwiki.com/wiki/Need_for_Speed_Rivals#High_frame_rate

Needs exe to be recompiled with PC + Deltatime spec.

30 FPS Console Spec is very limited.

- Deltatime is not used at all. Maybe cannot be re-enabled too. Causes timestep fixed bugs, see above.

- Speeds up above 30FPS and not the other way around, see BF4 for this.

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

```
# GameTime.ForceSimRate
0x8611 BA 3C 00 00 00 EB 48 BA 3C 00 00 00 EB 69 00 # main // write 60 int32

0x865D EB B2 90 # jmp

# GameTime.MaxSimFps
0x5F6906  48 E8 94 0D 91 01 #
0x1F076A0 41 C7 46 28 00 00 70 42 C4 81 7A 10 46 28 C3 # main // write 60 float32
```

</details>

## Resolution Patch

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

```
# Render.ResolutionScale
0x5CF1CD # float32 (default 1.0f)
```

</details>
