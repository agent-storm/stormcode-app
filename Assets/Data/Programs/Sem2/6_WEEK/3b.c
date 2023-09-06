//AIM:  Write a program to search the given element by using binary search
//Source code

#include<stdio.h>
#include<conio.h>
void main()
{
int a[100],i,key,n,flag=0,high,mid,low=0;
//clrscr();
printf("enter the size array:");
scanf("%d",&n);
printf("enter an element of array:");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("enter the key value:");
scanf("%d",&key);
high=n-1;
while(low<=high)
{
mid=(low+high)/2;
if(key==a[mid])
{
flag=1;
break;
}
else if(key<a[mid])
high=mid-1;
else if(key>a[mid])
low=mid+1;
}
if(flag==0)
printf("key value notfound:");
else
printf("key value found at %d index:",mid);
getch();
}

