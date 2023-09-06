//AIM: C Program to find area of circle.

//Source Code

#include<stdio.h>
#include<conio.h>
#include<float.h>

#define pi 3.14 //Important line(Constant declaration)

void  main()
{
   float radius, area;
//   clrscr();
   printf("\nEnter the radius of Circle : ");
   scanf("%f", &radius);
   area = pi * radius * radius;
   printf("\nArea of Circle in float: %f", area);
   getch();
}

