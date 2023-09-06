//AIM: C program to perform arithmetic operations using switch case

//Source code

#include<stdio.h>
#include<conio.h>
void main()
{
int ch,a,b,res;
//clrscr();
printf("\nEnter two numbers:");
scanf("%d%d",&a,&b);
printf("\nMenu");
printf("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder");
printf("\n Enter your choice:");
scanf("%d",&ch);
switch(ch)
{
case 1: res=a+b;
	break;
case 2: res=a-b;
	break;
case 3: res=a*b;
	break;
case 4: res=a/b;
	break;
case 5: res=a%b;
	break;
default:printf("\n Invalid choice!!");
	break;
}
printf("\nResult=%d",res);
getch();  
 }

