//AIM: C program to print sample strings like “hello world”, “Welcome to C Programming”
//      with different formats using escape sequences. 


#include<stdio.h>
#include<conio.h>
void main()
{
//clrscr();
printf("Hello World\n Welcome to C programming\n"); 	//use of new line
printf("Hello World\t Welcome to C programming\n"); 	// use of horizontal tab
printf("\"Hello World\" \"Welcome to C programming\"\n");	// use of "
printf("\'Hello World\' \'Welcome to C programming\'\n"); 		// use of '
printf("Hello World \\Welcome to C programming\n"); 		// use of \
printf("Hello World \b Welcome to C programming\n"); 		// use of back space
printf("Hello World\rWelcome to C programming\n");  		//use of carriage return
getch();
}

/* Output:
	Hello World
 	Welcome to C programming
	Hello World      Welcome to C programming
	"Hello World" "Welcome to C programming"
	'Hello World' 'Welcome to C programming'
	Hello World \Welcome to C programming
	Welcome to C programming
*/





