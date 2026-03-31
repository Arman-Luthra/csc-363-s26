.section .text

MV fp, sp
JR func_main
HALT

func_main:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4

GETI t0
LA t1, 0x20000000
SW t0, 0(t1)

GETI t0
LA t1, 0x20000004
SW t0, 0(t1)

LA t1, 0x20000000
LW t2, 0(t1)
LA t1, 0x20000004
LW t3, 0(t1)

BLT t2, t3, print_less
BEQ t2, t3, print_equal
J print_greater

print_less:
LA t0, 0x10000000
PUTS t0
J main_end

print_equal:
LA t0, 0x10000004
PUTS t0
J main_end

print_greater:
LA t0, 0x10000008
PUTS t0
J main_end

main_end:
MV sp, fp
LW fp, 0(fp)
RET

.section .strings
0x10000000 "a is less than b\n"
0x10000004 "a is equal to b\n"
0x10000008 "a is greater than b\n"
