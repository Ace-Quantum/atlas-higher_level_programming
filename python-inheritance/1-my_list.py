#!/usr/bin/python3
"""This is a sub class of list made to print a sorted list"""
class MyList(list):
    """The sub class in question"""
    def print_sorted(self):
        print(sorted(self))
