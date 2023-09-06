//AIM:  C Program to print the data type values and their ranges in C

#include <stdio.h>
#include <conio.h>
#include <limits.h>
#include <float.h>
void main()
{
//clrscr();
printf("The number of bits in a byte %d\n", CHAR_BIT);
printf("SIGNED CHAR : size=%d and range = %d to %d \n",sizeof(signed char),SCHAR_MIN, SCHAR_MAX);
printf("CHAR : size=%d and range = %d to %d \n",sizeof(unsigned char),0,UCHAR_MAX);
printf("UNSIGNED INT  : size=%d and range = %d to %ld \n",sizeof(unsigned int),0,UINT_MAX);
printf("SHORT INT   : size=%d and range = %d to %d \n",sizeof(short int),SHRT_MIN, SHRT_MAX); 
printf(" INT        : size=%d and range = %d to %d \n",sizeof(int),INT_MIN,INT_MAX);
printf("LONG INT    : size=%d and range = %ld to %ld \n",sizeof(long int),LONG_MIN, LONG_MAX);
printf("FLOAT       : size=%d and range = %.10e to %.10e\n",sizeof(float),FLT_MIN,FLT_MAX);
printf("DOUBLE      : size=%d and range = %.10e to %.10e\n",sizeof(double),DBL_MIN, DBL_MAX);
getch();
}


/*	Output:
	The number of bits in a byte 8
	SIGNED CHAR : size=1 and range = -128 to 127
	CHAR : size=1 and range = 0 to 255
	UNSIGNED INT  : size=4 and range = 0 to -1
	SHORT INT   : size=2 and range = -32768 to 32767
	 INT        : size=4 and range = -2147483648 to 2147483647
	LONG INT    : size=4 and range = -2147483648 to 2147483647
	FLOAT       : size=4 and range = 1.1754943508e-038 to 3.4028234664e+038
	DOUBLE      : size=8 and range = 2.2250738585e-308 to 1.7976931349e+308
*/
