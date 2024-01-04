#!/usr/bin/python3
range_tracker = 0
for i in range(0, 9):
    for j in range(i + 1, 10):
        print("{0}{1}".format(i, j), end=", " if i != 8 or j != 9 else "\n")
