#include <stdio.h>

void addOne(int *x);


int main(void)
{

  int a = 0; // asigns value of 0 to variable a
  int *b = &a; // points to what is located at position a

  printf("%i, value of a\n", a);
  printf("%i, value of b referening what is stored at location a\n", *b);

  addOne(&a); // why must you use & vs *

  printf("%i, new value of a\n", a);
  printf("%i, value of b without updating value of b\n", *b);
}

//
void addOne(int *x)
{
  *x = *x + 1;
}