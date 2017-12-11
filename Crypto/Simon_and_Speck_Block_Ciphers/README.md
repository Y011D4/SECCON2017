# Simon and Speck Block Ciphers
__Genre__: Crypto
__Point__: 100pts

> Simon and Speck Block Ciphers  
> https://eprint.iacr.org/2013/404.pdf  
> Simon_96_64, ECB, key="SECCON{xxxx}", plain=0x6d564d37426e6e71, cipher=0xbb5d12ba422834b5

## Writeup
I looked up and found a nice python library ([here](https://github.com/inmcm/Simon_Speck_Ciphers/tree/master/Python)).

The unknown characters in key (flag) are only 4 and can be solved by brute-force attack.

```py
import codecs
from simon import SimonCipher
from speck import SpeckCipher


plain = 0x6d564d37426e6e71
cipher = 0xbb5d12ba422834b5

flag = False
for i in range(48, 126):
    for j in range(48, 126):
        for k in range(48, 126):
            for l in range(48, 126):
                key = "SECCON{"+chr(i)+chr(j)+chr(k)+chr(l)+"}"
                key = key.encode().hex()
                key = int(key, 16)
                my_simon = SimonCipher(key, key_size=96, block_size=64)
                simon_ciphertext = my_simon.encrypt(plain)
                if(simon_ciphertext==cipher):
                    flag = True
                    break
            if(flag):
                break
        if(flag):
            break
    if(flag):
        break

print("Flag: {0}".format("SECCON{"+chr(i)+chr(j)+chr(k)+chr(l)+"}"))
```

```
SECCON{6Pz0}
```

