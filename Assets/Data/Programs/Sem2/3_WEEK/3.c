//AIM: C program to convert temperature from Fahrenheit to Celsius and vice versa

//Source code

#include <stdio.h>
#include<conio.h>

void main()
{
    float celsius, fahrenheit;
//    clrscr();
     printf("Enter temperature in Fahrenheit: ");
    scanf("%f", &fahrenheit);
	// fahrenheit to celsius  conversion formula
     celsius = (fahrenheit - 32) * 5/9;
    printf("%.2f Fahrenheit = %.2f Celsius\n", fahrenheit, celsius);

    // celsius to fahrenheit conversion formula
    fahrenheit = (celsius * 9 / 5) + 32;
    printf("%.2f Celsius = %.2f Fahrenheit", celsius, fahrenheit);
    getch();
}

