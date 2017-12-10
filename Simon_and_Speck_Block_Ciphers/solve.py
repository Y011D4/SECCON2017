#Simon_96_64, ECB, key="SECCON{xxxx}", plain=0x6d564d37426e6e71, cipher=0xbb5d12ba422834b5
import codecs
from simon import SimonCipher
from speck import SpeckCipher
#my_speck = SpeckCipher(0x123456789ABCDEF00FEDCBA987654321)
#my_simon = SimonCipher(0xABBAABBAABBAABBAABBAABBAABBAABBA)
#
#my_plaintext = 0xCCCCAAAA55553333
#print(my_plaintext)
#speck_ciphertext = my_speck.encrypt(my_plaintext)
#print(speck_ciphertext)
#speck_plaintext = my_speck.decrypt(speck_ciphertext)
#print(speck_plaintext)
#print(my_plaintext)
#simon_ciphertext = my_simon.encrypt(my_plaintext)
#print(simon_ciphertext)
#simon_plaintext = my_simon.decrypt(simon_ciphertext)
#print(simon_plaintext)




plain = 0x6d564d37426e6e71
cipher = 0xbb5d12ba422834b5


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
                    print("key", i, j, k, l)

#key = "A"
#key = key.encode().hex()
#print(key)
#print("0x"+str(key))
#key = int(key, 16)
#print(key)
