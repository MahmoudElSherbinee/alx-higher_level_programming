#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals_dict = {'I': 1, 'V': 5,
                           'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for symbol in reversed(roman_string):
        current_value = roman_numerals_dict[symbol]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total
