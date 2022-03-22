---
layout: single
---

# The Order 1886

[Game Index](/patch/#ps4)

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/06/27/oodle-res-framerate-patches/)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "The Order 1886"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "60 FPS Unlock"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x4547C4, "01" ]
        # screen flip mode
        # 0x87C1F7 # dword valid are 1-6
                # see notes below

        # notes
        # according to the from gpcs4
        # https://github.com/Inori/GPCS4/blob/2cb81156a1a1fd914a46fbd99cecddd6f93e7dfd/GPCS4/SceModules/SceVideoOut/sce_videoout_types.h#L115-L123
        # mode 2 is pretty much flip as soon as possible, or vsync off with eye sore screen tearing
        # default is 3 which i guess is double buffered vsync
        # it would be good if triple buffering worked here
        # as it allows for 40-60 fps and not hard locking to 30-40 all the time
        # on base hw.
        # r13d loads into edx, which i think is param for SubmitFlip.
{% endhighlight %}

</details>

## Resolution Patch (900p)

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/06/27/oodle-res-framerate-patches/)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "The Order 1886"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "Resolution Patch (900p)"
  author: "illusion"
  note:
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x450EF5, "75" ]
        - [ bytes, 0x450EFD, "40 06 00 00" ]
        - [ bytes, 0x450F07, "84 03 00 00" ]
{% endhighlight %}

</details>

## 16:9 Aspect Ratio (Full Screen)

Author: [illusion](https://twitter.com/illusion0002)

[Article](https://illusion0001.github.io/patches/2021/06/27/oodle-res-framerate-patches/)

In file `eboot.bin`

<details>
<summary>Code 1.02 (Click to Expand)</summary>

{% highlight yml %}
- game: "The Order 1886"
  app_ver: "01.02"
  patch_ver: "1.0"
  name: "16:9 Aspect Ratio (Full Screen)"
  author: "illusion"
  note: "\nNative 1080p will cause visual issues, 900p or below must be used.\n720p doesn't need additional changes."
  arch: generic_orbis
  enabled: False
  patch_list:
        - [ bytes, 0x450E8C, "39 8E E3 3F" ]
{% endhighlight %}

</details>