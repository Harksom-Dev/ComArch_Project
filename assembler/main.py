from instructions import inst as Instruction


class AssemblyTranslator:

    __machineLang = []                      #all instructions in assembly that translated to machine language   
    __fillValue = []                        #collect all .fill variables and make list of pair [symbolic,values]
    __assembly = []                         #save all instructions in assembly line by line
    __inst = Instruction

    #*dummy functions 

    def __printer(self):                    #TODO: write machine language to text file
        open("textToSimulator.txt", "w")

    def __twos_com(self, num):
        d = int(num, 2)

        flipped = (d ^ 65536) + 1 
        tcom = str(bin(flipped)).replace('0b', '')
        signBit = tcom[0]
        signed = "1"
        osigned = "0"
        while(len(tcom) < 32):  # hard-code extended
            if(signBit == "1"):
                tcom = signed + tcom
            else:
                tcom = osigned + tcom
        num = tcom
        #flipped = bin(~d)
        #print("Sign_BIT is " + signBit)


    
    #*used functions

    def __fillFinding(self):                #TODO: this function should be call first and find .fill in assembly file and return line where .fill is                        
        for i in self.__assembly:           #TODO: and then collect all .fill variables and make list of pair [symbolic,values]
            if(i[1]==".fill"):
                sheet =[i[0],i[2]]              
                self.__fillValue.append(sheet)


    def __binToDec(self,binary):            #TODO: convert intput num in binary to decimal number
        if(type(binary) is str):
            return int(binary,2)                
        else:
            return print('Type of binary not string')


    def translator(self,item):              #TODO: make this function that

        textTranslated = ""

        labels, instcode, regA, regB, destReg = item[0], item[1], item[2], item[3], item[4] 

        indexOfInst = self.__inst["name"].index(instcode)
        type = self.__inst["type"][indexOfInst]
        optc_bin = self.__inst["optc_bin"][indexOfInst]

        if type == "R" :
            textTranslated += "0000000"
            textTranslated += optc_bin
            textTranslated += self.__regDecoder(regA)
            textTranslated += self.__regDecoder(regB)
            textTranslated += "0000000000000"
            textTranslated += self.__regDecoder(destReg)

        elif type == "I" :
            textTranslated += "0000000"
            textTranslated += optc_bin
            textTranslated += self.__regDecoder(regA)
            textTranslated += self.__regDecoder(regB)

            destReg_symbolic = ""
            isSymbolic = False
            for i in range(len(self.__fillValue)):
                if(self.__fillValue[i][0] == destReg):
                    destReg_symbolic = self.__fillValue[i][1]
                    isSymbolic = True
                    break;
                isSymbolic = False

            textTranslated += self.__twos_com(int(destReg_symbolic)) if isSymbolic else self.__twos_com(destReg)

        elif type == "J" :
            textTranslated += "0000000"
            textTranslated += optc_bin
            textTranslated += self.__regDecoder(regA)
            textTranslated += self.__regDecoder(regB)
            textTranslated += "0000000000000"
            textTranslated += self.__regDecoder(destReg)

        elif type == "O" :
            textTranslated += "0000000"
            textTranslated += optc_bin
            textTranslated += self.__regDecoder(regA)
            textTranslated += self.__regDecoder(regB)
            textTranslated += "0000000000000"
            textTranslated += self.__regDecoder(destReg)


        print(textTranslated)        #!for debugging purposes
        

    def __regDecoder(self,number):                  #TODO: decode reg from dec to bin like from '5' to '101'
        number = int(number)     
        if( number >= 0 and number < 8 ): 
            if(number==0):
                return "000"
            elif(number==1):
                return "00"+bin(number).replace("0b", "")
            elif(number<4):
                return"0"+bin(number).replace("0b", "")
            elif(number>3):
                return bin(number).replace("0b", "")        #? https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
        # elif number < 0 and number > -7:
        #    return bin(number if number>0 else number+(1<<3)).replace("0b", "")
        else: 
            return print("Invalid")   


    def __simplify(self,listTransformed):           #TODO: this function should delete all comments and formating

        resList = []

        for item in listTransformed:
            if (item[0] in Instruction["name"]):    #ckeck instions of this line have the same name as the instruction in the instruction list
                if (item[0]  == "halt"):            #and spacial case for "halt" it can be in both item[0] and item[1] 
                    labels, instcode, regA, regB, destReg = None, item[0], None, None, None
                elif item[1] == "halt":
                    labels, instcode, regA, regB, destReg = item[0], item[1], None, None, None
                else:
                    labels, instcode, regA, regB, destReg = None, item[0], item[1], item[2], item[3]        #if have the same name as the instruction in the instruction list
            elif (item[1] == ".fill") :
                labels, instcode, regA, regB, destReg = item[0], item[1], item[2], None, None

            else:
                labels, instcode, regA, regB, destReg = item[0], item[1], item[2], item[3], item[4]     #otherwise 

            sheet = [labels, instcode, regA, regB, destReg]     #contains data in instruction list format
            resList.append(sheet)
        return resList


    def stringReader(self,filelocation = "assembler\demofile copy.txt"):

        f = open(filelocation, "r")
        f = f.read()
        splited = f.splitlines()                        #split each line 1 on 1 into list

        splited = [i.split() for i in splited]          #split each element in arr to sub list in from [['asdasd', 'add', '1', '2', '3'], ...]
        print(splited)                                  #!for debugging purposes

        instList = self.__simplify(splited)             #contains all assembly code in instruction list format like [labels, instcode, regA, regB, destReg]
        self.__assembly= instList
        print(*instList,sep='\n')                       #!for debugging purposes
        
        self.__fillFinding()                            #!for debugging purposes
        print(self.__fillValue)                         #!for debugging purposes
        self.translator([None, 'lw', '0', '2', 'neg1'])   #!for debugging purposes




if __name__ == "__main__":

    asbt = AssemblyTranslator()

    asbt.stringReader()

    #then read instList and decode them as binary string