#include <stdio.h>

/* print Fahrenheit-Celsius table for f = 0, 20, ..., 300 */

int main()
{
	int fahr;
	for (fahr = 0; fahr <= 300; fahr += 20) {
		printf("%4d %6.2f\n", fahr, (5.0/9.0) * (fahr-32.0));
	}
}

