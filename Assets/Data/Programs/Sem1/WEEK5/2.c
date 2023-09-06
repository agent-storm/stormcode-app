//AIM:  C program to print prime numbers in the given range.

//Source code

#include <stdio.h>
#include <conio.h>
void main()
{
 int n,i,j,count=0;
// clrscr();
 printf("Enter any postive integer: ");
 scanf("%d",&n);
 for(i=2;i<=n;i++)
 {
  for(j=2;j<=i;j++)
  {
    if(i%j==0)
    count++;
  }
  if(count==1)
  printf("\n%d\t",i);
  count=0;
 }
 getch();
}

