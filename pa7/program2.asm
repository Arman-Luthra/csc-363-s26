.section .text

MV fp, sp
JR func_main
HALT

func_main:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4
ADDI sp, sp, -4
ADDI sp, sp, -4

LI t0, 0
SW t0, -4(fp)
SW t0, -8(fp)

prompt_loop:
LA t0, 0x10000000
PUTS t0
GETI t0
SW t0, -4(fp)
LI t1, 1
BLT t0, t1, prompt_loop

collatz_loop:
LW t0, -4(fp)
LI t1, 1
BGT t0, t1, collatz_body
J collatz_done

collatz_body:
PUTI t0
LW t2, -8(fp)
ADDI t2, t2, 1
SW t2, -8(fp)
LI t1, 2
DIV t3, t0, t1
MUL t4, t3, t1
SUB t5, t0, t4
LI t6, 0
BEQ t5, t6, even_step
LI t7, 3
MUL t8, t0, t7
ADDI t8, t8, 1
SW t8, -4(fp)
J collatz_loop

even_step:
SW t3, -4(fp)
J collatz_loop

collatz_done:
LW t0, -4(fp)
PUTI t0
LW t0, -8(fp)
PUTI t0

MV sp, fp
LW fp, 0(fp)
RET

.section .strings
0x10000000 "Please enter a positive integer\n"
