#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    for x in range(0, (len(new_string) - 1)):
        if new_string[x - 1] == "c" or new_string[x - 1] == "C":
            del new_string[x - 1]
    return new_string
