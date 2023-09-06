//AIM:  C Program to display colors using switch case (VIBGYOR).

//Source code

#include<conio.h>
void main()
{
char color;
//clrscr();
printf("Enter the Colour Code:");
scanf("%c",&color);
switch(color)
{
case 'v':
case 'V':printf("VIOLET");
	 break;
case 'i':
case 'I':printf("INDIGO");
	 break;
case 'b':
case 'B':printf("BLUE");
	 break;
case 'g':
case 'G':printf("GREEN");
	 break;
case 'y':
case 'Y':printf("YELLOW");
	 break;
case 'o':
case 'O':printf("ORANGE");
	 break;
case 'r':
case 'R':printf("RED");
	 break;
default:printf("Invalid choice!!");
}
getch();
}

