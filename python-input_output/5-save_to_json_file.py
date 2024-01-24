#!/usr/bin/python3
"""
Documentation
"""

import json

def save_to_json_file(my_obj, filename):
    """
    More documentation
    """


    with open(filename, 'w') as f:
        json.dump(obj, f)
