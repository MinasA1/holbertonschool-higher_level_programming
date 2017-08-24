#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)):
        '''init instance'''
        self.__size = size
        self.__position = position
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
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        '''sets the position and checks if valid tuple'''
        if type(value) is not tuple or ((value[0] or value[1]) < 0) or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        '''return square'''
        return self.__size ** 2
    def my_print(self):
        '''prints the square in #'''
        for x in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for y in range(self.__position[0]):
                print(" ",end="")
            for j in range(self.__size):
                print("#", end="" if y < self.__position[0] else "\n")
        if self.__size == 0:
            print()
