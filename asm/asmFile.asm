; %macro rw 4
;     mov rax, %1
;     mov rdi, %2
;     mov rsi, %3
;     mov rdx, %4
;     syscall
; %endmacro

section .data
    ; Initialize array of size 64, each element of size 1 byte
    numArray times 64 db 1

    msgVal db "Value: "
    lenmsgVal equ $-msgVal

    msgRes db "Result of array addition is: "
    lenmsgRes equ $-msgRes

    count db 5
    temp1 db 0

    newLine db 0AH

section .bss
    result resw 1
    temp resw 2
    num resb 2


section .text
    global _start
    _start:
    
    mov rbp, numArray

    ; This loop runs once for each number entered
    nextnum:
        rw 1, 1, msgVal, lenmsgVal
        rw 0, 0, num, 3
        mov rcx, 0  
        mov rax, 0
        mov rsi, num
        
        ; This loop runs once for each digit in the number
        up1:
            ; Move byte pointed to by rsi to cl
            mov cl, byte[rsi]
            ; 0AH - New Line char, telling end of current input
            ; If equal, jump to "packed"
            cmp cl, 0AH
            je packed

            ; If 0-9, skip subtracting 07H
            cmp cl, 39H
            jbe down1

            sub cl, 07H

            down1:
            sub cl, 30H
            ; Conversion to proper numerical value complete

            rol al, 4  ; move current 4 bits to the left to make space for new hex digit
            add al, cl ; al = al + cl
            inc rsi    ; next index
        jmp up1

        packed:
        mov byte[rbp], al  ; Move the numerical packed value into array
        inc rbp            ; Increment index

        dec byte[count]
    jnz nextnum
    ; Input over


    ; Start addition
    mov rsi, numArray
    mov ax, 00H
    mov bx, 00H
    mov cx, 05H  ; Counter, holds size of array
    
    up2:
        ; Move i'th element of array to bl
        mov bl, byte[rsi]
        ; ax = ax + bx
        add ax, bx

        ; move to next index and decrement counter
        inc rsi
        dec cx
    jnz up2

    mov word[result], ax
    mov bp, 04H

    rw 1, 1, newLine, 1
    rw 1, 1, msgRes, lenmsgRes
    
    up:
        rol ax, 4    ; Get digit to print
        mov bx, ax   ; Store value in bx as temp
        and ax, 0FH  ; AND with 0FH to get units digit
        cmp al, 09H  ; compare with 09H to check whether to add 07H or not
        jbe down
        add al, 07H
    
        down:
        add al, 30H
        mov byte[temp], al

        rw 1, 1, temp, 1
        mov ax, bx
        dec bp
    jnz up

    rw 1, 1, newLine, 1
    rw 1, 1, newLine, 1
    
    rw 60, 0, 0, 0
    syscall

; mov rax, rbx
; mov rax, 5