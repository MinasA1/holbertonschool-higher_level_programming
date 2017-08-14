#!/usr/bin/python3
def multiply_by_2(my_dict):
    my_new_dict = {}
    for key in my_dict:
        my_new_dict[key] = my_dict[key] * 2
    return(my_new_dict)
