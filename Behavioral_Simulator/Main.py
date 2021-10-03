from Convert import ConB 
from dataclasses import dataclass,field
DEFMEMORY = []
DEFREGS = [0] * 8
TARGETFILE = "Behavioral_Simulator/test.txt"

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
    state.numMemory += 1


# add regA and regB and put vaule to rD
def add(rs,rt,rD):
    ans = int(rs) + int(rt)
    state.reg[rD] = int(ans)
    return 'notjump'


# need to get approved
def nand(rs,rt,rD):
    # nand on bit only cant do on 10-base 
    if(rs > rt):
        rs = format(rs,'0b')   #convert back from base 10 to base 2
        length = len(rs)
        rt = format(rt,'0'+ str(length)+'b')   #convert back from base 10 to base 2
        
    else: 
        rt = format(rt,'0b')   #convert back from base 10 to base 2
        length = len(rt)
        rs = format(rs,'0'+ str(length)+'b')   #convert back from base 10 to base 2
    #need to fix length to the same rs and rt

    a = 0
    ans = ""
    for i in range(length): # loop throught the end of vaule in rs and rt and do a NAND operation
        # rsl.append(rs[i])
        # rtl.append(rt[i])
        if(rs[i] == '1' and  rt[i] == '1'):
            ans += '0'
        else:
            ans += '1'
            a += 2**(length-1-i) # compute and answer to be base 10 vaule
    

    state.reg[rD] = a
    return 'notjump'




def lw(rs,regB,rD): # get vaule from mem
    sum = int(rs + rD) #get vaule of regA + offes(rD) to locate mem 
    ans = int(state.mem[sum]) # locate vaule of mem to variable
    state.reg[regB] = ans # store the target reg with mem

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
    return 'notjump'

def beq(rs,rt,rD):
    if(rs == rt): # check the conditon of beq
        return  int(rD)    # return 1+ offsetfield to change pc now we not +1 on rD becuz pc in for gonna + 1 for it's self when finish loop
    else:
        return 'notjump' #return -1 for inform that we not change pc

def jalr(rs,rd):
    state.reg[rd] = state.pc+1 # store pc + 1 in regB dont need to +1 because we always +1 at the end of for
    state.pc = rs
    return 'jalr' # return jump address which is regA
def halt():
    return 'halt'
def noop():
    return 'noop'



#compute func return int only jump loc
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
        # rd = state.reg[regB] #accest regB in rt loc
        return jalr(rs,regB)
    elif(opcode == 6):  #HALT
        return halt()
    else:   #NOOP
        return noop()

f.close()