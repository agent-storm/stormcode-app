//AIM:  C program to print minimum and maximum elements in the 1-D array.
//Source code

#include<stdio.h>
#include<conio.h>
void main()
{
  int a[20],i,size,min,max;
//  clrscr();
  printf("Enter the array size: ");
  scanf("%d",&size);
  printf("Enter the elements into array: ");
  for(i=0;i<size;i++)
  scanf("%d",&a[i]);
  min=a[0];
  max=a[0];

  for(i=0;i<size;i++)
    	 if(min>a[i])
   	  min=a[i];
 for(i=0;i<size;i++)
    	 if(max<a[i])
   	  max=a[i];
   	  printf("maximum value is:%d\n",max);
 	  printf("minimum value is:%d\n",min);
 	  getch();
}

