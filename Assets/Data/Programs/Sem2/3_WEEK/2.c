//AIM: C program to calculate simple interest
//Source Code
#include <stdio.h>
#include<conio.h>
#include<float.h>
void main()
{
    float principle, time, rate, SI;
//    clrscr();
    printf("Enter principle ,Time,rate ");
    scanf("%f %f %f", &principle,&time,&rate);
    // Calculate simple interest
    SI = (principle * time * rate) / 100;
    printf("Simple Interest = %f", SI);
    getch();
}

