#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if 96 <= ord(letter) <=123:
            ord(letter) = ord(letter) - 32
            print("{}".format(letter))
        else:
            print("{}".format(letter))
