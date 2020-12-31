#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float price;
    do
    {
        price = get_float("Change owed: ");
    }
    while (price < 0);

    int change = round(price * 100);
    printf("%i\n\n", change);

    int q = change / 25;
    printf("Number of quarters: %i\n", q);

    int d = (change - (q * 25)) / 10;
    printf("Number of dimes: %i\n", d);

    int n = (change - q * 25 - d * 10) / 5;
    printf("Number of nickels: %i\n", n);

    int p = (change - q * 25 - d * 10 - n * 5);
    printf("Number of pennys: %i\n\n", p);

    int t = q + d + n + p;
    printf("%i\n", t);
}