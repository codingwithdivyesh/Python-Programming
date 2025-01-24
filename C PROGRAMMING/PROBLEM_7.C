#include <stdio.h>

#define PI 3.14
int main(){
float radius;

printf(" ENTRY radius for cricle = ");
scanf("%f",&radius);

float radius_answer = PI * radius * radius ;

printf(" your answer is :%f",radius_answer);


return 0;
}