#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    res = 0
    for i in range(len(arguments) - 1):
        res = res + int(arguments[i+1])
    print("{:d}".format(res))
