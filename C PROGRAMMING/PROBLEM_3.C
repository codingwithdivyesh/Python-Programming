#include <stdio.h>

int main(){

int a, b, temp;
printf(" entry two numbers:");
scanf("%d %d",&a, &b);
temp= a;
a = b;
b = temp;

printf("after swapping : a =%d, b =%d\n", a,b);



return 0;
}