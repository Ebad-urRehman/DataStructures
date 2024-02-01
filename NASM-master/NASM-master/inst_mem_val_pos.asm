ERROR

if we move memory values at first 

forexample

num1: 10, 20 ,39 ,48 ,56 ,29

now assembler get 10 as op code 0A00

all instructions are in garbage value till the real instruction come


THE FIX


how to avoid this we use UNCONDITIONAL JUMPS

lets write start after memory assignment

and write jump start before memory assignments

jump start

num1: dw 1,3,4,5,6
label here
start:

processor always take labels as adress


ANOTHER SMALL FIX DURING RUN TIME

these garbage op codes can be change to NOP(not an operation)


make values*2 NOP as there are 2 bytes in a single value