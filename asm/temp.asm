section .bss
    temp resw 1

section .data
    mov rax, 2
    mov temp, rax

    mov rax, 5
    mul rax, temp

    mov rsi, rax
    mov rax, 1
    mov rdi, 1
    syscall