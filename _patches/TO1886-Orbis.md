# The Order 1886

## 60 FPS Unlock

Author: [illusion](https://github.com/illusion0001)

[Article](https://illusion0001.github.io/patches/2021/06/27/oodle-res-framerate-patches/)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

```
0x4547C4 01

# screen flip mode
0x87C1F7 # dword valid are 1-6
         # see notes below

# notes
# according to the re work at gpcs4
# https://github.com/Inori/GPCS4/blob/2cb81156a1a1fd914a46fbd99cecddd6f93e7dfd/GPCS4/SceModules/SceVideoOut/sce_videoout_types.h#L115-L123
# mode 2 is pretty much flip as soon as possible, or vsync off with eye sore screen tearing
# default is 3 which i guess is double buffered vsync
# it would be good if triple buffering worked here
# as it allows for 40-60 fps and not hard locking to 30-40 all the time
# on base hw.
# r13d loads into edx, which i think is param for SubmitFlip.
```

</details>

## Resolution Patch

Author: [illusion](https://github.com/illusion0001)

[Article](https://illusion0001.github.io/patches/2021/06/27/oodle-res-framerate-patches/)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

```
# launch param -use720p
# "Use 720p resolution in fullscreen mode"
# SDK limits not letting us go below 720p.

0x450EF5 75

# For 16:9 to work; 1080p will cause visual issues
# 900p or below is a must.
# 720p doesn't need additional changes.
# 1280x720 -> 1600x900

0x450EF5 75

0x450EFD 40 06 00 00

0x450F07 84 03 00 00

# launch param -use4k
# "Use 4K resolution in fullscreen mode"
# SDK limits might come back to haunt us.
# 0x450F7E 75
# This doesn't work, SDK does not allow buffers to be created larger than
# 1920x1080
```

</details>

## 16:9 Aspect Ratio (Full Screen)

Author: [illusion](https://github.com/illusion0001)

[Article](https://illusion0001.github.io/patches/2021/06/27/oodle-res-framerate-patches/)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

```
# Native 1080p will cause visual issues, 900p or below must be used.
# 720p doesn't need additional changes.

0x450E8C 39 8E E3 3F
```

</details>
