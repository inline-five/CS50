#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int newkey(int k);


int main(int argc, string argv[])
{

    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int l = strlen(argv[1]);

    for (int i = 0; i < l; i++)
    {
        if (isdigit(argv[1][i]) == false) // !isdigit()
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int k = atoi(argv[1]);

    string plaintext = get_string("plaintext: ");
    int n = strlen(plaintext);
    printf("ciphertext: ");

    for (int i = 0; i < n; i++)
    {
        if (isupper(plaintext[i]))
        {
            if (plaintext[i] + newkey(k) <= 'Z')
            {
                printf("%c", plaintext[i] + (newkey(k)));
            }
            else if (plaintext[i] + newkey(k) > 'Z')
            {
                printf("%c", ((plaintext[i] + newkey(k)) - 90) + 64);
            }
        }

        else if (islower(plaintext[i]))
        {
            if (plaintext[i] + newkey(k) <= 'z')
            {
                printf("%c", plaintext[i] + (newkey(k)));
            }
            else if (plaintext[i] + newkey(k) > 'z')
            {
                printf("%c", ((plaintext[i] + newkey(k)) - 122) + 96);
            }
        }

        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}

////key function
int newkey(int k)
{
    return k % 26;
}