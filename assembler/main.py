from instructions import inst as Instruction


class AssemblyTranslator:
    #*dummy functions 
    def __symbolCheck(self):                #!: check destReg if it haveing symbolic variables
        return

    def __symbolDecoder(self):              #!: make this function that return values of symbolic variables like 'five'(string) should return 5(int)
        return
        

    def __regDecoder(self):                 #TODO: decode reg from dec to bin like from '5' to '101'     
        if( self > -8 and self < 8 ): 
            return bin(self).replace("0b", "")    #? https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
        else: 
            return print("Invalid")    
    

    def __fillFinding(self):                #TODO: this function should be call first and find .fill in assembly file and return line where .fill is                        
        return                              #TODO: and then collect all .fill variables and make list of pair [symbolic,values]

    def __simplify(self,listTransformed):   #TODO: this function should delete all comments and formating

        resList = []

        for item in listTransformed:
            if (item[0] in Instruction["name"]):    #ckeck instions of this line have the same name as the instruction in the instruction list
                labels, instcode, regA, regB, destReg = None, item[0], item[1], item[2], item[3]        #if have the same name as the instruction in the instruction list
            else:
                labels, instcode, regA, regB, destReg = item[0], item[1], item[2], item[3], item[4]     #otherwise 

            sheet = [labels, instcode, regA, regB, destReg]     #contains data in instruction list format
            resList.append(sheet)
        return resList

    #*used functions
    def stringReader(self,filelocation = "assembler\demofile.txt"):

        f = open(filelocation, "r")
        f = f.read()
        splited = f.splitlines()                        #split each line 1 on 1 into list

        splited = [i.split() for i in splited]          #split each element in arr to sub list in from [['asdasd', 'add', '1', '2', '3'], ...]
        print(splited)                                  #!for debugging purposes

        instList = self.__simplify(splited)               #contains all assembly code in instruction list format like [labels, instcode, regA, regB, destReg]

        print(instList)                                 #!for debugging purposes
        return instList


if __name__ == "__main__":
    asbt = AssemblyTranslator()
    asbt.stringReader()

    #then read instList and decode them as binary string
