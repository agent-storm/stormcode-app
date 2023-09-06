/*AIM:  C program that declares Class awarded for a given percentage of marks, where mark 
            <40%= Failed, 40% to <60% = Second class, 60% to <70%=First class, >= 70% =   
            Distinction.  Read percentage from standard input. 
*/

//Source code

#include<stdio.h>
#include<conio.h>
void main()
{
float per;
//clrscr();
printf("Enter percentage of Marks");
scanf("%f",&per);
if(per>=70)
printf("grade=Distinction");
else if (per>=60 && per<=70)
printf("grade=First Class");
else if(per>=40&&per<=60)
printf("grade=Second Class");
else printf("grade=Fail");
getch();
}

