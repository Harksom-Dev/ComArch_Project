item = ['wqe', 'nand', '1', '1', '1']
        labels, instcode, regA, regB, destReg = item[0], item[1], item[2], item[3], item[4] 

        indexOfInst = self.inst["name"].index(instcode)
        type = self.inst["type"][indexOfInst]
        print(indexOfInst,type)