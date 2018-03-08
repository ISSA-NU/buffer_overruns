# Return Oriented Programming

ROP is an advanced version of r2l attack, with its malicious payload constructed using the existing system "gadgets".

A gadget is a piece of instruction such as 
```assembly
push rdi; ret
```

ROP makes uses of all these small gadgets to form its powerful exploit logic. Some researchers even claim ROP to be turing complete.

NOTE: Please perfom this exploit on 64 bit system.

## Return to system

By manipulating the **RET** of the `foo` function, execute the follow code in sequence:

```c
system("ifconfig")
system("whoami")
system("/bin/sh")
```

and then return gracefully from the shell.