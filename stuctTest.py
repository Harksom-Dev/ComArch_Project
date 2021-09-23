# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from dataclasses import dataclass,field
from typing import List
a = [0,0,0,0,0,0,0]
@dataclass
class stateStruct:
    pc: int = field(default=0)
    mem: list[int] = field(default_factory=list)
    reg: list[int] = field(default_factory=list)
    numMemory: int = field(default=0)


p = stateStruct()

print(p)  # Point(x=1.5, y=2.5, z=0.0)