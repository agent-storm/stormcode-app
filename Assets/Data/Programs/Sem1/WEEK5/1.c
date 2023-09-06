//AIM:  C program to calculate sum of individual digits of a number
//Source Code
#include<stdio.h>
#include<conio.h>
void main()
{
   int n,r,sum=0;
//   clrscr();
   printf("Enter any positive integer:");
   scanf("%d",&n);
  do
   {
     r=n%10;
     sum=sum+r;
     n=n/10;
   } while(n>0);
printf("\nSum of individual digits is=%d",sum);
   getch();
}

