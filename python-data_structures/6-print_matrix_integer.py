#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        for x in row:
            print("{:d}".format(x), end=' ' if i != (len(row) - 1) else '\n')
            i = i + 1
        i = 0
