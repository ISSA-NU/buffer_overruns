# Shellcode

With the help of reverse-engineering tool, construct your embedded shellcode to execute '/bin/sh'.

NOTE: Please perform this exploit on 64 bit system.

## Basics

1. The first six arguments in a function are passed via register `rdi`, `rsi`, `rdx`, `rcx`, `r8`, and `r9`, while the rest go to the stack.

2. Stack space is reserved by those arguments stored in registers.

3. An integer or pointer return value is retruned in `rax`.

4. `rsp` is the stack pointer.

5. `rbp` is the base pointer.

6. `syscall` instruction triggers the kernel interruption.

7. b'\x00' (a null byte) will be treated as the end of buffer. Valid payload should not have it. Instead, instruction such as `xor rax rax` may produce b'\x00' for us.

8. The %rax of `execve` is 59 (0x3b).

## Call bash

Can you construct the shellcode which would effectively call ?

```c
execve("/bin/sh/", ["/bin/sh"], null);
```