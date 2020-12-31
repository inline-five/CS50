#include <time.h>
#include <stdio.h>

int main()
{
    clock_t tic = clock();
    
    int a = 5;
    int b = 5;

    for (int i = 0; i < 999999000; i++)
    {
        a += b;
    }

    clock_t toc = clock();

    printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);

    return 0;
}