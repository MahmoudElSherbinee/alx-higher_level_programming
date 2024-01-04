#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arguments = sys.argv
    number_of_arguments = len(arguments)
    if number_of_arguments != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if number_of_arguments == 4:
        file_name = arguments[0]
        first_digit = int(arguments[1])
        operator = arguments[2]
        second_digit = int(arguments[3])
        operators = ["+", "-", "*", "/"]
        if operator not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if operator == "+":
                res = add(first_digit, second_digit)
            elif operator == "-":
                res = sub(first_digit, second_digit)
            elif operator == "*":
                res = mul(first_digit, second_digit)
            elif operator == "/":
                res = div(first_digit, second_digit)
            print("{:d} {:s} {:d} = {:d}"
                  .format(first_digit, operator, second_digit, res))
            exit(0)
