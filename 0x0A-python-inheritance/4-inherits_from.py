#!/usr/bin/python3
def inherits_from(obj, a_class):
    """checks if object is subclass"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
