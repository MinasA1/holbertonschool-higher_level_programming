#!/usr/bin/python3
"""JSON repr to file"""


import json


def save_to_json_file(my_obj, filename):
    """JSON repr to file"""
    js = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(js)
        f.close()
