//AIM: C program to search the given element by using linear search 
//Source code

#include<stdio.h>
#include<conio.h>
void main()
 {
 int i,j,a[100],key,n,flag=0;
// clrscr();
 printf("Number of elements in the array\n");
 scanf("%d",&n);
 printf("\n Enter %d elements\n",n);
 for(i=0;i<n;i++)
 scanf("%d",&a[i]);
 printf("Element to be searched\n");
 scanf("%d",&key);

  for(i=0;i<n;i++)
   {
    if(key==a[i])
     {
       flag=1;
       break;
      }
    }
    if(flag==1)
    printf("key  value found at %d index",i);
    else
    printf("key value not found");
    getch();  }

