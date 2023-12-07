import random
import time
import os

os.system("cls")  #dodane cls na początek, bo bez tego kolorowanie ascii się czasami bugowało
print("\33[31m    ____       _       __  __      _____")  # czerwony
time.sleep(0.25)
print("\33[33mU  / ___| UU  / \\  UU |  \\/  | UU | ____| U")  # żółty
time.sleep(0.25)
print("\33[92m \\| |  _ /  \\/ _ \\/  \\| |\\/| |/  \\|  _|  /")  # zielony
time.sleep(0.25)
print("\33[96m  | |_| |   / ___ \\   | |  | |    | |___")  # cyjan
time.sleep(0.25)
print("\33[94m   \\____|  /_/   \\_\\  |_|  |_|    |_____|")  # niebieski
time.sleep(0.25)
print("\33[95m   _||||_   \\\\   //   _||  ||_   _//   \\\\_")  # fioletowy
time.sleep(0.25)
print("\33[97m  (__)(__) (__) (__) (__)  (__) (__)   (__)")  # jasny biały
time.sleep(0.25)

random_num = random.randrange(1, 100)
print("\33[0m\nThe program has chosen a number from 1 to 100, now you can start guessing.")

try:
    input_num = int(input("Enter a number: "))
    attempt = 0
    while input_num != random_num:
        if input_num < random_num:
            attempt += 1
            print(f"\nThe clue number is higher than the entered one. Keep guessing.\nNumber of attempts: {attempt}\n")
        elif input_num > random_num:
            attempt += 1
            print(f"\nThe clue number is lower than the entered one. Keep guessing.\nNumber of attempts: {attempt}\n")
        input_num = int(input("Enter a number: "))
    attempt += 1
    os.system("cls")
    print(f"\33[92mCongratulations! The clue number was {random_num}.\nYou have guessed it within {attempt} attempts.\n\n")
    os.system("pause")
except ValueError:
    os.system("cls")
    print("\33[91mHaha, i've secured it - this is not an integer number.\nYou've ruined the game.\n\n")
    os.system("pause")
