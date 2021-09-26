# Need for Speed: Rivals

## Framerate Patch (Cheat Engine CT)

Can run at arbitrary framerates, For use with `NFS14` 64-bit executable, maybe someone can port this to dll injection and add support for retail. (Credits Please.)

Gametick: 41 C6 C4 01 90

FPS: 74 0C

<details>
<summary>CT XML (Click to Expand)</summary>

```xml
<?xml version="1.0" encoding="utf-8"?>
<CheatTable CheatEngineTableVersion="34">
  <Forms/>
  <CheatEntries>
    <CheatEntry>
      <ID>4</ID>
      <Description>"GameTick"</Description>
      <LastState Value="44 0F B6 60 52" RealAddress="1402815F8"/>
      <ShowAsHex>1</ShowAsHex>
      <ShowAsSigned>0</ShowAsSigned>
      <VariableType>Array of byte</VariableType>
      <ByteLength>5</ByteLength>
      <Address>1402815F8</Address>
    </CheatEntry>
    <CheatEntry>
      <ID>5</ID>
      <Description>"FPS"</Description>
      <LastState Value="75 0C" RealAddress="14000C4C0"/>
      <ShowAsHex>1</ShowAsHex>
      <ShowAsSigned>0</ShowAsSigned>
      <VariableType>Array of byte</VariableType>
      <ByteLength>2</ByteLength>
      <Address>14000c4c0</Address>
    </CheatEntry>
  </CheatEntries>
  <UserdefinedSymbols/>
</CheatTable>
```

</details>
