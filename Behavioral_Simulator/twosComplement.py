class twosComplement:
    #instruction    decBin | dec(int) , bit(int)
    #               binDec | num(string), bit(int)
    def twosCom_decBin(dec, bit):
        if dec >= 0 :
            bin1 = bin(dec).split("0b")[1]
            while len(bin1) < bit:
                bin1 = '0'+bin1
            return bin1
        else:
            bin1 = -1*dec
            return bin(bin1 - pow(2,bit) ).split("0b")[1]
    
    def twosCom_binDec(num,bit):
        while len(num) < bit:
            num = '0' + num
        if num[0] == '0':
            return int(num,2)
        else:
            return -1 * (int(''.join('1' if x == '0' else '0' for x in num), 2) + 1)


"""     print("this is (1111111111111101) dec is  " + str(twosCom_binDec('1111111111111111',16)))
    print("this is (-1) bi is " + str(twosCom_decBin(-1, 16))) """