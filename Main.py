from Convert import ConB 
from dataclasses import dataclass,field
DEFMEMORY = []
DEFREGS = [0] * 8
TARGETFILE = "test.txt"

#create dataclass(similar to struct in c) for store all of machine code
@dataclass
class stateStruct:
    pc: int = field(default=0)
    mem: list[int] = field(default_factory=list)
    reg: list[int] = field(default_factory=list)
    numMemory: int = field(default=0)


#start reading a target file
f = open(TARGETFILE,"r")
#initialize state
state = stateStruct(0,DEFMEMORY,DEFREGS)



#read in the entire machine-code file into memory#
#not implement exit condition yet
for line in f:
    #print(line)
    state.mem.append(line)
    # print("memory[",state.numMemory,"] =",state.mem[state.numMemory])
    state.numMemory += 1


# add regA and regB and put vaule to rD
def add(rs,rt,rD):
    ans = int(rs) + int(rt)
    state.reg[rD] = int(ans)
    #print("rs =",rs,"rt =",rt,"rD =",rD)
    #print(ans)
    return 'notjump'


# need to get approved
def nand(rs,rt,rD):
    # nand on bit only cant do on 10-base 
    rs = format(rs,'03b')   #convert back from base 10 to base 2
    rt = format(rt,'03b')   #convert back from base 10 to base 2
    # print("rs= ",rs)   
    # print("rt=",rt)
    # rsl = []
    # rtl = []
    a = 0
    ans = ""
    for i in range(0,3): # loop throught the end of vaule in rs and rt and do a NAND operation
        # rsl.append(rs[i])
        # rtl.append(rt[i])
        if(rs[i] == '1' and  rt[i] == '1'):
            ans += '0'
        else:
            ans += '1'
            a += 2**(2-i) # compute and answer to be base 10 vaule
    
    # print("string =",ans)
    # print(a)
    # ans = int(ans)
    # print("int =",ans)
    # ans --> base 10 converter then return

    state.reg[rD] = a
    return 'notjump'



def lw(rs,regB,rD): # get vaule from mem
    sum = int(rs + rD) #get vaule of regA + offes(rD) to locate mem 
    ans = int(state.mem[sum]) # locate vaule of mem to variable
    state.reg[regB] = ans # store the target reg with mem
    #need to do something if we lw from stack
    return 'notjump'



def sw(rs,rt,rD):
    #rd might not be a correct dest(stack might increase)
    #not check continue of list conditon yet
    pos = rs + rD   # get position (regB + offsetField)
    curpos = len(state.mem) -1  #check last of memmory location
    if(pos <= curpos): #check condition for prevent ouf of bound for memlist
        state.mem[pos] = rt
    elif((pos - curpos) == 1): #add vaule in the new mem location
        state.mem.append(rt)    
    else:
        print("Error")  #incase it store in the mem that we dont have stack pointer?
    #are we need to delete a vaule in stack ?
    return 'notjump'

def beq(rs,rt,rD):
    if(rs == rt): # check the conditon of beq
        return  int(rD)   # return 1+ offsetfield to change pc now we not +1 on rD becuz pc in for gonna + 1 for it's self when finish loop
    else:
        return 'notjump' #return -1 for inform that we not change pc

def jalr(rs,rd):
    state.reg[rd] = state.pc # store pc + 1 in regB dont need to +1 because we always +1 at the end of for
    return int(state.reg[rs]) # return jump address which is regA
def halt():
    return 'halt'
def noop():
    return 'noop'



#maybe starting translate to 2 bit
#compute  it's may return only where to jump the rest will do in sub function
# return -1 mean not jump
# return -2 for halt ?
# return -3 for noop ?
def compute(opcode,regA,regB,rD):
    if(opcode == 0):    #ADD
        rs = state.reg[regA] #accest regA in rs loc
        rt = state.reg[regB] #accest regB in rt loc
        return add(rs,rt,rD)
    elif(opcode == 1):  #NAND
        rs = state.reg[regA] #accest regA in rs loc
        rt = state.reg[regB] #accest regB in rt loc
        return nand(rs,rt,rD)
    elif(opcode == 2):  #LW
        rs = state.reg[regA] #accest regA in rs loc
        return lw(rs,regB,rD)
    elif(opcode == 3):  #SW
        rs = state.reg[regA] #accest regA in rs loc
        rt = state.reg[regB] #accest regB in rt loc
        return sw(rs,rt,rD) 
    elif(opcode == 4):  #BEQ
        rs = state.reg[regA] #accest regA in rs loc
        rt = state.reg[regB] #accest regB in rt loc
        return beq(rs,rt,rD)
    elif(opcode == 5):  #JALR
        rs = state.reg[regA] #accest regA in rs loc
        rd = state.reg[regB] #accest regB in rt loc
        return jalr(rs,rd)
    elif(opcode == 6):  #HALT
        return halt()
    else:   #NOOP
        return noop()

# opt = 1
# Ra = 4
# Rb = 3
# Rd = 3
# print("opt=",opt,"regA=",Ra,"regB=",Rb,"rD=",Rd)
# compute(opt,Ra,Rb,Rd)
#compute(3,0,1,10)
#print(state.reg[Rb])
# i = 0
# for i in range(0,7):
#     print(state.reg[i])

# for i in range(0,len(state.mem)):
#     print(state.mem[i])
# ############################################################################################################################
# for i in range(state.pc,state.numMemory):
#     print(i)
#     print(state.mem)
#     print(state.reg)


# a = ConB(int(state.mem[4]))
# a.findReg()
# print((a.opcode))
# print(a.regA)
# print(a.regB)
# print(a.offsetField)
#when we write c

f.close()