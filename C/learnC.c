#include <stdio.h>

int main()
{
	int x = 0;
	int y = 0;
	while (x < 10) {
		x = x + 1;
		y = y + x;
		printf("%i%i\n", x, y);
		x = x + 1;
		printf("x is stored at %p\n", &x);
	}
}
