
//AIM:  C program to construct a pyramid of numbers as follows 
//    1
//    2  3
//    4  5  6
//Source code

#include<stdio.h>
#include<conio.h>
void main()
{
int i,j,n,k=1;
//clrscr();
printf("Enter number of rows");
scanf("%d",&n);
for(i=1;i<=n;i++)
{printf("\n");
for(j=1;j<=i;j++)
{
printf("%3d",k);
k++;
}
}
getch();
}

