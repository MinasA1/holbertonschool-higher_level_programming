#!/usr/bin/python3
"""module rectangle"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    def __str__(self):
        """__str__ method , prints all info for the class instance"""
        str = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return str.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """getter for private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        Rectangle.validator(mode=1, width=value)
        self.__width = value

    @property
    def height(self):
        """getter for private height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        Rectangle.validator(mode=1, height=value)
        self.__height = value

    @property
    def y(self):
        """getter for private y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        Rectangle.validator(y=value)
        self.__y = value

    @property
    def x(self):
        """getter for private x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        Rectangle.validator(x=value)
        self.__x = value

    def validator(mode=0, **kwargs):
        """
        validates the right type and value
        width and height if mode is 1
        y and x if mode is 0
        """
        for key, val in kwargs.items():
            if type(val) is not int:
                raise TypeError("%s must be an integer" % key)
            if mode == 0 and val < 0:
                raise ValueError("%s must be >= 0" % key)
            if mode == 1 and val <= 0:
                raise ValueError("%s must be > 0" % key)

    def area(self):
        """returns the area of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints the Rectangle instance with the character #"""
        if self.y != 0:
            print("\n" * self.y, end="")
        for i in range(self.__height):
            if self.x != 0:
                print(" " * self.x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """updates the instance with given args"""
        func = {0: 'id', 1: 'width', 2: 'height', 3: 'x', 4: 'y'}
        funclist = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, val in enumerate(args):
                if i in func:
                    setattr(self, func[i], val)
        else:
            for key, val in kwargs.items():
                if key in funclist:
                    setattr(self, key, val)

    def to_dictionary(self):
        """returns a dict represantation of a Rectangle"""
        js = {'id': self.id, 'width': self.width, 'x': self.x, 'y': self.y}
        js['height'] = self.height
        return js
