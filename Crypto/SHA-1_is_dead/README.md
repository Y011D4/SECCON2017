# SHA-1 is dead
__Genre__: Crypto
__Point__: 100pts

> SHA-1 is dead  
> http://sha1.pwn.seccon.jp/  
> Upload two files satisfy following conditions:
> 
> 1. file1 != file2
> 1. SHA1(file1) == SHA1(file2)
> 1. SHA256(file1) <> SHA256(file2)
> 1. 2017KiB < sizeof(file1) < 2018KiB
> 1. 2017KiB < sizeof(file2) < 2018KiB  
> 
> \* 1KiB = 1024 bytes

## Writeup
In https://shattered.io/, there are 2 pdfs whose SHA-1 are same.
It is known that when both H(A)=H(B) and len(A)=len(B) are satisfied H(A+C)=H(B+C).
Therefore I downloaded the 2 pdfs, added many  same lines as line 3423 just after that line and made the size of 2 pdfs over 2017KiB.
After I uploaded those, I obtained the flag:

```
SECCON{SHA-1_1995-2017?}
```
