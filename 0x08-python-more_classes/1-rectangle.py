#!/usr/bin/python3
class Rectangle:
    """class rectangle"""
    def __init__(self, width=0, height=0):
        """__init__ method.

        Args:
            width (int): Rectangle's width.
            height (int): Rectangle's height.
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """private width method"""
        return self.__width
    @property
    def height(self):
        """private height method"""
        return self.__height
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be integer")
        self.__width = value
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if type(value) is not int:
            raise TypeError("height must be integer")
        self.__height = value
