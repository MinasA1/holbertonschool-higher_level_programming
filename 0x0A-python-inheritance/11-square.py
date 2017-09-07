#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "class Square inherits from Rectangle"""
    def __init__(self, size):
        """instansiation method"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method that overwrites the inherited one"""
        return self.__size **2

    def __str__(self):
        """__str__ method"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
