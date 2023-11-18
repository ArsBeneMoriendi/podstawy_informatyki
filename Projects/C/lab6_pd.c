#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include "windows.h"

static int random;
static int attempt;
static int input;

void draw()
{
    srand(time(0));
    random = (rand() % 100 + 1);
    printf("\nThe program has chosen a number from 1 to 100, now you can start guessing.");
}

void checking()
{
    printf("\nEnter a number: ");

    if (scanf("%i", &input) == 1)
    {
        if(input < random)
        {
            attempt++;
            printf("\nThe clue number is higher than the entered one. Keep guessing.\nNumber of attempts: %i\n", attempt);
            checking();
        }
        else if(input > random)
        {
            attempt++;
            printf("\nThe clue number is lower than the entered one. Keep guessing.\nNumber of attempts: %i\n", attempt);
            checking();
        }
        else
        {
            attempt++;
            system("cls");
            system("Color A");
            printf("Congratulations! The clue number was %i.\nYou have guessed it within %i attempts.\n\n", random, attempt);
            system("pause");
        }
    }
    else
    {
        system("cls");
        system("Color 4");
        printf("Haha, i've secured it - this is not an integer number.\nYou've ruined the game.\n\n");
        system("pause");
    }
}

int main()
{
    system("Color 4"); //czerwony
    printf("\n    ____       _       __  __      _____\n");
    Sleep(250);
    system("Color E"); //zółty
    printf("U  / ___| UU  / \\  UU |  \\/  | UU | ____| U\n");
    Sleep(250);
    system("Color A"); //zielony
    printf(" \\| |  _ /  \\/ _ \\/  \\| |\\/| |/  \\|  _|  /\n");
    Sleep(250);
    system("Color B"); //cyjan
    printf("  | |_| |   / ___ \\   | |  | |    | |___\n");
    Sleep(250);
    system("Color 9"); //niebieski
    printf("   \\____|  /_/   \\_\\  |_|  |_|    |_____|\n");
    Sleep(250);
    system("Color D"); //różowy
    printf("   _||||_   \\\\   //   _||  ||_   _//   \\\\_\n");
    Sleep(250);
    system("Color F"); //jasny biały
    printf("  (__)(__) (__) (__) (__)  (__) (__)   (__)\n");
    Sleep(250);
    system("Color 7"); //zwykły biały

    draw();
    checking();

    return 0;
}
