#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    LAST = number % 10
    print(LAST, end="")
    return LAST
