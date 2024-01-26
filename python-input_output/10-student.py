#!/usr/bin/python3
"""
Now we're getting into classes and JSON
"""

class Student:


"""
here's some documentation!
"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(elm) = str for elm in attrs):
            return True
        else:
            return vars(self)