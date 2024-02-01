[org 0x0100]

mov ax, 0
; xor ax, ax
mov cx, cx
mov bx, num1

mov cx, 3
outerloop:
    add ax, [bx]
    add bx, 2
    sub cx, 1
    JNZ outerloop
add [result], ax
mov ax, 0x4c00
int 0x21

num1: dw 5, 10, 15
result: dw 0
