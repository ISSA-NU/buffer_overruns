# Smashing the Stack

Smash the stack by manipulating the buffer overflow vulnerability.

NOTE: Please perform this exploit on 64 bit system.

[Back to Main](../README.md)

## Part 1 - Control Flow

By manipulating the input, can you change the value of variable **a** in function `foo` to make it print something?

## Part 2 - Find Return Address

By manipulating the input, can you change the logic flow of the victim program such that function `foo` will call function `bar`?