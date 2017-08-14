#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        new_list.append(replace if i == search else i)
    return(new_list)
