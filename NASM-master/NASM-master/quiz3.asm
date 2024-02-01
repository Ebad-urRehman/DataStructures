[org 0x0100]

jmp start

numbers: dw 4, 6
result: dw 0
start:
mov ax, 0
mov bx, [numbers + 2]
mov cx, bx
outerloop:
add ax, 4
sub cx, 1
jnz outerloop

mov [result], ax

mov ax, 0x4c00
int 0x21