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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Hey look I returned a list of dictionaries
        """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
        
    @classmethod
    def save_to_file(cls, list_objs):
        """
        this will save into a json file
        """

        ret_list = []
        if list_objs is not None:
            for i in list_objs:
                ret_list.append(i.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(ret_list))
            
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)