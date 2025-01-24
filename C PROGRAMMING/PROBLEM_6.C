#include <stdio.h>

int main(){

int num1, num2;

printf(" entry two numbers:");
scanf("%d %d", &num1, &num2);

if ( num1 > num2 )
printf(" the largest number is: %d\n",num1);
else if (num2 > num1)
printf(" the largest number is: %d\n",num2);
else
printf("both numbers are equal .\n");


return 0;
}


// and#include <stdio.h>

int main() {
    int num1, num2, num3;

    // Prompt the user to enter three numbers
    printf("Enter three numbers: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    // Compare the numbers
    if (num1 > num2 && num1 > num3) {
        printf("The largest number is: %d\n", num1);
    } else if (num2 > num1 && num2 > num3) {
        printf("The largest number is: %d\n", num2);
    } else if (num3 > num1 && num3 > num2) {
        printf("The largest number is: %d\n", num3);
    } else {
        printf("At least two of the numbers are equal and the largest.\n");
    }

    return 0;
}



