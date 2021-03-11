# The Last of Us Patches

## Improved Loading

<details> 
<summary>Code PS4 (Click to Expand)</summary>

```
1.00

from

C6 80 D5 06 00 00 00

to

E8 DB E3 B2 FF 90 90

from

BE A0 A0 00 FF B0 07 E8 CC 90 F9 FF 4C 8D A4

to

C6 80 D5 06 00 00 00 C6 80 30 00 00 00 01 C3

####

1.10

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

## Infected's Severed Head Crash Bug Fix

<details> 
<summary>Code PS3 (Click to Expand)</summary>

```
1.00
0 006b06a8 483a4b95
0 00a5523c 3d400001
0 00a55240 7f9d5000
0 00a55244 409d0008
0 00a55248 813d0040
0 00a5524c 4e800020

1.11
0 006d9368 483aa7ed
0 00a83b54 3d400001
0 00a83b58 7f9d5000
0 00a83b5c 409d0008
0 00a83b60 813d0040
0 00a83b64 4e800020
```

</details>

<details> 
<summary>Code PS4 (Click to Expand)</summary>

```
1.00

48 8B 43 40 48 89 85 D0 F3 FF FF 4C 89 EF

to

E8 10 46 50 00 90 90 90 90 90 90 4C 89 EF

~~~

89 4C 24 34 C5 FA 2A C1 C5 FA 11 44 24 68 C5 FA 2A C8 C5 DA 5A E4 48 8D 15 70 AB 6E 00

to

48 89 85 D0 F3 FF FF 48 83 FB 00 0F 84 04 00 00 00 48 8B 43 40 C3 48 8D 15 70 AB 6E 00

####

1.10

48 8B 43 40 48 89 85 E0 F3 FF FF

to

E8 D0 53 56 00 90 90 90 90 90 90

~~~

BE A0 A0 00 FF 4C 89 EF C5 E2 5E DE 8B 48 3C 44 8B 70 48 48 8D 05

to

48 89 85 E0 F3 FF FF 48 83 FB 00 0F 84 04 00 00 00 48 8B 43 40 C3
```

</details>

## Disable Camera Shake


<details> 
<summary>Code PS3 (Click to Expand)</summary>

```
1.11 
0 00994234 997d
```

</details>

<details> 
<summary>Code PS4 (Click to Expand)</summary>

```
1.10

Find

C6 83 EC 06 00 00 01 C6 83 EA 06 00 00 00

Replace

C6 83 EC 06 00 00 01 C6 05 1C 8A 51 01 01
```

</details>
