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
        if id != none:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects