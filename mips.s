.text
.globl main
Main:
	.data
	x: .word 1
	y: .word 2
	main:
		lw $a0, x
		add $t1, 2, 1
		lw $r0, y
		j $ra
