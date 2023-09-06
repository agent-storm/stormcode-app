//AIM: C Program to initialize, assign & print different data type values

//Source Code
#include<stdio.h>
#include<conio.h>
void main()
{
	
signed char ch='C',k; //signed char (or)simply char
short int si=5;
int  i=6,r;      //signed int (or)simply int
long int li=7; //long int (or)signed long int
float f=5.6,j;
double d=7.8,l;
signed int ui=-3;
//clrscr();
printf("Initialization values \nch=%c\n si=%hd\n i=%d\n li=%ld\n f=%f\n d=%lf\n ui=%i\n",ch,si,i,li,f,d,ui);
r=89;
j=32.5;
k='h';
l=d;
printf("assignment values \nr=%d \nj=%f \nk=%c \nl=%f",r,j,k,l);
getch();
}

/* Output:
	Initialization values
	ch=C
	 si=5
	 i=6
	 li=7
	 f=5.600000
	 d=7.800000
	 ui=-3
	assignment values
	r=89
	j=32.500000
	k=h
	l=7.800000
*/

