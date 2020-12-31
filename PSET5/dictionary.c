// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

node *head = NULL;
node *temp = NULL;
node *p = NULL;
int counter = 0;

// Number of buckets in hash table
const unsigned int N = 210000;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{

    p = table[hash(word)];

    while (p != NULL)
    {
        if (strcasecmp(word, p->word) == 0)
        {
            return true;
        }
        p = p->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash = 0;

    for (int i = 0, n = strlen(word); i < n; i++)
    {
        hash = (hash << 2) ^ tolower(word[i]);
    }
    return hash % N;

}
// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *opendic = fopen(dictionary, "r");
    if (opendic == NULL)
    {
        return 1;
    }

    //read strings from file into nodes
    char words[LENGTH + 1] = {0}; //**** delete the = {0} for testing
    while (fscanf(opendic, "%s", words) != EOF)
    {
        counter++;

        temp = malloc(sizeof(node));
        if (temp == NULL)
        {
            return false;
        }

        strcpy(temp->word, words);
        temp->next = NULL;

        if (table[hash(words)] == NULL)
        {
            table[hash(words)] = temp;
        }
        else
        {
            temp->next = table[hash(words)];
            table[hash(words)] = temp;
        }
    }
    /*for (int i = 0; i < N; i++)
        {
            p = table[i];
            while (p != NULL)
            {
                printf("Table [%i] : ", i);
                printf("%s\n", p->word);
                p = p->next;
            }
        }*/
    fclose(opendic);
    return true;

}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{

    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next;
            free(table[i]);
        table[i] = tmp;
        }
    }
    return true;


}