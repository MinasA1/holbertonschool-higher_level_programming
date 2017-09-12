#!/usr/bin/python3
"""class student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """instansiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json method retrrieves a dict repr
        args:
          attrs (list)
        """
        d = self.__dict__
        if attrs is None:
            return d
        else:
            filt_d = {}
            for element in attrs:
                for key, val in d.items():
                    if element == key:
                        filt_d[key] = val
            return filt_d

    def reload_from_json(self, json):
        """attribute replacement from json"""
        for key, val in json.items():
            setattr(self, key, val)
