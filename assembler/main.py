from instructions import inst as Instruction


class AssemblyTranslator:

    __machineLang = []                      #all instructions in assembly that translated to machine language   
    __fillValue = []                        #collect all .fill variables and make list of pair [symbolic,values]
    __assembly = [] 
    __inst = Instruction

    #*dummy functions 

    def __printer(self):                    #TODO:
        open("textToSimulator", "w")
        return

    def __fillFinding(self):                #TODO: this function should be call first and find .fill in assembly file and return line where .fill is                        
        return                              #TODO: and then collect all .fill variables and make list of pair [symbolic,values]

    def __binToDec(self,binary):            #TODO: convert intput num in binary to decimal number
        if(type(binary) is str):
            return int(binary,2)                #TODO: intput string binary
        else:
            return print('Type of binary not string')




    
    #*used functions
    def __isSymbolic(self,dest):            #TODO: make this function that
        if dest in self.__fillValue:
            return True
        else:
            return False

    def translator(self,item):              #TODO: make this function that

        textTranslated = ""

        labels, instcode, regA, regB, destReg = item[0], item[1], item[2], item[3], item[4] 

        indexOfInst = self.__inst["name"].index(instcode)
        type = self.__inst["type"][indexOfInst]
        optc_bin = self.__inst["optc_bin"][indexOfInst]

        if type == "R" :
            textTranslated += optc_bin 
            textTranslated += self.__regDecoder(regA) + self.__regDecoder(regB)
            textTranslated += "0000000000000"
            textTranslated += self.__isSymbolic(destReg) and self.__fillValue[self.__fillValue.index(destReg)][0] or self.__regDecoder(destReg)


        print(textTranslated)        #!for debugging purposes
        
        return

    def __regDecoder(self,number):                  #TODO: decode reg from dec to bin like from '5' to '101'
        number = int(number)     
        if( number > -8 and number < 8 ): 
            return bin(number).replace("0b", "")    #? https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
        else: 
            return print("Invalid")   


    def __simplify(self,listTransformed):           #TODO: this function should delete all comments and formating

        resList = []

        for item in listTransformed:
            if (item[0] in Instruction["name"]):    #ckeck instions of this line have the same name as the instruction in the instruction list
                if (item[0]  == "halt"):
                    labels, instcode, regA, regB, destReg = "done", item[0], None, None, None
                elif item[1] == "halt":
                    labels, instcode, regA, regB, destReg = "done", item[1], None, None, None
                else:
                    labels, instcode, regA, regB, destReg = None, item[0], item[1], item[2], item[3]        #if have the same name as the instruction in the instruction list
            elif (item[1] == ".fill") :
                labels, instcode, regA, regB, destReg = item[0], item[1], item[2], None, None

            else:
                labels, instcode, regA, regB, destReg = item[0], item[1], item[2], item[3], item[4]     #otherwise 

            sheet = [labels, instcode, regA, regB, destReg]     #contains data in instruction list format
            resList.append(sheet)
        return resList


    def stringReader(self,filelocation = "assembler\demofile.txt"):

        f = open(filelocation, "r")
        f = f.read()
        splited = f.splitlines()                        #split each line 1 on 1 into list

        splited = [i.split() for i in splited]          #split each element in arr to sub list in from [['asdasd', 'add', '1', '2', '3'], ...]
        print(splited)                                  #!for debugging purposes

        instList = self.__simplify(splited)               #contains all assembly code in instruction list format like [labels, instcode, regA, regB, destReg]
        self.__assembly.append(instList)
        print(*instList,sep='\n')                                 #!for debugging purposes
        return instList


if __name__ == "__main__":
    asbt = AssemblyTranslator()
    asbt.stringReader()
    # asbt.translator(['wqe', 'nand', '1', '1', '1'])
    #then read instList and decode them as binary string
