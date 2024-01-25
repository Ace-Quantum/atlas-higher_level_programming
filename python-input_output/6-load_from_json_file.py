#!/usr/bin/python3
"""
Here's more documentation
"""
import json


def load_from_json_file(filename):
    """
    And some more
    """

    with open(filename, "r") as f:
        return json.loads(f.read())
