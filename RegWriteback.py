from os import stat
from Convert import ConB
from Main import *

def printStruct(x):
        print('@@@\nstate:')
        print('\tpc :',state.pc)
        print('\tmemory:')
        for i in range(len(DEFMEMORY)):
            print('\t\tmem[ {} ] {}'.format(i,int(DEFMEMORY[i])))
        # print(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC)))
        print('\tregisters:')
        for i in range(len(DEFREGS)):
            print('\t\treg[ {} ] {}'.format(i,state.reg[i]))
        print('end state')
        # print(DEFMEMORY)

def SimulateEx():
    address = 0
    
    while(state.pc != state.numMemory):
        a = ConB(int(state.mem[state.pc]))
        a.findReg()
        print(printStruct(state.pc))
        test = compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))
        if(test == 'noop'):
            #print(printStruct(address))
            state.pc+=1
        elif(test == 'halt'):
            #print(printStruct(address))
            state.pc += 1
            break
        elif(test == 'notjump'):
            #print(printStruct(address))
            state.pc += 1
        else:
            #print(printStruct(address))
            state.pc +=  test +1
            #address = state.pc
        #print("#############################################################",state.pc)

        
SimulateEx()
#print(DEFREGS)





    # #=================================CHECK================================================#
    # print('Mem is ',format(i))
    # print(int(state.mem[i]))
    # print('opcode is {}'.format(a.opcode))
    # print('regA is {}'.format(a.regA))
    # print('regB is {}'.format(a.regB))
    # print('regC is {}'.format(a.regC))
    # print('return is ',format(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))))
    # print('_________________________________________________')
    # #=================================CHECK================================================#


# a = ConB(int(state.mem[0]))
# a.findReg()
# # print('opcode is {}'.format(a.opcode))
# # print('regA is {}'.format(a.regA))
# # print('regB is {}'.format(a.regB))
# # print('regC is {}'.format(a.regC))
# print(DEFMEMORY)
# print(DEFREGS)
# print(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC)))
# print('_________________________________________________')