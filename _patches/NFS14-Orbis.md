# Need for Speed: Rivals

## Framerate Patch (Proof of Concept)

https://www.pcgamingwiki.com/wiki/Need_for_Speed_Rivals#High_frame_rate

~~Needs exe to be recompiled with PC + Deltatime spec.~~

Solved. Game can now be run at any FPS without slow down or speedups, although logics are mostly still borked.

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

```
# GameTime.VariableSimTickTimeEnable
0x494B83 48 B2 01

# GameTime.MaxSimFps
0x5F6906  48 E8 94 0D 91 01 # call
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
