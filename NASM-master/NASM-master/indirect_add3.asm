[org 0x0100]

mov ax, 0x8787; moving garbage value to regsiter
xor ax, ax ; to solve the problem if we take xor of two same value then 0 store in ax
; problem is in register there may be any garbage value 

; famous concept
;INDIRECT ADRRESSING
mov bx, num1; it assigsn adress to register

add ax, [bx]
add bx, 2 ; here it is adress + 2

add ax, [bx]
add bx, 2 ; here it is adress + 

add ax, [bx]
add bx, 2 ; here it is adress + 

mov [result], ax
mov  ax, 0x4c00         ; exit .. 
int  0x21



num1: dw 5, 10, 15
result: dw 0