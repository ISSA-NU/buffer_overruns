#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  char buf[20];
  strcpy(buf, argv[1]);
  printf("%s\n", buf);
  fflush(stdout);
  return 0;
}