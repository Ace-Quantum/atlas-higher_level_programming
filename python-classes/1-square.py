#!/usr/bin/python3
"""
I'm not sure how to document this
"""
class Square:
    """I imagine I need something here too"""
    __size = None

    def __init__(self, size_input=None):
        self.is_new = True
        if size_input is not None:
            self.size = size_input
