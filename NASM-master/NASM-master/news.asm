[org 0x0100]

mov ax, [num1]
mov [num1 + 6],ax

mov ax, [num1]
add [num1+6],ax

mov ax, [num1 + 4]
add [num1+6], ax

mov  ax, 0x4c00         ; exit .. 
int  0x21 

num1: db 5 ,10 ,15 ,0
