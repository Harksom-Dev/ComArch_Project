# testing read and write from file 
#testing struct

from typing import NamedTuple
from dataclasses import dataclass,field

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
    



f.close()