#!/usr/bin/python3
"""
this is some documentation
"""
class Rectangle:
    """
    this is more documentation
    """
    _Rectangle__height = None
    _Rectangle__width = None

    def __init__(self, width=0, height=0):
        self._Rectangle__width = width
        self._Rectangle__height = height

    def _Rectangle__width(self, value):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif size < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__width = width

    def _Rectangle__height(self, value):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif size < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__height = height
