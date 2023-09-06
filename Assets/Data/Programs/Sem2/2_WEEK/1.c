//AIM: C program to perform all arithmetic operations

//Source code

#include <stdio.h>
#include <conio.h>
void main()
{
    int a, b, sum, sub, mult, mod;
    float div;
//    clrscr();

// Read two numbers from user
    printf("Enter any two numbers : ");
    scanf("%d%d", &a, &b);

//Performs all arithmetic operations
    sum = a + b;
    sub = a - b;
    mult = a * b;
    div = a / b;
    mod = a % b;


//Prints the result of all arithmetic operations
    printf("SUM = %d \n", sum);
    printf("DIFFERENCE = %d \n", sub);
    printf("PRODUCT = %d \n", mult);
    printf("QUOTIENT = %f \n", div);
    printf("MODULUS = %d", mod);
    getch();
}

