# Address Space Layout Randomization

User space and kernel space ASLR are used as system level defense mechnisms in order to significantly increase the difficulty for an attacker to reliably predict the memory position of stack, heap, libc, and other shared libraries, making advanced buffer overflow techniques such as r2l or ROP ineffective.

ASLR can be bypassed under certain constrains (bad coding practice). It could also be brute-forced. Doing so is much easier on 32 bit system as compared to on 64 bit system.

NOTE: Please execute this attack set on the 32 bit system. 

## Part 1 - Return-to-PLT

## Part 2 - Brute Force