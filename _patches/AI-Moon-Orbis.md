# Alien: Isolation

## Skip Save Confirm Screen

[Article](https://illusion0001.github.io/patches/2021/09/09/AlienIsolation-Patches/)

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

```
0x19BE0A EB
```

</details>

## Custom FOV

[Article](https://illusion0001.github.io/patches/2021/09/09/AlienIsolation-Patches/)

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.04 (Click to Expand)</summary>

```
0x15F8C6 E8 3A 84 1D 00 # Call
0x337D05 C7 84 21 38 00 00 00 00 00 C8 42 C5 FA 10 41 38 C3 # set float
# 00 00 C8 42 = 100.0f as example, tweak this to your liking.
# highlight 00 00 C8 42 for float value
```

</details>
