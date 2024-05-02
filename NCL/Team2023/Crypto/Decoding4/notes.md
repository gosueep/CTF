# Decoding 4

Given:
- password: `securepassword1!`
- `file.enc`

### Strategy

I essentially just did it with CBC to get everything but the first block decoded. I then simply manually fixed the magic bytes. 
However, I think ECB may give the correct first block regardless.
I don't know the IV stuff too well, but this could work in the future.



## AES ECB No Padding:
```
.PNG
.
...
IHDRäPYÊü..øú®¶
```

## PNG magic Bytes:
89504E470D0A1A0A0000000D49484452


## AES CBC:
```
ìd{w82)ofc89yx'j...ô...0.....pG.µ....sRGB.®Î.é.. .IDATx^´½..¤iU÷}*.N.gzrØÙ.Ù.
.dv.V.P. (*(..AäÓÏp)â«¼&Ô.. .&..T..` m`AX..(°Àîìî..éééÜ]9¼×ï.ûTÝ]SUÝ³Ëû\WOMw=á~îô?ç.Râ.Ï{a;.LJ:..>[Ò.z£!õfC...4kUi.H*..B¡ ÅÑ.Éçóvn³!.ZIüh·Û.ÿÔj5á§ÙlêO½^×{ê}.MiT.Ò¬·ô
```


## Trying different IV's
```
6d001679f18e1ac2f2a8b6ff6c5d425a 000001f4000002300806000000704799b5000000017352474200aece1
6d001679f18e1ac2f2a8b6ff6c5dee58 000001f4000002300806000000704799b5000000017352474200aece1
ec647b773832296f666338397978276a 000001f4000002300806000000704799b5000000017352474200aece1
```