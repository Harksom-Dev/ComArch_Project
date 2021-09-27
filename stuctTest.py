# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


from dataclasses import dataclass,field
from typing import List
reg = [0] * 8
mem = []
class asd:
    rrr = [0] * 8

@dataclass
class stateStruct:
    pc: int = field(default=0)
    mem: list[int] = field(default_factory=list)
    reg: list[int] = field(default_factory=list)
    numMemory: int = field(default=0)



p = stateStruct(0,mem,reg)

print(p)  # Point(x=1.5, y=2.5, z=0.0)

def AND(A, B):
    return A & B;   

# Function to simulate NOT Gate
def NOT(A):
    return ~A+2

# Function to simulate NAND Gate
def NAND(A, B):
    return NOT(AND(A, B))

print(AND(1,0))
print(NOT(101))
