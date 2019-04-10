#include <execinfo.h>
#include <stdio.h>
#include <stdlib.h>

void baz(void)
{
	void *callstack[128];
	int i, frames;
	char **strs;

	frames = backtrace(callstack, 128);
	strs = backtrace_symbols(callstack, frames);
	for (i = 0; i < frames; i++)
		printf("%s\n", strs[i]);
	free(strs);
}

void bar(void)
{
	baz();
}

void foo(void)
{
	bar();
}

int main(void)
{
	foo();
	return 0;
}
