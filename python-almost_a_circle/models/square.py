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
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = self.integer_validator("size", value)

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

