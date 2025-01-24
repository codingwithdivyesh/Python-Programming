#include <stdio.h>


int main(){

int hight, weight;

printf(" entry the hight :");
scanf("%d",&hight);
printf(" entry the weight:");
scanf("%d",&weight);

int triangle = hight * weight / 2;

printf("area of the %d and %d is :%d",hight,weight,triangle);


return 0;


}