#!/usr/bin/python3
"""
This is some documentation
"""


def read_file(filename=""):
    """
    This is more documentation
    """


    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
