from twoscom import twosComplement as tc


class ConB():
    def __init__(self, decnum):
        self.decnum = decnum
        self.bi = format(decnum, '025b')
        self.opcode = ""
        self.regA = ""
        self.regB = ""
        self.regC = ""
        self.twocom =""
    
    def findReg(self):
        x = self.bi
        if(x[0:3] == "000" or x[0:3] == "001"):  # R-type (and, nand)
            self.opcode = str(int(x[0:3],2))
            self.regA = str(int(x[3:6],2))
            self.regB = str(int(x[6:9],2)) 
            #self.temp = x[9:22]
            self.regC = str(int(x[22:25],2))
        elif(x[0:3] == "101"): # J-type (jalr)
            self.opcode = str(int(x[0:3],2))
            self.regA = str(int(x[3:6],2))
            self.regB =  str(int(x[6:9],2))
            #self.temp = x[9:25]
        elif(x[0:3] == "010" or x[0:3] == "011" or x[0:3] == "100"): # I-Type (lw, sw, beq)
            self.opcode = str(int(x[0:3], 2))
            self.regA =  str(int(x[3:6], 2))
            self.regB =  str(int(x[6:9], 2))
            #self.temp = "temp is invalid"
            #self.desReg = "destReg is invalid  
            self.regC = x[9:25]
            c = tc.twosCom_binDec(self.regC, 16)  
            self.regC = str(c)     
            
        else : # O-type (halt, noop)
            self.opcode =  str(int(x[0:3], 2))
            self.temp =  str(int(x[3:25], 2))
            #self.regA = "regA is invalid"
            #self.regB = "resB is invalid"
            #self.desReg = "destReg is invalid"
            #self.offsetField = "offsetFeild is invalid"

            
""" print("======================================================================================")
convert4 = ConB(16842749)
print("Code is " + convert4.bi)
convert4.findReg()
l = convert4.regC
print("[offsetFeild is ] " + l) """


""" convert1 = ConB(16842749)
convert1.findReg()

print("OPCODE IN DEC : " + convert1.opcode)
print(convert1.regA + "  " + convert1.regB + "  " + convert1.regC )
print("this is twocom " + convert1.twocom)
 """
