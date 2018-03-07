# Return-to-libc Attack

r2l attacks are often the first choice when non-executable stack is turned on. It leverages the existing glibc code to construct its malicious code. It is often perceived as simplified version of ROP attack.

NOTE: Perform this attack in 32 bit system, as there are too many NULL bytes in 64-bit system addresses.

## Part 1 - Return to shell_exec

With the help of GDB, can you identify the return address of the function `str_copy`? Can you change it to the address of `shell_exec`?

## Part 2 - Return to system

With the help of GDB, can you make change to the program execution flow such that str_copy will return directly to `system()` with customized arguments?

Say we would like to invoke the following line:

```c
system("/bin/sh")
```