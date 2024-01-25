#!/usr/bin/python3
"""
Making a sub sub class
"""

rec = __import__('9-rectangle').Rectangle

class Square(rec):
    """
    This is a sub class of rectangle
    It shows a square
    """


    def __init__(self, size):
        self.__size = integer_validator(self, "size", size)

    def area(self, size):
        return self.__size ** 2