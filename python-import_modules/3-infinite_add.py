#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(argv)
    result = 0

    for i in range(1, num):
        result = result + int(argv[i])

    print(result)
