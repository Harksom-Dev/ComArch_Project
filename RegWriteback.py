from Convert import ConB
from Main import *

for i in range(len(state.mem)):
    a = ConB(int(state.mem[i]))
    a.findReg()
    print('pc is ',format(i))
    print(state.mem[i])
    print('opcode is {}'.format(a.opcode))
    print('regA is {}'.format(a.regA))
    print('regB is {}'.format(a.regB))
    print('regC is {}'.format(a.regC))
    print(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC)))
    print('_________________________________________________')

    
    # if(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))== 'noop'):
    #     i+= 1
    # elif(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC))== 'halt'):
    #     break
    # else:
        
        


# a = ConB(int(state.mem[6]))
# a.findReg()
# print('opcode is {}'.format(a.opcode))
# print('regA is {}'.format(a.regA))
# print('regB is {}'.format(a.regB))
# print('regC is {}'.format(a.regC))
# print(compute(int(a.opcode),int(a.regA),int(a.regB),int(a.regC)))