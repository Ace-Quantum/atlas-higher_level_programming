#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        for x in row:
            print("{:d}".format(x), end=' ' if i != 2 else '')
            i = i + 1
        i = 0
        print()
