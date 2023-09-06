//AIM:  C Program to calculate roots of quadratic equation (using if-else). 
//Source code


#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
float a,b,c,d,r1,r2;
//clrscr();
printf("ENTER THE VALUES OF a,b,c:\n");
scanf("%f%f%f",&a,&b,&c);
d=(b*b)-(4*a*c);
if(d==0)
{
printf("\n Roots are equal:");
r1=-b/(2*a);
r2=-b/(2*a);
printf("\n The value of root1 = %f",r1);
printf("\n The value of root2 = %f",r2);
}
else  if(d>0)
{
printf("\n Roots are real and distinct:");
r1=(-b+sqrt(d))/(2*a);
r2=(-b-sqrt(d))/(2*a);
printf("\n The value of root1 = %f",r1);
printf("\n The value of root2 = %f",r2);
}
else
printf("\n Root are imaginary");
getch();
}

