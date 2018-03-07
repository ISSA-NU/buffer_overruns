#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void shell_exec() {
  system("id");
  printf("Call me by your name.\n");
}

void str_copy(const char *buff1) {
  char buff[12];
  strcpy(buff, buff1);
}

int main(int argc, char *argv[]) {
  str_copy(argv[1]);
  return 0;
}
