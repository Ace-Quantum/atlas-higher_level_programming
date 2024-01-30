#!/usr/bin/python3

"""
Sometimes you scream into the void
"""

import json

class Base:

    """
    And it's only to make yourself feel better
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Hey look I returned a list of dictionaries
        """
        return json.dumps(list_dictionaries)