#!/usr/bin/python3

"""
I really wish I hadn't yammered
"""

class Base:

    """
    And I'd take it back if I could
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):

        """
        here's some documentation
        """

        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0 and (name == "height" or name == "width"):
            raise ValueError(name + " must be > than 0")
        elif value < 0:
            raise ValueError(name + " must be >= 0")
        return value
