#!/usr/bin/python3
class Rectangle:
    """class rectangle"""
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        """__init__ method.

        Args:
            width (int): Rectangle's width.
            height (int): Rectangle's height.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
    def __str__(self):
        """__str__ method"""
        if self.__width is 0 or self.__height == 0:
            return ""
        return "\n".join((str(self.print_symbol) * self.__width) for i in range(self.__height))
    def __repr__(self):
        """__repr__ method"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    def __del__(self):
        """__del__ method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    @classmethod
    def square(cls, size=0):
        """classmethod square
        Args:
           size (int)
        Return: class Rectangle as Square
        """
        return cls(size, size)
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
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method bigger_or_equal
        Args:
           rect_1 (Rectangle)
           rect_2 (Rectangle)
        Return: the bigger rectangle
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
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
