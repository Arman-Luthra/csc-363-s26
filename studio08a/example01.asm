; Symbol table GLOBAL
; Function: INT main([])

.section .text

MV fp, sp
JR func_main
HALT

func_main:
SW fp, 0(sp)
MV fp, sp
ADDI sp, sp, -4

ADDI sp, sp, 4
MV sp, fp
RET

.section .strings 