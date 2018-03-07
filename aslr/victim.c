#include <stdio.h>
#include <string.h>

void shell() {
  system("/bin/sh");
  exit(0);
}

int main(int argc, char *argv[]) {
  int i = 0;
  char buf[256];
  strcpy(buf, argv[1]);
  printf("%s\n", buf);
  return 0;
}