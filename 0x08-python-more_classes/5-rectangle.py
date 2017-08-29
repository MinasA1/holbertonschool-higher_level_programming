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
    def __str__(self):
        """__str__ method"""
        if self.__width is 0 or self.__height == 0:
            return ""
        return "\n".join(("#" * self.__width) for i in range(self.__height))
    def __repr__(self):
        """__repr__ method"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    def __del__(self):
        """__del__ method"""
        print("Bye rectangle...")
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
    def area(self):
        """public area method.
        returns the rectangle area
        """
        return self.__width * self.__height
    def perimeter(self):
        """public perimeter method
        returns the perimeter
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)
