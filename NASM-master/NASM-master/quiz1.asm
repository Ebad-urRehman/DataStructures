[org 0x0100]

jmp start

number: dw 4
result: dw 0

start:
xor ax, ax


mov ax, [number]
mov cx, [number]
; outerloop:
;     add ax, ax
;     sub cx, 1
;     JNZ outerloop
mul ax
mov [result], ax
mov ax, 0x4c00
int 0x21