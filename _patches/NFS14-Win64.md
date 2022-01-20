# Need for Speed: Rivals

[Game Index](README.md#games)

[Installation Guide](https://illusion0001.github.io/install-instructions/)

## Framerate Patch (Cheat Engine Table) (Proof of Concept)

Author: [illusion](https://twitter.com/illusion0002)

https://www.pcgamingwiki.com/wiki/Need_for_Speed_Rivals#High_frame_rate

Can run at arbitrary framerates, For use with `NFS14` 64-bit executable, maybe someone can port this to dll injection and add support for retail. (Credit Please.)

[Cheat Table](https://storage.googleapis.com/assets-illusion0001/ct_win32/Rivals_VarFPS.CT)

<details>
<summary>CT Auto Asm Src (Click to Expand)</summary>

```
[ENABLE]
aobScanModule(gametick, NFS14.exe, 44 0F B6 60 52 44 88 65 99 41 8B 56 0C 85 D2 74 0D)
aobScanModule(fps, NFS14.exe, 75 0C 48 8B 05 FF E3 A3 01)
alloc(alloc1,32,"NFS14.exe"+3B7375)
label(_gametick)
label(_fps)
label(ret)
label(orgincode)
label(exit)
registersymbol(_gametick)
registersymbol(_fps)

alloc1:
mov [rbp+34], 0x43480000

orgincode:
movss xmm6,[rbp+34]

exit:
jmp ret

"NFS14.exe"+3B7375:
jmp alloc1
ret:

// keep alloc'd mem here

gametick:
_gametick:
db 41 C6 C4 01 90
fps:
_fps:
db 74

[DISABLE]
_gametick:
db 44 0F B6 60 52
_fps:
db 75

unregistersymbol(_gametick)
unregistersymbol(_fps)
```

</details>
