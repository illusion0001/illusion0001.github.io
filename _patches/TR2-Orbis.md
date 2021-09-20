# Rise of the Tomb Raider

## 60 FPS Unlock

[Video](https://youtu.be/xnPVxnp5NHw)

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

```
0x49226C 31 F6
```

</details>

## Resolution Patch

[Video](https://youtu.be/xnPVxnp5NHw)

Features some minor flickering at the bottom right is caused by the patch.

Author: [illusion](https://github.com/illusion0001)

In file `eboot.bin`

<details>
<summary>Code 1.06 (Click to Expand)</summary>

```
# Base
# This game creates a separate container for resolution
# Which means we can set this to whatever res we want.
# At least it's true for tr3/tr11 anyway.
0x4AC076 00 05 00 00
0x4AC082 D0 02 00 00
```

</details>
