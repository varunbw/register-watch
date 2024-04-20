section .data
    count db 4

section .text

    global _start
    _start:
    labels:
    mov rax, 5
    mul rax, count
    cmp rbx, rax