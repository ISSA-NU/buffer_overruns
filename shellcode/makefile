CC=gcc
CFLAGS=-fno-stack-protector -z execstack

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
