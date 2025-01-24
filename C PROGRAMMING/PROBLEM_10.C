#include <stdio.h>


int main(){
int number1 , number2 , number3 ;

printf(" entry the number one : ");
scanf("%d",&number1);
printf(" entry the number second : ");
scanf("%d",&number2);
printf(" entry the number thired : ");
scanf("%d",&number3);

int largest = number1;

if (number2>largest) {
   largest = number2;

}

 if(number3>largest) {
    largest = number3;
 }

 printf("The largest number is: %d\n", largest);

return 0;
}
