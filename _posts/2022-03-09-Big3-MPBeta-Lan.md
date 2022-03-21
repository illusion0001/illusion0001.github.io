---
layout: single
title: "Uncharted 3 Multiplayer Beta Now Playable Without PSN (PS3)"
excerpt: "Online or Offline, you decide."
header:
  teaser: "https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/big3-pic0.png"
  overlay_image: "https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/big3-pic0.png"
  overlay_filter: 0.5
  og_image: "https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/big3-pic0.png"

categories: patches
tags: uncharted ps3 rpcs3 patches
twitter: {card: "summary_large_image"}

gallery:
  - url: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/DiscPhoto-2-Scaled.png
    image_path: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/DiscPhoto-2-Scaled.png
  - url: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/DiscPhoto-3-Scaled.png
    image_path: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/DiscPhoto-3-Scaled.png

gallery0:
  - url: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-12.png
    image_path: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-12.png
  - url: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-13.png
    image_path: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-13.png
  - url: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-15.png
    image_path: https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-15.png

toc: true
toc_sticky: true
---

# Intro

It is no secret that I have been on the Uncharted Reloaded team for a while, a group of dedicated and talented individuals in an attempt to revive the multiplayer servers that was offline since it's closure in 2019.

## The Problem

Recently I was tasked with solving a crash in one of the multiplayer public beta upon entering a secret LAN mode.

Yes, this is the same beta that was ran during June 28th to July 14th back in 2011. More details [here](https://blog.playstation.com/2011/06/28/uncharted-3-multiplayer-beta-details/).

Normally it is not possible to access this mode because on the start screen, you'll be prompted to sign in to PlayStation Network.

<div align="center">
<video width="100%" controls>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-0c.mp4" type="video/mp4">
</video>
</div>

It is possible to have access to the menus that was previous locked behind a PSN sign in prompt. Before you ask, this **does not** get rid of PSN authentication, it simply unlocks the menu. The code probably goes something like this.

```cpp
if (sku == NPUA07618) {
  LockMenuFeature = true;
  } else {
  LockMenuFeature = false;
  }
```

The game has a so called blacklist of titleIDs that will restrict access to certain features, such as gore, violence and others, there is a simple trick to get around this but first let me show you something special.

<div align="center">
<video width="100%" controls>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/Cell-XMB-0b.mp4" type="video/mp4">
</video>
</div>

That's right, Yours truly (finally) got a PlayStation 3!

Special thanks goes to the [Patrons](https://www.patreon.com/illusion0001), Vampyre, a member of the team and *you* for supporting me to be able to get a hold of such not-so rare piece of hardware.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/DiscPhoto-1-Scaled.png" %}

It is a Slim model PS3, check it out, quite a beauty isn't it? This will become useful later on.

Now back to the task at hand. 

## Infinite Solutions, Infinite Possibility

What is this simple trick you may ask? Well it is quite simple, by changing the SKU ID, which consists of the Game's Title ID that you can find printed on the spine of the case or disc.

{% include gallery id="gallery" layout="half" %}

Oh wait, is that too small? Let me zoom in.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/DiscPhoto-4-Scaled.png" %}

<div align=center>
<em>I apologize if I ruin the illusion that printed material are full color but they are not. <i class="twa thinkhappy"></i></em>
</div>

For SKU blacklist, in this case it only restricts the use of the main menu.

What will happen if the SKU is changed?

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-11stack.png" %}

With this one simple trick, we can have access to the whole menu, which includes but not limited to: Online Mode used during the beta, a Local Multiplayer mode and a options menu with a blank controller page. Will get back to that in a moment.

The funny thing about this SKU check code is it will fallback to whatever the default is set to (in this case its `UP9000-BCUS98233_00`) if the string does not match. Hot singles in your `strcmp` (string compare)? With that knowledge the SKU can be anything but the blacklisted ID of the game.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/CE-0b.png" %}

<div align=center>
<em><a href="https://www.youtube.com/user/ZEROx2085">ZEROx</a> says hi! Part of the code was written by him. :)</em>
</div>

As for LAN mode, why is it a curiosity? Because upon entering a local username, it crashes with an assertion.

```
{PPU[0x100200e] Thread (NetInit) [0x008eaebc]} SIG: Thread terminated due to fatal error.

LookupSymbolValue: Symbol '0x6f1c3f87' ("") not found!
(consider the alternate LookupSymbol)
```

A script file cannot be found, how strange. such is life I suppose.

So I had a brilliant idea, mess around in the game's memory in the area where the SKU is located.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/CE-0c.png" %}

At first I thought I was out of luck but fear not, with a little bit of trial and error of changing true to false, there is a solution.

You may have already noticed there is some `01` at the top. If you guess correctly that it should be `00` you would be correct!

<div align="center">
<video width="100%" controls>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/RPCS3-login.mp4" type="video/mp4">
</video>
</div>

The crash is solved! But it doesn't go anywhere, or does it?

<div align="center">
 <audio controls>
  <source src="https://img-assets.illusion0001.workers.dev/assets/misc/JakeChudnowMoonMen.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio>
</div>

<div align=center>
<em>Jake Chudnow  - Moon Men (<a href="https://youtu.be/sIN3gRV2T7A">Unreleased</a>)</em>
</div>

Let's try it on a real PS3.

<div align="center">
<video width="100%" controls>
  <source src="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-011.mp4" type="video/mp4">
</video>
</div>

Oh my. It works? What's with the poor performance on the menu?

Here, let's put some numbers on the screen.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-0f.png" %}

It turns out you were never supposed to be able to enter this menu, and Uncharted TV is setup for an online only environment. The rapid flicker and slowdowns are caused by the game trying to do the following:

Spawn video decoding threads -> tries to find video files on a non existent server (they were shutdown a while ago) -> despawn threads -> cycle repeat indefinitely.

```
http://d2i32rosu1so9x.cloudfront.net/1.mp4
http://d2i32rosu1so9x.cloudfront.net/2.mp4
http://d2i32rosu1so9x.cloudfront.net/u3-reveal.mp4
http://d2i32rosu1so9x.cloudfront.net/u3-e32011-trailer.mp4
http://d2i32rosu1so9x.cloudfront.net/5.mp4
http://d2i32rosu1so9x.cloudfront.net/6.mp4
```

Some of the URLs the game tries to access for videos.

A solution to this would be to outright get rid of Uncharted TV and stop the game from spawning video threads and causing slow down or if we do eventually get the online functionality working, host our own videos instead. 

Alright, where do we begin?

Luckily the video panel goes away when you enter the options menu and comes back when the user returns, with a little bit of back and forth scanning. I narrowed it down to this address. `1224C60` setting this byte to 0 will temporary turn off the video panel but the video threads are still being spawned in. Time for a breakpoint. There are two write addresses, let's have a look.

```
00700834
0070158C
```

Oh wow, check this out, this is exactly what we are after. It even has text reference to the thread name and the relevant calls to spawn a new ppu thread.

```cpp
  if (*(char *)(DAT_01224d18 + 0x2124) == '\0') {
    FUN_00700804(param_1);
    FUN_00c93f28(param_1,param_2);
    iVar12 = FUN_0070015c(param_1,0x1e);
    if (iVar12 != 0) {
      *(undefined4 *)((int)puVar7 + 0x84) = 0x21;
      ...
      *(undefined *)(param_1 + 0x120) = 1; // enable uctv byte
      **(undefined *)(param_1 + 0x1bc) = 0;
      sys_ppu_thread_create(param_1 + 0x98,&PTR_FUN_010ae048,param_1,100,0x8000,1,"YouTubeStream");
    }
  }
return 0;
```

Since the code turns it on, let's turn it off.
{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-0e.png" %}

<div align=center>
<em>That doesn't look good. <i class="twa-2x twa-eyes"></i></em>
</div>

It's worse than before and the video panel is not even shown, well something must have went wrong in the code. Should we take another look?

```cpp
      if (((*(int *)(param_1 + 0xb0) != 0) && (*(int *)(param_1 + 0xa4) != 0)) && (iVar12 != 0)) {
        uVar15 = 0xffffffff; // -1
        FUN_00c97c30(iVar12,0,0xe1000);
        ...
        return -1;
```

Ah, it could have been that if that byte was 0 it could have return -1 which is `ffffffff` in hex and caused it to run into the issue we were having earlier, let's return 0 and skip the code that tries to spawn the threads and accompanying video panel.


{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-010.png" %}

<div align=center>
<em>Hella yes! We got our performance back, and no mosh pit of slowdowns, shaka brah!</em>
</div>

Here comes the moment of truth, will other players be able to connect after the various patches has been applied?

{% include gallery id="gallery0" %}

<div align=center>
<em>Hooray! <i class="twa twa-party-popper"></i> (You can click on the images to view them bigger now.)</em>
</div>

What about the blank controller page I mentioned earlier? After loading into the multiplayer menu, the assets necessary for it is also loaded.

{% include img1 image_path="https://img-assets.illusion0001.workers.dev/assets/images/UC3-MP-BetaPlayableLan/GameOS-XMB-14.png" %}

## Closing Words

Well that's all for this post, below is where you can find the patch and support me as a independent patch creator. Have a good rest of your day! I'll catch you next time.

# Credits

[Uncharted Reloaded](https://discord.gg/qr6SjGM4gH) and Vampyre for their support.

[ZEROx](https://www.youtube.com/user/ZEROx2085) for help with some of the written code.

# Patch

<a href="/_patch/new_md/Big3-Beta-Cell" class="button" role="button"><i class='fas fa-download'></i> Patch</a>

{% include_relative _supporters.md %}
