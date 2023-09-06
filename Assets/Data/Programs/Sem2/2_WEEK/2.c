//AIM: C program to demonstrate relational and operators. (<,>,<=,>=,==,!=) 

//Source code
#include<stdio.h>
#include<conio.h>
void main()
{
int a,b,c;
//clrscr();
printf("\n Enter a,b values:");
scanf("%d%d",&a,&b);
printf("\n\n RELATIONAL OPERATORS");
printf("\n %d <  %d = %d",a,b,a<b);
printf("\n %d >  %d = %d",a,b,a>b);
printf("\n %d <= %d = %d",a,b,a<=b);
printf("\n %d >= %d = %d",a,b,a>=b);
printf("\n %d == %d = %d",a,b,a==b);
printf("\n %d != %d = %d",a,b,a!=b);
getch();
}

