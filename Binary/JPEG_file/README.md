# JPEG file
__Genre__: Binary
__Point__: 100pts
> JPEG file  
> Read this JPEG is broken.  
> It will be fixed if you change somewhere by 1 bit.  
> [tktk-892009a0993d079214efa167cda2e7afc85e6b9cb38588cba9dab23eb6eb3d46](https://files-quals.seccon.jp/tktk-892009a0993d079214efa167cda2e7afc85e6b9cb38588cba9dab23eb6eb3d46)

## Writeup
I looked up the data structure of JPEG file.
[Here](http://www.setsuki.com/hsp/ext/jpg.htm) has useful contents (sorry, it's Japanese).  
JPEG file is split by a marker, FF, from which the segment starts.
The 1 byte just after the FFs indicates the kind of segments.

Using the binary editor (like Stirling), I investigated the JPEG binary data.
I found that in 0x26F-0x270 is `FF FC`.
According to the web page above, FF FC is not defined as segments.
Therefore I modified `FF FC` into `FD FC` and obtained the JPEG file that contained the flag:

```
SECCON{jp3g_study}
```