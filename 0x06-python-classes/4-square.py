#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        '''init instance'''
        self.__size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        '''sets the size and checks if its positive int'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        if value is not 0:
            self.__size = value
    def area(self):
        '''return square'''
        return self.__size ** 2
