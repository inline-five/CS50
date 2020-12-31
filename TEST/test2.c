#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>
#include <time.h>

int main(void)
{
    clock_t tic = clock();
    int times = 0;

    for (int i = 0; i < 1; i++)
    {
        int counter = 0;
        int demo = 23;
        int flag = 1;
        int a[] = {18, 19, 20, 21, 22, 23};


        while (flag)
        {
            times += 1;
            for (int j = 0; j < 6; j++)
            {
                if (demo % a[j] == 0)
                {
                    counter += 1;
                    if (counter == 5)
                    {
                        flag = 0;

                    }
                }
                else if (demo % a[j] != 0)
                {
                    break;
                }
            }
            counter = 0;
            demo += 23;
        }
    }
    clock_t toc = clock();

    printf("Elapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);
    printf("%d \n", times);
}
