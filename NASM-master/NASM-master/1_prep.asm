; . REGISTER + OFFSET ADDRESSING
[org 0x0100]

mov bx, 0
mov cx, 4
xor ax, ax

label1:
    add ax, [num1 + bx]
    add bx, 2
    sub cx, 1
    jnz label1


mov [result], ax

num1: db 10, 20, 30, 40
result: dw 0

mov ax, 0x4c00
int 0x21