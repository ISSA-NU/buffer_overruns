#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void bar() { print("Are you watching closely?\n"); }

int foo(const char *buff1) {
  unsigned int a = 0xbeef;
  char buff[256];
  strcpy(buff, buff1);
  if (a == 0xfeed) {
    printf("Feed me with buffer.\n");
  }
  return 1;
}

int main(int argc, char *argv[]) {
  int a = foo(argv[1]);
  return 0;
}
