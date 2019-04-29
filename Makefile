program: program.c
	cc -no-pie -rdynamic -g -o program program.c

run: program
	./program | ./srcline.py

clean:
	rm -f *.o program
