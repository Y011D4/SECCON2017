import sys
def _l(idx, s):
    return s[idx:] + s[:idx]
def main(p, k1, k2):
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
t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
i1 = 0
i2 = 0
c = ""
p = "SECCON"
k1 = "cde"
#for a in p:
#    print(a)
#    print(s.find(a))
#    print(t[s.find(a)][38])
#    print(t[s.find(a)][s.find(k1[i1])])

    
code = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
p = "SECCON{aaaaaaaaaaaaaaaaaaaaaaaaaa}"
k = "Wdivssaaaaaaae"
k1 = k
k2 = k[::-1]
print(main(p, k1, k2))
#for i in range(len(s)):
#    #k = "Xaaaa"+s[i]+"aa"+s[(i+18)%len(s)]+"aaaad"
#    #k = "0daa"+s[i]+"Jaa1"+s[(i+18)%len(s)]+"aaaa"
#    k = "0di"+s[i]+"CJaa1U"+s[(i+18)%len(s)]+"aaa"
#    k1 = k
#    k2 = k[::-1]
#    #print(main(p, k1, k2))
#    if(main(p, k1, k2)[-3]=="t"):
#        print(main(p, k1, k2))
#        print(k)
#        print(s[i], s[(i+18)%len(s)], i)
    
#k[5], k[8]は確定
p = "SECCON{Welc0me_to_SECCON_CTFaaaaa}"
k = "0divsJ0a1aaaaa"
k1 = k
k2 = k[::-1]
print(main(p, k1, k2))
p = "SECCON{Welc0me_to_SECCON_CTF_2017}"
k = "0divsJ191aaaaa"
k1 = k
k2 = k[::-1]
print(main(p, k1, k2))
