#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

void bar() {
    printf("Part-1 Completed.\nNext task is to execute /bin/sh command by calling system() function by exploiting the buffer overflow vulnerability in this code.\n");
    exit(0);
}

void foo() {
    char buff[30];
    int i;
    i = read(0, buff, 200);
}

int main(void) {
    foo();
    return 0;
}
