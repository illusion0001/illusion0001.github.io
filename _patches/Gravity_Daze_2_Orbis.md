# Gravity Rush 2

## 60 FPS Unlock (WORK-IN-PROGRESS)

<details>
<summary>Current Progress Preview Image (Click to Expand)</summary>

<p align="center">
<img src="https://storage.googleapis.com/assets-illusion0001/images/Gravite2-FrameratePatch/GR2-FPS3.png">
</p>

</details>

```
Help wanted! Check the rest of the game and add it to lookup table.
Pull Request are always welcome.

Current known softlock locations are:
End of Intro (regression caused by code?)
End of Epiosde 1
Beginning of Epiosde 2
Entirety of Epiosde 3
```

Notes: there are minor issues with this patch:

UI are double speed (there is a float for this but 735 of them doesn't particularly excite me to look through it..)

Some animations are double speed but movement is half speed? (best seen when looking at the miners during intro)

Some in-game cinematics are double speed.

Video playback stuttering.

[Article](https://illusion0001.github.io/patches/2021/12/19/Gravite2-FrameratePatch/)

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.11 (Click to Expand)</summary>

```
# All codes must be applied for patch to function properly!

# Framerate
0x44A981 00 00 00 00

# Flag Check Call
0x1068E4B E8 2D 61 03 FF

# Level Check Call
0x122B921 E8 2B 36 E7 FE EB 18

# Level Check Function
0x9EF50 C3 43 C6 04 3C 00 66 41 81 7C 24 00 65 70 E9 AB 01 00 00 EB 7C 89 35 AD 05 A6 01 E9 6A 00 00 00 49 8B 0C 24 48 89 0D 85 05 A6 01 EB E6 4C 89 15 84 05 A6 01 48 89 0D 85 05 A6 01 89 35 87 05 A6 01 89 3D 85 05 A6 01 4C 8D 15 AD 05 A6 01 48 8D 0D A7 05 A6 01 BF 00 01 11 4E 41 80 3A 02 0F 84 CC 00 00 00 41 80 3A 01 0F 84 F8 00 00 00 41 80 3A 03 0F 84 D9 00 00 00 48 8B 0D 41 05 A6 01 8B 3D 47 05 A6 01 E9 8B FF FF FF 48 89 FB 48 8B 03 C3 48 89 3D 48 05 A6 01 48 89 35 49 05 A6 01 48 8D 3D 7A 01 00 00 48 8D 35 4E 05 A6 01 48 39 0F 74 7C 48 39 4F 08 74 76 48 39 4F 10 74 70 48 39 4F 18 74 6A 48 39 4F 20 74 64 39 4F 28 74 5F 48 39 4F 2C 74 59 48 39 4F 34 74 53 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 EB 79 EB 7C 4C 8B 15 81 04 A6 01 48 8B 0D BE 04 A6 01 8B 35 84 04 A6 01 8B 3D 82 04 A6 01 48 89 FB 48 8B 03 C3 C7 01 89 88 08 3D BE 01 00 00 00 E8 5F C9 35 01 E9 CA FF FF FF C7 01 89 88 88 3C BE 00 00 00 00 E8 4A C9 35 01 E9 B5 FF FF FF 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 90 C6 06 01 EB 03 C6 06 03 48 8B 3D 2A 04 A6 01 48 8B 35 2B 04 A6 01 C3 0F 84 5C FE FF FF 66 41 81 7C 24 00 73 6D 0F 84 4E FE FF FF 66 41 81 7C 24 00 66 74 0F 84 40 FE FF FF E9 AB FE FF FF 60

# Currently known softlock level lookup table.
# ep00_c, ep01_d, ep02_a and ep03 are known to softlock the game
# todo: playthrough the story episodes and add any sections that
# softlock the game to this lookup table
0x9F170 65 70 30 31 5F 64 00 78 65 70 30 31 5F 63 6F 6D 65 70 30 32 5F 61 00 78 65 70 30 32 5F 61 00 35 65 70 30 31 5F 30 30 34 65 70 30 33 65 70 30 30 5F 63 00 78 65 70 30 30 5F 63 00 32

# Skip sleeping draw thread
0x451DAA EB 0C

# Flag startup
0x458AE0 C7 05 61 6A 6A 01 02 00 00 00

# Loading
0xFCCEE6 C6 05 5E 26 B3 00 02 EB 62
0xFCCF2F EB B5

# After loading
0xFCCF80 8B 05 C6 25 B3 00
```

</details>

## Semi-functional video stutter fix (FOR PATCH DEVELEOPERS ONLY)

[Article](https://illusion0001.github.io/patches/2021/12/19/Gravite2-FrameratePatch/)

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.11 (Click to Expand)</summary>

```
# Semi-functional video stutter fix
# DO NOT apply this as the draw thread will stall indefinitely after it has to sleep for 30ms during video playback.
# For patch develeopers only!

# if game_flag =! 2
# Sleep drawthread for 30ms during video playback
0x9F0CB 80 3D 28 B5 A7 01 04 0F 84 D4 2C 3B 00 48 E9 DA 2C 3B 00 48 8D 74 24 40 80 3D 10 B5 A7 01 02 0F 84 3B E3 07 01 C6 05 03 B5 A7 01 04 E9 2F E3 07 01

# Call
0x0451DA4 48 E9 21 D3 C4 FF 90 90
0x111D426 E9 B3 1C F8 FE
```

</details>
