#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

void printalpha(char *text);

int main(void)
{
    char *dig = "12345";
    char *alpha = "123ZX";
    
    
    printalpha(alpha);
    
    return 0;
}



void printalpha(char *text)
{
    int text_yes = 0;
    
    while (*text != '\0')
    {
        if (!isdigit(*text))
        {
            //printf("This is not a digit: %c\n", *text);
            text_yes = 1;
            text++;
        }
        else
        {
            text++;
            
        }
    }
    
    if (text_yes == 1)
    {
        printf("This contains an alpha char\n");
    }
}