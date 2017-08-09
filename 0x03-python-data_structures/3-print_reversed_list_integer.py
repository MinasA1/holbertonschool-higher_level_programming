#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) != 0:
        for i, c in reversed(list(enumerate(my_list))):
            print("{:d}".format(my_list[i]))
