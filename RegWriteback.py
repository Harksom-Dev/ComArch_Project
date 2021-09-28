from Convert import ConB
from Main import *

def printStruct(x):
        a = ConB(int(state.mem[x]))
        a.findReg()
        print('@@@\nstate:')
        print('\tpc {}:'.format(x))
        print('\tmemory:')
        for i in range(len(DEFMEMORY)):
            print('\t\tmem[ {} ] {}'.format(i,int(DEFMEMORY[i])))
        # print(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC)))
        print('\tregisters:')
        for i in range(len(DEFREGS)):
            print('\t\treg[ {} ] {}'.format(i,int(DEFREGS[i])))
        print('end state')

def SimulateEx():
    address = 0
    for i in range(len(state.mem)):
        a = ConB(int(state.mem[address]))
        a.findReg()
        if(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))== 'noop'):
            print(printStruct(address))
            address+=1
        elif(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))== 'halt'):
            print(printStruct(address))
            break
        elif(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))== 'notjump'):
            print(printStruct(address))
            address+=1
        else:
            print(printStruct(address))
            JAddress =  compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))
            address = JAddress + address

        
SimulateEx()






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