CC=gcc
CFLAGS=-g -fno-stack-protector

all: check

default: check

clean:
	rm -rf victim *.o

victim: victim.o
	$(CC) $(CFLAGS) $< -o $@

check: clean victim
	./victim

gdb: clean victim
	gdb ./victim

%.o: %.c
		$(CC) $(CFLAGS) $< -c -o $@

dist:
 	dir=`basename $$PWD`; cd ..; tar cvf $$dir.tar ./$$dir; gzip $$dir.tar %
