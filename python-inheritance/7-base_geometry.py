#!/usr/bin/python3
"""
This is a module that holds a class
"""


class BaseGeometry:
    """
    I legit don't know what I'm doing here
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        return value
