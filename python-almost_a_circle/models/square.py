#!/usr/bin/python3

"""
time for squares
"""

from models.rectangle import Rectangle

class Square(Rectangle):

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
        super().__init__(id, width=0, height=0, x=0, y=0)
        self.__width = super.integer_validator("size", size)
        self.__height = super.integer_validator("size", size)
        self.__x = super.integer_validator("x", x)
        self.__y = super.integer("y", y)
