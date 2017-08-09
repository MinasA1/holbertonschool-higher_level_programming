#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return(my_list)
    else:
        new_list = [None] * len(my_list)
        for i in range(0, len(my_list)):
            new_list[i] = my_list[i]
        new_list[idx] = element
        return(new_list)
