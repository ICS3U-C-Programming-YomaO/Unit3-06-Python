#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: October 2025
# This program generates a random number between 0 and 9
# and checks if the user guessed it correctly

import random

def main():
    # generate random number between 0 and 9
    correct_number = random.randint(0, 9)

    try:
        # get user input
        guess = int(input("Guess a number between 0 and 9: "))

        # check if guess is correct
        if guess == correct_number:
            print("Correct!")
        else:
            print(" Wrong guess. The correct number was {}.".format(correct_number))

    except ValueError:
        # exception handling
        print("ERROR! You have to enter a INTEGER between 0 and 9!")

    finally:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
