; disadvantage of assembly language we can compare 
; values in registers only because there is only one adress bus so it is not possible to swap or cmp two values in memory
[org 0x0100]
jmp start

data: dw 6, 4, 5, 2

start:
    mov cx, 4

    outerloop:
        mov bx, 0
        ; we have to do 3 iterations so condition for breaking inner loop is cmp bx, 6
        innerloop:
        mov ax, [data + bx] ; first value moved to reg ax
        cmp ax, [data + bx + 2] ; comparing first value with 2nd
        jbe noswap ; it execute when values are equal
        ; jbe stands for jump if below or equal
        ; this works if carry flag sets
        ; alternative is jna jump if not above

        ; swap algo
        mov dx, [data + bx + 2] ; moving 2nd val to dx
        mov [data + bx + 2], ax ; moving 1st val to 2nd mem adress
        mov [data + bx], dx     ; moving dx to 1st val


        noswap:
        add bx, 2
        cmp bx, 6
        jne innerloop

    sub cx, 1
    jnz outerloop
mov ax, 0x4c00
int 0x21