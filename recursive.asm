	    lw	0	6	pos1	x6 = 1
	    lw	0	1	n	    x1 = input[n]
	    lw	0	2	r	    x2 = intput[r]
                                                    sw	5	1	stack	save n to stack
                                                    add	5	6	5	    increment stack pointer
                                                    sw	5	2	stack 	save r to stack
                                                    add	5	6	5	    increment stack pointer
	    lw	0	4	comAdr	x4 = combi
	    jalr	4	7	    call combi x7 = retrunaddress
	    halt
combi   sw	5	7	stack	savereturn address on stack
	    add	5	6	5	    increment stack pointer
	    lw	1	6	neg1	x6 = n-1
	    sw	5	6	stack	save new n vaule to stack for (n-1,r)
	    add	5	6	5	    increment stack pointer
        lw  
	    lw	
	    beq	1	2	L1Adr	if n == r jump to L1
	    beq	0	2	L1Adr	if r ==0 jump to L1
	
	
L1      lw  0   6   pos1    x6 = 1
	    add	3	6	3	x3 += 1
	
L2	
	
combi	.fill	comAdr
pos1	.fill	1
neg1	.fill	-1
L1	    .fill	L1Adr
L2	    .fill	L2Adr
n	    .fill	4       input
r	    .fill	2       input
stack	.fill	0