#!/usr/bin/python3

"""
do some documentation
here's some more I guess
Idk what else to do with this
perhaps another line will make you happy
"""

import sys
from os.path import isfile

save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

if isfile("./add_item.json"):
    my_list = load("./add_item.json")
else:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save(my_list, "add_item.json")
