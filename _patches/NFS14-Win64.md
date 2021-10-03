# Need for Speed: Rivals

## Framerate Patch (Cheat Engine Table) (Proof of Concept)

https://www.pcgamingwiki.com/wiki/Need_for_Speed_Rivals#High_frame_rate

Can run at arbitrary framerates, For use with `NFS14` 64-bit executable, maybe someone can port this to dll injection and add support for retail. (Credits Please.)

[Cheat Table](https://assets.illusion0001.workers.dev/0:down/assets/ct_win32/Rivals_VarFPS.CT)

<details>
<summary>CT Auto Asm Src (Click to Expand)</summary>

```lua
[ENABLE]
aobScanModule(gametick, NFS14.exe, 44 0F B6 60 52 44 88 65 99 41 8B 56 0C 85 D2 74 0D)
aobScanModule(fps, NFS14.exe, 75 0C 48 8B 05 FF E3 A3 01)
label(_gametick)
registersymbol(_gametick)
label(_fps)
registersymbol(_fps)

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
