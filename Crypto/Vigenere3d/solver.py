import sys
def _l(idx, s):
    return s[idx:] + s[:idx]
def vigenere3d(p, k1, k2):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
    i1 = 0
    i2 = 0
    c = ""
    for a in p:
        c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)
    return c
#print(main(sys.argv[1], sys.argv[2], sys.argv[2][::-1]))

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
c = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"

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


def solve_p(k):
    p = "SECCON{__________________________}"
    p = list(p)
    for i in range(7, len(p)):
        for ch in s:
            p[i] = ch
            p_str = "".join(p)
            if(vigenere3d(p, k, k[::-1])[i]==c[i]):
                break
    return "".join(p)
    

k = solve_k()
print("key: {0}".format(k))
p = solve_p(k)
print("plain: {0}".format(p))
