# Grand Theft Auto V

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## 60 FPS Unlock

[Video](https://youtu.be/FqTg3Sij3MQ)

CPU Limited. For use with 9th generation of game consoles.

Author: [illusion](https://twitter.com/illusion0002)

Ported Author: [GraFfiX_221211](https://twitter.com/GraFfiX_221211)

In file `eboot.bin`


<details>
<summary>Code 1.38 (Click to Expand)</summary>

```
0xD3BB5E 01 00 00 00 
```

</details>

## Skip Intro

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`


<details>
<summary>Code 1.38 (Click to Expand)</summary>

```
0x2F3E794 00
0x286EFB8 00
```

</details>

<!--

Commenting this out when to re-test this when FCAT gets implemented.

<details>
<summary>Code 1.00 (Click to Expand)</summary>

```
BF 02 00 00 00 31 F6 E8 87 67 CB 00

BF 01 00 00 00 31 F6 E8 87 67 CB 00

##### do not apply code below
# this will introduce screen tear when param above is loaded with 0
# 2 will become 20hz
# 1 becomes 30hz
# 0 is unlocked
# code will skip sceVideoOutSetFlipRate
# 0F 44 F7 8B 3D B8 6D A4 01 E9 93 52 A6 00
# 0F 45 F7 8B 3D B8 6D A4 01 E9 93 52 A6 00
#####
```

</details>

<details>
<summary>Code 1.33 (Click to Expand)</summary>

```
BF 02 00 00 00 31 F6 E8 E7 69 DE 00

BF 01 00 00 00 31 F6 E8 E7 69 DE 00

##### do not apply code below
# this will introduce screen tear when param above is loaded with 0
# 2 will become 20hz
# 1 becomes 30hz
# 0 is unlocked
# code will skip sceVideoOutSetFlipRate
# 0F 44 F7 8B 3D A8 95 11 02 E9 53 5A C8 00
# 0F 45 F7 8B 3D A8 95 11 02 E9 53 5A C8 00
#####
```

</details>

-->
