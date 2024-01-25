#!/usr/bin/python3
"""
this is documentation
"""


def append_write(filename="", text=""):
    """
    This is more documentation
    """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)

    return len(text)
