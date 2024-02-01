[org 0x0100]
; jump to start
jmp start
multiplicand: db 4
multiplier: db 6
result: dw 0

; moving values to registers
start:
mov ah, [multiplicand]
mov bh, [multiplier]
mov cx, 6
mov dh, 0

; loop for all bits to multiply
outerloop:
    ; to make sure dh has always ah at first
    mov dh, ah
 
    ; if a 0 is encountered in LSB
    shr dh, 1
    jnc is_zero
        ; if 0 is not encountered but 1
        add [result], dh
        sub cx, 1
 
    ; just giving a shift when LSB is 0
    is_zero:
        shl dh, 1
        add [result], dh
        ; outerloop condition
        sub cx, 1
        jnz outerloop

mov ax, 0x4c00
int 0x21

