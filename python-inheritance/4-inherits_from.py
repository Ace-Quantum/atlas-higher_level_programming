#!/usr/bin/python3
"""This is a module for returning if obj belongs to a subclass of specified class"""

def inherits_from(obj, a_class):
    """idk, check if the class from the object is a sub class of the specified class
    Ah, okay so type will return the class. That's how it's worked this whole time. Got it.
    Actually I don't get it??? Why does this need to be in an if statement?"""
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
