#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i, c in reversed(list(enumerate(my_list))):
        print("{:d}".format(my_list[i]))
