#include <stdio.h>

int main(){

int num;
printf(" entry a number:");
scanf("%d",&num);

if (num > 0)
printf("the number is positive.\n");
else if(num < 0)
printf("the number is negative.\n");
else
printf("the number is zero.\n");


return 0;
}

