# Gravity Rush 2

## 60 FPS Unlock (NON-WORKING) (WORK-IN-PROGRESS)

<details>
<summary>Current Progress Preview Image (Click to Expand)</summary>

![](https://storage.googleapis.com/assets-illusion0001/images/patches/preview/GravityDaze2/GD2-32FPS.png)

</details>

```
Help wanted! Find a way to disable internal frame limter.
Pull Request is always welcome.

1. Internal Frame Limter caps out at 31-32 FPS.

2. sceVideoOutSetFlipRate 0x1 for new frame every 33.33ms.
   They likely used kernel function for proper frame-pacing.
```

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.00 (Click to Expand)</summary>

```
BE 01 00 00 00 E8 86 F2 F6 00

BE 00 00 00 00 E8 86 F2 F6 00
```

</details>

<details>
<summary>Code 1.11 (Click to Expand)</summary>

```
BE 01 00 00 00 E8 86 10 FB 00

BE 00 00 00 00 E8 86 10 FB 00
```

</details>

## 60 FPS Mode

```
Help wanted! Find a way to disable internal frame limter.
Pull Request is always welcome.

This will make the game run at half speed. It was used for remastered to run at 60FPS.
```

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.00 (Click to Expand)</summary>

```
C6 05 3C D2 65 01 01

C6 05 3C D2 65 01 00
```

</details>

<details>
<summary>Code 1.11 (Click to Expand)</summary>

```
C6 05 BC 65 6A 01 01

C6 05 BC 65 6A 01 00
```

</details>
