#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(argv)

    if num < 1:
        print("0 arguments.")

    elif num == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(num - 1))

        for i in range(1, num):
            print("{0}: {1}".format(i, argv[i]))        
