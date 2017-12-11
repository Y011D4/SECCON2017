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
