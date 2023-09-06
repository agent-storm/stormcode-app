//AIM:  C program to store 10 elements in the 1-D array and print sum of the array.
//Source code

#include<stdio.h>
#include<conio.h>
 
void main()
 {
   int i, arr[50], sum=0, num=10;
//   clrscr();
   printf("\nEnter the %d values into an array :",num);
   for (i = 0; i < num; i++)
   scanf("%d", &arr[i]);
   for (i = 0; i < num; i++)
   sum = sum + arr[i];
   for (i = 0; i < num; i++)
   printf("\na[%d]=%d", i, arr[i]);
   printf("\nSum=%d", sum);
   getch();
}

