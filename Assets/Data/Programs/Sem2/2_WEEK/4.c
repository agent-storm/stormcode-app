//AIM: C program to demonstrate pre-increment and post-increment

//Source code

#include<stdio.h>
#include<conio.h>
void main()
{
 int a,b,x,y,z,w;
// clrscr();
 printf("Enter the values for a and b");
 scanf("%d%d",&a,&b);
 printf("\n The values of a = %d and b = %d",a,b);
 printf("\n The post-increment value of a = %d",a++);
 printf("\n The pre-increment value of a = %d",++a);
 printf("\n The post-increment value of b = %d",b++);
 printf("\n The pre-increment value of b = %d",++b);
getch(); 
}

