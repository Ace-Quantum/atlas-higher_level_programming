#!/usr/bin/python3
"""
This is some documentation
"""


def write_file(filename="", text=""):
    """
    This is more documentation
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
