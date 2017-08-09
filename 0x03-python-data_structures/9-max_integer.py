#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return(None)
    j = my_list[0]
    for i, c in enumerate(my_list):
        if j < my_list[i]:
            j = my_list[i]
    return(j)
