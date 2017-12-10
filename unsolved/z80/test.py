mem = [0x22, 0x47, 0x00, 0x3d, 0x53, 0x77, 0x23, 0x3d, 0x45, 0x77, 0x23, 0x3d, 0x43, 
  0x77, 0x23, 0x77, 0x23, 0xc5, 0x0c, 0x77, 0x23, 0xc5, 0xfd, 0x77, 0x23, 0x3d, 
  0x7b, 0x77, 0x23, 0x39, 0x44, 0x00, 0x47, 0xc5, 0x46, 0x31, 0x44, 0x00, 0x78, 
  0x31, 0x46, 0x00, 0xfd, 0x22, 0xf9, 0x1e, 0x00, 0xfd, 0x7b, 0xf1, 0x1e, 0x00, 
  0x77, 0x23, 0x39, 0x45, 0x00, 0x3e, 0x31, 0x45, 0x00, 0xc1, 0x1e, 0x00, 0x3d, 
  0x7d, 0x77, 0x75, 0x03, 0x0b, 0x09] + [0x00]*1000

print(list(map(chr, mem)))

ADDR = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
def readAddr():
    global ADDR
    result = 0
    for i in range(15, -1, -1):
        result += result
        if(ADDR[i]==1):
            result |= 1
    print(result)
    return result

DATA = [1,1,1,1,1,1,1,1]
def readData():
    global DATA
    result = 0
    for i in range(7, -1, -1):
        result += result
        if(DATA[i]==1):
            result |= 1;
    print(result)
    return result

def dispWork(offset):
    print(mem[offset])


readAddr()
readData()

mem[0x66] = 0xc3
mem[0x67] = 0x00
mem[0x68] = 0x00
HALT = 0
RFSH = 0
clocks = 0
#while(clocks<=10):
#    if(HALT==0):
#        print("HALT")
#        dispWork(0x47)
#        mem[0x44] = 0x03
#        mem[0x45] = 0x0b
#        mem[0x46] = 0x09
#        clocks += 1
#        while(HALT==0):
#            clocks += 1
#        break
#
#    if(RFSH==0):
#        clocks += 1
#        break
#
#    rfsh = RFSH
#    mreq = MREQ
#    iorq = IORQ
#    busack = BUSACK
#    rd = RD
#    wr = WR
#    m1 = M1
#
#    addr = readAddr()
#    data = readData()
#
#    if(mreq==0):
#        if(rd==0):
#            #mem[addr]をD0-7に書き込み
#            #data = memRead(addr)
#            print(None)
#        elif(wr==0):
#            #mem[addr]にdataを書き込み
#            #memWrite(addr, data)
#            print(None)
#    clocks += 1
#
#
#
