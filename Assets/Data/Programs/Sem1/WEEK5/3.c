//AIM:  C program to read 2 numbers x and n then compute the sum of the Geometric 
//            Progression. 1+x+ x2+x3+ - - - - - - - +xn 
//Source code

#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
int sum=0,n,x,i;
//clrscr();
pos: printf("\n Enter the  x value: ");
     scanf("%d",&x);
     printf("\n Enter n:");
     scanf("%d",&n);
     if(n<0)
     {
       printf("\n Entered n value is negative so enter  positive value");
           goto pos;
     }
      else
      for(i=0;i<=n;i++)
        {  
         sum=sum+pow(x,i);
        }
      printf("\n Sum of series upto %d terms is:%d",n,sum);
      getch();
     }

