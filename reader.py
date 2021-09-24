# testing read and write from file 
#testing struct

from typing import NamedTuple
from dataclasses import dataclass,field
opcodeList = [0,1,2,3,4,5,6,7]
#create dataclass(similar to struct in c) for store all of machine code
@dataclass
class stateStruct:
    pc: int = field(default=0)
    mem: list[int] = field(default_factory=list)
    reg: list[int] = field(default_factory=list)
    numMemory: int = field(default=0)


#struct testing
f = open("test.txt","r")
#initialize struct
state = stateStruct()
#print(state)


#read in the entire machine-code file into memory#
#not implement exit condition yet
for line in f:
    #print(line)
    state.mem.append(line)
    state.numMemory += 1
    print("memory[",state.numMemory,"] =",state.mem[state.numMemory-1])
    
# add regA and regB and put vaule to rD
def add(regA,regB,rD):
    ans = regA + regB
    ansDict = {
        rD : ans
    }
    return ansDict #return rD(destination of reg) and ans(sum of a and b)

def AND(a,b):
    return a & b

def NOT(a):
    return ~a+2

print (NOT(2))
def nand(regA,regB,rD):
    return 0
def lw(regA,regB,rD):
    return 0
def sw(regA,regB,rD):
    return 0
def beq(regA,regB,rD):
    return 0
def jalr(regA,regB):
    return 0
def halt():
    return 0
def noop():
    return 0
#maybe starting translate to 2 bit
#compute  it's may return only regs location and vaule ?
def Alu(opcode,regA,regB,rD):
    newReg = {}
    if(opcode == 0):
        newReg = add(regA,regB,rD)
        return newReg
    elif(opcode == 1):
        rD = nand(regA,regB,rD)
    elif(opcode == 2):
        regB = lw(regA,regB,rD)
    elif(opcode == 3):
        regB = sw(regA,regB,rD)
    elif(opcode == 4):
        rD = beq(regA,regB,rD)
    elif(opcode == 5):
        regB = jalr(regA,regB)
    elif(opcode == 6):
        rD = halt(regA,regB,rD)
    else:
        print("test")



print(Alu(0,1,2,5))







#when we write c

f.close()