#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include "windows.h"

static int input = 0;
static int random = 0;
static int attempt = 0;

void draw()
{
    srand(time(0));
    random = (rand() % 100 + 1);
    printf("\nThe program has chosen a number from 1 to 100, now you can start guessing.");
}

void checking()
{
    printf("\nEnter a number: ");
    scanf("%i", &input);

    if(input < random)
    {
        attempt++;
        printf("The clue number is higher than the entered one. Keep guessing.\nNumber of attempts: %i\n", attempt);
        checking();
    }
    else if(input > random)
    {
        attempt++;
        printf("The clue number is lower than the entered one. Keep guessing.\nNumber of attempts: %i\n", attempt);
        checking();
    }
    else
    {
        attempt++;
        system("Color A");
        printf("Congratulations! You have guessed the number within %i attempts.\n", attempt);
        system("pause");
    }
}

int main()
{
    system("Color C"); //czerwony
    printf("\n    ____      ____        _      \n");
    Sleep(250);
    system("Color E"); //zółty
    printf("U  / ___| UU |  _ \\  UU  / \\  U  \n");
    Sleep(250);
    system("Color A"); //zielony
    printf(" \\| |  _ /  \\| |_) |/  \\/ _ \\/   \n");
    Sleep(250);
    system("Color B"); //miętowy
    printf("  | |_| |    |  _ <    / ___ \\   \n");
    Sleep(250);
    system("Color 9"); //niebieski
    printf("   \\____|    |_| \\_\\  /_/   \\_\\  \n");
    Sleep(250);
    system("Color D"); //różowy
    printf("   _|||_    _//   \\\\_  \\\\   //  \n");
    Sleep(250);
    system("Color F"); //jasny biały
    printf("  (__)__)  (__)   (__)(__) (__) \n");
    Sleep(250);
    system("Color 7"); //zwykły biały

    draw();
    checking();

    return 0;
}
