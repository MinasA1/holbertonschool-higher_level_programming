#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return(None)
    new_list = [False] * len(my_list)
    for i, c in enumerate(my_list):
        if my_list[i] % 2 == 0:
            new_list[i] = True
    return(new_list)
