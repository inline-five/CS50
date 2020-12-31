#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // variables needed:
    int card_len = 0;
    long long digit = 0;
    long long loop = 1;
    int first_loop = 0;
    int digit_sum = 0;

    long long card = get_long("Number: "); // hard coded card
    long long card_copy = card;

    // get card length by checking length of number
    do
    {
        card = card / 10;
        card_len += 1;
    }
    while (card != 0);

    // place each digit into array called checksum[]
    int checksum[card_len];
    for (int i = 0; i < card_len; i++)
    {
        digit = card_copy % (10 * loop);
        checksum[i] = digit / loop;
        loop *= 10;
    }

    // Add the sum to the sum of the digits that weren’t multiplied by 2.
    for (int i = 1; i < card_len; i++)
    {
        first_loop = checksum[i] * 2;
        i += 1;

        if (first_loop < 10)
        {
            digit_sum += first_loop;
        }
        else if (first_loop >= 10)
        {
            digit_sum += first_loop % 10;
            digit_sum += 1;
        }
    }

    // add all the remaining digits togheer
    for (int i = 0; i < card_len; i++)
    {
        digit_sum += checksum[i];
        i += 1;
    }

    // test the card digits
    if (digit_sum % 10 == 0)
    {
        if ((card_len == 13 || card_len == 16) && checksum[card_len - 1] == 4)
        {
            printf("VISA\n");
        }
        else if ((card_len == 15 && checksum[card_len - 1] == 3) &&
                 (checksum[card_len - 2] == 4 || checksum[card_len - 2] == 7))
        {
            printf("AMEX\n");
        }
        else if (card_len == 16 && checksum[card_len - 1] == 5 && (checksum[card_len - 2] == 1 || checksum[card_len - 2] == 2 ||
                 checksum[card_len - 2] == 3 || checksum[card_len - 2] == 4 || checksum[card_len - 2] == 5))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}