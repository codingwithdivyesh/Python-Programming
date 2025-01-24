#include <stdio.h>

int main(){

float prinicipal , roi , timeperiod;

printf(" entry the prinicipal number here= ");
scanf("%f",&prinicipal);
printf(" entry the roi number here= ");
scanf("%f",&roi);
printf(" entry the number of time period here= ");
scanf("%f",&timeperiod);


float  simple_interest = (prinicipal * roi * timeperiod) /100;


printf(" the  simple interest is :%.1f\n",simple_interest);


return 0;
}