# Ghost of Tsushima: Director's Cut

**This page has been moved to the [website](https://illusion0001.github.io/patch).**

<!--


[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

Mandatory Notes: Enable "Better Framerate Mode" in the game options menu on Neo. Not very useful for Base Console due to hardware limits.

Dev Notes: 60 FPS mode everywhere, yes even in IGCs (in game cinematics). which is an upgrade over Prospero ver.

In file `eboot.bin`

<details>
<summary>Code 2.13 (Click to Expand)</summary>

```
0x707B1A EB 12
```

</details>

## Untested Resolution Patches

**Do not use these unless you know what you are doing!**

### 1080p for Pro

Author: [illusion](https://twitter.com/illusion0002)

Mandatory Notes: Enable "Better Framerate Mode" in the game options menu on Neo.

In file `eboot.bin`

<details>
<summary>Code 2.13 (Click to Expand)</summary>

```
0x706BD1 80 07 00 00 # int32 1920

0x706BD5 38 04 00 00 # int32 1080
```

</details>


### Disable Checkerboarding?

Author: [illusion](https://twitter.com/illusion0002)

Mandatory Notes: Enable "Better Framerate Mode" in the game options menu on Neo.

In file `eboot.bin`

<details>
<summary>Code 2.13 (Click to Expand)</summary>

```
0x706BEA 00
```

</details>
