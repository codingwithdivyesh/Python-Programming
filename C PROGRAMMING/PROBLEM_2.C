#include <stdio.h>

int main(){

float feet, inches;
printf(" entry feet :");
scanf("%f",&feet);

inches = feet * 12;

printf("%.2f feet is %.2f inches\n", feet, inches);


return 0;
}