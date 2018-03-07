#include <stdio.h>
#include <stdlib.h>

char shellcode[] = "<THE ACTUAL SHELL CODE COMES HERE>";

int main() {
  void (*f)() = (void (*)())shellcode;
  f();
  return 0;
}
