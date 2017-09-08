#!/usr/bin/python3
"""obj from Json file"""


import json


def load_from_json_file(filename):
    """obj from JSON file"""
    with open(filename, 'r') as f:
        file = f.read()
        f.close()
    return json.loads(file)
