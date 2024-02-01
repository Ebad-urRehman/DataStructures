[org 0x0100]

; start of code 

mov  ax, 5              ; move the constant 5 into register ax 
mov  bx, 10             

add  ax, bx             ; add value of bx into the value of ax 

mov  bx, 15             ; add constant 15 into the value of bx 
add  ax, bx

mov ax, [num1]

mov  ax, 0x4c00         ; exit .. 
int  0x21               ; .. is what the OS should do for me

; last statement stops normal execution and called interupt

num1: dw, 5

; oop code is neccesary for a progrma and operand

; move is op code
; some instructions needs two operands (works only on two operands) ie. source and destination
;sime operate on one operand 
; A1 is 
; op code is different in diff cases i.e in from mem to reg its diff than reg to reg

; for memory it uses [1700] which is an adress

; to check wheter it is correct
; check at last the adress must be 00000017 the next of it is 0500 or 0A00 for 5 or 10

;all memory variables below are global varibales
; its not a good practice


;;;
; num1: dw 5
;       dw 10
;       dw 15
;       dw 0


;; now we can acees the 2nd adress by [Num1+2]

;; num1: dw 5, 10, 15, 0 ; valid instruction
; watch the listing carefully 


;;; you can alocate a full space
; as [num1 + 6]

mov ax, [num1]
mov [num1 + 6],ax

mov ax, [num1]
add [num1+6],ax

mov ax, [num1 + 4]
add [num1+6], ax

