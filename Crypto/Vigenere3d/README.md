# Vigenere3d
__Genre__: Crypt
__Point__: 100pts
> Vigenere3d
> ```py
> import sys
> def _l(idx, s):
>     return s[idx:] + s[:idx]
> def main(p, k1, k2):
>     s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
>     t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
>     i1 = 0
>     i2 = 0
>     c = ""
>     for a in p:
>         c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
>         i1 = (i1 + 1) % len(k1)
>         i2 = (i2 + 1) % len(k2)
>     return c
> print main(sys.argv[1], sys.argv[2], sys.argv[2][::-1])
> ```
> $ python Vigenere3d.py SECCON{**************************} **************  
> POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9

## Writeup
There are two steps.
1. Find the key
1. Find the plain text

### Find the key
It turns out that the order difference in `s` between `s[i]` and `s[len(s)-i]` is important.
Therefore the key is first initialized to `key = "AAAAAAAAAAAAAA"` (14 characters) and `key[i](0<=i<=6)` is obtained in order for `SECCON{` in plain text to be encrypted into `POR4dny`.
Since `key` has 14 characters, 7 chars are just needed to be known in both plain and encrypted text.

```py
def solve_k():
    p = "SECCON{__________________________}"
    k = ["A"] * 14
    for i in range(7):
        for ch in s:
            k[i] = ch
            k_str = "".join(k)
            if(vigenere3d(p, k_str, k_str[::-1])[i]==c[i]):
                break
    return "".join(k)

print("key =", solve_k())
```
It is found that `key = _KP2Za_AAAAAAA` satisfies the condition.

### Find the plain text
Now that the key is found, we can decrypt.
```py
def solve_p(key):
    p = "SECCON{__________________________}"
    p = list(p)
    for i in range(7, len(p)):
        for ch in s:
            p[i] = ch
            p_str = "".join(p)
            if(vigenere3d(p, k, k[::-1])[i]==c[i]):
                break
    return "".join(p)
print(solve_p(key))
```

```
SECCON{Welc0me_to_SECCON_CTF_2017}
```
