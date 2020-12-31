#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "isvowel_helper.h"


int main(void) 
{
    char string[50] = {'\0'};
    char string2[150 ] = {'\0'};
    
    printf("Enter a word: ");
    scanf("%s", string);
    int len = strlen(string);
    
    if (len > 50)
    {
        printf("Error: two many characters in string. Make more room in array.\n");
        return 1;
    }
    else
    {
       convert(string, string2, len); 
       printf("\n%s, %lu, %lu\n", string2, strlen(string), strlen(string2));
       return 0;
    }
    
}

