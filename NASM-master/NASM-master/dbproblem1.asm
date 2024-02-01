[org 0x0100]
mov ah, [num1]
mov bl, [num1+1]
add ah,bl

mov bh,[num1+2]

add ah, bh
mov bh,[num1+3]


mov  ax, 0x4c00 
int 0x21

num1: db 5, 10, 15, 0