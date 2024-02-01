[org 0x0100]
jmp start
num1: dw 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

start:
    mov ax, 0
    mov bx, 0
outerloop:
    add ax, [num1+bx]
    add bx, 2

    cmp bx, 20
    jne outerloop

mov ax, 0x4c00
int 0x21
