#include <stdio.h>

int main()
{
    int num1;
    int num2;
    int multi;
    printf("Enter the first number: ");
    scanf("%i", &num1);
    printf("Enter the second number: ");
    scanf("%i", &num2);
    printf("Enter the multiplier: ");
    scanf("%i", &multi);
    printf("You entered the number %i, %i ", num1, num2);
    printf("\nThe result is %i", (num1+num2)*multi);

    int i;
    int num;
    int sum;
    sum=0;
    for (i=0; i<=10; i++)
    {
        printf("\n\nEnter a number from 0 to 9: ");
        scanf("%i", &num);
        sum=sum+num;
        printf("The actual sum is %i \n", sum);
    }

    return 0;
}
