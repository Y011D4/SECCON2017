# Ps and Qs
__Genre__: Crypto
__Point__: 300pts

> Very smooth  
> Decrypt index.html from PCAP.  
> Please, submit the flag in the format: "SECCON{" + Answer + "}"  
> \* Answer is written in index.html  
> [very_smooth_36c055008b945516b9c17e2ecce1c582c184b57c2945bbffba20372a8f9a3449.zip](https://files-quals.seccon.jp/very_smooth_36c055008b945516b9c17e2ecce1c582c184b57c2945bbffba20372a8f9a3449.zip)

## Writeup
First, I opened the .pcap file.
In line 30, 46 and 58, there is a modulus used for RSA (Secure Sockets Layer -> TLSv1 Record Layer: Handshake Protocol: Certificate -> Certificates -> Cerificate: ... -> signedCertificate -> subjectPublicKeyInfo -> subjectPublicKey: ... -> modulus).  
The modulus is:
```
0x00d546aa825cf61de97765f464fbfe4889ad8bf2f25a2175d02c8b6f2ac0c5c27b67035aec192b3741dd1f4d127531b07ab012eb86241c09c081499e69ef5aeac78dc6230d475da7ee17f02f63b6f09a2d381df9b6928e8d9e0747feba248bffdff89cdfaf4771658919b6981c9e1428e9a53425ca2a310aa6d760833118ee0d71
```
We must factorize this modulus to see ciphers but usually it's impossible.
As the title of this problem indicates, however, the factorization can be done by [Pollard's p − 1 algorithm](https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm)
Hence I wrote a program with reference to [here](http://www.cnblogs.com/Christmas/p/5185512.html):

```py
import math

n = 0x00d546aa825cf61de97765f464fbfe4889ad8bf2f25a2175d02c8b6f2ac0c5c27b67035aec192b3741dd1f4d127531b07ab012eb86241c09c081499e69ef5aeac78dc6230d475da7ee17f02f63b6f09a2d381df9b6928e8d9e0747feba248bffdff89cdfaf4771658919b6981c9e1428e9a53425ca2a310aa6d760833118ee0d71
z = []
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def gcd(a, b):
    if(b==0):
        return a
    return gcd(b, a%b)

def e(a, b):
    return pow(a, b)%n

def mysqrt(n):
    x=n
    y=[]
    while(x>0):
        y.append(x%100)
        x=x//100
    y.reverse()
    a=0
    x=0
    for p in y:
        for b in range(9,-1,-1):
            if(((20*a+b)*b)<=(x*100+p)):
                x=x*100+p - ((20*a+b)*b)
                a=a*10+b
                break
    return a

B1=mysqrt(n)
for j in range(0,len(prime)):
    for i in range(1, int(math.log(B1)/math.log(prime[j]))+1):
        z.append(prime[j])

for pp in prime:
    i=0
    x=pp
    while(1):
        x=e(x,z[i])
        i=i+1
        y=gcd(n,x-1)
        if(y!=1):
            print (y)
            p = y
            exit(0)
        if(i>=len(z)):
            break
print(p)
```
I found:
```
p = 11807485231629132025602991324007150366908229752508016230400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
```
The next step is a private .pem file to see the communication in the .pcap.
```py
import sys
sys.setrecursionlimit(1000000)  # long type,32bit OS 4B,64bit OS 8B(1bit for sign)
from Crypto.PublicKey import RSA

n = 0x00d546aa825cf61de97765f464fbfe4889ad8bf2f25a2175d02c8b6f2ac0c5c27b67035aec192b3741dd1f4d127531b07ab012eb86241c09c081499e69ef5aeac78dc6230d475da7ee17f02f63b6f09a2d381df9b6928e8d9e0747feba248bffdff89cdfaf4771658919b6981c9e1428e9a53425ca2a310aa6d760833118ee0d71
p = 11807485231629132025602991324007150366908229752508016230400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
q = n//p
e = 65537


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

phi = (p-1)*(q-1)
d = mulinv(e, phi)
key = RSA.construct([n, e, d])
print(key.exportKey().decode("utf-8"))
```
```bash
$ python genpem.py > private.pem  
$ openssl rsa -in private.pem -out private.pem.unencrypted  
```
(The second line is not needed for this problem. However, if .pem file is encrypted it is necessary.)

I imported the obtained .pem file into wireshark.

|IP address|Port|Protocol|Key File|
|:--|:--|:---|:--|
|127.0.0.1|443|http|(path to .pem)|

OK. Now I can see contents in http protocol!
```
SECCON{One of these primes is very smooth.}
```
