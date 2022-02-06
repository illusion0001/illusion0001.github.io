# The Last of Us

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## Improved Loading

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/02/10/t1r-improve-loading/)

Notes: Update 1.11 already has the fix.

In file `eboot.bin`

<details>
<summary>Code PS4 1.00 (Click to Expand)</summary>

```
from

C6 80 D5 06 00 00 00

to

E8 DB E3 B2 FF 90 90

from

BE A0 A0 00 FF B0 07 E8 CC 90 F9 FF 4C 8D A4

to

C6 80 D5 06 00 00 00 C6 80 30 00 00 00 01 C3
```

</details>

<details>
<summary>Code PS4 1.10 (Click to Expand)</summary>

```
from

0F 8F 47 01 00 00 41 C6

to

0F 8F 4E 01 00 00 41 C6
~~~
from

74 27 48 8D 3D 48 24

to

74 2E 48 8D 3D 48 24
~~~
from

C6 80 DF 06 00 00 00 44 89 F0 48 83 C4 08 5B 41 5E 41 5F 5D C3 90 90 90 90 90 90 90

to

C6 80 DF 06 00 00 00 C6 80 30 00 00 00 01 44 89 F0 48 83 C4 08 5B 41 5E 41 5F 5D C3
```

</details>

## Intro Skip

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2022/02/05/uncharted-tlou-introskips/)

In file `eboot.bin`

<details>
<summary>Code PS4 1.10/1.11 (Click to Expand)</summary>

```
0x614A C6 87 E5 34 00 00 01
```

</details>

## University Nailbomb Softlock Fix

Author: [illusion](https://twitter.com/illusion0002), [ZEROx](https://github.com/Xcedf)

[Article](https://illusion0001.github.io/patches/2021/12/04/t1-nailbomb-softlock-patch/)

In file `eboot.bin`

<details>
<summary>Code PS4 1.11 (Click to Expand)</summary>

```
# call

0x6A67A7 E9 A4 38 9D FF 90 90 90 90 90

# main

0x7A050 44 89 05 99 4C 7A 01 4C 8D 05 2A CF 5C 01 41 81 38 F0 8E BC 40 74 22 41 81 38 CF F0 66 A4 74 19 41 81 38 6A 06 B6 9A 74 10 41 81 38 5C 5D 81 11 74 07 41 81 38 C8 5F D3 4A 44 8B 05 60 4C 7A 01 0F 85 1B C7 62 00 E9 1C C9 62 00
```

</details>

## Infected's Severed Head Crash Bug Fix

Author: [illusion](https://twitter.com/illusion0002), [ZEROx](https://github.com/Xcedf)

[Article](https://illusion0001.github.io/patches/2021/02/15/t1-head-crash-bug-fix/)

In file `eboot.bin`

<details>
<summary>Code PS4 1.00 (Click to Expand)</summary>

```
48 8B 43 40 48 89 85 D0 F3 FF FF 4C 89 EF

to

E8 10 46 50 00 90 90 90 90 90 90 4C 89 EF

~~~

89 4C 24 34 C5 FA 2A C1 C5 FA 11 44 24 68 C5 FA 2A C8 C5 DA 5A E4 48 8D 15 70 AB 6E 00

to

48 89 85 D0 F3 FF FF 48 83 FB 00 0F 84 04 00 00 00 48 8B 43 40 C3 48 8D 15 70 AB 6E 00

```

</details>

<details>
<summary>Code PS4 1.10 (Click to Expand)</summary>

```
48 8B 43 40 48 89 85 E0 F3 FF FF

to

E8 D0 53 56 00 90 90 90 90 90 90

~~~

BE A0 A0 00 FF 4C 89 EF C5 E2 5E DE 8B 48 3C 44 8B 70 48 48 8D 05

to

48 89 85 E0 F3 FF FF 48 83 FB 00 0F 84 04 00 00 00 48 8B 43 40 C3
```

</details>

<details>
<summary>Code PS4 1.11 (Click to Expand)</summary>

```
48 8B 43 40 48 89 85 E0 F3 FF FF

E8 72 53 56 00 90 90 90 90 90 90

55 48 89 E5 41 57 41 56 41 55 41 54 53 48 83 E4 E0 48 81 EC 00 01 00 00 C5 FA 10 B7 C4 28 00 00

48 89 85 E0 F3 FF FF 48 83 FB 00 74 04 48 8B 43 40 C3 81 EC 00 01 00 00 C5 FA 10 B7 C4 28 00 00
```

</details>

## Disable Camera Shake

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/03/03/uc3-t1-camshake/)

In file `eboot.bin`

<details>
<summary>Code PS4 1.10 (Click to Expand)</summary>

```
Find

C6 83 EC 06 00 00 01 C6 83 EA 06 00 00 00

Replace

C6 83 EC 06 00 00 01 C6 05 1C 8A 51 01 01
```

</details>

## Improved Cheat Codes

Author: [illusion](https://twitter.com/illusion0002), [ZEROx](https://github.com/Xcedf)

[Article](https://illusion0001.github.io/cheatcodes/2021/03/12/t1-cheat-porting/)

In file `eboot.bin`

<details>
<summary>Code PS4 1.10 (Click to Expand)</summary>

```
qmenu

E8 B5 A8 F9 FF BF A0 00 00 00 49 89 C7 E8 D8 1D C1 00 48 89 C3 48 8D 35 1C 36 02 01 31 C9 45 31 C0 4C 89 FA 48 89 DF E8 6E DB 9B 00 4C 89 F7 48 89 DE E8 63 EA 9B 00 BF A0 00 00 00

90 90 90 90 90 BF A0 00 00 00 E8 DB 1D C1 00 48 89 C3 48 8D 35 60 62 02 01 48 8D 15 D2 5A 4B 01 48 89 DF E8 E2 A5 9B 00 4C 89 F7 48 8B F3 E8 67 EA 9B 00 90 90 90 90 BF A0 00 00 00

flashlight

C4 C1 7A 11 95 D4 07 00 00 41 80

C4 81 7A 11 8D D4 07 00 00 41 80

call1

66 45 89 B4 5F F4 00 00 00 44 29

E8 59 8A B9 00 90 90 90 90 44 29

call2

47 F4 00 00 00 44 89 CE 29 D6 66 0F

47 F4 00 00 00 E8 1B 86 B9 00 66 0F

subr1 and 2

55 48 89 E5 41 57 41 56 41 55 41 54 53 48 83 EC 18 48 8D 05 88 DD B7 00 41 BD C8 00 00 00 48 89 F1 48 89 FB BE 00 20 F0 FF 48 89 CF 48 89 4D D0 8B 50 3C 44 03 68 40 B0 02 83 C2 28 C4 E1 FA 2A C2 48 89 55 C8 48 8D 15 0C EB 56 00 C4 C1 FA 2A CD E8 CA C2 F8 FF 41 BF 01 00 00 00 45 31 F6 45 31 E4 66 66 66 66 66 2E 0F 1F 84 00 00 00 00 00 4A 8B 84 F3 C8 29 00 00 89 C1 83 E1 01 48 85 C0

80 3D A1 32 90 00 00 74 0D 66 41 C7 84 5F F4 00 00 00 6F 09 EB 09 66 45 89 B4 5F F4 00 00 00 C3 F1 48 89 FB BE 00 20 F0 FF 48 89 CF 48 89 4D D0 8B 50 3C 44 03 68 40 B0 02 83 C2 28 C4 E1 FA 2A C2 48 89 55 C8 48 8D 15 0C EB 56 00 C4 C1 FA 2A CD E8 CA C2 F8 FF 41 BF 01 00 00 00 45 31 F6 45 31 E4 66 66 66 66 66 2E 0F 1F 84 00 00 00 00 00 44 89 CE 80 3D 2E 32 90 00 00 75 02 29 D6 C3 C0

call3 (tools pickup 5)

FF 84 BB 48 64 01 00 8B 5D 88

67 67 E8 19 FD FF FF 8B 5D 88

subr3

E8 70 DB 01 01 5D C3 90 90 90 90 90 90 90 90 90 90 90 90 90 90

E8 70 DB 01 01 5D C3 C7 84 BB 48 64 01 00 05 00 00 00 C3 90 90

Text

63 3A 2F 70 65 72 66 6F 72 63 65 2F 64 69 73 63 62 6F 74 30 32 2F 74 31 70 73 34 66 69 6E 61 6C 2D 31 2E 31 30 2F 74 31 70 73 34 2F 73 72 63 2F 67 61 6D 65 2F 67 61 6D 65 2D 69 6E 76 65 6E 74 6F 72 79 2E 63 70 70 00 49 6E 69 74

49 6E 66 69 6E 69 74 65 20 45 76 65 72 79 74 68 69 6E 67 20 28 41 6D 6D 6F 2C 20 49 74 65 6D 73 2C 20 53 6B 69 6C 6C 73 2C 20 50 61 72 74 73 29 00 61 6D 65 2F 67 61 6D 65 2D 69 6E 76 65 6E 74 6F 72 79 2E 63 70 70 00 49 6E 69 74
```

</details>
