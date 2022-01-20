# Hellblade: Senua's Sacrifice

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

[Framerate analysis](https://youtu.be/DO8zPsX_ahE)

This game already runs with uncapped framerate.

Only useful for Base Console.

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

```
# all code below must be applied

# allow screenpercentage to be used
0x252C934 74 0D

# call
0x2702C8D 67 67 E8 7D 0A 22 00

# main code
0x2923710 C3 48 8B 05 C8 72 E1 02 C7 00 00 00 86 42 C3 89

# Presets:

# 540p target
C7 00 00 00 48 42 C3 89

# 720p target // default, search for this, then replace with others
C7 00 00 00 86 42 C3 89

# 900p target
C7 00 F6 A8 A6 42 C3 89

# 50.0f  = 00 00 48 42
# 67.0f  = 00 00 86 42
# 83.33f = F6 A8 A6 42
```

</details>

## Skip Startup Videos

Author: [illusion](https://twitter.com/illusion0002)

[Demo](https://cdn.discordapp.com/attachments/650395105479360514/858528041557557278/SkipMovieDemo.mp4)

Curiously enough, it makes no difference in loading times.

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

```
0x1E5C0C2 48 E9 87 06 00 00
```

</details>

## Disable Motion Blur

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

```
0x178EE71 EB 40
```

</details>

## Disable Film Grain

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

```
0x156032F EB
```

</details>

## Disable Post Processing

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

```
0x15602B5 48 E9
```

</details>
