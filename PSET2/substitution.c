#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
// #include <stdbool.h> for true/false bool data type


int main(int argc, string argv[])
{
    if (argc != 2) // check for 2 comm. line arguments
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    //         key ex =  "jtrekyavogdxpsncuuzlfbmwhq"
    //         key ex =  "JTREKYAVOGDXPSNCUIZLFBMWHQ"
    const string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const int alpha_len = strlen(alpha);
    string key = argv[1]; // char key[strlen(argv[1])]; strcpy(key, argv[1]);
    int key_len = strlen(key);

    // validate key
    for (int i = 0; i < key_len; i++)
    {
        if (isalpha(key[i]) == false) // letters only (!isalpha)
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
        else if (key_len != 26) // must be 26 chars long
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        for (int j = 1 + i; j <= key_len; j++) // check for dupes
        {
            if (key[i] == toupper(key[j]) || key[i] == tolower(key[j]))
            {
                printf("No duplicates allowed.\n");
                return 1;
            }
        }
    }

    // get input from user
    string plaintext = get_string("plaintext: ");
    int plain_len = strlen(plaintext);
    printf("ciphertext: ");

    // run over each letter to change letters, but keep other chars
    for (int i = 0; i < plain_len; i++)
    {
        for (int j = 0; j < alpha_len; j++)
        {
            if (plaintext[i] == toupper(alpha[j]))
            {
                printf("%c", toupper(key[j]));
            }
            else if (plaintext[i] == tolower(alpha[j]))
            {
                printf("%c", tolower(key[j]));
            }
        }
        if (ispunct(plaintext[i]) || isspace(plaintext[i]) || isdigit(plaintext[i]))
        {
            printf("%c", plaintext[i]);
        }
    }

    printf("\n");
}