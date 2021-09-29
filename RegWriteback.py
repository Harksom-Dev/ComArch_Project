from os import stat
from Convert import ConB
from Main import *

def printStruct(x): #use for print in each step
        print('@@@\nstate:')
        print('\tpc :',state.pc)
        print('\tmemory:')
        for i in range(len(DEFMEMORY)):     #print each memory in that step
            print('\t\tmem[ {} ] {}'.format(i,int(DEFMEMORY[i])))
        print('\tregisters:')
        for i in range(len(DEFREGS)):   #print each registers in that step
            print('\t\treg[ {} ] {}'.format(i,state.reg[i]))
        print('end state')
        return ''

def Simulate():
    instructionCount = 0  #for count Instruction 
    #state.pc = -1   #state.mem(0) for Initial registers
    while(state.pc != state.numMemory):
        a = ConB(int(state.mem[state.pc]))
        a.findReg()
        print(printStruct(state.pc))
        test = compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))
        instructionCount+=1
        if(test == 'noop'): #if compute return noop
            #print(printStruct(state.pc))    
            state.pc+=1
            #instructionCount+=1
        elif(test == 'halt'):   #if compute return halt
            print('machine halted \n total of {} instructions executed\n final state of machine:'.format(instructionCount))
            #print(printStruct(state.pc))
            state.pc += 1
            #instructionCount+=1
            break
        elif(test == 'notjump'):    #if compute return notjump
            #print(printStruct(state.pc))
            state.pc += 1
            #instructionCount+=1
        else:   #if compute return Jump Address
            state.pc +=  test +1
            #print(printStruct(state.pc))
            #instructionCount+=1
        

    #print after instruction done
    print(printStruct(state.pc))
 
Simulate()
