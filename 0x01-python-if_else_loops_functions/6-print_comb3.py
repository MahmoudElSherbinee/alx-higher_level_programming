#!/usr/bin/python3
for x in range(0, 10):
    for y in range(1, 10):
        if x == 8 and y == 9:
            print("{:d}{:d}\n".format(x, y), end="")
            break
        if x != y:
            if y > x:
                print("{:d}{:d}, ".format(x, y), end="")
