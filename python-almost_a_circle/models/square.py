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
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.integer_validator("width", value)
        self.height = self.integer_validator("width", value)

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overiding str
        """

        return "[Square] ({0}) {1}/{2} - {3}".format(
            self.id, self.x, self.y, self.size)
        

