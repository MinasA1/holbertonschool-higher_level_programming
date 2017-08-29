#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        '''init instance, size- positive int'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if size != 0:
            self.__size = size