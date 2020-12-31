#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{

    string text = get_string("Text: ");
    float letters = 0, words = 1, sentences = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
        else if (isspace(text[i]))
        {
            words++;
        }
        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
    }

    float l = 100 / words * letters;
    float s = 100 / words * sentences;

    float index = (0.0588 * l) - (0.296 * s) - 15.8;

    int indexr = (round(index));

    if (indexr >= 1 && indexr < 16)
    {
        printf("Grade %i\n", indexr);
    }
    else if (indexr < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade 16+\n");
    }
}