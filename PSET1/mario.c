#include <cs50.h>
#include <stdio.h>

int get_height(string prompt);

int main(void)
{
    int n = get_height("Height: ");


    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            printf(" ");
        }
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
    printf("\n");
    }



}

// Prompt user for positive integer
int get_height(string prompt)
{
    int h;
    do
    {
        h = get_int("%s", prompt);
    }
    while (h < 1 || h > 8);
    return h;
}