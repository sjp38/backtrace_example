program: program.c
	cc -rdynamic -g -o program program.c

clean:
	rm -f *.o program
