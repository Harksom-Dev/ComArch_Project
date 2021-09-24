# testing read and write from file 
#testing struct

from os import stat
from typing import NamedTuple
from dataclasses import dataclass,field
opcodeList = [0,1,2,3,4,5,6,7]
DEFMEMORY = []
DEFREGS = [0] * 8
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
state = stateStruct(0,DEFMEMORY,DEFREGS)
#print(state)


#read in the entire machine-code file into memory#
#not implement exit condition yet
for line in f:
    #print(line)
    state.mem.append(line)
    print("memory[",state.numMemory,"] =",state.mem[state.numMemory])
    state.numMemory += 1
    
print(state)


# add regA and regB and put vaule to rD
def add(rs,rt,rD):
    ans = rs + rt
    state.reg[rD] = ans
    return -1


####### not sure #############
def AND(a,b):
    return a & b

def NOT(a):
    return ~a

def nand(rs,rt,rD):
    ans = NOT(AND(rs,rt))
    state.reg[rD] = ans
    return -1
###### notsure ################



def lw(regA,regB,rD): # get vaule from mem
    sum = regA + rD #get vaule of regA + offes(rD) to locate mem 
    ans = state.mem[sum] # locate vaule of mem to variable
    state.reg[regB] = ans # store the target reg with mem
    return -1



def sw(regA,regB,rD):
    #rd might not be a correct dest(stack might increase)
    
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
#compute  it's may return only where to jump the rest will do in sub function
# return -1 mean not jump
def compute(opcode,regA,regB,rD):
    if(opcode == 0):    #ADD
        rs = state.reg[regA]
        rt = state.reg[regB]
        newReg = add(rs,rt,rD)
        return newReg 
    elif(opcode == 1):  #NAND
        rs = state.reg[regA]
        rt = state.reg[regB]
        newReg = nand(rs,rt,rD)
        return newReg
    elif(opcode == 2):  #LW
        rA = state.reg[regA]
        newReg = lw(rA,regB,rD)
        return newReg
    elif(opcode == 3):  #SW
        regB = sw(regA,regB,rD)
    elif(opcode == 4):  #BEQ
        rD = beq(regA,regB,rD)
    elif(opcode == 5):  #JALR
        regB = jalr(regA,regB)
    elif(opcode == 6):  #HALT
        rD = halt(regA,regB,rD)
    else:   #NOOP
        print("test")

opt = 0
Ra = 0
Rb = 1
Rd = 7
print("opt=",opt,"regA=",Ra,"regB=",Rb,"rD=",Rd)
compute(opt,Ra,Rb,Rd)
#print(state.reg[Rb])
i = 0
for i in range(0,7):
    print(state.reg[i])

#############################################################################################################################
# for i in range(state.pc,state.numMemory):
#     print(i)
#     print(state.mem)
#     print(state.reg)





#when we write c

f.close()