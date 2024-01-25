#!/usr/bin/python3
"""
I once again do not know what I am doing
"""


base = __import__('7-base_geometry').BaseGeometry

class Rectangle(base):
    """
    This is a sub class, I think
    """


    def __init__(self, width, height):
        self.__width = base.integer_validator(self, "width", width)
        self.__height = base.integer_validator(self, "height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {0}/{1}".format(self.__width, self.__height)