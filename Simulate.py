from Convert import ConB
from Main import *

def printStruct():
    a = ConB(int(state.mem[1]))
    a.findReg()
    print(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC)))
    return 

print(printStruct())