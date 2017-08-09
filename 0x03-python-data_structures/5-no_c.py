#!/usr/bin/python3
def no_c(my_string):
    l = list(my_string)
    for i, c in enumerate(my_string):
        if c == 'c' or c == 'C':
            l[i] = ""
    my_string = "".join(l)
    return(my_string)
