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
        self.__size = value
    def area(self):
        '''return square'''
        return self.__size ** 2
    def my_print(self):
        '''prints the square in #'''
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end=""if j < self.__size -1 else "\n")
        if self.__size is 0:
            print()
