        lw      0   2   mcand       x2 = mcand
        lw      0   3   mplier      x3 = mplier
        lw      0   4   pos1        set temp to x4 (now equal to 1)
mul     nand    3   4   6           x6 = mplier nand temp
        nand    6   6   6           x6 = x6 nand x6 equal to mplier and temp
        beq     6   0   1           if x6 = 0 not do a add func
        add     1   2   1           ans = ans + mcand
        add     2   2   2           mcand += mcand (shift left 1 bit)
        add     4   4   4           temp += temp for check next bit in mplier
        lw      0   5   limit       x5 = limit num
        lw      0   7   mul         x7 = mul address
        beq     4   6   1           if temp = limit it's mean it's out of 15 bit stop now
        jalr    7   5               if not jump to do mul again (we dont care about x5)
        halt
mcand   .fill   33 
mplier  .fill   44
pos1    .fill   1
limit   .fill   32768   limit of 15 bit num