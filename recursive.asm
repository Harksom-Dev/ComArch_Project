	    lw		0	6	pos1	x6 = 1
	    lw		0	1	n	    x1 = input[n]
	    lw		0	2	r	    x2 = intput[r]
		sw		5	1	stack	save n to stack
		add		5	6	5	    increment stack pointer
		sw		5	2	stack 	save r to stack
		add		5	6	5	    increment stack pointer
	    lw		0	4	comAdr	x4 = combi
	    jalr	4	7	    call combi x7 = returnaddress
	    halt	
combi   lw		0	6	neg1	x6 = -1
		lw		5	2	stack	load new r vaule from stack
		add		5	6	5		decrement stack pointer	
	    lw		5	1	stack	load new n vaule from stack
		add		5	6	5		decrement stack pointer	
	    beq		2	0	L1Adr	if r == 0 jump to L1
	    beq		1	2	L1Adr	if n == r jump to L1
		lw		0	6	pos1	x6 = 1
		lw		1	4	neg1	x4 = n-1
		sw		5	4	stack	save n-1 to stack
		add		5	6	5	    increment stack pointer
		lw		2	4	neg1	x4 = r-1
		sw		5	4	stack	save r-1 to stack
		add		5	6	5	    increment stack pointer
		lw		1	4	neg1	x4 = n-1
		sw		5	4	stack	save n-1 to stack
		add		5	6	5	    increment stack pointer
		sw		5	2	stack	save r to stack
		add		5	6	5	    increment stack pointer
		beq		5	6	stopAdr	if stack poiner == 0 it's mean program need to stop(since this version stack->0 is poiter to address)
		

	
L1      lw  	3   3   pos1    x3 += 1
		lw		0	4	comAdr	x4 = combi
		jalr	4	7
		
stop	halt
	
stop	.fill	stopAdr
combi	.fill	comAdr
pos1	.fill	1
neg1	.fill	-1
L1	    .fill	L1Adr
n	    .fill	4       input
r	    .fill	2       input
stack	.fill	0