#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void foo(const char *buff1) {
  unsigned int a = 0xbeef;
  char buff[256];
  strcpy(buff, buff1);
  if (a == 0xfeed) {
    printf("Part III completed\n");
  }
}

int main(int argc, char *argv[]) {
  foo(argv[1]);
  return 0;
}
