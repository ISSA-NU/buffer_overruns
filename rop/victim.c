#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void foo() {
  char buff[30];
  int i = read(0, buff, 200);
}

int main(void) {
  foo();
  return 0;
}
