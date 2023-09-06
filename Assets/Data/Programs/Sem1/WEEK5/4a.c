//AIM:  C program to construct a pyramid of numbers as follows 
//1
//1 2
//1 2 3
//Source code

#include<stdio.h>
#include<conio.h>
void main()
{
int i,j,n;
//clrscr();
printf("Enter number of rows");
scanf("%d",&n);
for(i=1;i<=n;i++)
{
for(j=1;j<=i;j++)
printf("%3d",j);
printf("\n");
}
getch();  }

