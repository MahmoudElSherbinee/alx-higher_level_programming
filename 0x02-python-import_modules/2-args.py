#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    number_of_arguments = len(arguments)
    i = 1
    if number_of_arguments == 0:
        print("{:d} arguments.".format(number_of_arguments))
    elif number_of_arguments == 1:
        print("{:d} argument:".format(number_of_arguments))
        print("{:d}: {:s}".format(i, arguments[i-1]))
    else:
        print("{:d} arguments:".format(number_of_arguments))
        for i in range (1, number_of_arguments+1):
        #while i <= number_of_arguments:
            print("{:d}: {:s}".format(i, arguments[i-1]))
        #    i = i + 1