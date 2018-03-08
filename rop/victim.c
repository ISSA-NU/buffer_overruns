#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void foo(int a) {
  char buff[30];
  int i = a + 1;
  printf("Foo has argument %d\n", a);
  i = read(0, buff, i);
}

int main(void) {
  foo(199);
  return 0;
}
