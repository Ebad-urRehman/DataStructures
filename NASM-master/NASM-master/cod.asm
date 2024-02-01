[org 0x0100]

; start of code 

mov  ax, 5              ; move the constant 5 into register ax 
mov  bx, 10             

add  ax, bx             ; add value of bx into the value of ax 

mov  bx, 15             ; add constant 15 into the value of bx 
add  ax, bx

mov ax, [num1]
mov bx, [num2]

mov [num3], ax

; mov [num3], [num1] ;invalid

mov  ax, 0x4c00         ; exit .. 
int  0x21               ; .. is what the OS should do for me


num1: dw 5
num2 dw 10
num3 dw 15
num4: dw 0
