#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = [0] * 2
    for i, v in enumerate(tuple_a):
        c[i] += v
        if i == 1: break
    for i, v in enumerate(tuple_b):
        c[i] += v
        if i == 1: break
    return tuple(c)
