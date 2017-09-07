#!/usr/bin/python3
class BaseGeometry():
    """class BaseGeometry"""
    def area(self):
        """area Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator
        args:
          string (name)
          int  (value)
        raises value and type errors
        """
        if type(value) is not int:
            raise TypeError("%s must be an integer" % name)
        if value <= 0:
            raise ValueError("%s must be greater than 0" % name)
