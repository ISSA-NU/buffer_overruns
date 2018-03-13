# Address Space Layout Randomization

User space and kernel space ASLR are used as system level defense mechnisms in order to significantly increase the difficulty for an attacker to reliably predict the memory position of stack, heap, libc, and other shared libraries, making advanced buffer overflow techniques such as r2l or ROP ineffective.

ASLR can be bypassed under certain constrains (bad coding practice). It could also be brute-forced. Doing so is much easier on 32 bit system as compared to on 64 bit system.

NOTE: Please execute this attack set on the 32 bit system. 

[Back to Main](../README.md)

## Part 1 - Return-to-PLT

Turn on ALSR by

```bash
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
```

Now, try to invoke a `system` call by manipulating the vulnerable buffer.

## Part 2 - Brute Force

Turn on ALSR using the same command specified above.

Now, try to execute effectively

```c
system('/bin/sh');
```