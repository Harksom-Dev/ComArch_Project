class ConB:
    def __init__(self, decnum):
        self.decnum = decnum
        self.bi = format(decnum, '025b')
        self.opcode = ""
        self.regA = ""
        self.regB = ""
        self.regC = ""
    
    def twos_com(self):
        d = int(self.regC, 2 )
        #print("decimal is " + str(d))
        #print("before flip is " + str(bin(d)).replace('0b', ''))
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
        self.regC =  str(int(tcom, 2))
        #flipped = bin(~d)
        #print("Sign_BIT is " + signBit)

       
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
            self.regC = str(int(x[9:25], 2))
            if( x[9] == "1" ):
                print(" - use 2's complement - ")               
                self.twos_com()
            else:
                print(" - did not use 2's complement - ")
                self.regC = str(int(x[9:25], 2))
            
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


convert1 = ConB(655361)
convert1.findReg()
print("OPCODE IN DEC : " + convert1.opcode)
print(convert1.regA + "  " + convert1.regB + "  " + convert1.regC)