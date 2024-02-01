[org 0x0100]


mov ax, 5
mov bx, 10
add ax, bx,

mov ax, [num1] ;valid
mov bx, [num2] ;valid

mov [num3], ax

;mov [num3], [num1] ;invalid


mov ax, 0x4c00
int 0x21

num1: dw 2
num2: dw 34
num3: dw 45
num4: dw 0