from instructions import inst as Instruction


class AssemblyTranslator:

    __machineLang = []                      #all instructions in assembly that translated to machine language   
    __fillValue = []                        #collect all .fill variables and make list of pair [symbolic,values]
    __assembly = []                         #save all instructions in assembly line by line
    __inst = Instruction

    #*dummy functions 

    def __printer(self):                                #TODO: write machine language to text file
            file = open("textToSimulator.txt", "a")     #TODO: "r" - Read - Default value. Opens a file for reading, error if the file does not exist
            for i in self.__machineLang:                #TODO: "a" - Append - Opens a file for appending, creates the file if it does not exist
                file.write(str(i)+"\n")                 #TODO: "x" - Create - Creates the specified file, returns an error if the file exists
            file.close()                                #TODO: "w" - Write - Opens a file for writing, creates the file if it does not exist

    def twosCom_decBin(self, dec, bit):
        if dec >= 0 :
            bin1 = bin(dec).split("0b")[1]
            while len(bin1) < bit:
                bin1 = '0'+bin1
            return bin1
        else:
            bin1 = -1*dec
            return bin(bin1 - pow(2,bit) ).split("0b")[1]


    
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
            textTranslated += self.__regDecoder3bit(regA)
            textTranslated += self.__regDecoder3bit(regB)
            textTranslated += "0000000000000"
            textTranslated += self.__regDecoder3bit(destReg)

        elif type == "I" :
            textTranslated += "0000000"
            textTranslated += optc_bin
            textTranslated += self.__regDecoder3bit(regA)
            textTranslated += self.__regDecoder3bit(regB)

            sybolicAddress = ""
            isSymbolic = False 
            for i in range(len(self.__assembly)):
                if(self.__assembly[i][0] == destReg):
                    sybolicAddress = str(i)
                    isSymbolic = True
                    break;
                isSymbolic = False


            if isSymbolic :
                textTranslated += self.twosCom_decBin(int(sybolicAddress),16)
            else :
                if (int(destReg) < 0) :
                    textTranslated += self.twosCom_decBin(int(destReg))   
                else :
                    textTranslated += '{0:016b}'.format(int(destReg))


        elif type == "J" :
            textTranslated += "0000000"
            textTranslated += optc_bin
            textTranslated += self.__regDecoder3bit(regA)
            textTranslated += self.__regDecoder3bit(regB)
            textTranslated += "0000000000000"
            textTranslated += self.__regDecoder3bit(destReg)
            textTranslated += "0000000000000000"                   #? Bit 15 - 0 should be zero "0"*16 


        elif type == "O" :
            textTranslated += "0000000"
            textTranslated += optc_bin
            textTranslated += self.__regDecoder3bit(regA)
            textTranslated += self.__regDecoder3bit(regB)
            textTranslated += "0000000000000"
            textTranslated += self.__regDecoder3bit(destReg)
            textTranslated += optc_bin                          #? Bit 24 - 22 opcode
            textTranslated += "0000000000000000000000"          #? Bit 21 - 0 should be zero "0"*22


        print(textTranslated)                                             #!for debugging purposes
        print(self.__binToDec(textTranslated))                            #!for debugging purposes
        self.__machineLang.append(self.__binToDec(textTranslated))        #!for debugging purposes
        

    def __regDecoder3bit(self, number):                  #TODO: decode reg from dec to bin like from '5' to '101'
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
        # print(splited)                                  #!for debugging purposes

        instList = self.__simplify(splited)             #contains all assembly code in instruction list format like [labels, instcode, regA, regB, destReg]
        self.__assembly= instList
        print(*instList,sep='\n')                       #!for debugging purposes
        
        self.__fillFinding()                            #!for debugging purposes
        print(self.__fillValue)                         #!for debugging purposes

        # self.translator([None, 'sw', '7', '1', 'stack'])
        for element in instList:
            print(element)
            self.translator(element)                    #!for debugging purposes
        print(*self.__machineLang,sep='\n')             #!for debugging purposes




if __name__ == "__main__":

    asbt = AssemblyTranslator()

    asbt.stringReader()

    #then read instList and decode them as binary string