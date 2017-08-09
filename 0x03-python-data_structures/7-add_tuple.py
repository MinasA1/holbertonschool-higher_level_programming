#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    tlist = [0] * 2
    if len_a == 2:
        lim_len_a = 2
    elif len_a > 2:
        lim_len_a = 2
    elif len_a < 2:
        lim_len_a = len_a
    if len_a != 0:
        for i in range(0, lim_len_a):
            tlist[i] = tuple_a[i]
    if len_b == 2:
        lim_len_b = 2
    elif len_b > 2:
        lim_len_b = 2
    elif len_b < 2:
        lim_len_b = len_b
    if len_b != 0:
        for i in range(0, lim_len_b):
            tlist[i] += tuple_b[i]
    tuple(tlist)
    return(tlist)
