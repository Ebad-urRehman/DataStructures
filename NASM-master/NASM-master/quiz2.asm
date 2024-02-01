[org 0x0100]

jmp start
numlist: dw 10, 13, 15
dividend: dw 0
divisor: dw 0
divisor: dw 0


start:
ax 10
bx 2

mov [dividend], ax
mov [divisor], bx
idiv ax, bx

outerloop:
imul 2, ax
sub ax, 1
jnz 
