#!/usr/bin/python3
"""
Now we're getting into classes and JSON
"""

class Student:


    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ret_atters = dict()
        if type(attrs) is list and all(type(elm) == str):
            for K in attrs:
                if hasattr(self, K):
                    ret_atters.append(K)
            return ret_atters
        else:
            return vars(self)