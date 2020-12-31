#include <stdio.h>

void addOne();


int main(void)
{

// b is a box with 1 layer (1 star)
// a doesn't have a box, so I need to package it (with a &)
int a = 1;
int *b = &a;


// I want to know what's inside the box. It has 1 layer so I unwrap // it with 1 star
printf("what is the value of b ? %d\n", *b); // 1


// The logic is the same for double pointers
// c is a box with 2 layers (2 stars)
// b has a box but it only has 1 layer, I am adding 1 more layer to // it (with a &)
int **c = &b;


printf("what is the value of c ? %d\n", **c); // 1

}
