char code[] = "<PASTE YOUR SHELLCODE HERE>";

int main(int argc, char **argv) {
  int (*func)();
  func = (int (*)())code;
  (int)(*func)();
  return 0;
}