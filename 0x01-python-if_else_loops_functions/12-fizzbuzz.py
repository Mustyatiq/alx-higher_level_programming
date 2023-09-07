#!/usr/bin/python3
def fizzbuzz():
    "a function that prints the numbers from 1 to 100 separated by a space"
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"FizzBuzz", end=" ")
        elif number % 5 == 0:
            print(f"Buzz", end=" ")
        elif number % 3 == 0:
            print(f"Fizz", end=" ")
        else:
            print(f"{number}", end=" ")
