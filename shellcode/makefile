CC=gcc
CFLAGS=-g -O0 -fPIC -fno-builtin -z execstack -fno-stack-protector

all: check

default: check

clean:
	rm -rf *.o

victim: victim.o
	$(CC) $(CFLAGS) victim.o -o victim

%.o: %.c
	$(CC) $(CFLAGS) $< -c -o $@

gdb: clean victim
	gdb ./victim

check: clean victim
	./victim

dist:
 	dir=`basename $$PWD`; cd ..; tar cvf $$dir.tar ./$$dir; gzip $$dir.tar %
