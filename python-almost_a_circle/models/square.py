#!/usr/bin/python3

"""
time for squares
"""

rec = __import__("rectangle").Rectangle

class Square(rec):

    """
    What do I do
    """

    @property
    def size(self, value):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = self.integer_validator("size", value)

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = super.integer_validator("size", size)
        self.__height = super.integer_validator("size", size)
        self.__x = super.integer_validator("x", x)
        self.__y = super.integer("y", y)
