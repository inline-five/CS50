/*
CS50x 2021 PSET 1, Lab 1
https://cs50.harvard.edu/x/2021/labs/1/
*/

#include <cs50.h>
#include <stdio.h>

int get_start_population(void);
int get_end_population(int start_pop);
void print_years(int start_pop, int end_pop);

int main(void)
{
    // TODO: Prompt for start size

    int start_pop = get_start_population();
    int end_pop = get_end_population(start_pop);
    print_years(start_pop, end_pop);

}

int get_start_population(void)
{
    int start_pop = 0;
    do
    {
        start_pop = get_int("Start size: ");

    } while (start_pop < 9);

    return start_pop;
}

int get_end_population(start_pop)
{
    int end_pop = 0;
    do
    {
        end_pop = get_int("End size: ");
    } while (end_pop < start_pop);

    return end_pop;
}

void print_years(int start_pop, int end_pop)
{
    int years = 0;

    while (start_pop < end_pop)
    {
        start_pop += (int) start_pop/3 - (int) start_pop/4;
        years += 1;
    }

    printf("Years: %d\n", years);
}
