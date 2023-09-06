//AIM: C program to sort the given elements using bubble sort technique. 
//Source code

#include <stdio.h>
#include <conio.h>
void main()
{
  int a[100], n, i, j, s;
//  clrscr();
  printf("Enter number of elements\n");
  scanf("%d", &n);
  printf("Enter %d integers\n", n);
    for (i = 0; i < n; i++)
    scanf("%d", &a[i]);
    for (i= 0 ; i < ( n - 1 ); i++)
     {
       for (j = 0 ; j < n - i- 1; j++)
	{
	  if (a[j] > a[j+1]) /* For decreasing order use < */
	   {
	     s= a[j];
	     a[j]   = a[j+1];
	     a[j+1] = s;
	   }
	}
     }
     printf("Sorted list in ascending order:\n");
     for ( i = 0 ; i < n ; i++ )
     printf("%d\n", a[i]);
     getch();
}

