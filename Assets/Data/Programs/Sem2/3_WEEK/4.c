//AIM:  C program for computing the volume of sphere, cone and cylinder assume that 
//		Dimensions are integers use type casting where ever necessary.   

//Source code

#include <stdio.h>
#include <conio.h>
void main()
{
    int r,h;
    float vol_of_sphere,vol_of_cone,vol_of_cylinder;
//    clrscr();
    printf("Enter radius of the sphere : ");
    scanf("%d",&r);
    printf("Enter the height of the cone and cylinder:");
    scanf("%d",&h);
    vol_of_sphere = (float)(1.33 * 3.14 * r * r * r);
    vol_of_cylinder =(float) (3.14 * r * r * h);
    vol_of_cone = (float)(0.33 * 3.14 * r * r * h);
    printf("\n Volume of sphere is : %.3f",vol_of_sphere);
    printf("\n Volume of cylinder is : %.3f",vol_of_cylinder);
    printf("\n Volume of cone is   : %.3f",vol_of_cone);
    getch();
}

