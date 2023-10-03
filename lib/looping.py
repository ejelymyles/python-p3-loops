#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    squared_elements = [element * element for element in int_list]
    return squared_elements
    pass

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
