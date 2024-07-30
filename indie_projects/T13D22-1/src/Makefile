CC=gcc
CFLAGS=-Wall -Wextra -Werror
BUILD=../build/

all: cipher

cipher: filehandler.o cipher.o filewriter.o
	$(CC) $(CFLAGS) $(BUILD)filehandler.o $(BUILD)cipher.o $(BUILD)filewriter.o -o $(BUILD)cipher

cipher.o: cipher.c
	$(CC) $(CFLAGS) -c cipher.c -o $(BUILD)cipher.o

filehandler.o: filehandler.c
	$(CC) $(CFLAGS) -c filehandler.c -o $(BUILD)filehandler.o

filewriter.o: filewriter.c
	$(CC) $(CFLAGS) -c filewriter.c -o $(BUILD)filewriter.o

clean:
	rm -rf $(BUILD)*.o $(BUILD)cipher

rebuild: clean all
