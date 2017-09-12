#!/usr/bin/python3
"""obj to JSON"""


def class_to_json(obj):
    """
    class_to_JSON
    args:
      obj (class)
    """
    return obj.__dict__
