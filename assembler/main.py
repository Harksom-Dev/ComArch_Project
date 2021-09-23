from instructions import inst as Instruction

# 
def symbolCheck():
    print()

def stringReader():

    f = open("demofile.txt", "r")
    f = f.read()
    arr = f.splitlines()        #split each line 1 on 1 into list

    arr = [i.split() for i in arr]      #split each element in arr to sub list in from [['asdasd', 'add', '1', '2', '3'], ...]
    print(arr)

    instList = []
    
    for item in arr:
        if (item[0] in Instruction["name"]):    #ckeck 
            labels, instcode, regA, regB, destReg = None, item[0], item[1], item[2], item[3]
        else:
            labels, instcode, regA, regB, destReg = item[0], item[1], item[2], item[3], item[4]
        
        symbolCheck() #TODO: make this function that return values of symbolic variables like five should return 5 (int)

        sheet = [labels, instcode, regA, regB, destReg]
        instList.append(sheet)

    print(instList)
    return instList


stringReader()
