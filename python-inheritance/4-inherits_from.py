#!/usr/bin/python3
"""This is a module for returning true if object belongs to class"""


def inherits_from(obj, a_class):
    """idk, check if the class from the object is a sub class 
    of the specified class
    Ah, okay so type will return the class. 
    That's how it's worked this whole time. Got it."""

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
