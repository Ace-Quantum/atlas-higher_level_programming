#!/usr/bin/python3
"""
I'm not sure how to document this
"""
class Square:
    """I imagine I need something here too"""
    _Square__size = None

    def __init__(self, size_input=0):
        if size_input is not None:
            if type(size_input) != int:
                raise TypeError("size must be an integer")
            elif size_input < 0:
                raise ValueError("size must be >= 0")
            else:
                self._Square__size = size_input
