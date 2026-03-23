Symbol table GLOBAL
name true type InnerType.STRING location 0x10000000 value "True\n"
name false type InnerType.STRING location 0x10000004 value "False\n"
Function: InnerType.INT main([])

Symbol table main
name a type InnerType.INT location -4
name b type InnerType.INT location -8

.section .text
MV fp, sp
JR func_main
HALT

func_main:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4

;Allocate space for a and b
ADDI sp, sp, -4
ADDI sp, sp, -4

;Read a
GETI t0
SW t0, -4(fp)

;Read b
GETI t1
SW t1, -8(fp)

;Compare a and b
BLE t0, t1, printfalse
printtrue:
LA t2, 0x10000000
PUTS t2
J end

printfalse:
LA t2, 0x10000004
PUTS t2

end:
MV sp, fp
LW fp, 0(fp)
RET

.section .strings
0x10000000 "True\n"
0x10000004 "False\n"



