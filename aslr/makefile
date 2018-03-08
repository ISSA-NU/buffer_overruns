CC=gcc
CFLAGS=-g -O0 -fPIC -fno-builtin -z execstack -fno-stack-protector

all: check

default: check

clean:
	rm -rf *.o

victim_r2p: victim_r2p.o
	$(CC) $(CFLAGS) $< -o $@

victim_bf: victim_bf.o
	$(CC) $(CFLAGS) $< -o $@

%.o: %.c
	$(CC) $(CFLAGS) $< -c -o $@

gdb: clean victim_bf
	gdb ./victim_bf

check: clean victim_bf
	./victim_bf

dist:
 	dir=`basename $$PWD`; cd ..; tar cvf $$dir.tar ./$$dir; gzip $$dir.tar %
