#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    for x in my_list:
        if x > i:
            i = x
    return i
