class ConB:
    def __init__(self, decnum):
        self.decnum = decnum
        self.bi = format(decnum, '025b')
        self.opcode = ""
        self.regA = ""
        self.regB = ""
        self.desReg = ""
        self.temp = ""
        self.offsetField = ""
    def twosComplement(self):
        x = self.bi
        n = len(x)
        i = n-1
        while( i>= 0):
            if(x[i] == '1'):
                break 
            i -=1
        if(i== -1):
            return '1'+x
        k = i-1
        while(k >= 0):
            #flip
            if(x[k] == 1 ):
                x = list(x)
                x[k] = '0'
                x = ''.join(x)
            else:
                x = list(x)
                x[k] = '1'
                x = ''.join(x)
            k-=1
        return x 
       
    def findReg(self):
        x = self.bi
        if(x[0:3] == "000" or x[0:3] == "001"):  # R-type (and, nand)
            self.opcode = x[0:3]
            self.regA = x[3:6]
            self.regB = x[6:9]
            self.temp = x[9:22]
            self.desReg = x[22:25]
            self.offsetField = "offsetFeild is invalid"
        elif(x[0:3] == "101"): # J-type (jalr)
            self.opcode = x[0:3]
            self.regA = x[3:6]
            self.regB = x[6:9]
            self.temp = x[9:25]
            self.desReg = "destReg is invalid"
            self.offsetField = "offsetFeild is invalid"
        elif(x[0:3] == "010" or x[0:3] == "011" or x[0:3] == "100"): # I-Type (lw, sw, beq)
            self.opcode = x[0:3]
            self.regA = x[3:6]
            self.regB = x[6:9]
            self.temp = "temp is invalid"
            self.desReg = "destReg is invalid"
            self.offsetField = x[9:25]
            if(x[9] == "1" ):
                p = ConB.twosComplement(self.offsetField)
                self.offsetField =  p
            else:
                self.offsetField = x[9:25]

        else : # O-type (halt, noop)
            self.opcode = x[0:3]
            self.temp = x[3:25]
            self.regA = "regA is invalid"
            self.regB = "resB is invalid"
            self.desReg = "destReg is invalid"
            self.offsetField = "offsetFeild is invalid"
            
            

           
            
            





print("======================================================================================")
convert2 = ConB(8454151)
convert2.findReg()
print(" lw        0         1         five")
print("Maachine code is " + str(convert2.decnum))
print("[Code is   ] " + convert2.bi)
print("[Opcode is ] " + convert2.opcode)
print("[RegA is   ] " + convert2.regA)
print("[RegB is   ] " + convert2.regB)
print("[desReg is ] " + convert2.desReg)
print("[Temp is   ] " + convert2.temp)
print("[offsetFeild is ] " + convert2.offsetField)

print("======================================================================================")

convert3 = ConB(655361)
convert3.findReg()
print(" add     1         2         1")
print("Maachine code is " + str(convert3.decnum))
print("[Code is   ] " + convert3.bi)
print("[Opcode is ] " + convert3.opcode)
print("[RegA is   ] " + convert3.regA)
print("[RegB is   ] " + convert3.regB)
print("[desReg is ] " + convert3.desReg)
print("[Temp is   ] " + convert3.temp)
print("[offsetFeild is ] " + convert3.offsetField)


