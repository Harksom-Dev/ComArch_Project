from Convert import * 
from reader import *

def splitdata(x):
    a = []
    f = open(x, "r")
    a = f.read()
    arr = a.split("\n")
    return arr

print(splitdata("test.txt"))

def simulateEX(x):
    print('@@@\nstate:\n\t\tpc 0\n\t\tmemory:')
    arr = splitdata(x)
    numReg = 8
    for i in range(len(arr)):
        print('\t\t\t\tmemory[{0}]={1}'.format(i,arr[i]))
    print('\t\tregiters:')
    for i in range(numReg):
        print('\t\t\t\treg[{0}]{1}'.format(i,' '))
    print('end state')
    

# simulateEX("test.txt")
a = ConB(int(state.mem[0]))
print(a.decnum)
a.findReg()
print(a.bi)
print((a.opcode))
print(a.regA)
print(a.regB)
 
