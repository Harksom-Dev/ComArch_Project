from os import stat
from Convert import ConB
from Main import *

def printStruct(x):
        print('@@@\nstate:')
        print('\tpc :',state.pc+1)
        print('\tmemory:')
        for i in range(len(DEFMEMORY)):
            print('\t\tmem[ {} ] {}'.format(i,int(DEFMEMORY[i])))
        print('\tregisters:')
        for i in range(len(DEFREGS)):
            print('\t\treg[ {} ] {}'.format(i,state.reg[i]))
        print('end state')
        return ''

def Simulate():
    Programcount=0
    state.pc = -1
    while(state.pc != state.numMemory):
        a = ConB(int(state.mem[state.pc]))
        a.findReg()
        test = compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))
        if(test == 'noop'):
            print(printStruct(state.pc))
            state.pc+=1
            Programcount+=1
        elif(test == 'halt'):
            print('machine halted \n total of {} instructions executed\n final state of machine:'.format(Programcount))
            print(printStruct(state.pc))
            state.pc += 1
            Programcount+=1
            break
        elif(test == 'notjump'):
            print(printStruct(state.pc))
            state.pc += 1
            Programcount+=1
        else:
            state.pc +=  test +1
            print(printStruct(state.pc))
            Programcount+=1
            #address = state.pc
        #print("#############################################################",state.pc)
        

        
Simulate()
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