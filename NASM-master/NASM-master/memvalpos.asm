;
; carry flag if we take some borrow in situation
; 5-10 then Carry flag is set
[org 0x0100]
jmp start
num1: dw 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

start:
    xor ax, ax
    mov cx, 0
outerloop:
    add ax, [num1+cx]
    add cx, 2

    cmp cx, 20
    jne outerloop

mov ax, 0x4c00
int 0x21