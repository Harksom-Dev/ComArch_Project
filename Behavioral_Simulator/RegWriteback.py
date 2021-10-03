from os import stat
from Convert import ConB
from Main import *

textList = []
def printer(des = "Behavioral_Simulator/ExSimulator.txt", inputList = textList):  #TODO: write machine language to text file
            file = open(des, "a")                            #TODO: "r" - Read - Default value. Opens a file for reading, error if the file does not exist
            for i in inputList:                              #TODO: "a" - Append - Opens a file for appending, creates the file if it does not exist
                file.write(str(i)+"\n")                      #TODO: "x" - Create - Creates the specified file, returns an error if the file exists
            file.close()                                     #TODO: "w" - Write - Opens a file for writing, creates the file if it does not exist

def printStruct(x): #use for print in each step
    textList.append('@@@\nstate:')
    textList.append('\tpc ' + str(state.pc))
    textList.append('\tmemory:')
    for i in range(len(DEFMEMORY)):     #print each memory in that step
        textList.append('\t\t\tmem[ {} ] {}'.format(i,int(DEFMEMORY[i])))
    textList.append('\tregisters:')
    for i in range(len(DEFREGS)):   #print each registers in that step
        textList.append('\t\t\treg[ {} ] {}'.format(i,state.reg[i]))
    textList.append('end state\n')
    return ''

def Simulate():
    SimulateEX = []
    instructionCount = 0  #for count Instruction 
    while(state.pc != state.numMemory):
        DATA = ConB(int(state.mem[state.pc]))     
        DATA.findReg()
        printStruct(state.pc)
        test = compute(int(DATA.opcode),int(DATA.regA),int(DATA.regB),int(DATA.regC))
        if(test == 'noop'): #if compute return noop
            state.pc+=1
            instructionCount+=1
        elif(test == 'halt'):   #if compute return halt
            textList.append('machine halted \n total of {} instructions executed\n final state of machine:\n'.format(instructionCount))
            state.pc += 1
            instructionCount+=1
            break
        elif(test == 'notjump'):    #if compute return notjump
            state.pc += 1
            instructionCount+=1
        elif(test == 'jalr'):
            state.pc += 0
        else:   #if compute return Jump Address
            state.pc +=  test +1
            instructionCount+=1
    textList.append(printStruct(state.pc))      #for final state
    return SimulateEX
 
Simulate()
printer("Behavioral_Simulator/ExSimulator.txt",textList)         #Write file from textList(Simulater list) to ExSimulator.txt file