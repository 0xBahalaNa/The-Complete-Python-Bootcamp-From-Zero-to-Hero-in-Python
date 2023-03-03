"""

Milestone 3 Project: FizzBuzz

This is my implementation of FizzBuzz in Python.
The program will print every number from 1 to 100.
For every number divisible by 3, it will print Fizz.
For every number divisible by 5, it will print Buzz.
For every number divisible by 3 AND 5, it will print FizzBuzz.
"""

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
